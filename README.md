<div align="center">
  <h1>Formosa Humanizer</h1>
  <p>
    <a href="https://github.com/nagameTW/formosa-humanizer/actions/workflows/validate.yml"><img src="https://github.com/nagameTW/formosa-humanizer/actions/workflows/validate.yml/badge.svg" alt="CI"></a>
    <a href="./LICENSE"><img src="https://img.shields.io/github/license/nagameTW/formosa-humanizer?style=flat-square&logo=opensourceinitiative&logoColor=white&color=3DA639" alt="License"></a>
  </p>
</div>

把 AI 寫的中文改得像台灣人寫的。英文原版 [blader/humanizer](https://github.com/blader/humanizer) 和簡中版的規則都不是為繁中寫的，本版照台灣用語和中文標點從頭改過。他會找出混進文字裡的中國用語，也不會把「」換成英文引號。與原版的差異見 [docs/design.md](docs/design.md)。

他只拿掉明顯的 AI 習慣，不補原文沒寫的內容。適用於載得動 skill 的環境，例如 Claude Code、Codex CLI、Claude.ai 與 Claude Desktop。其他聊天介面可以把 `SKILL.md` 整份貼進對話當提示詞，但檔案模式不會運作。

## 改寫範例

| 改寫前 | 改寫後 |
|------|------|
| 該軟件通過雲端服務器處理視頻數據，用戶反饋質量顯著提升。 | 這套軟體透過雲端伺服器處理影片資料，使用者回饋品質明顯提升。 |
| 或許在某種程度上可以認為，該政策可能會對結果產生某些影響。 | 該政策可能影響結果。 |
| 問題從來不是「不完整」。這套工具能真正「賦能」你的團隊，帶來「質」的飛躍。 | 問題不在完整不完整。這套工具能實際幫上團隊，讓成果明顯不一樣。 |
| 這個功能還不穩定,建議先在測試環境驗證.確認沒問題後再上線? | 這個功能還不穩定，建議先在測試環境驗證。確認沒問題後再上線嗎？ |

一篇完整文章的改寫見 [docs/example.md](docs/example.md)，每種模式的前後對照見 [PATTERNS.md](PATTERNS.md)。

## 安裝

### Claude Code 外掛

```
/plugin marketplace add nagameTW/formosa-humanizer
/plugin install humanizer-zh-tw@humanizer-zh-tw
```

安裝後以 `/humanizer-zh-tw:humanizer-zh-tw` 呼叫。

### Claude.ai 或 Claude Desktop

需要付費方案（Pro、Max、Team 或 Enterprise），並開啟程式碼執行功能。

1. 下載 [humanizer-zh-tw.zip](https://github.com/nagameTW/formosa-humanizer/releases/latest/download/humanizer-zh-tw.zip)，不用解壓縮。
2. 到 [Customize > Skills](https://claude.ai/customize/skills) 上傳這個 ZIP，並打開。
3. 開新對話，說「幫我把這段文字去掉 AI 味」再貼上文字。

請使用上方連結，不要用 GitHub 的「Download ZIP」。後者解開的資料夾叫 `formosa-humanizer-main`，Claude 要求資料夾名稱與技能名稱相同。

### Skills CLI

```bash
npx skills add nagameTW/formosa-humanizer --global
```

更新與手動安裝見 [docs/install.md](docs/install.md)。

## 使用

```
/humanizer-zh-tw

［貼上要處理的文字］
```

也可以用自然語言，例如「幫我把這段文字去掉 AI 味：［文字］」。指向檔案時，他就地改寫，只動散文，程式碼區塊和 frontmatter 不碰。例如「幫我把 docs/announcement.md 去 AI 味」。

若要貼近自己的文風，先提供寫作範本，見 [docs/usage.md](docs/usage.md)。

## 49 種模式總覽

| 分類 | 模式 |
|------|------|
| 內容（1 到 6） | 誇大意義、堆疊知名度、尾綴式膚淺分析、宣傳語言、模糊歸因、公式化「挑戰與展望」段落 |
| 語言與語法（7 到 13） | AI 詞彙、迴避「是」、否定式排比與尾綴否定、三段式法則、刻意換詞、虛假範圍、被動語態與無主詞句 |
| 風格（14 到 19） | 西式破折號、粗體濫用、內嵌標題列表、英文標題大小寫、表情符號與裝飾性標題、引號錯誤 |
| 溝通（20 到 22） | 聊天協作痕跡、知識截止免責與投機補白、諂媚語氣 |
| 填充與迴避（23 到 33） | 填充片語、過度限定、通用正面結論、四字格堆疊、假權威套語、路標式宣告、標題後贅句、差異敘事與文件自述、人造金句、格言公式、假坦率開場 |
| 中文專屬（34 到 38） | 中國用語混入、標點西化、括號補充濫用、連續重複行、萬用受眾套語 |
| 節奏與立場（39 到 41） | 節奏與版面均勻化、情感貼標籤與罐頭意象、假平衡騎牆 |
| 標點（42 到 44） | 冒號與分號當萬用連接詞、引號當強調工具、驚嘆號連發 |
| 工具痕跡（45 到 46） | AI 工具殘留物（utm 參數、引用殘碼、佔位符）、幻覺引用與假精確 |
| 防禦與含糊（47 到 48） | 跟不存在的人爭論、模糊關聯 |
| 寫給錯的讀者（49） | 回覆時重講對方已知的事 |

偵測要點在 `SKILL.md`，前後範例在 `PATTERNS.md`，中國用語對照表在 `references/zh-cn-glossary.md`。

## 這個工具不做什麼

- 不生成內容。他只改寫你交給他的文字，不擴寫，不補建議，也不多生一段。
- 不保證能通過 AI 偵測器。目標是讓人讀起來自然，不針對 GPTZero、朱雀這類統計式偵測器。上游專案的立場相同。
- 不改變聊天助理的口氣。他只處理交給他的文字，安裝後 AI 的聊天語氣不變。
- 不捏造內容。原文沒有的事實不會加入。若句子需要具體細節，他會詢問，或寫成不含細節的平實版本。

## 版本

- **1.7.0**（2026-10-02）：目前版本。各版的變更見 [CHANGELOG.md](CHANGELOG.md)。

## 開發

```bash
python3 scripts/validate-package.py
```

此指令檢查版本、模式編號與 README 的數字是否一致。發布前的其他檢查與文件同步規則見 [AGENTS.md](AGENTS.md)。

## 專案結構

```
├── SKILL.md                  # 技能本體，agent 讀取的指令
├── PATTERNS.md               # 每種模式的改寫前後範例
├── references/
│   └── zh-cn-glossary.md     # 中國用語對照表
├── docs/
│   ├── install.md            #   Skills CLI 與手動安裝
│   ├── usage.md              #   照自己的文風改
│   ├── example.md            #   完整改寫範例
│   ├── design.md             #   與英文原版的差異
│   └── PROMOTION.md          #   推廣與搜尋發現性筆記
├── scripts/
│   └── validate-package.py   # 版本、模式編號與 README 數字檢查
├── agents/openai.yaml        # Codex 介面說明
├── .claude-plugin/           # Claude Code 外掛與 marketplace 設定
├── .cursor-plugin/           # Cursor 外掛設定
├── .github/                  # CI、release ZIP 打包、issue 範本
├── AGENTS.md                 # 給 AI 編碼代理的指引
├── CHANGELOG.md              # 各版本的變更
├── LICENSE
└── NOTICE
```

## 回饋

覺得有用的話，歡迎給個星星。遇到沒抓到的 AI 痕跡，或改壞的句子，請[開 issue](https://github.com/nagameTW/formosa-humanizer/issues/new/choose)。

## 授權與致謝

MIT 授權。

- 模式目錄與方法論來自 [blader/humanizer](https://github.com/blader/humanizer)（MIT）。
- 簡體中文移植的先行者 [op7418/Humanizer-zh](https://github.com/op7418/Humanizer-zh)。他的 issue 區的社群回報，是本版許多在地化修正的依據。
- 原始資料來源：[Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing)，由 [WikiProject AI Cleanup](https://en.wikipedia.org/wiki/Wikipedia:WikiProject_AI_Cleanup) 維護。
- 中國用語對照參考教育部《重訂國語辭典》「大陸地區語詞對照表」附錄，以及 [g0v/moedict-data-csld](https://github.com/g0v/moedict-data-csld) 的兩岸差異詞語開放資料。
