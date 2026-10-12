# ExecPlan Standard

仅将本标准用作后备或补充。适用的仓库合同可以增加要求或替代这些默认规则。

## Core contract

ExecPlan 是自包含（self-contained）、持续维护的动态文档（living）、以结果为中心的设计与执行文档。仅拥有相关工作树和单份计划的贡献者，必须能够在没有先前聊天记录或私有机器上下文时理解、实施、验证、暂停、恢复和修复该工作。

先解释用户可见的目的，再说明实施细节。以通俗语言定义不明显的术语。写明精确的路径、模块、命令、工作目录、预期观察结果、接口、依赖项、安全约束和恢复行为。验收必须证明行为真实可用，而非仅展示看似合理的修改。

当进度、发现或决策变化时，保持计划准确。更新所有受影响部分，并追加带日期的变更说明，解释计划为何变化。

## Required sections

每份计划均包含并持续维护以下标题：

1. `Purpose / Big Picture`
2. `Progress`
3. `Surprises & Discoveries`
4. `Decision Log`
5. `Outcomes & Retrospective`
6. `Context and Orientation`
7. `Plan of Work`
8. `Concrete Steps`
9. `Validation and Acceptance`
10. `Idempotence and Recovery`
11. `Artifacts and Notes`
12. `Interfaces and Dependencies`

`Progress` 对新计划默认采用 [progress-contract.md](progress-contract.md) 的结构化 JSON，带时间戳的复选框由发布工具生成，并反映每一个停止点。已有仓库合同优先；旧格式继续可读，明确修订或接入才迁移。`Surprises & Discoveries` 将重要观察与简洁证据配对。`Decision Log` 记录选择、理由、日期和作者；适用独立门禁时还记录条件性授权证据。`Outcomes & Retrospective` 将结果与原始目的对照，并记录剩余缺口和经验。

叙述部分先以散文书写。仅在列表、表格和片段可使计划更易执行或验证时使用它们。当 Markdown 文件仅包含计划时，不要以外层代码围栏包裹。

## Authoring and execution

确定方案前，阅读适用说明、架构、接口、源代码、测试和仓库状态。解决会实质影响实施的决策；不要将其留给执行者。使用可独立验证的里程碑，且仅在原型能降低具体不确定性时引入原型。

一份计划只拥有一个目标。将新发现的独立目标记录为另一任务的候选项，而非扩展当前计划。仅请求使用此 skill 本身不授予编写计划、实施变更、提交、推送或进行外部操作的权限。当用户请求实施且当前任务授权、产品模式与仓库规则允许时，编写可在无需例行编写后批准的情况下流入执行。

执行时，当前连续任务已明确绑定且唯一的精确计划路径可复用，但须核实路径和适用合同；未绑定、绑定冲突或无法唯一确定时才请求路径。不得按最近修改时间、文件名相似度或目录顺序猜选。路径用于选择执行工件，并非批准门。沿获授权计划推进至下一里程碑，无需询问例行后续步骤；但遇到待处理或 `superseded` 批准门、授权缺失、合同冲突、破坏性操作、外部写入、特权要求、完整性漂移或实质范围扩张时停止。

适用独立业务或仓库门禁时，添加一条包含以下内容的 `Decision Log` 条目：

- `authorization_state`: `not-required`, `approval-pending`, `approved`, or `superseded`;
- `authorization_source`: the accountable user/owner and concrete request, or a durable decision path and revision;
- `authorization_evidence`: dated or revisioned evidence that the source approved the exact decision and scope;
- `authorized_scope`: the decision revision, normalized repository/file boundary, and protected invariants.

agent 可以记录批准，但不能自行创建批准；没有可追责证据的 `approved` 标签必须失效关闭。批准仅可在同一决策修订、匹配或更窄的范围及文件允许清单，且受保护不变量不变时继承。例行进度、发现、验证证据和非实质执行细节更新保留授权。实质的 TO-BE、目标、接口、持久化/科学/安全合同或不变量变更，将其标为 `superseded`。运行时、工具、sandbox、特权、破坏性操作、外部写入或购买、基线/写入前原像和高风险恢复检查仍相互独立。

## Repository placement defaults

优先遵循仓库定义的位置和命名。若均不存在，将新计划存放在 `docs/exec-plans/active/YYYY-MM-DD-<short-kebab-name>.md`，并在验证与回顾完成后将完成的计划移至 `docs/exec-plans/archive/`。

叙述正文默认使用简体中文；用户或适用仓库合同明确指定另一语言时，遵从该指定。始终保留规范的英文 section headings。计划可引用已检入的 `.agent/PLANS.md`，但必须嵌入独立执行所需的全部任务特定上下文。不得让计划依赖 personal skill、未提交记忆或不可访问的对话。

## Cross-repository additions

当任务跨越多个仓库时，如已定义则确定权威协调仓库。若未定义权威且存储选择影响所有权，停止并获得该决策，切勿任意选择。

为每个参与仓库记录：

- absolute path, role, branch, and baseline commit;
- initial dirty state and the policy for pre-existing changes;
- exact allowed and prohibited paths;
- the versioned interface or artifact exchanged with other repositories;
- the validation command and expected result;
- commit and rollback requirements.

将其他仓库的未提交工作树视为不稳定输入。优先使用已声明的版本化工件，包含 schema 或格式版本、适用时的完整性哈希和产生该工件的提交。使每个仓库中的验证和提交均可独立审查。仓库合同要求时，在相关提交元数据中使用共享计划标识符。

## Closure and recovery

关闭前，运行每项验收检查，记录简洁证据，更新所有持续维护的动态部分，列出相关提交或工件，并解释所有剩余缺口。说明哪些步骤可安全重试以及如何从部分工作中恢复。仅在计划的可观察结果已被证明后归档。

若某一步失败，保留无关的用户工作及诊断失败所需证据。不得为图方便扩展允许清单、重写治理规则或删除意外文件。指出阻塞因素和最小安全恢复操作。
