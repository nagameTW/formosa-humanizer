# 安裝細節

[README](../README.md#安裝) 列出三種常用的安裝方式。本頁補充 Skills CLI 的行為、更新方式與手動安裝。

## Skills CLI

```bash
npx skills add nagameTW/formosa-humanizer --global
```

`skills` 會找出已安裝的 agent（Claude Code、GitHub Copilot 等），並裝進每一個。安裝前先執行一次第三方安全掃描。檔案放在 `~/.agents/skills/`，各 agent 共用同一份。

更新既有安裝：

```bash
npx skills update humanizer-zh-tw --global
```

若不加 `--global`，技能裝在目前的專案。可以隨專案 commit，讓協作者使用。

## 手動安裝

若不使用 `skills` CLI，把整個 repo clone 到 agent 放技能的目錄。以 Claude Code 為例：

```bash
git clone https://github.com/nagameTW/formosa-humanizer.git ~/.claude/skills/humanizer-zh-tw
```

其他 agent 改用各自的技能目錄。

請 clone 整個 repo。若只複製 `SKILL.md`，`PATTERNS.md` 與 `references/` 不會一起過去，`SKILL.md` 內的連結會失效。裝好後，重新啟動 agent 或重新載入技能。
