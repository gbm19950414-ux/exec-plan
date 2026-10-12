# <Short, action-oriented title>

此 ExecPlan 是一份持续维护的动态文档。随着工作推进，保持 `Progress`、`Surprises & Discoveries`、`Decision Log` 和 `Outcomes & Retrospective` 准确。存在管辖仓库合同时在此说明，同时保持本计划自包含。

## Purpose / Big Picture

说明变更后用户获得什么，以及如何观察到其正常工作。

## Progress

<!-- execplan-progress:start -->
```json
{
  "schema": "execplan-progress/v1",
  "plan_id": "replace-with-stable-plan-id",
  "title": "本轮交付名称",
  "objective": "写明希望成立的可观察结果",
  "execution_status": "planned",
  "assessment": {
    "outcome": "unassessed",
    "summary": "尚未验收",
    "evidence": []
  },
  "milestones": [
    {
      "id": "m1",
      "title": "第一个可独立验证的里程碑",
      "state": "todo",
      "depends_on": [],
      "evidence": []
    }
  ],
  "next_action": "记录下一项具体动作",
  "updated_at": "2026-09-28T00:00:00+08:00",
  "published_sha256": ""
}
```
<!-- execplan-progress:end -->

<!-- 填写真实身份与带时区核对时间；publish 生成复选框摘要。 -->

## Surprises & Discoveries

- Observation: 记录重要的意外事实。
  Evidence: 引用简洁的命令结果、测试结果或检查过的工件。

## Decision Log

- Decision: 记录重要选择。
  Rationale: 解释为何选择该方案。
  Date/Author: YYYY-MM-DD / 姓名或角色。

- Authorization: 对无门禁工作省略此条目，或使用 `not-required`。适用独立门禁时，
  记录其授权而非自行创建授权。
  `authorization_state`: `not-required`, `approval-pending`, `approved`, or
  `superseded`.
  `authorization_source`: 可追责的用户/所有者及其请求，或持久决策路径和修订。
  `authorization_evidence`: 精确决策和范围的带日期或修订证据；`approved` 必需。
  `authorized_scope`: 决策修订、规范化仓库/文件边界及受保护不变量。

## Outcomes & Retrospective

将完成的行为与原始目的对照；记录缺口和经验。

## Context and Orientation

向不了解仓库背景的读者说明相关当前状态。定义不明显的术语并写明精确路径。

## Plan of Work

以散文描述有序、可独立验证的里程碑和预期编辑。

## Concrete Steps

写明精确的工作目录、命令和简短的预期观察结果。

## Validation and Acceptance

定义可观察的验收行为、输入、输出和测试预期。

## Idempotence and Recovery

说明安全重试、部分失败处理、回滚以及对无关工作的保护。

## Artifacts and Notes

保留简洁证据、重要片段、哈希或指向版本化工件的链接。

## Interfaces and Dependencies

写明所需模块、类型、服务、数据格式、版本、签名和所有权边界。

Change note (YYYY-MM-DD): 初始创建；说明本计划的来源和目的。
