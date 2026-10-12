# ExecPlan（执行计划）

这个 Codex skill 为复杂、跨模块或跨仓库工作建立和维护**自包含的实施计划**。计划记录目标、步骤、决策、实际证据和恢复办法，让另一位协作者仅凭仓库与计划就能接续工作。它不自行产生业务批准；`check` 的同步成功也不代表成果已经验收。

首次使用请先阅读 [一页上手指引](docs/for-a-friend.md)。进度格式在 [progress-contract.md](skills/exec-plan/references/progress-contract.md)，模板在 [execplan-template.md](skills/exec-plan/assets/execplan-template.md)。跨工具的架构图工作由独立的 [Diagram Workbench](https://github.com/gbm19950414-ux/diagram-workbench) 负责；本轮共享实施的唯一计划位于其 `docs/exec-plans/active/2026-10-12-share-workbench-and-execplan.md`。

## 安装到 Codex

首版支持 Apple 芯片 Mac、Codex 和 Python 3.11+。进度脚本使用 Python 标准库及 POSIX 文件锁；原生 Windows 不在首版支持范围。

```sh
git clone https://github.com/gbm19950414-ux/exec-plan.git
cd exec-plan
git checkout v0.1.0-rc.2
sh scripts/install-skill.sh install
sh scripts/install-skill.sh status
python3 -m unittest discover -s skills/exec-plan/scripts -p 'test_*.py'
python3 skills/exec-plan/scripts/execplan_progress.py check examples/fictional-plan.md
```

安装脚本只链接完整 `skills/exec-plan` 目录到 `~/.agents/skills/exec-plan`，不覆盖已有同名文件。Codex 未显示 skill 时重新启动，并用 `$exec-plan` 明确调用。脚本的第二个参数可指定临时 skills 目录，便于演练。排查见 [故障排查](docs/troubleshooting.md)。

## 在项目中使用

让 Codex 使用 `$exec-plan` 编写计划时，先检查项目 `AGENTS.md` 和 `.agent/PLANS.md`。在空白项目中，使用 [模板](skills/exec-plan/assets/execplan-template.md) 建立计划，并写入真实路径、命令、预期结果和决策证据。参照 [完整虚构示例](examples/fictional-plan.md) 学习进度与关闭流程。

计划的 `Progress` JSON 是里程碑状态的维护区。编辑后运行：

```sh
python3 skills/exec-plan/scripts/execplan_progress.py publish /absolute/path/to/plan.md
python3 skills/exec-plan/scripts/execplan_progress.py check /absolute/path/to/plan.md
```

`check` 只读，退出码 0 表示已同步或兼容旧格式，2 表示需要发布，1 表示错误；要同时看输出中的 `synced` 或 `legacy`。`publish` 写入生成摘要和指纹，重复运行且内容不变时保持字节不变。它不会填写证据、改变批准或将计划标为已验收。

若消费者项目或应用必须在**没有个人 skill 安装**的环境中继续维护进度，将 `skills/exec-plan/scripts/execplan_progress.py` 固定复制到项目的 `tools/`，连同协议版本与来源标签纳入版本控制；之后调用项目自己的副本。skill 文本只是操作说明，计划正文仍须自包含。

## 更新、回退与协作

使用 `git fetch --tags`，切换到目标版本标签后链接会使用该版本；不要把 checkout 移走。旧标签可用于回退。`sh scripts/install-skill.sh uninstall` 只移除指向当前 checkout 的本工具链接。已有同名安装必须由用户核对来源后手工处理。

发现问题请开 Issue，开放性建议可用 Discussions；修改请 Fork、提交分支与 PR，并附验证结果。详见 [贡献指南](CONTRIBUTING.md) 和 [更新记录](CHANGELOG.md)。本仓库原创内容使用 [MIT 许可证](LICENSE)。
