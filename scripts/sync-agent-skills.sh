#!/usr/bin/env bash
set -euo pipefail

repo_root="$(cd "$(dirname "$0")/.." && pwd)"
cd "$repo_root"

skill_dirs=()
for dir in */; do
  dir="${dir%/}"
  if [[ -f "$dir/SKILL.md" ]]; then
    skill_dirs+=("$dir")
  fi
done

if [[ "${#skill_dirs[@]}" -eq 0 ]]; then
  echo "No skills found."
  exit 1
fi

for target in .agents/skills .claude/skills .cursor/skills; do
  rm -rf "$target"
  mkdir -p "$target"
  for skill in "${skill_dirs[@]}"; do
    ln -s "../../$skill" "$target/$skill"
  done
  echo "Synced ${#skill_dirs[@]} skills to $target"
done
