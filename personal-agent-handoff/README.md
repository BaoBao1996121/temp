# Personal Agent · Claude 交接包

**入口：[CLAUDE_HANDOFF.md](CLAUDE_HANDOFF.md)**  
**直接转交的提示词：[CLAUDE_START_PROMPT.md](CLAUDE_START_PROMPT.md)**

这是 2026-11-04 的需求、研究和设计交接，不是可运行的 Agent 软件包。目标是让 Claude 不必阅读整个聊天历史，也不必重做已完成的 REA 安装和泛调研，就能接着核对证据并推进实现。

## 阅读顺序

1. [主 handoff](CLAUDE_HANDOFF.md)：产品目标、用户要求、最新发现、核心设计和第一轮动作。
2. [用户五轮报告原件](sources/最简PersonalAgent完整调研与设计取舍.md)：完整读取；它是本次更新的研究依据。
3. [更新设计](02_UPDATED_DESIGN.md)：内核、状态、协作、Nudge、记忆、长期职责和插件边界。
4. [实施与验收](03_IMPLEMENTATION_AND_EVAL.md)：可交付切片、验收样例、对照实验及真实测试边界。
5. [研究与证据](01_RESEARCH_AND_EVIDENCE.md) 和 [决策变更](04_DECISIONS_AND_CHANGES.md)：核查具体结论、历史纠偏和待决项。

机器可读的待实现案例在 [acceptance_cases.json](schemas/acceptance_cases.json)。这些是验收规格，所有案例都是 `not_implemented_not_run`，不是已经通过的测试。

## 本包提供了什么，没有提供什么

提供：本轮完整汇总报告原件、原 Codex 逆向任务、历史分析包和安装失败记录、更新后的设计与启动提示。

没有提供：用户本机的官方安装包、HOST/EVAL 原件、第五轮的完整专题、全部 REA Evidence、五轮测试脚本或运行日志。综合报告中 12 个相对链接指向的专题都未随本次上传。详见 [来源清单](sources/MANIFEST.json)。

因此：报告称本机 REA 已实际运行；本轮只是核对资料与整理交接，没有重新运行 REA 或原函数实验。早期容器的安装失败已成为历史状态，不能当成本机仍未安装。

## 使用方式

把整个文件夹交给本机 Claude Code，使用启动提示词。仅能上传单文件时，先给 `CLAUDE_HANDOFF.md`，并补充原始五轮报告；完整包可以避免关键细节遗漏。

原始研究所在用户本机路径是定位线索，需要实际盘点确认。Claude 在其他机器或聊天环境中拿不到本机资料时，应注明复核限制，不编造复跑结果。

## 校验与私有范围

包内文件哈希见 [MANIFEST.sha256](MANIFEST.sha256)，内容/路径检查记录见 [交接包校验](validation/handoff_checks.json)。这些只验证交接文件完整性，不验证产品运行效果。

本包含本机路径、私有研究边界及历史材料，不应原样作为开源仓库发布物。公开代码和 Prompt 独立编写，发布时另做隐私与许可清理。
