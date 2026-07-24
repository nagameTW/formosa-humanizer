# AGENTS.md

給在此 repo 工作的 AI 編碼代理（Claude Code、Codex、Warp 等）的指引。改編自
[blader/humanizer](https://github.com/blader/humanizer) 的 AGENTS.md。

## 這個 repo 是什麼

一個完全以 Markdown 實作的可攜 agent skill。執行時的產物是 `SKILL.md`：agent
讀它的 YAML frontmatter 和底下的編輯指令。沒有 build 步驟，用字不要把支援範圍
限縮到某一兩個 harness。

## 關鍵檔案

- `SKILL.md` — 技能本體。可攜的 YAML frontmatter（`name`、`description`、
  `license`、`metadata.version`）後接編號的模式清單（每個模式只留「需要注意的
  詞彙」「問題」與一行指向 PATTERNS.md 的指標）。**這是唯一的真相來源（source
  of truth）。** 技能是 model-invoked，SKILL.md 全文每次相關輪次都會載入，所以
  保持精簡：規則與偵測要點留這裡，完整範例放 PATTERNS.md。
- `PATTERNS.md` — 每個模式的改寫前後範例，編號與 SKILL.md 一致。只在校準改寫
  尺度或需要對照時查閱，不參與日常偵測。新增或修改模式時，SKILL.md 的偵測要點
  與 PATTERNS.md 的範例要一起更新。
- `references/zh-cn-glossary.md` — 模式 34 的完整中國用語對照表（資訊科技、日常
  與職場、自媒體與網路用語、動詞慣用法、商業黑話、語感層）。SKILL.md 模式 34 只
  留問題描述與一行指標，實際詞表在此。改動兩岸對照詞時只動這裡，SKILL.md 不重複。
- `README.md` — 給人看：安裝、使用、模式總覽表、版本歷史。
- `CHANGELOG.md` — 依 Keep a Changelog，每次改行為都要記。
- `.claude-plugin/plugin.json` — Claude Code 外掛 manifest，含 `version`。
- `.claude-plugin/marketplace.json` — 單一 repo 的 marketplace 進入點；**刻意
  不放 version**，讓 `plugin.json` 當套件版本的唯一來源。
- `scripts/validate-package.py` — 無外部相依的同步檢查，本地與 CI 都跑。

## 維護契約（改東西前先讀）

`SKILL.md`、`PATTERNS.md`、`README.md`、`CHANGELOG.md`、`plugin.json` 必須保持
同步。改行為或內容時，**在同一次改動裡**一起更新，不要分開：

- **模式：** 新增、刪除或重編號任何模式時，同一次要更新 SKILL.md 的偵測要點與
  指標、PATTERNS.md 對應編號的範例（兩檔模式編號必須完全一致，validate 會擋）、
  README 的「N 種模式總覽」標題數字與總覽表對應分類列、SKILL frontmatter
  description 與 plugin.json description 裡的「N 種模式」、以及所有交叉引用
  （「見模式 X」）。編號從 1 連續，非必要不重編。改動模式 34 的中國用語詞條時，
  詞表在 `references/zh-cn-glossary.md`，改那裡；SKILL.md 模式 34 只留指標，不放表。
- **版本：** 版本存在三處——SKILL frontmatter 的 `metadata.version`、README
  版本歷史、plugin.json 的 `version`。一起 bump。版本放在 `metadata` 底下；
  **top-level `version` key 不可攜**，別用。marketplace.json 不放 version。
  版本號依 SemVer：新增模式或規則是 MINOR，修正是 PATCH。
- **相容性：** 安裝與使用的措辭保持 harness 中立。技能應能在任何載得動 Markdown
  技能指令的 agent harness 運作；Claude Code、Codex 等只是例子，不是限制。
  frontmatter 不要加 `compatibility:` 或 `allowed-tools:`（不可攜，validate 會擋）。
- **驗證：** 發布前跑 `python3 scripts/validate-package.py`（檢查版本一致、模式
  編號連續、README 數字對得上），以及 `npx skills add . --list`、
  `claude plugin validate .`。
- **非顯而易見的修正：** 若為了處理棘手的失敗模式（反覆改錯、語氣跑掉）而改了
  提示詞，在 CHANGELOG 加一行說明改了什麼、為什麼。

## 編輯 SKILL.md

- 保留有效的 YAML frontmatter（格式與縮排）。
- frontmatter 底下的提示詞才是產品。把它當一份謹慎的指令文件來編輯，不是程式碼。
- 去 AI 味的方法論與規則本身，遵循 SKILL.md 內文的原則（含「保留 markdown
  結構」「不要為改而改」），不要越界成生成內容。
