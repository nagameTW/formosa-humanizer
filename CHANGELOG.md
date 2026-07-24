# Changelog

本檔案格式依 [Keep a Changelog](https://keepachangelog.com/zh-TW/1.1.0/)，版本號依 [SemVer 2.0.0](https://semver.org/lang/zh-TW/)。

## [Unreleased]

## [1.0.0] - 2026-07-24

### Added

- 以上游 blader/humanizer v2.9.1 為基底重寫的繁體中文技能，共 38 種模式
- 核心規則「保護中文標點」：全形標點不得改為半形，引號依教育部規範使用「」『』
- 中文專屬模式 34 到 38：中國用語混入（附對照表）、中文標點西化、括號補充濫用、連續重複行、萬用受眾套語
- 模式 26「四字格與成語堆疊」，取代英文專屬的連字號複合詞規則
- 上游 v2.9.0 的禁止捏造規則、語音校準、偵測指引與三種呼叫模式
- Claude Code 外掛封裝（`.claude-plugin/`），支援 `/plugin marketplace add` 安裝

### Changed

- 破折號規則在地化：辨識夾在中文句子裡的西式用法，而非全面禁用；全形破折號（——）與數字區間（1939–1945）視為合法
- AI 詞彙表（模式 7）改為真實中文 LLM 輸出的高頻詞，不再翻譯英文詞表
- frontmatter 縮減為可攜格式：移除 `allowed-tools`，description 改為單行
