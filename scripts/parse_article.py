import sys, re, html
from html.parser import HTMLParser

class ArticleParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_content = False
        self.depth = 0
        self.in_p = False
        self.in_img_skip_tag = False
        self.current_text = []
        self.blocks = []  # list of ('p', text) or ('img', url)
        self.skip_tags = {'script', 'style', 'figcaption'}
        self.skip_depth = 0
        self.last_img_attrs = None

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if not self.in_content:
            if tag == 'div' and 'entry-content' in (attrs.get('class') or ''):
                self.in_content = True
                self.depth = 1
            return
        if self.in_content:
            if tag == 'div':
                self.depth += 1
            if tag in self.skip_tags:
                self.skip_depth += 1
                return
            if self.skip_depth:
                return
            if tag == 'p':
                self.in_p = True
                self.current_text = []
            elif tag == 'img':
                for key in ('data-lazy-src', 'data-src', 'src'):
                    val = attrs.get(key)
                    if val and val.startswith('http') and not val.startswith('data:'):
                        self.blocks.append(('img', val))
                        break
            elif tag == 'br' and self.in_p:
                self.current_text.append(' ')

    def handle_endtag(self, tag):
        if not self.in_content:
            return
        if tag in self.skip_tags:
            if self.skip_depth:
                self.skip_depth -= 1
            return
        if self.skip_depth:
            return
        if tag == 'p' and self.in_p:
            text = ''.join(self.current_text).strip()
            text = re.sub(r'\s+', ' ', text)
            if text:
                self.blocks.append(('p', text))
            self.in_p = False
        if tag == 'div':
            self.depth -= 1
            if self.depth <= 0:
                self.in_content = False

    def handle_data(self, data):
        if self.in_content and self.in_p and not self.skip_depth:
            self.current_text.append(html.unescape(data))

def main():
    path = sys.argv[1]
    out_path = sys.argv[2]
    with open(path, 'rb') as f:
        raw = f.read()
    content = raw.decode('utf-8', errors='replace')
    parser = ArticleParser()
    parser.feed(content)
    with open(out_path, 'w', encoding='utf-8') as out:
        for kind, val in parser.blocks:
            if kind == 'p':
                out.write('P\t' + val + '\n')
            else:
                out.write('IMG\t' + val + '\n')

if __name__ == '__main__':
    main()
