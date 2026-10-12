# execplan-progress/v1

这是通用执行进度交换格式，不是 Life Projects 的领域模型。正文仍需包含独立执行所需上下文；脚本不可用不阻止工作，只令消费者显示待同步。

## 格式和唯一维护者

在 `## Progress` 中放置唯一 `<!-- execplan-progress:start -->` / `<!-- execplan-progress:end -->`，中间为 json 代码块。模板给出完整例子。当前里程碑由 JSON 维护，`execplan-summary` 区是生成结果；迁移前的 Progress 移至带日期的历史记录，不静默丢弃。

必填：schema（固定 execplan-progress/v1）、plan_id（稳定，与路径无关）、title、objective、execution_status、assessment、milestones、next_action、updated_at（带时区 ISO 时间）、published_sha256（初始空）。可选：project_id、goal_id（独立于计划 ID 的显式关联）、gap、authority_ref（已有账本路径/对象 ID/修订号）。

execution_status 为 planned/active/paused/blocked/closed/unknown。assessment 为 outcome（unassessed/met/not_met/insufficient_evidence）、summary、evidence 文本列表；met 必须有证据，但脚本不能验证证据真实性。milestones 是 id/title/state/depends_on/evidence 对象列表；state 为 todo/doing/blocked/done/cancelled/unknown。依赖仅同计划的稳定里程碑 ID，必须唯一、存在且无环。不从顺序推断依赖，不从全部完成、目录或 closed 推断 met。未知日期不补造；updated_at 是本次核对时间，不是历史任务完成时间。

已有账本拥有的任务不复制进 milestones；使用 authority_ref，里程碑仅描述计划自身的实施与验收结果。计划目标与具体目标 ID 不要求一一对应，跨计划接续由消费者明确关联。

## 发布和读取

从技能根运行 `python3 scripts/execplan_progress.py check /absolute/plan.md`（只读）或 `python3 scripts/execplan_progress.py publish /absolute/plan.md`（显式写入）。check 的退出码 0 表示已发布或兼容旧格式（输出区分 synced/legacy），2 表示待发布，1 表示格式错误。可选 `--expected-sha256` 指原始文件字节 SHA-256，防止发布已被他人改变的前像。

publish 校验、生成摘要，再记录指纹并原子替换；不会自动改状态、核对时间、正文、批准或验收。使用配套 .publish.lock 协作锁和写前前像检查；编辑者仍应避免同时修改同份文档。已发布且未改变时重复运行不改字节。

指纹算法：读取原始 UTF-8 文本，定位唯一 JSON 区，仅将该区 `published_sha256` 的字符串值替换为空字符串（保留引号、空白和其余全部字节），对结果计算 SHA-256。不排除正文、JSON、生成摘要或时间。合法且指纹匹配、摘要与 JSON 一致才为 synced；仅结构合法不等于已同步。消费者独立实现/随应用固定携带此版本，不在运行时导入个人技能目录。

旧格式返回 legacy，不自动迁移；未知版本和重复身份显式报错。缺失、未发布、错误的来源都不能覆盖上次可靠结果。协议检查不等于内容真实、用户认可或允许执行。
