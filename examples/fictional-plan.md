# 核对虚构发票的合计

这是随仓库交付的**虚构示例**。从本仓库根目录操作即可重复观察验收结果；没有真实业务方或真实发票。

## Purpose / Big Picture

读取两项虚构费用，检查 ID 不重复且声明的合计等于实际求和。运行校验脚本时应输出 `OK total=17; entries=2`。

## Progress

<!-- execplan-progress:start -->
```json
{
  "schema": "execplan-progress/v1",
  "plan_id": "fictional-invoice-total-v1",
  "title": "核对虚构发票合计",
  "objective": "样本的唯一费用 ID 与合计能被脚本检查",
  "execution_status": "closed",
  "assessment": {
    "outcome": "met",
    "summary": "示例脚本对两项费用返回预期合计；仅证明虚构数据的演示行为",
    "evidence": [
      "从仓库根运行 python3 examples/fictional-project/check.py，得到 OK total=17; entries=2"
    ]
  },
  "milestones": [
    {
      "id": "input",
      "title": "固定两项虚构费用及声明合计",
      "state": "done",
      "depends_on": [],
      "evidence": [
        "examples/fictional-project/expenses.json 包含 5 和 12，声明合计 17"
      ]
    },
    {
      "id": "check",
      "title": "验证 ID 与实际求和",
      "state": "done",
      "depends_on": [
        "input"
      ],
      "evidence": [
        "python3 examples/fictional-project/check.py 输出 OK total=17; entries=2"
      ]
    }
  ],
  "next_action": "如需用于真实项目，复制模板并替换所有虚构输入与证据",
  "updated_at": "2026-10-12T00:00:00+08:00",
  "published_sha256": "f50a07dde83c31f06eb6a54bed84f21e01704e41ec037339c9f434d711a5f2a1"
}
```
<!-- execplan-progress:end -->

<!-- execplan-summary:start -->
<!-- Generated from the JSON above; edit the JSON, not these checkboxes. -->
- [x] (2026-10-12T00:00:00+08:00) input · 固定两项虚构费用及声明合计 [完成]
- [x] (2026-10-12T00:00:00+08:00) check · 验证 ID 与实际求和 [完成]
<!-- execplan-summary:end -->

## Surprises & Discoveries

示例输入只有两项，检查范围明确；真实发票可能需要货币精度与来源核对，本示例不作这些判断。

## Decision Log

2026-10-12，示例作者：使用整数金额与两个唯一 ID，只演示自包含计划、校验及进度同步。此示例没有业务批准门；若复制到其他项目，须重新核对其指令与授权。

## Outcomes & Retrospective

按样本运行校验得到预期输出。`check` 证明此文档的进度摘要与正文同步，不证明外部发票真实性。目标只涉及虚构输入和演示脚本。

## Context and Orientation

计划位于 `examples/fictional-plan.md`；输入位于 `examples/fictional-project/expenses.json`，检查逻辑位于同目录 `check.py`。工作目录为本仓库根，可由 `git rev-parse --show-toplevel` 确认。没有外部服务或个人路径。

## Plan of Work

固定样本输入，使用一个读取相邻 JSON 的 Python 脚本检查唯一 ID 和合计，然后记录运行证据并关闭计划。

## Concrete Steps

从仓库根运行 `python3 examples/fictional-project/check.py`；成功时打印 `OK total=17; entries=2`，出错时退出非零。修改此计划的正文或 JSON 后，运行 `python3 skills/exec-plan/scripts/execplan_progress.py publish examples/fictional-plan.md`，再运行同脚本的 `check` 子命令。

## Validation and Acceptance

实际样本输出必须与上述文本一致。将 `claimed_total` 暂改为 18 的临时副本应失败；不要在仓库原件上留此修改。`check` 输出 `synced` 只代表文档同步。示例结果与真实消费者项目各自的验收相互独立。

## Idempotence and Recovery

重复运行检查不修改输入；重复 `publish` 且文本不变时保持字节相同。若脚本失败，保留 JSON 与错误输出，修复样本或计划后重新检查，不覆盖其他文件。

## Artifacts and Notes

验收命令及预期输出已写入 `Progress`；本仓库的 CI 再次执行该命令和进度 `check`。

## Interfaces and Dependencies

Python 3.11+ 标准库；`expenses.json` 包含 `expenses` 数组，每项有唯一文本 `id` 与整数 `amount`，`claimed_total` 为整数。进度协议是 `execplan-progress/v1`，与消费者具体业务数据分开。

Change note (2026-10-12): 建立完整的虚构演示计划与输入。
