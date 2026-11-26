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
- [可复用实践详解](../docs/reusable-practices.md)
- [最佳实践缺口自查](../docs/best-practices-checklist.md)
- [新资源记录模板](resource-record-template.md)
- [知识维护约束](../AGENTS.md)

## 2026-11-13 新增

本轮 1 条。不是基础查阅资源，不进入基础查阅资源表。评估为文档核对。未在项目试用，未安装。以下只记录已打开的文档，本仓库不克隆、不编译、不执行该 CLI。

### Cocos CLI（官方）0.2.0-beta.1

- 资源：Cocos CLI（官方）0.2.0-beta.1（仓库 cocos/cocos-cli）
- 类型：官方命令行工具，不是基础查阅文档
- 评估：文档核对
- 采用结论：已打开的文档列出命令行 `cocos build`（平台示例为 web-desktop、web-mobile、android、ios 等）、全局选项 `--no-interactive`，以及 `cocos start-mcp-server`。这些用法不经过编辑器界面，可供 Codex 不开编辑器直接构建并检查项目。对应 [开发 SOP](../docs/development-sop.md#品质与发布控制) 中尽早在真实目标平台构建，以及短任务模板里把构建日志作为证据。`docs/zh/commands.md` 的 `cocos build` 另有 `--log-dest` 指定日志文件路径。未试用，未安装。
- 发布/更新日：GitHub Release 发布于 2026-11-12（页面时间为 2026-11-12T13:04:57Z）。版本号为 0.2.0-beta.1，仍是 beta。
- 来源链接：见下方本条来源链接。链接均指向 tag `0.2.0-beta.1`，本轮打开返回正常。
- 核实日（Asia/Shanghai）：2026-11-13
- 引擎版本与平台：`docs/zh/commands.md` 点名的构建平台是 web-desktop、web-mobile、android、ios 等，未点名微信、TapTap 等小游戏目标。`README-zh.md`、`docs/zh/quick-start.md`、`docs/zh/commands.md` 未说明能否用于现有 Creator 3.x 项目。README 引擎徽章指向 `https://github.com/cocos/cocos4`，原生环境链接指向 Creator 3.8 英文手册；这两处不记成对现有 3.x 项目的兼容结论。目标平台仍待确认。
- 是否已在项目试用：否
- 是否已安装：否
- 授权：仓库为 MIT License。以各站点条款为准。
- 注意：
  1. 仍是 beta。
  2. 安装说明是从源码克隆后编译：`README-zh.md` 要求 Node.js 22.17.0；`docs/zh/quick-start.md` 写 Node.js 22.17.0 或更高版本。tag 内 `.nvmrc` 为 22.17.0。
  3. 上述三份中文文档未说明能否用于现有 Creator 3.x 项目。
  4. 上述文档未列出微信、TapTap 等小游戏目标。
  5. MCP 端口记载不一致：`docs/zh/commands.md` 写 `cocos start-mcp-server` 默认端口 3000；`README-zh.md` 与 `docs/zh/quick-start.md` 的示例为 `--port 9527`。`9527` 也是 `commands.md` 里 `cocos simulator` 预览端口的默认值，与 MCP 默认端口不是同一处说明。

### 本条来源链接

- Cocos CLI（github.com/cocos）：<https://github.com/cocos/cocos-cli>
- 0.2.0-beta.1 Release（github.com/cocos）：<https://github.com/cocos/cocos-cli/releases/tag/0.2.0-beta.1>
- README-zh.md（tag 0.2.0-beta.1）：<https://github.com/cocos/cocos-cli/blob/0.2.0-beta.1/README-zh.md>
- docs/zh/quick-start.md（tag 0.2.0-beta.1）：<https://github.com/cocos/cocos-cli/blob/0.2.0-beta.1/docs/zh/quick-start.md>
- docs/zh/commands.md（tag 0.2.0-beta.1）：<https://github.com/cocos/cocos-cli/blob/0.2.0-beta.1/docs/zh/commands.md>

## 2026-11-16 新增

本轮 1 条。不是基础查阅资源，不进入基础查阅资源表。评估为文档核对。未在项目试用，未安装。以下只记录已打开的文档，本仓库不安装、不登录、不执行该 CLI。

### TapTap CLI（官方）v2026.11.13

- 资源：TapTap CLI（官方）v2026.11.13（npm 包 `@taptap/cli`）
- 类型：TapTap 官方命令行工具 / 随版本提供的 AI Agent Skills，不是基础查阅文档，也不是 Cocos 引擎工具
- 评估：文档核对
- 采用结论：值得作为 Codex + TapTap 发布与测试流程的候选接入点记录。适用阶段是测试、构建后的包体管理与发布（资料 / 包体 / 提审 / 测试计划），不替代 Cocos 工程内构建。官方文档说明这是连接本地环境与 TapTap 开发者中心的 CLI，可直接运行命令，也可配合 AI 助手（README 点名适配 Codex）。它用于创建游戏草稿、维护资料、上架资质、提审发布、包体管理与自测、测试计划和素材库等开发者中心操作，并提供 `taptap-cli app analyze-status`、提审预检与 `--dry-run`。与知识库已强调的区分直接相关：官方更新日志 2026-11-11 写明「可用包体类型中没有小游戏，不代表小游戏功能未开通」，并要求用小游戏包体列表核对开通结果；官方更新日志 2026-11-12 新增 `package-management diagnose-package-type`，用于区分尚未保存包体类型、已保存类型与游戏形态冲突、无需上传包体等情况，诊断只读取不自动修改声明。这些能力服务于开发测试发布流程。未在本用户项目试用。本轮 7 天窗口内的同一工具多个版本合并为一条，以 npm 上最新的 v2026.11.13 为准，不另开 v2026.11.10 / v2026.11.11 / v2026.11.12。
- 发布/更新日：这个 CLI 本身不是本窗口首次发布（npm 记载包创建于 2026-08-28）。本条记的是最近 7 天内的实质更新。npm 页面记录 v2026.11.13 发布于 2026-11-13T08:57:51.886Z。官方文档更新日志在 2026-11-16 核对时详细记到 2026-11-12（`v2026.11.12`）。同版本包内 CHANGELOG 对 v2026.11.13 只写了 “Improve reliability and usability.”，不补写官方站点日志里没有的功能点。7 天窗口内的实质变更按来源分开记：
  1. 官方站点更新日志 2026-11-11：更准确地区分小游戏开通状态与包体类型；图片素材交接保留平均色；发布流程维护（不改命令用法）。
  2. 官方站点更新日志 2026-11-12：新增 `package-management diagnose-package-type`；设置新图片时需同时提供图片地址和完整素材信息（文件大小、格式、宽度、高度及平均色），不能只填地址或自行猜测平均色；命令名称更简洁，旧别名仍可用。
  3. 包内 CHANGELOG v2026.11.12：与诊断命令、H5 上传前检查已保存包体类型、命令缩名一致。站点日志里的图片完整素材信息要求不记入这条包内 CHANGELOG。
  4. 包内 CHANGELOG v2026.11.11 主要是文档与测试修订。官方站点 2026-11-11 的小游戏开通说明不记成包内 CHANGELOG 的内容。
- 来源链接：见下方本条来源链接。各条写明 2026-11-16 的核对结果。
- 核实日（Asia/Shanghai）：2026-11-16
- 引擎版本与平台：这是 TapTap 开发者中心 CLI，不是 Cocos 构建工具，引擎版本不适用。目标平台仍待确认。各小游戏平台、TapTap 应用分发、TapTap 小游戏不是同一件事。官方文档将 APK、Windows、H5、Tap 小游戏等当作不同包体/能力路径。包内 README.zh.md 的功能表将包体管理写为「上传和管理 APK、Windows、H5 包」；该表不改写成已列出 Tap 小游戏上传。官方站点更新日志 2026-11-11 讨论了小游戏开通状态与包体类型的区分。当前目标不记成 TapTap 小游戏或 TapTap 应用分发。
- 是否已在项目试用：否
- 是否已安装：否
- 授权：npm 包页与 README 均标 MIT License。以各站点条款为准。
- 依赖与权限（仅文档所述，本仓库不安装、不登录、不执行）：
  1. npm 分发版要求 Node.js v16+。官方安装命令为 `npm i -g @taptap/cli --registry=https://registry.npmjs.org/`，需全局包写入权限。
  2. 需已注册并完成必要认证的 TapTap 开发者账号。`taptap-cli auth login` 会在本机保存凭证；授权后 AI 助手可以开发者身份执行写操作。官方安全说明要求先在测试游戏或非生产资料上验证，正式操作前核对 developerId / appId 等。本记录不写入登录凭证。
  3. AI Skills 随 CLI 一起提供并与当前 CLI 版本严格对应。查看清单用 `taptap-cli skills list`，更新并同步用 `taptap-cli update`。README.zh.md 还写了可在项目根目录运行 `npx skills add taptap/cli -a universal`。
  4. 写操作（创建游戏、上传包体、提交审核等）支持 `--dry-run` 预览，正式执行常需 `--yes` 与幂等键。
  5. 包内 README 列出的 Skills 包括：`taptap-cli`、`taptap-suite`、`taptap-identity`、`taptap-publish-game`、`taptap-app-edit`、`taptap-community-management`、`taptap-qualification`、`taptap-asset-library`、`taptap-materials`、`taptap-package-management`、`taptap-dashboard-stats`、`taptap-player-feedback`、`taptap-test-plan`、`taptap-whats-new`、`taptap-official-message-push`、`taptap-game-sign`。这份清单是文档所列，未在本机安装。

### 本条来源链接

- 官方文档（developer.taptap.cn）：<https://developer.taptap.cn/v3/cli/>（2026-11-16 打开为 HTTP 200）
- 官方更新日志（developer.taptap.cn）：<https://developer.taptap.cn/v3/cli/changelog/>（2026-11-16 打开为 HTTP 200）
- 官方 Skill 参考（developer.taptap.cn）：<https://developer.taptap.cn/v3/cli/skill-reference/>（2026-11-16 打开为 HTTP 200）
- 官方命令参考（developer.taptap.cn）：<https://developer.taptap.cn/v3/cli/command-reference/>（2026-11-16 打开为 HTTP 200）
- npm 包页（www.npmjs.com）：<https://www.npmjs.com/package/@taptap/cli>。本轮已读到包页内容：最新版本 2026.11.13，License MIT，Updated 2026-11-13T08:57:52.122Z。直接 curl 曾返回 403，不记成页面不存在。
- 包内 CHANGELOG（cdn.jsdelivr.net）：<https://cdn.jsdelivr.net/npm/@taptap/cli@2026.11.13/CHANGELOG.md>（2026-11-16 打开为 HTTP 200）
- 包内 README.zh.md（cdn.jsdelivr.net）：<https://cdn.jsdelivr.net/npm/@taptap/cli@2026.11.13/README.zh.md>（2026-11-16 打开为 HTTP 200）
- 不作为来源：README 与 npm 元数据提到 `https://github.com/taptap/cli`，2026-11-16 打开为 HTTP 404，公共不可访问。

## 2026-11-16 可复用实践来源

同日上一节记录的是 TapTap CLI。本节只补方法来源，不新增工具，也不改写上一节。

正文见 [可复用实践详解](../docs/reusable-practices.md)。评估为文档核对，核实日 2026-11-16（Asia/Shanghai），未在项目试用。这些链接不进入基础查阅资源表。本仓库不安装、不执行这些来源里的软件。

### 本条来源链接

- Project Horseshoe 2008 报告第 4 节（www.projecthorseshoe.com）：<https://www.projecthorseshoe.com/reports/ph08/ph08r4.htm>
- Rami Ismail，Prototypes & Vertical Slice（ltpf.ramiismail.com，2022-09-26）：<https://ltpf.ramiismail.com/prototypes-and-vertical-slice/>
- Gabler 等，How to Prototype a Game in Under 7 Days（www.gamedeveloper.com，2005-10-26）：<https://www.gamedeveloper.com/game-platforms/how-to-prototype-a-game-in-under-7-days>
- Florencio，What you should take out of Pre-Production（www.gamedeveloper.com，2022）：<https://www.gamedeveloper.com/game-platforms/what-you-should-take-out-of-pre-production>
- Mike Ambinder，Valve's Approach to Playtesting，GDC 2009 PDF（cdn.fastly.steamstatic.com）：<https://cdn.fastly.steamstatic.com/apps/valve/2009/GDC2009_ValvesApproachToPlaytesting.pdf>
- The Level Design Book，Playtesting（book.leveldesignbook.com）：<https://book.leveldesignbook.com/process/blockout/playtesting>
- Steve Swink，Principles of Virtual Sensation（www.gamedeveloper.com，2006-11-14）：<https://www.gamedeveloper.com/design/principles-of-virtual-sensation>
- Creative Commons FAQ（creativecommons.org）：<https://creativecommons.org/faq/>
- 微信小游戏运行机制（developers.weixin.qq.com）：<https://developers.weixin.qq.com/minigame/dev/guide/runtime/operating-mechanism>
- 微信小游戏运行性能概述（developers.weixin.qq.com）：<https://developers.weixin.qq.com/minigame/dev/guide/performance/perf-action-runtime-overview.html>
- 微信小游戏性能评测标准（developers.weixin.qq.com）：<https://developers.weixin.qq.com/minigame/dev/guide/performance/perf-mesure>
- 微信小游戏代码包（developers.weixin.qq.com）：<https://developers.weixin.qq.com/minigame/dev/guide/base-ability/code-package.html>
- wx.onHide（developers.weixin.qq.com）：<https://developers.weixin.qq.com/minigame/dev/api/base/app/life-cycle/wx.onHide.html>
- Cocos Creator 3.8 项目预览调试（docs.cocos.com）：<https://docs.cocos.com/creator/3.8/manual/zh/editor/preview/>
- Cocos Creator 3.8 性能剖析器（docs.cocos.com）：<https://docs.cocos.com/creator/3.8/manual/zh/advanced-topics/profiler.html>
- Cocos Creator 3.8 多分辨率适配（docs.cocos.com）：<https://docs.cocos.com/creator/3.8/manual/zh/ui-system/components/engine/multi-resolution.html>
- Cocos Creator 3.8 SafeArea（docs.cocos.com）：<https://docs.cocos.com/creator/3.8/manual/zh/ui-system/components/editor/safearea.html>
- Android Core app quality guidelines（developer.android.com，页面写明 Last updated 2026-11-13 UTC）：<https://developer.android.com/docs/quality-guidelines/core-app-quality>
- Simon Tatham，How to Report Bugs Effectively（www.chiark.greenend.org.uk）：<https://www.chiark.greenend.org.uk/~sgtatham/bugs.html>
- Codex 定制说明（已在基础查阅资源中，不另开条目）：<https://learn.chatgpt.com/docs/customization/overview>

## 2026-11-17 新增

本轮 1 条。不是基础查阅资源，不进入基础查阅资源表。评估为文档核对。未购买、未安装、未在项目试用。以下只记录已打开的商店页与作者论坛说明，本仓库不购买、不下载、不安装、不执行该插件。

### Cocos MCP AI Master v1.0.0

- 资源：Cocos MCP AI Master v1.0.0（Cocos Store 商品 10014，作者 GameAIMaster）
- 类型：Cocos Creator 编辑器扩展 / MCP 工具（付费商店插件），不是基础查阅文档，也不是官方 Cocos/Codex 产品
- 评估：文档核对
- 采用结论：值得作为 Codex + Cocos 编辑器联调的候选接入点记录。商店与作者说明这是 Creator 3.8.8 编辑器扩展，把编辑器操作封装为 MCP，供 AI 编程 Agent 调用；接入说明点名 Codex CLI（名单出自商店与作者说明）。文档所述能力用于经编辑器操作修改场景、界面、动画、资源与脚本（不直接改项目私有格式文件），核对节点结构、组件属性、界面布局、运行画面与构建结果并报差异，以及构建、预览和玩家视角截图，服务于开发中的画风与布局核对、构建试玩闭环。未在本用户项目试用。与已记录的 Funplay MCP for Cocos v0.7.2 不是同一产品，本条不改写该条目。本产品是 Cocos Store 付费闭源商店插件，商店与作者均写明仅支持 Creator 3.8.8，启用需激活码，且未发现公开源代码仓库。本库的 Creator 版本仍待确认。
- 发布/更新日：商店页可见「最近更新时间 2026-11-16」，版本 v1.0.0，Creator 版本要求 v3.8.8。商店页面数据 `3x_version_data.update_time` = 1794818163，即 2026-11-16T08:36:03Z，也就是 2026-11-16 16:36:03（Asia/Shanghai）。作者论坛帖由 GameAIMaster 发表于 2026-11-16，更新声明写 1.0.0 为「首个正式版本」。作者同日回复写明当天提交商店并已审核通过，并给出商店链接。这是本 7 天窗口内的首次公开发布，不是对已有条目的版本更新。
- 来源链接：见下方本条来源链接。商店页与作者论坛帖在 2026-11-17 打开均为 HTTP 200。未发现公开源代码仓库。
- 核实日（Asia/Shanghai）：2026-11-17
- 引擎版本与平台：商店 dependency 与 Creator 版本要求为 3.8.8。作者说明其他 3.x 需升级到 3.8.8 并能正常打开后才可接入；本条只转录该文档要求。文档写操作系统为 Windows x64、macOS（Intel 与 Apple 芯片）。商店「支持平台」显示 Android | IOS | HTML5；本条只记该商店标签。作者文档提到「按平台构建发布」，未点名微信或 TapTap。本库 Creator 版本与目标平台仍待确认。
- 是否已在项目试用：否
- 是否已安装：否
- 授权：专有许可（著作权归作者，购买获得自用授权）。商店商品说明「许可声明」写明：插件包、源码与文档的著作权归作者所有；购买获得的是在购买者自己的项目中使用本插件的授权。未经作者书面许可，不得复制、转售、再分发插件包或源码，也不得将本插件代码或其衍生代码用于其他产品。商店个人标价 ¥288.00（`price_person` = 288.00）。2026-11-17 核对日所见限时折扣为 ¥188（`discount_price_zh` = 188），开始于 2026-11-16 00:00:00（Asia/Shanghai，时间戳 1794758400），结束于 2026-12-16 00:00:00（Asia/Shanghai，时间戳 1797350400）。折扣可能过期，只记核对日所见。商店文案写付费虚拟商品一经购买成功概不退款。以各站点条款为准。未购买。
- 依赖与权限（仅文档所述，本仓库不购买、不下载、不安装、不执行）：
  1. 需先安装 Cocos Creator 3.8.8；插件无法独立运行。本库 Creator 版本仍待确认。
  2. 需在 Cocos Store 购买并下载 zip；从「已购资源」下载，保持压缩包导入，先不要解压；经「扩展」→「扩展管理器」导入。项目级扩展，每个项目各装一次。
  3. Cocos Store 下单付费后需向作者客服索取激活码，在 MCP Server 面板激活后才能启用。本记录不写具体联系方式。
  4. 默认接入端点为 `http://127.0.0.1:3600/mcp`。端口被占用时自动调整，以面板提示为准。面板提供「自动配置」。作者给出的配置示例：

     ```json
     {
       "mcpServers": {
         "cocos-mcp": {
           "url": "http://127.0.0.1:3600/mcp"
         }
       }
     }
     ```

  5. 使用编辑器内置 Node.js。文档写无需单独安装 Node.js。不提供 AI 大模型 API。
  6. 支持本机、局域网或用户自行配置的隧道。插件不提供隧道服务。
  7. 商店与作者说明点名可接入 Codex CLI。同页还有其他客户端，本条不展开整份名单。

### 本条来源链接

- 官方商店页（store.cocos.com）：<https://store.cocos.com/app/detail/10014>（2026-11-17 打开为 HTTP 200）
- 作者论坛说明（forum.cocos.org，GameAIMaster，2026-11-16）：<https://forum.cocos.org/t/topic/178155>（2026-11-17 打开为 HTTP 200）
- 未发现公开 GitHub 或其它源代码仓库，本条不编造仓库地址。

## 2026-11-18 新增

本轮 1 条。不是基础查阅资源，不进入基础查阅资源表。评估为文档核对。未在项目试用，未安装。以下只记录已打开的 tag `v2.0.0` 文档，本仓库不安装、不执行该技能包。

### awesome-gamedev-agent-skills v2.0.0

- 资源：awesome-gamedev-agent-skills v2.0.0（仓库 gamedev-skills/awesome-gamedev-agent-skills）
- 类型：开源 Agent Skills 技能包（含 router 与学科/引擎/类型/工作流技能），不是基础查阅文档，也不是 Cocos 官方或 Codex 官方产品
- 评估：文档核对
- 采用结论：值得作为跨引擎「画风 / 手感 / 音效」方法技能的候选记录，供 Codex 在讨论设计与开发时按需读取。采用理由只针对学科技能，不针对类型（genre）技能，也不提供玩法建议。已打开的 v2.0.0 文档说明：共 79 个技能 + 一个 router；`npx skills add gamedev-skills/awesome-gamedev-agent-skills` 会安装 router 和全部 79 个技能。README 写明同一套 `SKILL.md` 可在 OpenAI Codex 等客户端原生加载；手拷贝时 Codex 的技能目录是 `.agents/skills/`（与 Gemini CLI、GitHub Copilot、Antigravity 共用该路径）。与本库痛点直接相关、且文档称为可跨引擎的学科技能包括：`create-game-assets`（先锁定视觉目标/风格说明与资产清单，再成套制作并做检查，而不是一次生成即视为可发布）、`game-feel`（震屏、顿帧、缓动、挤压拉伸、击退与分层视听反馈等）、`audio-design`（总线布局、响度、闪避、自适应音乐与音效变化；文档里的 Godot / Unity / FMOD/Wwise 映射是例子）。文档列出的 12 个受检引擎是 Godot、Unity、Unreal、Ebitengine、Phaser、PixiJS、three.js、Bevy、pygame、LÖVE、Defold、Roblox。`docs/VERSION-SUPPORT.md`（核实日 2026-11-11）没有 Cocos / Cocos Creator。本条不写成兼容 Cocos，也不把其中的 Unity / Godot / Phaser / 通用 Web 技能当作 Cocos 实现。router 对「自定义 / 专有 / 无目录技能的引擎」的路径（`router/references/custom-engines.md` 与 router SKILL §7）要求：保持现有引擎与工具链；学科技能描述的是可移植方法，其中点名的 Godot/Unity 绑定只是例子，不是要求安装或迁移到那些引擎；不要把未知引擎做成 Godot 脚手架。Cocos 项目若未被识别为这 12 个引擎之一，应走这条路径，而不是套用其它引擎技能里的 API。README 也提醒：若代理已有很多技能，优先只装 router 与「你的引擎」捆绑，而不是全部安装。该仓库没有 Cocos 引擎捆绑。本条不建议把 79 个技能整包装进用户的游戏仓库。未在本用户项目试用，未安装。
- 发布/更新日：GitHub Release `v2.0.0` 发布于 2026-11-11T14:00:52Z，即 2026-11-11 22:00:52（Asia/Shanghai）。这是相对 2026-06-26 的 v1.1.0 的一次实质更新（质量重写 + 新技能 + 路由与评测），不是本窗口内对已有本库条目的版本修订（本库此前未记录该仓库）。默认分支在 v2.0.0 之后还有 2026-11-11 / 2026-11-12 的 README 横幅与赞助商文档提交，没有更新的 Release。本条以 tag `v2.0.0` 为准，不把默认分支未发布提交记成新版本。
- 来源链接：见下方本条来源链接。下列链接均在 2026-11-18 打开为 HTTP 200。除仓库首页外，链接都指向 tag `v2.0.0`。
- 核实日（Asia/Shanghai）：2026-11-18
- 引擎版本与平台：该技能包不是 Cocos 构建或编辑器工具。官方受检引擎不含 Cocos，Cocos 兼容性未在来源中建立，记为不适用 / 未支持。本库的 Creator 版本与目标平台仍待确认。文档中的 Godot / Unity / 其它引擎基线不记成用户项目版本。
- 是否已在项目试用：否
- 是否已安装：否
- 授权：Apache License 2.0（仓库 LICENSE 与 GitHub 元数据）。以各站点条款为准。
- 依赖与权限（仅文档所述，本仓库不安装、不执行）：
  1. 使用官方安装命令需要 Node.js 22.20 或更高版本（README）。命令为 `npx skills add gamedev-skills/awesome-gamedev-agent-skills`；`--list` 可先预览，`-g` 为全局，`-a <agent>` 指定客户端。README 举例有 `-a cursor`、`-a claude-code`、`-a gemini-cli`。
  2. 该命令会把 router 和全部 79 个技能写到客户端对应目录。手拷贝时，Codex 为项目内 `.agents/skills/`。
  3. 另有 Claude Code 插件市场安装方式；本条只转录，不展开为推荐。
  4. 本知识库与本轮自动化都不得替用户安装这些技能。

### 本条来源链接

- 仓库（github.com/gamedev-skills）：<https://github.com/gamedev-skills/awesome-gamedev-agent-skills>（2026-11-18 打开为 HTTP 200）
- Release v2.0.0（github.com/gamedev-skills）：<https://github.com/gamedev-skills/awesome-gamedev-agent-skills/releases/tag/v2.0.0>（2026-11-18 打开为 HTTP 200；Published 2026-11-11T14:00:52Z）
- CHANGELOG（tag v2.0.0 raw）：<https://raw.githubusercontent.com/gamedev-skills/awesome-gamedev-agent-skills/v2.0.0/CHANGELOG.md>（2026-11-18 打开为 HTTP 200）
- README（tag v2.0.0 raw）：<https://raw.githubusercontent.com/gamedev-skills/awesome-gamedev-agent-skills/v2.0.0/README.md>（2026-11-18 打开为 HTTP 200）
- LICENSE（tag v2.0.0 raw）：<https://raw.githubusercontent.com/gamedev-skills/awesome-gamedev-agent-skills/v2.0.0/LICENSE>（2026-11-18 打开为 HTTP 200，Apache License 2.0）
- 自定义引擎路径（tag v2.0.0）：<https://github.com/gamedev-skills/awesome-gamedev-agent-skills/blob/v2.0.0/router/references/custom-engines.md>（2026-11-18 打开为 HTTP 200）
- router SKILL（tag v2.0.0，§7 为未知引擎回退）：<https://github.com/gamedev-skills/awesome-gamedev-agent-skills/blob/v2.0.0/router/SKILL.md>（2026-11-18 打开为 HTTP 200）
- 版本支持表（tag v2.0.0）：<https://github.com/gamedev-skills/awesome-gamedev-agent-skills/blob/v2.0.0/docs/VERSION-SUPPORT.md>（2026-11-18 打开为 HTTP 200）
- create-game-assets（tag v2.0.0）：<https://github.com/gamedev-skills/awesome-gamedev-agent-skills/blob/v2.0.0/skills/disciplines/create-game-assets/SKILL.md>（2026-11-18 打开为 HTTP 200）
- game-feel（tag v2.0.0）：<https://github.com/gamedev-skills/awesome-gamedev-agent-skills/blob/v2.0.0/skills/disciplines/game-feel/SKILL.md>（2026-11-18 打开为 HTTP 200）
- audio-design（tag v2.0.0）：<https://github.com/gamedev-skills/awesome-gamedev-agent-skills/blob/v2.0.0/skills/disciplines/audio-design/SKILL.md>（2026-11-18 打开为 HTTP 200）

## 2026-11-19 新增

本轮 1 条。不是基础查阅资源，不进入基础查阅资源表。评估为文档核对。未在项目试用，未安装。以下依赖与权限只记录文档所述，本仓库不安装、不执行。

### Funplay MCP for Cocos v0.7.5

- 资源：Funplay MCP for Cocos v0.7.5（仓库 FunplayAI/funplay-cocos-mcp）
- 类型：Cocos Creator 编辑器扩展 / MCP 工具（含内置 project skills），不是基础查阅文档
- 评估：文档核对
- 采用结论：这是已记录的 Codex + Cocos 编辑器联调候选接入点的实质更新，值得追加文档核对。README（tag v0.7.5）写明：内置 skill 仍是 `funplay-cocos-mcp-workflow`（v4）与 `funplay-cocos-ui-composition`（现为 v5）；Project Skills 覆盖全部 12 个一键客户端（含 Antigravity）；Codex 与 Antigravity 共用 `.agents/skills`，可迁移旧内置 skill 且保留原文件。UI v5 覆盖把整页设计稿拆成可编辑 prefab，并按区域做忠实度检查，有助于画风/界面一致性核对。v0.7.4 的 Game View 截图修复与此核对相关。v0.7.5 让 Codex 可与 Antigravity 共用 `.agents/skills` 的一键安装。未在本用户项目试用。本条不改写 2026-11-12 的 v0.7.2 记录。
- 发布/更新日：GitHub Release v0.7.5 发布于 2026-11-18T10:00:29Z，CHANGELOG 日期为 2026-11-18。本条以 v0.7.5 为准。同一 7 天窗口内还有 v0.7.3 与 v0.7.4，不另开条目。
  1. CHANGELOG 写 v0.7.3 为 2026-11-17，GitHub Release 发布于 2026-11-18T04:36:30Z。新增内置 Cocos UI Skill v5：引导把整页设计稿转成可编辑、响应式 prefab；覆盖资源复用、独立导航层、可复用列表行，并按区域对照 Cocos 预览截图做忠实度检查；缺图时可选生图。
  2. CHANGELOG 写 v0.7.4 为 2026-11-17，GitHub Release 发布于 2026-11-18T06:44:31Z。修复 #28：Game View 截图能识别 Windows 风格路径和 URL 编码的 WebView preload 路径；游戏截图使用可见的原生 Game View 或 Cocos GameCanvas；没有游戏渲染表面时报错。
  3. v0.7.5：为 Google Antigravity 提供一键 MCP 配置，把项目级 Streamable HTTP 端点写入 `.agents/mcp_config.json`；Configure + Skills 会把缺失的内置 skill 安装到 `.agents/skills`，Antigravity 与 Codex 都可发现该目录。
  2026-11-19 打开的 Cocos 商店页显示版本 v0.7.2，最近更新时间 2026-11-10，标价免费，Creator 版本要求 v3.8.8。本条的 v0.7.5 以 GitHub Release 为准。
- 来源链接：见下方本条来源链接。下列链接均在 2026-11-19 打开为 HTTP 200。除仓库首页与 Cocos 商店页外，链接都指向 tag `v0.7.5`。
- 核实日（Asia/Shanghai）：2026-11-19
- 引擎版本与平台：与 2026-11-12 的 v0.7.2 条目保持一致，并基于本轮核对。Cocos 商店页仍写 Creator 版本要求 v3.8.8；仓库 README 徽章写 3.8+。4.0 兼容性在已核来源中未说明，待确认。目标平台待确认。README 明确该扩展是 Editor-only，不应作为游戏运行时依赖打进构建包。商店页的 Android / iOS / HTML5 标签不记为该扩展的运行平台。
- 是否已在项目试用：否
- 是否已安装：否
- 授权：tag v0.7.5 的 LICENSE 为 MIT License；Cocos 商店页标价为免费。以各站点条款为准。
- 依赖与权限（仅文档所述，本仓库不安装、不执行）：
  1. 需在 Cocos Creator 中安装扩展（商店或 GitHub Release zip，并校验 `SHA256SUMS.txt`）。2026-11-19 商店页仍为 v0.7.2；若要 v0.7.5，应以 GitHub Release 为准并校验校验和。
  2. 编辑器内嵌 HTTP MCP；README 示例为 `http://127.0.0.1:8765/` ，新项目使用项目派生端口，占用则回退。
  3. Codex 一键配置仍写入 `$CODEX_HOME/config.toml`（默认 `~/.codex/config.toml`），示例为 `[mcp_servers.funplay_cocos]`，`url = "http://127.0.0.1:8765/"`。Antigravity 一键配置写入项目 `.agents/mcp_config.json`。
  4. Configure + Skills 可能安装上述内置 skill；Codex 与 Antigravity 共用 `.agents/skills`，旧内置可迁移且不删除原文件。
  5. 全局安装会写入 `~/.CocosCreator/builtin-extensions/<Creator version>/funplay-cocos-mcp`。
  6. `execute_javascript` 安全检查默认开启，但不是完整沙箱，可被 `safety_checks: false` 关闭；扩展内没有额外审批开关，MCP 工具会直接执行。文件工具限制在当前项目根目录。

### 本条来源链接

- 仓库（github.com/FunplayAI）：<https://github.com/FunplayAI/funplay-cocos-mcp>（2026-11-19 打开为 HTTP 200）
- Release v0.7.5（github.com/FunplayAI）：<https://github.com/FunplayAI/funplay-cocos-mcp/releases/tag/v0.7.5>（2026-11-19 打开为 HTTP 200；Published 2026-11-18T10:00:29Z）
- CHANGELOG（tag v0.7.5 raw）：<https://raw.githubusercontent.com/FunplayAI/funplay-cocos-mcp/v0.7.5/CHANGELOG.md>（2026-11-19 打开为 HTTP 200）
- README（tag v0.7.5 raw）：<https://raw.githubusercontent.com/FunplayAI/funplay-cocos-mcp/v0.7.5/README.md>（2026-11-19 打开为 HTTP 200）
- LICENSE（tag v0.7.5 raw）：<https://raw.githubusercontent.com/FunplayAI/funplay-cocos-mcp/v0.7.5/LICENSE>（2026-11-19 打开为 HTTP 200，MIT License）
- Cocos 商店页（store.cocos.com，页面显示 v0.7.2）：<https://store.cocos.com/app/detail/8913>（2026-11-19 打开为 HTTP 200）
- CHANGELOG（tag v0.7.5 blob）：<https://github.com/FunplayAI/funplay-cocos-mcp/blob/v0.7.5/CHANGELOG.md>（2026-11-19 打开为 HTTP 200）
- README（tag v0.7.5 blob）：<https://github.com/FunplayAI/funplay-cocos-mcp/blob/v0.7.5/README.md>（2026-11-19 打开为 HTTP 200）
- LICENSE（tag v0.7.5 blob）：<https://github.com/FunplayAI/funplay-cocos-mcp/blob/v0.7.5/LICENSE>（2026-11-19 打开为 HTTP 200）

## 2026-11-24 新增

本轮 1 条。不是基础查阅资源，不进入基础查阅资源表。评估为文档核对。未在本用户项目试用，未安装。以下依赖与权限只记录文档与源码所述，本仓库不安装、不执行。

### @alanwalk/cocos-cli v1.0.0

- 资源：@alanwalk/cocos-cli v1.0.0（仓库 alanwalk/cocos-cli，npm 包 `@alanwalk/cocos-cli`）
- 类型：第三方命令行工具（含 Funplay MCP 安装与客户端注册辅助），不是基础查阅文档，也不是官方 `cocos/cocos-cli` 或官方 Codex/Cocos 产品
- 评估：文档核对
- 采用结论：这是 2026-11-23 首次公开发布的第三方 CLI，专门补齐已记录的 Funplay MCP 与官方 Creator 命令行构建之间的安装、生命周期和检查入口，值得追加文档核对。README 与 CHANGELOG 写明：可用本机 Creator 3.8.8 模板创建 2D/3D 项目；离线检查 `.meta`、重复 UUID 与无效序列化引用，查找资源引用，只读查看或比较 Prefab；用 Creator 导出的构建配置走原生命令行打包；`cocos mcp setup/update` 从 Funplay 官方 GitHub Release 安装或更新扩展（校验 `SHA256SUMS.txt`），`ensure/status/doctor/stop/restart` 管理编辑器与 MCP 连接，`register --client` 可为 11 种 Agent 客户端注册 MCP，并可加 `--skills` 安装 Funplay 内置 skill；`mcp preview` 在独立 Edge/Chrome 窗口打开当前场景并采集该标签页运行日志。MCP 场景编辑、资源管理和预览能力仍由已记录的 Funplay MCP 提供，本工具是配套的安装与连接层，不是另一套编辑器协议。未在本用户项目试用。本条不得记成官方 Cocos CLI 的新版本。
- 发布/更新日：GitHub Release v1.0.0 发布于 2026-11-23T14:47:24Z；CHANGELOG 日期为 2026-11-23；npm 包 `@alanwalk/cocos-cli@1.0.0` 发布于 2026-11-23T14:59:35Z。仓库创建于 2026-11-23T04:25:42Z。本条以 v1.0.0 为准。
- 来源链接：见下方本条来源链接。下列链接均在 2026-11-24 打开为 HTTP 200。除仓库首页与 npm 页外，源码与文档链接都指向 tag `v1.0.0`。
- 核实日（Asia/Shanghai）：2026-11-24
- 引擎版本与平台：README 写主要验收版本为 Creator 3.8.8；按项目声明的版本查找编辑器，并搜索 Windows 和 macOS 的常见安装目录，自定义位置可用 `--editor`。作者 VALIDATION.md 称 2026-11-23 在 Windows + Node.js v26.3.0 上验证了创建、离线检查、Web Desktop 构建及项目级 Funplay/Codex 注册；并写明 macOS、其他构建平台，以及真实编辑器中的未保存保护、正常退出和重启仍是独立验收项。4.0 及其他 Creator 版本兼容性在已核来源中未作为已验收范围，待确认。目标平台待确认。构建需要 Creator 支持的 GUI 环境。
- 是否已在项目试用：否
- 是否已安装：否
- 授权：tag v1.0.0 的 LICENSE 为 MIT License（Copyright (c) 2026 alanwalk）；npm 页亦标 MIT。以各站点条款为准。
- 依赖与权限（仅文档与 tag v1.0.0 源码所述，本仓库不安装、不执行）：
  1. Node.js >= 20（`package.json` `engines`）。浏览器预览文档建议 Node.js 22 或更高（需支持内置 WebSocket），并需要本机安装 Edge 或 Chrome。
  2. 全局安装命令为 `npm install -g @alanwalk/cocos-cli`，也可 `npx @alanwalk/cocos-cli`。包的 bin 名为 `cocos`。官方仓库 `cocos/cocos-cli`（本库已记录 0.2.0-beta.1）的 `package.json` 同样把 bin 设为 `cocos`。两者同时出现在 PATH 时会争用同一命令名。
  3. `cocos mcp setup [--global]` / `update` 会请求 `https://api.github.com/repos/FunplayAI/funplay-cocos-mcp/releases/latest`，下载对应 `Funplay.CocosMcp.<tag>.zip` 与 `SHA256SUMS.txt` 并校验 SHA256。项目级安装路径为 `<项目>/extensions/funplay-cocos-mcp`；`--global` 安装路径为 `~/.CocosCreator/builtin-extensions/<Creator版本>/funplay-cocos-mcp`。文档写连接以 Funplay 0.7.6 接口为基准。
  4. `cocos mcp register --client <客户端> [--skills]` 会写入对应 Agent 的 MCP 配置；Codex 为 `.codex/config.toml`。加 `--skills` 时通过已安装的 Funplay 扩展安装其内置 project skills。
  5. `cocos open` / `build` 会启动本机 Creator 进程。`mcp preview` 使用临时浏览器配置打开游戏标签页，将 Console、未捕获异常和浏览器报告的网络错误写入项目 `temp/cocos-cli/preview-*.jsonl`，单次上限 8 MiB。
  6. 运行时依赖为 `commander@14.0.3` 与 `fflate@0.8.3`。未设置 `COCOS_MCP_PORT` 且没有 Funplay 配置文件时，端口按项目派生；已有配置文件省略 `portMode` 时，Funplay 使用固定端口。

### 本条来源链接

- 仓库（github.com/alanwalk）：<https://github.com/alanwalk/cocos-cli>（2026-11-24 打开为 HTTP 200）
- Release v1.0.0（github.com/alanwalk）：<https://github.com/alanwalk/cocos-cli/releases/tag/v1.0.0>（2026-11-24 打开为 HTTP 200；Published 2026-11-23T14:47:24Z）
- npm 包（npmjs.com）：<https://www.npmjs.com/package/@alanwalk/cocos-cli>（2026-11-24 打开为 HTTP 200；1.0.0 发布于 2026-11-23T14:59:35Z）
- CHANGELOG（tag v1.0.0 raw）：<https://raw.githubusercontent.com/alanwalk/cocos-cli/v1.0.0/CHANGELOG.md>（2026-11-24 打开为 HTTP 200）
- README（tag v1.0.0 raw）：<https://raw.githubusercontent.com/alanwalk/cocos-cli/v1.0.0/README.md>（2026-11-24 打开为 HTTP 200）
- LICENSE（tag v1.0.0 raw）：<https://raw.githubusercontent.com/alanwalk/cocos-cli/v1.0.0/LICENSE>（2026-11-24 打开为 HTTP 200，MIT License）
- package.json（tag v1.0.0 raw）：<https://raw.githubusercontent.com/alanwalk/cocos-cli/v1.0.0/package.json>（2026-11-24 打开为 HTTP 200）
- 验收文档（tag v1.0.0 raw）：<https://raw.githubusercontent.com/alanwalk/cocos-cli/v1.0.0/docs/VALIDATION.md>（2026-11-24 打开为 HTTP 200）
- 构建说明（tag v1.0.0 raw）：<https://raw.githubusercontent.com/alanwalk/cocos-cli/v1.0.0/docs/BUILD_HANDOFF.md>（2026-11-24 打开为 HTTP 200）
- CHANGELOG（tag v1.0.0 blob）：<https://github.com/alanwalk/cocos-cli/blob/v1.0.0/CHANGELOG.md>（2026-11-24 打开为 HTTP 200）
- README（tag v1.0.0 blob）：<https://github.com/alanwalk/cocos-cli/blob/v1.0.0/README.md>（2026-11-24 打开为 HTTP 200）

## 2026-11-25 新增

本轮 1 条。不是基础查阅资源，不进入基础查阅资源表。评估为文档核对。未在本用户项目试用，未安装。以下依赖与权限只记录文档所述，本仓库不安装、不执行。

### sfx-skill v0.2.0

- 资源：sfx-skill v0.2.0（仓库 owoevan-dev/sfx-skill）
- 类型：跨引擎游戏音效 Agent Skill（含可编辑分层项目与本地渲染脚本），不是基础查阅文档，也不是官方 Codex/Cocos 产品
- 评估：文档核对
- 采用结论：这是 2026-11-22 首次公开发布的音效设计 skill，本条以 2026-11-24 发布的 v0.2.0 为准，用来补已有知识库里的音效流程缺口。文档写明：不使用音频生成模型，而是由 agent 把每个音效写成可编辑的分层项目（起音、主体、低频、尾音等），用合成音色和可选的 CC0 现场录音渲染变体，把整组调到同一响度，做成接缝可测量的循环，并生成单文件试听页供人听写反馈。项目文件可重复渲染得到同样的音频。安装方式包括 Codex（`codex plugin marketplace add owoevan-dev/sfx-skill` 与 `codex plugin add sfx-skill@sfx-skill`）以及其他 agent 的 `npx skills add owoevan-dev/sfx-skill`。官方导出目标是 Godot、Unity、Unreal、Roblox 和网页，另有不绑定引擎的 `generic`（16-bit 与 24-bit WAV）。已核来源没有 Cocos Creator 的导出目标或导入设置说明，本条不得记成兼容 Cocos。标准音频文件能否按项目需要导入 Creator，待确认。作者写明 Unreal 和 Roblox 的导出是依照官方文档制作，尚未在这两个引擎中实际打开；作者 CI 声称在 Linux、macOS 与 Windows、Python 3.10 到 3.14 上跑测试，并把 Godot 导出实际导入 Godot。这些都是作者自称的验收，不能当作本库或本用户项目的试用通过，也不标推荐已验证。v0.2.0 增加可选的 music-skill / Surge XT 层、读取游戏配乐以便音效引用主题、以及试听页的中日韩英多语言等；同一 7 天窗口内的 v0.1.0–v0.1.3 不另开条目。未在本用户项目试用。
- 发布/更新日：GitHub Release v0.1.0 发布于 2026-11-22T06:41:09Z（首次公开发布）；v0.2.0 发布于 2026-11-24T16:16:32Z（Asia/Shanghai 为 2026-11-25 00:16）。CHANGELOG 中 0.2.0 节未另写日期。本条以 v0.2.0 为准。
- 来源链接：见下方本条来源链接。下列链接均在 2026-11-25 打开，返回正常。除仓库首页外，源码与文档链接都指向 tag `v0.2.0`。
- 核实日（Asia/Shanghai）：2026-11-25
- 引擎版本与平台：已核文档未点名 Cocos Creator，也未点名微信、TapTap 等小游戏目标。导出目标为 Godot、Unity、Unreal、Roblox、网页和 `generic`。运行环境是开发者本机，渲染在 CPU 上离线完成，不需要 GPU。需要 Python 3.10 以上和 NumPy。目标平台待确认。
- 是否已在项目试用：否
- 是否已安装：否
- 授权：tag v0.2.0 的 LICENSE 为 MIT License（Copyright (c) 2026 sfx-skill contributors）。第三方条款见 THIRD_PARTY_NOTICES.md。可选录音来自 FSD50K 中作者在 Freesound 上声明为 CC0 的条目；FSD50K 数据集整体为 CC BY 4.0，本项目只选用其中的 CC0 录音。可选 Surge XT 为 GPL-3.0-or-later，其 FAQ 称用它做出的声音归使用者。以各站点条款为准。
- 依赖与权限（仅文档所述，本仓库不安装、不执行）：
  1. Python 3.10 以上，以及 NumPy（在已安装的 skill 目录执行 `python -m pip install -r skills/sound-effects/requirements.txt`；`doctor` 会打印命令）。
  2. Codex 安装为 `codex plugin marketplace add owoevan-dev/sfx-skill` 再 `codex plugin add sfx-skill@sfx-skill`。其他 agent 可用 `npx skills add owoevan-dev/sfx-skill`，或把 `skills/sound-effects` 复制到该 agent 的 skills 文件夹。
  3. 可选：PATH 上的 FFmpeg，用于导出或导入 Ogg、MP3、FLAC。
  4. 可选录音库：仅在用户同意后，从本项目 GitHub Release 或 Zenodo 上的 FSD50K 下载一次，文档写下载 2.9 GB，导入后连同压缩包约占 7.2 GB；每个文件比对公开校验码。文档写渲染全程离线，不会把数据发送出去。
  5. 可选：[music-skill](https://github.com/owoevan-dev/music-skill)（music-production）与 Surge XT，用于采样乐器层和 Surge 层。未安装时仍可用合成音色。
  6. skill 在开发者本机运行自己的 Python 脚本和已安装的 FFmpeg。不要把这一点写成已在本用户环境验证。

### 本条来源链接

- 仓库（github.com/owoevan-dev）：<https://github.com/owoevan-dev/sfx-skill>（2026-11-25 打开，返回正常）
- Release v0.2.0（github.com/owoevan-dev）：<https://github.com/owoevan-dev/sfx-skill/releases/tag/v0.2.0>（2026-11-25 打开，返回正常；Published 2026-11-24T16:16:32Z）
- Release v0.1.0（github.com/owoevan-dev）：<https://github.com/owoevan-dev/sfx-skill/releases/tag/v0.1.0>（2026-11-25 打开，返回正常；Published 2026-11-22T06:41:09Z）
- CHANGELOG（tag v0.2.0 raw）：<https://raw.githubusercontent.com/owoevan-dev/sfx-skill/v0.2.0/CHANGELOG.md>（2026-11-25 打开，返回正常）
- README 简体中文（tag v0.2.0 raw）：<https://raw.githubusercontent.com/owoevan-dev/sfx-skill/v0.2.0/README.zh-CN.md>（2026-11-25 打开，返回正常）
- LICENSE（tag v0.2.0 raw）：<https://raw.githubusercontent.com/owoevan-dev/sfx-skill/v0.2.0/LICENSE>（2026-11-25 打开，返回正常，MIT License）
- 导出说明（tag v0.2.0 raw）：<https://raw.githubusercontent.com/owoevan-dev/sfx-skill/v0.2.0/skills/sound-effects/references/export.md>（2026-11-25 打开，返回正常）
- SKILL.md（tag v0.2.0 raw）：<https://raw.githubusercontent.com/owoevan-dev/sfx-skill/v0.2.0/skills/sound-effects/SKILL.md>（2026-11-25 打开，返回正常）
- 第三方说明（tag v0.2.0 raw）：<https://raw.githubusercontent.com/owoevan-dev/sfx-skill/v0.2.0/THIRD_PARTY_NOTICES.md>（2026-11-25 打开，返回正常）
- 隐私说明（tag v0.2.0 raw）：<https://raw.githubusercontent.com/owoevan-dev/sfx-skill/v0.2.0/PRIVACY.md>（2026-11-25 打开，返回正常）
- CHANGELOG（tag v0.2.0 blob）：<https://github.com/owoevan-dev/sfx-skill/blob/v0.2.0/CHANGELOG.md>（2026-11-25 打开，返回正常）
- README 简体中文（tag v0.2.0 blob）：<https://github.com/owoevan-dev/sfx-skill/blob/v0.2.0/README.zh-CN.md>（2026-11-25 打开，返回正常）
- 可选配套 music-skill 仓库（github.com/owoevan-dev）：<https://github.com/owoevan-dev/music-skill>（2026-11-25 打开，返回正常；本条不单独归档 music-skill）

## 2026-11-26 新增

本轮 1 条。不是基础查阅资源，不进入基础查阅资源表。评估为文档核对。未在本用户项目试用，未安装。以下依赖与权限只记录文档所述，本仓库不安装、不执行。

### so-hot-right-now v0.2.0

- 资源：so-hot-right-now v0.2.0（仓库 mrsharpoblunto/so-hot-right-now，npm 包 `@thestraylight/so-hot-right-now`）
- 类型：TypeScript 热路径检查器 / Agent Skills（文档写明 Codex 与 Claude Code 均可读同一 Agent Skills 格式），不是基础查阅文档，也不是官方 Codex/Cocos 产品
- 评估：文档核对
- 采用结论：这是 2026-11-25 首次公开发布的热路径检查器，本条以 npm 与 git tag 的 v0.2.0 为准，用来补已有知识库里与性能预算相关的流程缺口。文档写明：按项目配置的引擎入口（roots）沿类型可解析的调用图，检查每帧或每 tick 热路径中的分配、闭包、字符串比较和哈希查找；可用 baseline 文件记录已有问题计数，新增问题会使检查失败，计数下降后也要重新记录 baseline，否则检查同样失败。函数需标记 `@hot` 或 `@hotIgnore <reason>`；匹配不到的根可以写成 `@hot <caller>`；也可用一行 `// hot-path: allow <reason>` 接受单个问题。提供两个 skill：`hot-paths`（编写与修复热路径）和 `hot-paths-setup`（接入配置、寻找 roots、写 config、记录 baseline）。`npx so-hot-right-now skills` 会复制到 `.claude/skills/`（Claude Code）和 `.agents/skills/`（Codex 及其他 Agent Skills 工具）；可用 `--target claude`、`--target codex` 或指定文件夹，也可用 `--global` 复制到用户主目录对应技能目录。也可 `codex plugin marketplace add mrsharpoblunto/so-hot-right-now` 再 `codex plugin add so-hot-right-now@so-hot-right-now`。README 写明 Codex 读取仓库 `.claude-plugin/` 下的 marketplace 文件，一份清单同时给两个 agent。已核来源未点名 Cocos Creator。内置 preset 仅为 browser、webgpu、react、audioWorklet，本条不得记成兼容 Cocos。Creator 工程的 TypeScript 版本、tsconfig 布局，以及更新循环能否配置为 roots，待确认。v0.2.0 相对此前增加 TypeScript 7 原生后端（发布提交写明通过原生后端支持 TypeScript 7，并使 typescript 成为 peer dependency；纳入该 tag 的前一提交为批量处理 TypeScript 7 的类型与符号请求）。同一 7 天窗口内的 npm 0.1.0 与 0.1.1 不另开条目。未在本用户项目试用。
- 发布/更新日：仓库创建于 2026-11-25T21:03:04Z。npm 包首次公开为 `@thestraylight/so-hot-right-now@0.1.0`，发布于 2026-11-25T21:49:04.589Z；0.1.1 发布于 2026-11-25T22:03:06.672Z。git tag `v0.2.0` 指向 commit `3567b1977aa33a69656f881b1530e5a7c72c7099`，该提交时间为 2026-11-25T22:44:43Z。标签页在 2026-11-26 打开为 HTTP 200，页面为 tagged this；GitHub Releases API 列表为空，因此不要写成正式 GitHub Release 对象。发布渠道以 npm 为准。npm `@thestraylight/so-hot-right-now@0.2.0` 发布于 2026-11-25T22:51:21.455Z（Asia/Shanghai 为 2026-11-26 06:51）。registry 的 `dist-tags.latest` 为 0.2.0，该版本 `gitHead` 与上述 tag commit 一致。本条以 v0.2.0 为准。
- 来源链接：见下方本条来源链接。除 npm 包页外，下列链接均在 2026-11-26 打开为 HTTP 200。npm 包页直接请求返回 HTTP 403（Cloudflare 拦截页），不记成页面不存在；包的存在与版本以 registry 为准。除仓库首页、npm 包页与 registry 外，源码与文档链接都指向 tag `v0.2.0`。
- 核实日（Asia/Shanghai）：2026-11-26
- 引擎版本与平台：已核文档未点名 Cocos Creator，也未点名微信、TapTap 等小游戏目标。检查器读取 `tsconfig.json` 所包含的 TypeScript/JavaScript；peer 依赖 TypeScript >= 5.0（文档称支持 5.x、6.x、7.x，并使用项目已安装的 TypeScript 版本）。需要 Node.js >= 22.18。运行在开发者本机的检查/lint 流程，不是游戏运行时依赖。目标平台待确认。Creator 兼容性待确认。
- 是否已在项目试用：否
- 是否已安装：否
- 授权：tag v0.2.0 的 LICENSE 为 MIT License（Copyright (c) 2026 Glenn Conner）。npm 0.2.0 元数据与 `plugins/so-hot-right-now/.claude-plugin/plugin.json` 亦标 MIT。以各站点条款为准。
- 依赖与权限（仅文档所述，本仓库不安装、不执行）：
  1. Node.js >= 22.18。`typescript` 为 peer dependency（>= 5.0），检查器使用项目安装的 TypeScript。
  2. 开发依赖安装示例为 `pnpm add -D @thestraylight/so-hot-right-now typescript`，然后 `npx so-hot-right-now init`，会在当前目录写入 `hot-path.config.mjs`（应放在 `tsconfig.json` 所在目录）。
  3. 常用命令：`npx so-hot-right-now report`、`npx so-hot-right-now baseline`、`npx so-hot-right-now`（相对 baseline 检查，文档建议放入 lint 脚本）。
  4. 技能复制与 Codex plugin 安装命令见采用结论。不要把这些命令写成已在本用户环境执行或验证。
  5. 运行时依赖为 `picomatch`（tag v0.2.0 的 `package.json` 写 `^4.0.7`）。文档写明：只跟踪类型检查器能解析的调用；经 `any` 或计算属性名的调用会中止向下走图。
  6. `init`、skills 复制和 Codex plugin 安装会在项目或用户目录写入配置/技能文件。不要把这一点写成已在本用户环境验证。

### 本条来源链接

- 仓库（github.com/mrsharpoblunto）：<https://github.com/mrsharpoblunto/so-hot-right-now>（2026-11-26 打开为 HTTP 200）
- Git tag 页（不是正式 GitHub Release 对象）：<https://github.com/mrsharpoblunto/so-hot-right-now/releases/tag/v0.2.0>（2026-11-26 打开为 HTTP 200，页面为 tagged this。同日 GitHub Releases API `GET /repos/mrsharpoblunto/so-hot-right-now/releases` 返回 HTTP 200 且正文为 `[]`，`releases/tags/v0.2.0` 返回 HTTP 404）
- npm 包页（www.npmjs.com）：<https://www.npmjs.com/package/@thestraylight/so-hot-right-now>（2026-11-26 直接请求返回 HTTP 403，页面为 Cloudflare 拦截，不记成页面不存在；包与版本以 registry 为准）
- npm registry：<https://registry.npmjs.org/@thestraylight/so-hot-right-now>（2026-11-26 打开为 HTTP 200；`dist-tags.latest` 为 0.2.0；0.2.0 发布于 2026-11-25T22:51:21.455Z；`gitHead` 为 `3567b1977aa33a69656f881b1530e5a7c72c7099`）
- jsDelivr package.json（cdn.jsdelivr.net）：<https://cdn.jsdelivr.net/npm/@thestraylight/so-hot-right-now@0.2.0/package.json>（2026-11-26 打开为 HTTP 200，version 0.2.0，license MIT）
- jsDelivr README（cdn.jsdelivr.net）：<https://cdn.jsdelivr.net/npm/@thestraylight/so-hot-right-now@0.2.0/README.md>（2026-11-26 打开为 HTTP 200）
- LICENSE（tag v0.2.0 raw）：<https://raw.githubusercontent.com/mrsharpoblunto/so-hot-right-now/v0.2.0/LICENSE>（2026-11-26 打开为 HTTP 200，MIT License）
- README（tag v0.2.0 raw）：<https://raw.githubusercontent.com/mrsharpoblunto/so-hot-right-now/v0.2.0/README.md>（2026-11-26 打开为 HTTP 200）
- package.json（tag v0.2.0 raw）：<https://raw.githubusercontent.com/mrsharpoblunto/so-hot-right-now/v0.2.0/package.json>（2026-11-26 打开为 HTTP 200）
- plugin.json（tag v0.2.0 raw）：<https://raw.githubusercontent.com/mrsharpoblunto/so-hot-right-now/v0.2.0/plugins/so-hot-right-now/.claude-plugin/plugin.json>（2026-11-26 打开为 HTTP 200，version 0.2.0，license MIT）
- marketplace.json（tag v0.2.0 raw）：<https://raw.githubusercontent.com/mrsharpoblunto/so-hot-right-now/v0.2.0/.claude-plugin/marketplace.json>（2026-11-26 打开为 HTTP 200）
- hot-paths SKILL.md（tag v0.2.0 raw）：<https://raw.githubusercontent.com/mrsharpoblunto/so-hot-right-now/v0.2.0/plugins/so-hot-right-now/skills/hot-paths/SKILL.md>（2026-11-26 打开为 HTTP 200）
- hot-paths-setup SKILL.md（tag v0.2.0 raw）：<https://raw.githubusercontent.com/mrsharpoblunto/so-hot-right-now/v0.2.0/plugins/so-hot-right-now/skills/hot-paths-setup/SKILL.md>（2026-11-26 打开为 HTTP 200）
- rules.md（tag v0.2.0 raw）：<https://raw.githubusercontent.com/mrsharpoblunto/so-hot-right-now/v0.2.0/plugins/so-hot-right-now/skills/hot-paths/rules.md>（2026-11-26 打开为 HTTP 200）
- docs/plugins.md（tag v0.2.0 raw）：<https://raw.githubusercontent.com/mrsharpoblunto/so-hot-right-now/v0.2.0/docs/plugins.md>（2026-11-26 打开为 HTTP 200）
- LICENSE（tag v0.2.0 blob）：<https://github.com/mrsharpoblunto/so-hot-right-now/blob/v0.2.0/LICENSE>（2026-11-26 打开为 HTTP 200）
- README（tag v0.2.0 blob）：<https://github.com/mrsharpoblunto/so-hot-right-now/blob/v0.2.0/README.md>（2026-11-26 打开为 HTTP 200）
- package.json（tag v0.2.0 blob）：<https://github.com/mrsharpoblunto/so-hot-right-now/blob/v0.2.0/package.json>（2026-11-26 打开为 HTTP 200）
