# 01 · 调研、逆向与证据交接

日期：2026-11-04。本文区分“本轮读到的材料”“材料报告的实验”和“我们的设计”，不声称重新执行用户本机研究。

## 1. 来源分层

| ID | 来源 | 本轮读取范围 | 适合支持什么 |
|---|---|---|---|
| R1 | [用户上传的第五轮综合报告](sources/最简PersonalAgent完整调研与设计取舍.md) | 全文，结论、版本范围及第一至十一节 | 本机研究进展、报告陈述的观察/隔离实验、局限和建议 |
| R2 | [原 Codex 研究任务](sources/codex_rea_grok_bot_task.md) | 全文 | 原研究意图、授权边界、调查优先级；不是执行结果 |
| R3 | [早期分析包](legacy/grok_bot_rea_analysis_20261103.zip) | 12 个成员文件全文，包括六项测试脚本/结果、索引与四份原创候选提示 | 历史代码分析范围；早期设计演变；不证明当前实现 |
| R4 | [早期安装尝试](legacy/rea_install_attempt_20261103.zip) | 全部成员文件，包括命令、错误和未实跑离线脚本 | 旧容器安装失败的历史事实；不是当前本机环境 |
| C1 | 本次聊天中用户的逐轮要求 | 当前上下文中的完整需求和纠偏 | 产品约束；已整理到主文档 U01–U10 |

源文件字节哈希和本轮读取状态在 [sources/MANIFEST.json](sources/MANIFEST.json)。用户原报告不做修订；更新后的设计另写，避免来源与推论混杂。

R1 的全文已经在本轮阅读。它链接的专题、样本、脚本没有随附件提供；“报告描述原函数已测”不能改写成“本轮亲自检查了该原函数”。

### 冲突时怎样处理

用户明确要求决定产品目标；R1 第十一节用于细化同一报告早前的未知结论。新样本和旧样本分别成立，不能用新样本修改历史记录。我们独立的设计可与参考产品不同，但要标为设计决定。

历史任务 R2 的“只研究”范围已经结束，不阻止本次交接进入实现。旧容器的 REA=false 和新本机的 REA 已运行也不冲突：环境和执行时间不同。

## 2. 已做调研如何沿用

此前对话调研过 Pi、OpenClaw、Grok Bot、Hermes、nanobot、NanoClaw、Letta，也讨论过持久工作流、消息 inbox/outbox、MCP 与渠道接入。这轮的任务是整合用户报告，不是重新核实这些项目的最新版本。

| 历史参考 | 已影响我们设计的方向 | 本轮保留方式 |
|---|---|---|
| Pi | 小内核、模型/循环/扩展分层、配置化角色 | 作为架构思路，不依赖未经本轮核实的具体 hook 名称 |
| OpenClaw | 接入、会话、目标续跑、团队路由与调度分层 | 参考职责分离，不把它与 Grok 样本拼成同一产品 |
| Hermes | 程序性经验、定向消息、执行/投递分别跟踪 | 作为已有方案动机；新代码需核实实际依赖 API |
| nanobot | 把一次模型工具循环与会话/长期目标分开 | 反映在 Task/Run/Goal 边界 |
| NanoClaw | 核心可理解、明确隔离、扩展不全部内置 | 不把逻辑工作目录当安全沙箱 |
| Letta | 长期身份、记忆和 conversation 分开 | 反映在 Bot、Room 和记忆范围 |
| 持久工作流与 outbox | 状态、外部副作用、重试和投递的边界 | 独立实现最小协议；不先上 Temporal/Kafka 等平台 |

早前对话出现过 Pi `agent_before_settle` 等 API 名称，也出现过“当前默认功能”的判断。本次附件没有为这些 API 提供新证据；Claude 真要集成时再查对应固定版本，不把聊天里提过等同于已验证依赖。

以下仅是历史参考入口，本轮没有重新访问或核验：

- Pi：`https://github.com/earendil-works/pi`
- OpenClaw：`https://docs.openclaw.ai/`
- Hermes：`https://github.com/NousResearch/hermes-agent`
- nanobot：`https://github.com/HKUDS/nanobot`
- NanoClaw：`https://github.com/nanocoai/nanoclaw`
- Letta：`https://docs.letta.com/`
- REA：`https://github.com/morluto/rea`

