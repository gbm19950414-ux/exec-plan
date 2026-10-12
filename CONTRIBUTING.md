# 参与贡献

明确缺陷或建议请开 Issue；方向讨论请用 Discussions。修改时 Fork 仓库、在分支上提交、运行 `python3 -m unittest discover -s skills/exec-plan/scripts -p 'test_*.py'`，再提交 PR 并说明预期行为与验证结果。不要提交真实消费者计划、个人资料或机器路径。

修改 skill 的授权或进度语义时，阅读 `skills/exec-plan/references/execplan-standard.md` 与 `progress-contract.md`，并让新示例保持自包含。自动测试与 `synced` 只能证明格式及同步行为，不能代替实际业务验收。
