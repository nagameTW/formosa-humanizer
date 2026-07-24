#!/usr/bin/env python3
"""驗證 humanizer-zh-tw 套件各面向是否同步、可攜，無外部相依。

改編自 blader/humanizer 的 validate-package.py（MIT）。差異：模式數自動偵測
（不寫死），README 用範圍式總覽表而非逐列編號，版本歷史容全形括號，行數為
軟上限（超過只警告不失敗，因中文範例較長）。

跑法：python3 scripts/validate-package.py
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL = (ROOT / "SKILL.md").read_text()
README = (ROOT / "README.md").read_text()
PLUGIN = json.loads((ROOT / ".claude-plugin" / "plugin.json").read_text())

# 行數軟上限：超過只警告。中文範例多，比原版 500 寬鬆。
LINE_SOFT_LIMIT = 900


def fail(message: str) -> None:
    raise SystemExit(f"✗ {message}")


def require(match: "re.Match[str] | None", message: str) -> "re.Match[str]":
    if match is None:
        fail(message)
    return match  # type: ignore[return-value]


# --- frontmatter：必須存在，且不含不可攜 key ---
frontmatter = require(
    re.match(r"\A---\n(.*?)\n---\n", SKILL, re.DOTALL),
    "SKILL.md 必須以 YAML frontmatter 開頭",
).group(1)

for nonportable_key in ("compatibility:", "allowed-tools:"):
    if re.search(rf"(?m)^{re.escape(nonportable_key)}", frontmatter):
        fail(f"移除不可攜的 frontmatter key：{nonportable_key[:-1]}")

# --- 版本：SKILL metadata.version / README 版本歷史 / plugin.json 三處一致 ---
skill_version = require(
    re.search(r'(?m)^\s+version:\s*["\']([^"\']+)["\']\s*$', frontmatter),
    "SKILL.md 缺 metadata.version",
).group(1)

# README 版本歷史容全形括號：- **1.3.0**（...）
readme_version = require(
    re.search(r"(?m)^- \*\*([0-9]+\.[0-9]+\.[0-9]+)\*\*", README),
    "README 缺版本歷史",
).group(1)

versions = {skill_version, readme_version, str(PLUGIN.get("version", ""))}
if len(versions) != 1:
    fail(f"版本不一致：{sorted(versions)}（SKILL / README / plugin.json 需相同）")

# --- 模式編號：自動抓，須從 1 連續無跳號無重複 ---
pattern_numbers = [int(n) for n in re.findall(r"(?m)^### ([0-9]+)\. ", SKILL)]
if not pattern_numbers:
    fail("SKILL.md 找不到任何 '### N. ' 模式標題")
expected = list(range(1, len(pattern_numbers) + 1))
if pattern_numbers != expected:
    fail(f"模式編號應為 1 到 {len(pattern_numbers)} 連續，實際為 {pattern_numbers}")
pattern_count = len(pattern_numbers)

# --- README 總覽表標題的數字須等於模式數：'## N 種模式總覽' ---
overview = require(
    re.search(r"(?m)^## ([0-9]+) 種模式總覽", README),
    "README 缺 'N 種模式總覽' 標題",
)
overview_count = int(overview.group(1))
if overview_count != pattern_count:
    fail(f"README 總覽標題寫 {overview_count} 種，但 SKILL 有 {pattern_count} 種模式")

# --- description 提及的模式數（若有 'N 種模式'）也要對得上 ---
for label, text in (
    ("SKILL frontmatter", frontmatter),
    ("plugin.json", PLUGIN.get("description", "")),
):
    m = re.search(r"([0-9]+) 種模式", text)
    if m and int(m.group(1)) != pattern_count:
        fail(f"{label} description 寫 {m.group(1)} 種模式，實際為 {pattern_count} 種")

# --- 行數軟上限：超過只警告 ---
line_count = len(SKILL.splitlines())
if line_count > LINE_SOFT_LIMIT:
    print(
        f"⚠ SKILL.md 有 {line_count} 行，超過建議上限 {LINE_SOFT_LIMIT}"
        "（可攜性與精簡度考量，考慮精簡）",
        file=sys.stderr,
    )

print(
    f"✓ humanizer-zh-tw v{skill_version} 通過驗證"
    f"（{pattern_count} 種模式，SKILL.md {line_count} 行）"
)