这些入口不是本轮发现的佐证；本轮产品机制事实以 R1 的证据级别和边界为准。

## 3. 样本、工具和版本

据 R1“证据与版本范围”及第十一节：

| ID | 样本/工具 | 已报告取得的内容 | 不能跨越的边界 |
|---|---|---|---|
| REA | 6.8.0 | 本机固定版本实际分析；第四轮另分析 12 个原字节模块，第五轮分析同包 EVAL 原模块 | 本交接未拿到 CLI/MCP 原输出，不代称本轮实跑 |
| Node | 隔离 26.13.0 | 本机运行环境 | 不改写为本交接容器的 Node 版本 |
| G078 | 官方桌面 0.78.1 | Linux 包、ASAR/JS；Windows 0.78.1.0 只读观察 | 桌面版本不等于 Host/模型服务版本 |
| HOST | 官方公开更新 2b353c7 | 公开 tgz、同源 SHA、Host bundle | 发布产物不证明账号云电脑实际部署版本 |
| H018 | 历史第三方归档 | 固定 commit 的 bundle 与切片 | 不证明官方来源或当前仍启用 |
| EVAL | HOST 同包 sand-eval-runner.cjs | 更完整评测运行器与提示装配链 | 不是已确认的生产服务端，未运行整个评测程序 |
| Muse | 官方网页 | 网页实际 REA 分析 | 受资格限制的其他产物和后台未取得 |

R1 记录的 HOST 主文件 SHA-256：

```text
328b715bed51ac13f549319f84af259b80936cd984e161af4c45a0faad0f1c35
```

下列 HOST LF 锚点仅对这个主文件有效。EVAL 的精确行号和字节证据在未附带的第五轮专题中，不能照抄 HOST 行号给 EVAL。

## 4. 发现登记：结论、范围、设计影响

### F01 · 长期 Bot、Worker、Room 不应合并

**报告内容：** H018 长期 peer 与 parent/worker 路径不同；当前 Host 另外观察到 peer 记录和群 Temporal 调度。Bot 可长期存在，Worker 关联有限委派；会话不应作为任务唯一身份。  
**证据级别：** R1 第一节描述的历史/当前静态与既有隔离材料，具体当前服务端创建销毁未知。  
**设计影响：** 稳定 Bot + 临时执行身份，共用 loop；用户直达；任务可跨多次 run。

### F02 · 当前群回传链有匹配和过时保护

**可见链：** 本地群入口 → 成员校验/分发 → runTemporalGroupMemberTurn → requestGrokBotRoomMemberTurn → 服务端未知 → receiveRoomMemberTurnResult → nonce/room 匹配 → 删除 pending/resolve → epoch 检查 → posts。

**HOST 锚点：** LF722149 起 Temporal 适配器；LF758648 起分发；LF760252 起 epoch。R1 第二节引用第三轮相关 15 项。  
**边界：** ACCEPTED/DUPLICATE 不是完成；peer 本地记账和内存去重不是接收方执行证据；服务端事务与恢复不可见。  
**设计影响：** 可查询委派；要求版本进入子任务与产物；晚到结果隔离保留；投递与验收分开。

### F03 · Goal idle 清零不等于有效进展

**原函数锚点：** GoalContinuationActionHandler LF595585–595760；ToolCountingStateTracker/createToolCountingMiddleware LF585170–585234；身份/时钟 LF490199 起。

R1 第三节报告原函数隔离结果：

- 无工具前三次续跑，第四次尝试前暂停，累计续跑仍为 3。
- model-step 只看 descriptors，工具未执行即可清零；连续 20 次同类无效描述仍清零。
- single-step 看 hasToolCall，包含失败信息仍清零。
- 完整 handle 在 await record 后加一；已记录失败结果清零，record 抛错时不加一。
- 模型异常保留已增加计数；暂停、身份不符、非法 ID 不进入模型。
- 时钟倒退不倒扣；无 anchor 的等待不计入工作时长。

**边界：** 局部控制流，不含真实工具/网络/模型/生产 scheduler，不能推出线上无限运行。  
**设计影响：** 活动、失败、进展和预算必须独立。

### F04 · 严格结束函数与 goal idle 是两个层次

