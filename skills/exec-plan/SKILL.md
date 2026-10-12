---
name: exec-plan
description: Create, review, maintain, execute, and close self-contained ExecPlans for complex, multi-hour, cross-module, or cross-repository work. Use when the user requests an ExecPlan or repository instructions require one; do not use for small bounded tasks or ordinary explanations.
metadata:
  short-description: Create and run self-contained execution plans
---

# Exec Plan（执行计划）

将 ExecPlan 用作复杂工作的持久化设计与执行工件。选择此 skill 并不授权创建文件、实施变更、提交、外部操作，或绕过任何批准门。

## 先确定适用权威

行动前，读取当前 `AGENTS.md` 指令链及其点名的所有仓库 `.agent/PLANS.md`。完整阅读被明确指定的 ExecPlan。

按以下顺序适用要求：

1. 当前任务授权、产品模式、权限与安全规则。
2. 适用的 `AGENTS.md` 指令链。
3. 协调仓库及参与仓库的 `.agent/PLANS.md` 文件，以及精确指定的 active ExecPlan。
4. [references/execplan-standard.md](references/execplan-standard.md) 中的默认规则。

仓库合同优先于此 skill 的默认规则。对于跨仓库工作，由协调合同决定计划的位置与生命周期；每个参与仓库则管理自身的所有权、路径、安全与验证。合同冲突时停止并报告冲突；不得自行编造优先级。

## 选择一个 intent

- **Author:** 检查相关仓库状态，并仅创建一份自包含（self-contained）的 ExecPlan。阅读标准参考并调整 [assets/execplan-template.md](assets/execplan-template.md)。存在独立门禁时记录适用的授权证据。遇到待处理的仓库必需门禁时停止；当用户请求实施且当前授权、产品模式与仓库规则均允许时，编写可在无需例行再次批准的情况下衔接执行。
- **Review:** 对照其管辖合同评估计划，并报告具体缺口。除非用户同时请求修改，否则保持只读。
- **Maintain:** 随工作进展更新持续维护的动态文档（living sections）及所有受影响的叙述部分。例行进度、发现、验证证据和非实质执行细节不会使既有授权失效。不得向 active plan 添加独立目标。
- **Execute:** 当前连续任务已明确绑定且唯一的精确计划路径时，复用并核实该路径；未绑定、绑定冲突或无法唯一确定时才请求路径。路径用于选择执行工件，本身并非批准门；不得按最近修改时间、文件名相似度或目录顺序猜选。完整阅读计划和管辖合同，验证所有适用的授权证据，只遵循获授权的范围，并在每一个停止点保持计划准确，无需为例行后续步骤询问用户。
- **Close/archive:** 运行指定验证，记录证据与提交，完成 `Outcomes & Retrospective`，并仅按仓库合同指示归档计划。

在 Author 时、当地合同缺失或不完整时，或当地合同没有定义所需生命周期规则时，阅读 [references/execplan-standard.md](references/execplan-standard.md)。生成的 ExecPlan 必须在没有此 personal skill 或先前聊天记录时仍可理解和执行。

## 授权记录

适用独立业务或仓库门禁时，在既有 `Decision Log` 中记录
`authorization_state`、`authorization_source`、`authorization_evidence` 和
`authorized_scope`；无门禁计划省略该记录或使用 `not-required`。agent 可以记录批准，
但不能自行创建批准。获批记录仅在同一决策修订、匹配或更窄的规范化范围及文件允许清单
（allowlist），且受保护不变量（protected invariants）不变时继续适用。实质变更将其标记为
`superseded` 并回到管辖门禁。独立的运行时、工具、sandbox、特权、破坏性操作、外部操作、
基线/写入前原像（preimage）与高风险恢复检查仍必须执行。

## 可同步的进度维护

新计划默认使用 [结构化进度合同](references/progress-contract.md) 和模板中的 `execplan-progress/v1` 区；仓库合同优先。旧计划仅在明确修订或接入时迁移，不因为只读审查就改写。

Author 初始化稳定身份、目标、里程碑和未知项；Maintain/Execute 在里程碑、阻碍、依赖或验收变化时更新 JSON 及受影响正文，并在交接、暂停、结束前运行 `scripts/execplan_progress.py publish <计划路径>`、再 `check`。先依据实际证据维护内容，再发布；发布不判断原意、不产生批准或验收。Review 只运行 `check`，不发布。Close/archive 保留评价和 ID，归档后核对新路径。

JSON 是当前里程碑的唯一人工维护区；复选框摘要由脚本生成。已有权威账本的事实只引用或生成带修订号的摘要，不另外手写相同状态。没有工具时仍可执行自包含计划，但对外记录待同步；不要手工伪造指纹。详见合同中的字段、命令和兼容边界。

发布前逐项核对 done 里程碑的证据是否覆盖其标题承诺，并检查正文是否仍声明该部分待核对或未交接；存在矛盾时先修正状态或收窄表述。synced 仅表示版本一致，不代替此语义核对。缺少实际执行所需的路径、命令或原始记录时明确记录交接缺口，不把模板占位或个人技能路径当成可独立执行的证据。
