# AGENTS.md

給在此 repo 工作的 AI 編碼代理（Claude Code、Codex、Warp 等）的指引。改編自
[blader/humanizer](https://github.com/blader/humanizer) 的 AGENTS.md。

## 這個 repo 是什麼

一個完全以 Markdown 實作的可攜 agent skill。執行時的產物是 `SKILL.md`：agent
讀它的 YAML frontmatter 和底下的編輯指令。沒有 build 步驟，用字不要把支援範圍
限縮到某一兩個 harness。

## 關鍵檔案

- `SKILL.md` — 技能本體。可攜的 YAML frontmatter（`name`、`description`、
  `license`、`metadata.version`）後接編號的模式清單與改寫前後範例。**這是唯一
  的真相來源（source of truth）。**
- `README.md` — 給人看：安裝、使用、模式總覽表、版本歷史。
- `CHANGELOG.md` — 依 Keep a Changelog，每次改行為都要記。
- `.claude-plugin/plugin.json` — Claude Code 外掛 manifest，含 `version`。
- `.claude-plugin/marketplace.json` — 單一 repo 的 marketplace 進入點；**刻意
  不放 version**，讓 `plugin.json` 當套件版本的唯一來源。
- `scripts/validate-package.py` — 無外部相依的同步檢查，本地與 CI 都跑。

## 維護契約（改東西前先讀）

`SKILL.md`、`README.md`、`CHANGELOG.md`、`plugin.json` 必須保持同步。改行為或
內容時，**在同一次改動裡**一起更新，不要分開：

- **模式：** 新增、刪除或重編號任何模式時，同一次要更新 README 的「N 種模式
  總覽」標題數字、總覽表對應分類列、SKILL frontmatter description 與 plugin.json
  description 裡的「N 種模式」、以及所有交叉引用（「見模式 X」）。編號從 1 連續，
  非必要不重編。
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