R1 第三节说明 resolveStepTurnEnd（LF587738 起）要求明确成功结果，能在并行工具失败时阻止结束。它不证明目标进展，与 F03 不矛盾。

**设计影响：** turn settling 先解决待执行/失败工具；task acceptance 再判任务；goal review 再判长期目标。不能一个布尔 done 覆盖全部。

### F05 · 电脑 Worker 还有专用失败 breaker

R1 第十一节报告 EVAL 的电脑操作 Worker 专用保护：连续 20 次失败触发，成功清零，审核拒绝/取消事件跳过，触发后锁定。

**边界：** 不是所有 Bot 通用能力，不是有效进展检查，也不是我们应复制的默认阈值。  
**设计影响：** 失败熔断独立建模；成功但重复无新信息也需停滞判断；外层预算仍兜底。

### F06 · 同包 EVAL 提供具体提示装配链

R1 第五、十一节：buildAgentForRun → createSystemPromptGeneratorForRun → renderSections/renderSystemPrompt → system；同包包含完整 createSystemPromptAssembly 与基础提示构造。

报告的默认章节顺序：base/spotlight/voice → profile/用户/团队 → multitask/时区 → memory/会话 → automations/tasks/skills/channels/成员目录/发送规则/MCP → 电脑环境。

缺功能可省略；override/frozenPrompt 改变结果；任务章节对 subagent/system override 不启用；工具 schema 单独构建，实际挂载工具也影响能力描述。记忆政策留 system，部分事实通过 gate 进入 UserInfo user。

**边界：** EVAL 的真实实现，不是生产最终请求。没有原始文件时不能给 Claude 伪造完整 prompt 或替它补动态变量。  
**设计影响：** 分层上下文构造、有来源/版本、有消息角色、有实际工具清单；测试不同 actor 与压缩状态下的输出。

### F07 · 压缩恢复具有 epoch 语义

R1 第十一节：同 epoch 冻结旧前缀，用 instructions_update 表达变化；下一 epoch 重读 live。依赖未解析保留旧值，明确删除才清空；切换对象重新准备 notes；压缩代次变化刷新 profile，异常清理临时代次。

**边界：** 原 helper 隔离验证，不是完整真实压缩回合。  
**设计影响：** 删除/未加载语义分开，上下文快照可追踪；即时取消/撤权必须由 runtime 执行，不能等下一次摘要。

### F08 · 记忆来源与受众必须另有强制边界

R1 第四节：user/bot owner 映射 /me、/bot；always_in_context/library；behavior、workstream；source/speaker/created_at；untrusted_raw/pending_review；team/user audience。

**HOST 锚点：** LF717318 schema；LF777025–777096 类型和默认集合；LF777102–777231 helpers；LF777254 起提示常量。

原 helper 测试报告：未信任前缀解析前跳过，旧 shard/未知类型不进该 view，按路径/时间/ID 排序；同 ID 此 helper 不去重；audience 只传递；路径前缀检查不能证明上游规范化。JSONL parser 用供应预验证记录的替身，没验证真实 Zod/后端隔离/抽取/遗忘。

**关键条件：** 8 种注册类型，但默认集合只有 4 种旧 profile/journal；dreamPrompt 没有在已读范围追到定时执行链。  
**设计影响：** 任务账本、长期记忆、摘要分开；事实有来源与范围；存储层检查访问，不依赖目录名称或 prompt。

### F09 · 同伴提醒有多个变体，启用仍未知

HOST LF774042–774085；R1 第五节。提醒包括不能代表用户批准、可沿原会话代问用户、后台结果写回 owner notes 等变体；本轮尚未追到生产选择/注入条件。

**设计影响：** 传递原始授权引用；同伴消息作为有身份的数据，而不是变成高优先级用户命令。不要选一段提示冒充当前产品统一行为。

### F10 · 调度配置、历史和远端收敛不同

R1 第十一节：服务接口有 workflow/run/过滤/重试资格；后台实现不可见。FileAutomationStore 分配置与运行历史；同 Bot 变更队列仅进程内串行。CloudSync 是 Bot 删除后的 routine 清理，流程列出→删除→回读；回读空也可消解一次 RPC 错误，本地 pending Set 未见跨实例恢复代码。

