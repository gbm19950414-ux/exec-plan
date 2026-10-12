# 故障排查

| 现象 | 检查及处理 |
|---|---|
| Codex 找不到 `$exec-plan` | 运行 `sh scripts/install-skill.sh status`，确认链接仍指向保留的 checkout；必要时重启 Codex。 |
| 安装报告冲突 | 已有同名文件或链接；先核对原安装。脚本不会覆盖。 |
| `python3` 版本太低 | 运行 `brew install python`，确保新版在 `PATH` 前面，再用 `python3 --version` 确认不低于 3.11。 |
| `check` 输出 `pending` | 进度或正文已改变，检查内容后运行 `publish`，再 `check`。 |
| `check` 输出 `legacy` | 旧格式仍可读；只有明确决定修订或迁移时才转换。 |
| `publish` 报冲突 | 文件在读取后被改变；重新读取最新内容，核对差异后再次发布。不要覆盖他人的修改。 |
| 退出码 0 但工作未完成 | `synced` 只代表指纹与摘要一致，需另外核对 `assessment` 与真实验收证据。 |

仍无法解决时开 Issue，附 Python 版本、命令与脱敏后的输出。
