# Cocos × Codex 开发工作流与技能库

单人用 Codex 做 Cocos 游戏的可复用 SOP、品质控制与最佳实践缺口自查。技能库只收分级条目。此为建议模板，不是唯一业界标准。

范围是跨游戏可复用的开发流程、品质控制、最佳实践缺口，以及有来源、按等级记录的资源。不收录游戏玩法建议。各小游戏平台、TapTap 应用分发、TapTap 小游戏不是同一件事。

## 从这里开始

1. 在目标游戏仓库填写或链接 [项目档案](templates/project-profile.md)，本库不设置统一 Cocos 版本。
2. 用 [任务路由](docs/task-routing.md) 选择本次路径，既有功能/缺陷不重走全套原型阶段。
3. 适用时使用候选技能：[UI 视口回归](.agents/skills/cocos-ui-viewport-check/SKILL.md)、[存档回归](.agents/skills/cocos-save-regression/SKILL.md)。技能在本仓库 `.agents/skills/` 下；目标游戏不会自动发现另一个仓库的技能。当前推荐让 agent 显式读取此仓库中的技能路径（并保留整个知识库 checkout 的相对目录）。单独复制技能目录会丢失支持文档，不作为当前发布方式；需要项目内安装时先打包支持文档并验证链接。不要默认安装到全局。
4. 用 [验证记录](templates/verification-record.md) 交付，不以文档核对冒充实测。素材导入先读 [素材库对接](docs/asset-library-contract.md)。

首批技能的 [来源和局限](knowledge/practice-evidence.md)：来自实际项目记录，但本轮未在游戏中重新运行，仍是候选，不是已验证的通用自动化。

## 角色与动作候选流程

[角色设计与动作技能](.agents/skills/character-motion-pipeline/SKILL.md) 配合 [项目规范模板](templates/character-motion-profile.md) 使用，覆盖母稿/视角、模型与任务记录、质检、透明帧、共框脚锚、真实尺寸和引擎同步。模型按项目配置，H3 不是通用强制项。[来源与当前限制](knowledge/character-motion-evidence.md) 明确：原项目动作尚未端到端通过，最新顺序为先静态设计、用户确认母稿、再动作；此前动作试验已停止，本文档不启动生成或改游戏资产。

## 待确认

- Cocos Creator 版本：待确认
- 目标平台：待确认（各小游戏平台、TapTap 应用分发或 TapTap 小游戏不是同一件事）

版本与具体小程序平台待确认，但不阻塞按 SOP 开工。查过文档不等于实测，未试用不标推荐已验证。全文说明见 [开发 SOP：待确认与用法](docs/development-sop.md#待确认与用法)。

## 导航

| 文档 | 内容 |
| --- | --- |
| [开发 SOP](docs/development-sop.md) | 先做样片再量产、一人开发阶段、品质与发布控制、文档最小集与短任务模板 |
| [可复用实践详解](docs/reusable-practices.md) | 2026-11-16 文档核对的 8 项方法：范围门禁、原型与样片、盲测、授权、手感反馈、性能预算、存档生命周期、可复现缺陷 |
| [最佳实践缺口自查](docs/best-practices-checklist.md) | 截至 2026-11-11（Asia/Shanghai）的未完成项，标记均为待确认 |
| [查阅资源](knowledge/resources.md) | 基础查阅资源；评估均为文档核对，核实日 2026-11-11（Asia/Shanghai） |
| [新资源记录模板](knowledge/resource-record-template.md) | 按候选、文档核对、试用通过、淘汰记录新条目 |
| [知识维护约束](AGENTS.md) | 稳定约束：分级、待确认项、检查节奏、不自动安装 |

## 记录状态

基础查阅资源与缺口的核对日均为 2026-11-11（Asia/Shanghai）。这些资源的评估是文档核对，不是试用通过，也不标推荐已验证。确认之前不要把缺口项改成完成。本轮新增 1 条的核实日为 2026-11-12（Asia/Shanghai），评估为文档核对。
2026-11-13 新增 Cocos CLI 0.2.0-beta.1（文档核对）。
2026-11-16 新增 TapTap CLI v2026.11.13（文档核对）。
2026-11-16 新增 8 项可复用实践详解（文档核对，未试用）。
2026-11-17 新增 Cocos MCP AI Master v1.0.0（文档核对）。
2026-11-18 新增 awesome-gamedev-agent-skills v2.0.0（文档核对）。
2026-11-19 新增 Funplay MCP for Cocos v0.7.5（文档核对）。
2026-11-24 新增 @alanwalk/cocos-cli v1.0.0（文档核对）。
2026-11-25 新增 sfx-skill v0.2.0（文档核对）。

## 本库校验

`python3 scripts/validate_handbook.py` 检查本地 Markdown 文件链接及简单技能 frontmatter。它不验证远程网址、锚点、任意 YAML、Cocos 行为或技能效果；游戏测试使用目标项目自己的命令。
