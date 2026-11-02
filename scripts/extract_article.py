import sys
import re
import html as htmlmod

def extract_entry_content(raw):
    start_m = re.search(r'<div class="single-box clearfix entry-content"[^>]*>', raw)
    if not start_m:
        return ""
    start = start_m.end()
    end_markers = ['related-posts', 'wp-pagenavi', 'entry-tags']
    end = len(raw)
    for marker in end_markers:
        idx = raw.find(marker, start)
        if idx != -1:
            end = min(end, idx)
    return raw[start:end]

def extract_images(block):
    imgs = []
    for m in re.finditer(r'<img[^>]+>', block):
        tag = m.group(0)
        src = None
        dm = re.search(r'data-src="([^"]+)"', tag)
        sm = re.search(r'\bsrc="([^"]+)"', tag)
        if dm and dm.group(1).startswith('http'):
            src = dm.group(1)
        elif sm and sm.group(1).startswith('http'):
            src = sm.group(1)
        if src and src not in imgs:
            imgs.append(src)
    return imgs

def strip_tags_to_text(block):
    # Remove script/style
    block = re.sub(r'<(script|style)[^>]*>.*?</\1>', '', block, flags=re.S)
    # Convert <br> and </p> to newlines
    block = re.sub(r'<br\s*/?>', '\n', block)
    block = re.sub(r'</p>', '\n\n', block)
    block = re.sub(r'<p[^>]*>', '', block)
    # Remove all remaining tags
    block = re.sub(r'<[^>]+>', '', block)
    block = htmlmod.unescape(block)
    lines = [l.strip() for l in block.split('\n')]
    text = '\n'.join(l for l in lines if l)
    return text

if __name__ == '__main__':
    path = sys.argv[1]
    out_path = sys.argv[2] if len(sys.argv) > 2 else path + '.extracted.txt'
    with open(path, encoding='utf-8', errors='replace') as f:
        raw = f.read()
    content = extract_entry_content(raw)
    imgs = extract_images(content)
    text = strip_tags_to_text(content)
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write("=== IMAGES ===\n")
        for i in imgs:
            f.write(i + "\n")
        f.write("=== TEXT ===\n")
        f.write(text + "\n")
    print("wrote", out_path)
