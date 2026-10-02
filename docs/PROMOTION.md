# 推廣與搜尋發現性

這份筆記記錄 repo 的搜尋現況、跟同類專案的差距，以及待辦的推廣項目。診斷做於 2026-07-24。

## 現況

repo 建立於 2026-07-24，Google 當時還沒收錄，直接搜 `nagameTW/humanizer-zh-tw` 全名也找不到。這是爬蟲還沒來的時間問題，不是排名問題，會隨時間自己好轉。

站內 metadata 其實不弱：15 個 topics、描述完整、內容量比對照組多。問題不在這裡。

## 差距在哪

同類的繁中去 AI 味專案至少有 12 個在競爭 `humanizer 繁體中文` 這類關鍵字（kevintsai1202、yelban/humanizer.tw、Raymondhou0917/speak-human-tw、shyuan/writing-humanizer 等）。排在最前面的 kevintsai1202/Humanizer-zh-TW 靠的是三樣東西，都不是 SEO 技巧：

1. **star 數**：663 顆，本專案 1 顆。GitHub 站內和 Google 都把 star 當強力排名訊號。
2. **fork 血緣**：它 fork 自 op7418/Humanizer-zh（約 13,800 star），上溯還接到 blader/humanizer（約 30,700 star），繼承了整條血緣在「humanizer」關鍵字下的權重。本專案是原創，拿不到這份繼承。
3. **外部連結**：Threads 原作者親自發文推廣、Tenten AI 的評測文列為榜首、至少 6 個 AI skill 聚合站各建了收錄頁。每一條都是反向連結加一個獨立的 Google 收錄入口。

反過來說，它的 SEO 技術面（0 topics、0 releases、描述較短）其實比本專案差。這代表追趕的重點該放在收錄、外部連結和 star，不是繼續磨 metadata。

## 已完成（repo 層）

- LICENSE 還原成乾淨的標準 MIT，GitHub 從判成 Other 改成正確辨識 MIT，拿回授權標章與搜尋篩選；上游致謝移到 NOTICE。
- repo 描述更新到 46 種模式並優化關鍵字，補上 homepage 欄。
- 發布 v1.6.1 GitHub Release（對照組沒有 release，這一項本專案領先）。
- README 首句補上「繁體中文」「台灣」「Claude skill」等實際查詢字。

## 待辦（需要帳號或時間，程式做不了）

依 CP 值排序：

1. **到 Google Search Console 提交 repo URL 要求索引。** 把「還沒被收錄」縮短到幾天內，是最急也最有效的一步。
2. **登錄 skill 聚合站。** explainx.ai、crossaitools.com、mcpmarket.com、shyft.ai、llmbase.ai、skillsmp.com 都收錄 GitHub 上的 Claude skill。對照組的外部連結有一半來自這裡，可以照樣複製，每站換一條反向連結和一個獨立收錄頁。
3. **在社群發文。** Threads、Facebook 社團、PTT，講清楚差異化賣點：46 種模式（對照組 24 種）、中國用語偵測、中文標點保護，這些都是對照組沒有的。衝 star 沒有捷徑，只能靠這個累積。
4. **爭取被評測文納入。** 投稿或聯繫 Tenten AI 那類做繁中去 AI 味評測的作者，把本專案納入下一輪比較。

## 2026-10-02 更新

- **改名**：repo 改成 `nagameTW/formosa-humanizer`。查的時候 GitHub 上至少有五個 repo 叫 humanizer-zh-tw（含 -Pro、Better- 變體），網頁搜尋這個名字也排在 kevintsai1202 和 slivenred 後面。名字已經變成通用詞，別人照名字搜會找到別的專案，改成獨特名稱才搜得到。技能名稱維持 `humanizer-zh-tw`。
- **Search Console 那項做不到**：github.com 的網址無法驗證擁有權。改成從自己的網站寫一篇文章連過來，在自己網站的 Search Console 送索引。
- **awesome list 已投稿**：VoltAgent/awesome-agent-skills#1142、BehiSecc/awesome-claude-skills#822。
- **賽道更擠了**：繁中去 AI 味 skill 至少還有 speak-human-tw（約 1k star）、acchuang/zh-tw-humanizer（56 種模式）、tentenco/shuorenhua-zh-tw、aeopress/writing-skills.TW、shyuan/writing-humanizer。

## 定位建議

與其正面搶「humanizer 繁體中文」這種已經很擠的紅海關鍵字，不如靠獨有功能吃長尾。「中國用語偵測」「中文標點保護」「語域對照」這些字目前競品講得少，本專案的描述和 README 已經佔到，值得在 topics、release notes 一致強化，吃這幾個字的搜尋。