**设计影响：** 记录 desired/observed 及未决清理；只在确有远端适配器时添加对账；RPC 失败可能结果已生效，需要读回。不要凭模块名画通用云同步系统。

### F11 · Routine 执行权限有真实分支约束

R1 第十一节报告六项原分支：routine run 拒绝创建另一个 routine；更新必须确认唤醒来源、仅能改自身、不得重新启用；需要 review 而 Host 无法 review 时拒绝更新。

**设计影响：** 周期 Worker 负责当前任务和发现，目标负责人/策略接口负责持久策略变更。不是照搬全部限制，而是明确派生与计划扩展的权限边界。不能据分支测试宣称调度闭环已完整验证。

### F12 · 当前生产后端仍是未知边界

R1 结论与第九/十一节：普通 Box 模型入口已退役；当前生产执行器、数据库、队列、租约、事务、全局预算和真实开关未取得。已有 HOST/EVAL 可继续离线研究，但不能替代服务端证据。

**设计影响：** 小框架独立实现可靠语义，不以“完整复刻 Grok 云端”为前置目标；不要把旧 Host 直接当运行底座。

## 5. 测试账目，不合并口径

| 范围 | 报告数量 | 本交接材料 | 应怎样描述 |
|---|---:|---|---|
| 前两轮 | 105 | R1 统计与链接；专题未附 | 历史样本与桌面等研究用例，不是当前云端测试 |
| 第三轮 HOST | 40 | R1 统计/部分机制描述；专题未附 | 当前取得 HOST 原函数相关验证，部署状态未知 |
| 第四轮 HOST | 25 | R1 详细摘要与复现入口；脚本未附 | goal 及 memory helpers 的隔离测试 |
| 第五轮 HOST | 22 | R1 第十一节 | 与 EVAL 18 合计新增 40，报告全部通过 |
| 第五轮 EVAL | 18 | R1 第十一节 | 评测运行器相关隔离测试，未跑完整评测程序 |
| 真实远端模型 | 0 | R1 第十节 | 不能报告线上/自主任务成功率 |
| 早期 ChatGPT H018 probe | 6 | R3 提供脚本与结果，但不含被测第三方模块原件 | 历史隔离测试，不重复并入本机轮次 |
| 早期对话所称机制实验 | 7 | 当前包未包含该独立实验原件 | 仅历史对话陈述，不计入本交接可复核结果 |

本轮只进行文档/来源/包完整性检查，没有执行上述任意一组原函数测试。即便以后复跑，也要记录具体脚本、样本哈希、依赖替身、退出码，不能沿用上一轮的“通过”。

## 6. 缺失原件与恢复路径

综合报告内 12 个相对链接的专题未随本轮上传。清单在 sources/MANIFEST.json，包含当前官方 Host 深挖、第五轮专题、第四轮验证、协作、提示、长期任务和 Muse 等。

用户本机研究根（R1 第十节给出，待确认）：

```text
C:\Users\asus\Documents\Codex\2026-11-03\github-rea-grok-bot-muse-personal\work\research\grok-bot-rea
```

R1 已给第四轮原入口，读取脚本并核对目录后再执行：

```powershell
Set-Location 'C:\Users\asus\Documents\Codex\2026-11-03\github-rea-grok-bot-muse-personal'
python work/research/grok-bot-rea/scripts/verify-phase4.py
```

据报告该脚本验证主文件 SHA 和 12 个模块原字节，然后用隔离 Node 跑 25 用例，不启动 Grok、模型或私人聊天。本交接未审阅该脚本，接手者仍需先读取核查。第五轮命令在对应专题，未在汇总中提供，不猜测文件名。

本机先前额度已满、云电脑休眠。那是研究时点记录，不推断今天仍然如此，也不自动唤醒或增加付费额度。可继续离线，不依赖真实账号实验启动产品实现。

## 7. 继续研究的优先级

仅为解除实际实现中的不确定性而补证。优先核对本地第五轮记录与哈希；按需要继续 EVAL turn settle、Worker revival、state adapter 与 gates。对它们当前知道“值得追”，不知道“已证明如何运行”。

新服务端证据和真实账号实验需要独立范围与授权。我们的最小实现不必等待所有这些未知解锁。开源实现应基于行为要求独立重写，第三方原提示和 bundle 留私有目录。
