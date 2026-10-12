#!/bin/sh
set -eu

skill_name="exec-plan"
repo_root=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd -P)
source_dir="$repo_root/skills/$skill_name"
action=${1:-status}
destination=${2:-"$HOME/.agents/skills"}
link="$destination/$skill_name"

if [ ! -f "$source_dir/SKILL.md" ]; then
  printf 'Missing skill: %s\n' "$source_dir" >&2
  exit 1
fi

case "$action" in
  status)
    if [ -L "$link" ] && [ "$(readlink "$link")" = "$source_dir" ]; then
      printf 'Installed: %s -> %s\n' "$link" "$source_dir"
    elif [ -e "$link" ] || [ -L "$link" ]; then
      printf 'Conflict: %s already exists\n' "$link" >&2
      exit 1
    else
      printf 'Not installed: %s\n' "$link"
    fi
    ;;
  install)
    if [ "$(uname -s)" != Darwin ] || [ "$(uname -m)" != arm64 ]; then
      printf 'This release supports Apple Silicon macOS (arm64).\n' >&2
      exit 1
    fi
    command -v python3 >/dev/null 2>&1 || { printf 'Install Python 3.11 or newer: brew install python\nThen check: python3 --version\n' >&2; exit 1; }
    python3 -c 'import sys; raise SystemExit(sys.version_info < (3, 11))' || { printf 'Make Python 3.11 or newer the active python3: brew install python\nThen check: python3 --version\n' >&2; exit 1; }

    if [ -L "$link" ] && [ "$(readlink "$link")" = "$source_dir" ]; then
      printf 'Already installed: %s\n' "$link"
      exit 0
    fi
    if [ -e "$link" ] || [ -L "$link" ]; then
      printf 'Conflict: %s already exists; no files changed.\n' "$link" >&2
      exit 1
    fi
    mkdir -p "$destination"
    ln -s "$source_dir" "$link"
    printf 'Installed: %s -> %s\n' "$link" "$source_dir"
    if ! git -C "$repo_root" describe --exact-match --tags HEAD >/dev/null 2>&1; then
      printf 'Tip: check out a release tag to keep the installed skill at a fixed version.\n'
    fi
    printf 'If Codex does not show the skill, restart Codex.\n'
    ;;
  uninstall)
    if [ -L "$link" ] && [ "$(readlink "$link")" = "$source_dir" ]; then
      rm "$link"
      printf 'Removed owned link: %s\n' "$link"
    elif [ -e "$link" ] || [ -L "$link" ]; then
      printf 'Conflict: %s belongs to another installation; no files changed.\n' "$link" >&2
      exit 1
    else
      printf 'Already absent: %s\n' "$link"
    fi
    ;;
  *)
    printf 'Usage: scripts/install-skill.sh {install|status|uninstall} [skills-directory]\n' >&2
    exit 2
    ;;
esac
