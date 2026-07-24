# Humanizer-zh-tw

去除文字中的 AI 生成痕跡，讓繁體中文讀起來像真人寫的。

這是 [blader/humanizer](https://github.com/blader/humanizer) 的台灣繁體中文在地化版本，以原版 v2.9.1 為基底重寫，不是逐句翻譯。原版依據維基百科的 [Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) 指南整理出 33 種 AI 寫作模式；本版把它們改編成中文語境的對應形態，再加上 5 種只有中文才有的痕跡，共 38 種模式。

技能本體是純 Markdown（`SKILL.md`），任何支援 skill 格式的 agent 環境都能用。

## 與英文原版的差異

繁體中文的 AI 痕跡和英文不完全一樣，直接翻譯規則會出問題（例如叫模型把中文引號改成英文直引號）。這一版做了這些調整：

- **保護中文標點的核心規則**：全形標點不得被改成半形，引號依教育部《重訂標點符號手冊》使用「」『』。這是簡體中文移植版最常見的災難，這裡從根本擋掉。
- **破折號規則重新設計**：英文原版全面禁用 em dash，但中文全形破折號（——）是合法標點。本版改成辨識「西式用法」：夾在中文句子裡的半形 em dash、被當萬用連接詞的破折號才改寫，數字區間（1939–1945）保留。
- **AI 詞彙表改用真實中文語料**：不是翻譯英文的 watch words，而是列中文 LLM 輸出實際高頻出現的詞（彰顯、賦能、格局、開啟新篇章……）。
- **五種中文專屬模式**：中國用語混入（附對照表）、中文標點西化、括號補充濫用、連續重複行、萬用受眾套語。
- **英文專屬模式在地化**：連字號複合詞濫用（英文限定）換成中文對應的痕跡「四字格與成語堆疊」。

原版 v2.9.0 之後的重要機制都有保留：禁止捏造事實（改寫不得加入原文沒有的資訊）、語音校準（提供寫作範本就模仿你的風格）、偵測指引（避免誤判真人寫作）、三種呼叫模式（貼文、檔案、嵌入）。

## 安裝

### Claude Code 外掛

```
/plugin marketplace add nagameTW/humanizer-zh-tw
/plugin install humanizer-zh-tw@humanizer-zh-tw
```

安裝後以 `/humanizer-zh-tw:humanizer-zh-tw` 呼叫。

### Skills CLI（跨環境）

```bash
npx skills add nagameTW/humanizer-zh-tw --global
```

更新既有安裝：

```bash
npx skills update humanizer-zh-tw --global
```

不加 `--global` 則安裝到目前專案，可以連同專案一起 commit 給協作者共用。

### 手動安裝

技能本體就是 `SKILL.md`，複製到你的 agent 環境放技能的目錄即可：

```bash
git clone https://github.com/nagameTW/humanizer-zh-tw.git ~/.claude/skills/humanizer-zh-tw
```

安裝後重新啟動 agent 或重新載入技能。

## 使用

直接呼叫並貼上文字：

```
/humanizer-zh-tw

［貼上要處理的文字］
```

或用自然語言：

```
幫我把這段文字去掉 AI 味：［文字］
```

指向檔案時會就地改寫，只動散文部分，程式碼區塊和 frontmatter 不碰：

```
把 docs/announcement.md 的內容人性化
```

### 語音校準

想讓改寫貼合你自己的文風，先給一段你寫過的東西：

```
/humanizer-zh-tw

這是我的寫作範本，請比對我的風格：
［貼上兩三段你自己寫的文字］

接著幫我改這段：
［貼上要處理的 AI 文字］
```

技能會分析你的句子節奏、用詞和標點習慣，照著改，而不是輸出千篇一律的「乾淨」文體。範本的優先度高於技能的預設規則。

## 支援環境

技能需要一個支援 skill 格式的 agent 環境才能運作，例如 Claude Code、Codex CLI 或其他相容工具。純聊天應用程式（網頁版聊天室、手機 App 的對話介面）沒有技能載入機制，貼上 SKILL.md 內容當提示詞可以充當替代方案，但檔案模式等功能不會生效。

## 這個工具不做什麼

- **不是 AI 偵測器繞過工具**。目標是讓文字對人類讀者來說自然好讀，不保證能通過 GPTZero、朱雀或任何統計式偵測器。上游專案對此的立場相同。
- **不改變聊天助理的說話風格**。技能處理的是你交給它的文字；裝了之後 AI 聊天的口吻不會改變。
- **不捏造內容**。改寫不會加入原文沒有的事實。需要具體細節才能寫好的句子，它會問你，或寫成不含細節的平實版本。

## 38 種模式總覽

| 分類 | 模式 |
|------|------|
| 內容（1 到 6） | 誇大意義、堆疊知名度、尾綴式膚淺分析、宣傳語言、模糊歸因、公式化「挑戰與展望」段落 |
| 語言與語法（7 到 13） | AI 詞彙、迴避「是」、否定式排比與尾綴否定、三段式法則、刻意換詞、虛假範圍、被動語態與無主詞句 |
| 風格（14 到 19） | 西式破折號、粗體濫用、內嵌標題列表、英文標題大小寫、表情符號、引號錯誤 |
| 溝通（20 到 22） | 聊天協作痕跡、知識截止免責與投機補白、諂媚語氣 |
| 填充與迴避（23 到 33） | 填充片語、過度限定、通用正面結論、四字格堆疊、假權威套語、路標式宣告、標題後贅句、差異敘事、人造金句、格言公式、假坦率開場 |
| 中文專屬（34 到 38） | 中國用語混入、標點西化、括號補充濫用、連續重複行、萬用受眾套語 |

每種模式在 `SKILL.md` 裡都有需要注意的詞彙、問題說明和改寫前後範例。

## English

Humanizer-zh-tw is a Traditional Chinese (Taiwan) adaptation of [blader/humanizer](https://github.com/blader/humanizer), a skill that removes signs of AI-generated writing. It adapts the upstream v2.9.1 pattern catalog to Chinese-language equivalents and adds five Chinese-specific patterns: Simplified-Chinese vocabulary leakage, westernized punctuation, parenthetical overuse, duplicated lines, and universal audience appeals. It also replaces the English-only em dash ban with a rule that distinguishes legitimate Chinese full-width dashes from western-style usage, and enforces CJK punctuation preservation, the most common failure of naive Chinese ports.

## 版本歷史

- **1.0.0**（2026-07-24）：首次發布。以上游 v2.9.1 為基底重寫，38 種模式，加入中文標點保護核心規則與 5 種中文專屬模式。

## 授權與致謝

MIT 授權。

- 模式目錄與方法論來自 [blader/humanizer](https://github.com/blader/humanizer)（MIT）
- 簡體中文移植的先行者 [op7418/Humanizer-zh](https://github.com/op7418/Humanizer-zh) 與其 issue 區的社群回報，提供了中文在地化的許多教訓
- 原始資料來源：[Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing)，由 [WikiProject AI Cleanup](https://en.wikipedia.org/wiki/Wikipedia:WikiProject_AI_Cleanup) 維護
