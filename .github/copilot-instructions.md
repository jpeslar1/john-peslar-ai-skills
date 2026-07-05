# John Peslar AI Skills Repository Instructions

This repository contains public agent skills for Codex, Claude Code, Cursor, and other tools that support the `SKILL.md` pattern.

## Skill Rules

- Every skill must live in a root-level folder named exactly like the skill.
- Every skill folder must include `SKILL.md`.
- Frontmatter must include `name`, `description`, `license`, and `metadata`.
- `name` must be lowercase hyphen-case and match the folder.
- `description` should include practical trigger phrases.
- Keep each `SKILL.md` concise. Move templates, examples, and source notes to `references/`.
- Do not include private client details, API keys, internal repo paths, or proprietary credentials.
- Use MIT license for public skills.

## Copy Rules

- Write direct, practical copy for founders, operators, marketers, and builders.
- Avoid hype that cannot be backed up.
- Use normal hyphens instead of em dashes or en dashes.
- Make every skill useful as a standalone artifact.

## Marketplace

When adding a skill, update:

- `README.md`
- `EXAMPLES.md` if the skill needs a user-facing example
- `.claude-plugin/marketplace.json`
- `.agents/plugins/marketplace.json`
- The relevant `plugins/<collection>/` folder
