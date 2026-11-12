# 查阅资源与技能库分级

新条目按候选、文档核对、试用通过分级；不适用则标淘汰。热度不等于价值。优先看 Cocos 与 Codex、画风与素材、手感、音效、测试、构建。工作日约 9:00（北京时间 / Asia/Shanghai）前后 30 分钟检查公开来源；每轮最多记 3 条，无实质新内容不写、不更新记录。不保证全网覆盖，也不会自动安装技能。

新条目用 [资源记录模板](resource-record-template.md) 填写。文档核对不得写成试用通过。

## 基础查阅资源

下列为基础查阅资源，不是 skill。评估均为文档核对，核实日为 2026-11-11（Asia/Shanghai）。未在项目试用，故不标推荐已验证。引擎版本与 Codex 兼容性：文档类不适用或未知，按你的 Creator 版本选择对应手册或仓库分支。授权以各站点条款为准。

| 资源 | 类型 | 评估 | 采用结论 |
| --- | --- | --- | --- |
| [Codex 定制说明](https://learn.chatgpt.com/docs/customization/overview) | 基础资源，非 skill | 文档核对 | 查阅 AGENTS 与 skill 分工；未试用 |
| [Cocos 模块范例仓库](https://github.com/cocos/cocos-test-projects) | 基础资源，非 skill | 文档核对 | 按 Creator 版本选分支；默认分支是 v3.8.7，另有 v3.8.x 与 v4.0.0 |
| [Cocos 小游戏发布索引（3.8）](https://docs.cocos.com/creator/3.8/manual/zh/editor/publish/publish-mini-game.html) | 基础资源，非 skill | 文档核对 | 按实际目标平台进入对应说明，不要默认是微信；4.0 亦有对应手册 |
| [TapTap 引擎适配](https://developer.taptap.cn/minigameapidoc/dev/engine/Cocos-Laya-Egret/) | 基础资源，非 skill | 文档核对 | 仅当目标是 TapTap 小游戏；插件页写 3.8.x 及以上、版本 1.2.2；转换源是微信小游戏构建，运行时不是微信；4.0 单独验证情况未知 |

### 来源链接

- Codex 定制说明（learn.chatgpt.com）：<https://learn.chatgpt.com/docs/customization/overview>
- Cocos 模块范例仓库（github.com/cocos）：<https://github.com/cocos/cocos-test-projects>
- Cocos 3.8 小游戏发布索引（docs.cocos.com）：<https://docs.cocos.com/creator/3.8/manual/zh/editor/publish/publish-mini-game.html>
- TapTap 小游戏引擎适配（developer.taptap.cn）：<https://developer.taptap.cn/minigameapidoc/dev/engine/Cocos-Laya-Egret/>
- 官方预览文档（[品质与发布控制](../docs/development-sop.md#品质与发布控制) 中引用）：<https://docs.cocos.com/creator/3.8/manual/zh/editor/preview/>

## 2026-11-12 新增

本轮 1 条。不是基础查阅资源，不进入上一节的表。评估为文档核对。未在项目试用。以下依赖与权限只记录文档所述，本仓库不安装、不执行。

### Funplay MCP for Cocos v0.7.2

- 资源：Funplay MCP for Cocos v0.7.2（仓库 FunplayAI/funplay-cocos-mcp）
- 类型：Cocos Creator 编辑器扩展 / MCP 工具（含内置 project skills），不是基础查阅文档
- 评估：文档核对
- 采用结论：值得作为 Codex + Cocos 编辑器联调的候选接入点记录。它在 Creator 编辑器内嵌 HTTP MCP 服务，说明支持 Codex，可用 `execute_javascript`（scene / editor 上下文）检查场景、截图、资源与脚本诊断，服务于画风核对与开发测试闭环。v0.7.2 明确修复了 Codex 一键配置对 `$CODEX_HOME` 和空 `[mcp_servers]` 父表的处理，并把 Configure + Skills / Project Skills 覆盖到全部 11 个一键客户端（含 Codex）。内置 skill 为 `funplay-cocos-mcp-workflow` 与 `funplay-cocos-ui-composition`（文档写为 v4 模板）。未在本用户项目试用。
- 发布/更新日：GitHub Release 与 Cocos 商店页均为 2026-11-10。同一 7 天窗口内还有 2026-11-09 的 v0.7.1；本条以 v0.7.2 为准，不另开一条。v0.7.1（2026-11-09）修复 `refresh_assets` 路径引起的缺资产/meta 错误，以及遗留坐标鼠标输入的释放清理；并正确 README 内置 skill 版本为 v4。
- 来源链接：见下方本条来源链接
- 核实日（Asia/Shanghai）：2026-11-12
- 引擎版本与平台：Cocos 商店页写 Creator 版本要求 v3.8.8；仓库 README 徽章写 3.8+，预览自动化说明针对 3.8.x。4.0 兼容性在已核来源中未说明，待确认。目标平台待确认。README 明确该扩展是 Editor-only，不应作为游戏运行时依赖打进构建包。商店页的 Android / iOS / HTML5 标签不记为该扩展的运行平台。
- 是否已在项目试用：否
- 授权：仓库为 MIT License；Cocos 商店页标价为免费。以各站点条款为准。
- 依赖与权限（仅文档所述）：
  1. 需在 Cocos Creator 中安装扩展（商店或 GitHub Release zip，并校验 `SHA256SUMS.txt`）。
  2. 编辑器内嵌 HTTP MCP；README 示例为 `http://127.0.0.1:8765/` ，新项目使用项目派生端口，占用则回退。
  3. 一键配置会写入 `$CODEX_HOME/config.toml`（默认 `~/.codex/config.toml`），示例为 `[mcp_servers.funplay_cocos]`，`url = "http://127.0.0.1:8765/"`。
  4. Configure + Skills 可能安装上述内置 skill；旧 Codex 内置可迁移到 `.agents/skills`，不删除原文件。
  5. 全局安装会写入 `~/.CocosCreator/builtin-extensions/<Creator version>/funplay-cocos-mcp`。
  6. `execute_javascript` 安全检查默认开启，但不是完整沙箱，可被 `safety_checks: false` 关闭；扩展内没有额外审批开关，MCP 工具会直接执行。文件工具限制在当前项目根目录。

### 本条来源链接

- Funplay MCP for Cocos v0.7.2（github.com/FunplayAI）：<https://github.com/FunplayAI/funplay-cocos-mcp>
- v0.7.2 Release（github.com/FunplayAI）：<https://github.com/FunplayAI/funplay-cocos-mcp/releases/tag/v0.7.2>
- CHANGELOG（github.com/FunplayAI）：<https://github.com/FunplayAI/funplay-cocos-mcp/blob/main/CHANGELOG.md>
- README（github.com/FunplayAI）：<https://github.com/FunplayAI/funplay-cocos-mcp/blob/main/README.md>
- Cocos 商店页（store.cocos.com）：<https://store.cocos.com/app/detail/8913>

## 相关文档

- [开发 SOP](../docs/development-sop.md)
- [最佳实践缺口自查](../docs/best-practices-checklist.md)
- [新资源记录模板](resource-record-template.md)
- [知识维护约束](../AGENTS.md)
