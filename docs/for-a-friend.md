# 给第一次使用者的一页说明

ExecPlan 是一份随工作更新的实施记录，适合需要多阶段执行、审查和接力的任务。请先按 [README](../README.md#安装到-codex) 安装完整 skill，随后在 Codex 中明确说：`使用 $exec-plan，为这个跨模块工作制定自包含的实施计划，先核对项目 AGENTS.md 和 .agent/PLANS.md。`

打开 [完整虚构示例](../examples/fictional-plan.md)。它演示目标、里程碑、来源、验收证据与关闭说明。进度中的 `published_sha256` 与生成摘要由脚本维护。

在临时目录演练一次更新：复制该示例，修改正文的一句说明，运行 `python3 skills/exec-plan/scripts/execplan_progress.py check <副本路径>`，预期退出码为 2；随后运行同一脚本的 `publish <副本路径>` 和 `check <副本路径>`，预期最后是 `synced`。试着编辑一个里程碑及其证据，再重复发布。复制 [模板](../skills/exec-plan/assets/execplan-template.md) 编写新计划时，先替换所有占位符并写入可在你项目中执行的路径与命令。

有问题或建议可开 Issue；愿意修改文档或脚本可 Fork、建分支、运行测试后发 PR。软件架构图另见 [Diagram Workbench](https://github.com/gbm19950414-ux/diagram-workbench)。
