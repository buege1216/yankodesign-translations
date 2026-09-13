---
layout: post
title: "RHYTHM：智慧型手機時代忘記做的隨身聽"
original_title: "RHYTHM Is the Walkman the Smartphone Era Forgot to Build"
source: https://www.yankodesign.com/2026/09/12/rhythm-is-the-walkman-the-smartphone-era-forgot-to-build/
date: 2026-09-12
image: https://www.yankodesign.com/images/design_news/2026/09/rhythm-is-the-walkman-the-smartphone-era-forgot-to-build/rhythm-diy-open-source-hi-res-portable-music-player-01.jpg
designer: Mithilesh Gupta Konda
categories: [technology]
tags: [DIY, Open Source, Music Player, Portable Audio]
---

> 原文：[RHYTHM Is the Walkman the Smartphone Era Forgot to Build](https://www.yankodesign.com/2026/09/12/rhythm-is-the-walkman-the-smartphone-era-forgot-to-build/)｜Audio, Music, Technology｜2026-09-12

智慧型手機把音樂變成了另一個爭搶你注意力的通知——一首歌被簡訊打斷，一張專輯被行事曆提醒切成好幾段。RHYTHM 的存在，就是要徹底推翻這種安排：它用真正的音響元件從零打造一台專屬的聆聽裝置，而不是借用手機的內臟、再隨便裝上一個耳機孔。這是一台從頭設計的數位隨身聽，只做一件事：把音樂好好播放出來，不會有螢幕跳出來要求你去做別的事。

這份堅持，從真正驅動聲音的核心元件就看得出來。RHYTHM 沒有像大多數平價播放器那樣，靠一顆整合式的音訊解碼晶片打天下，而是採用貨真價實的 ESS SABRE DAC——這正是專業 Hi-Fi 器材會用的等級——再搭配獨立的放大電路，而不是抄捷徑的簡化方案。一顆 ESP32-S3 負責處理檔案解析與運算，但真正還原聲音的工作，全部交給專為此打造的硬體獨立完成。

耳機輸出的設計，最能說明這一切為什麼重要。RHYTHM 沒有把單一內部訊號硬是分接到一個耳機孔，而是配置了兩組完全獨立、各自帶主動緩衝的 3.5mm 輸出孔，每一組都由專屬的放大晶片驅動。兩個人可以同時接上兩副完全不同的耳機，各自都能得到完整、不打折扣的訊號，不會有共用電路悄悄拖累接在後面的那個連接埠。

要讓訊號保持乾淨，電源供應的設計和音訊路徑一樣重要。RHYTHM 把數位邏輯與高頻切換線路，跟真正影響音色的類比電路徹底分開，兩邊各自用專屬的超低雜訊穩壓器供電。這是一個規格表上完全看不出來的不起眼決定，卻正是決定一段錄音裡安靜的段落，聽起來是否真的安靜的關鍵。

實體操作介面也得到了同樣的用心。一顆精密的機械式旋轉編碼器，搭配一組觸感明確的按鍵，負責處理導航操作，帶來觸控螢幕無法複製的手感。再搭配一片 2 吋彩色螢幕，這台裝置給人的感覺不像是縮小版的手機，反而更像一件為特定用途打造的儀器——一個可以憑手感在口袋或包包裡操作，不必低頭看螢幕的東西。

一個 microSD 插槽補齊了實用面向，把無損音樂檔案存在本機，不必依賴串流連線或App生態系。這種「以本機優先」的思路，貫穿了整個專案的哲學：RHYTHM 並不是想取代手機的便利性，而是刻意選擇放棄那份便利，用隨時連網的能力，換來一種圍繞單一、不受打擾任務打造的聆聽體驗。
