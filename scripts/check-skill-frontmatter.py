#!/usr/bin/env python3
"""Fail if any */SKILL.md frontmatter is not strict YAML or is missing required fields.

Usage: python3 scripts/check-skill-frontmatter.py
Rules: frontmatter parses with yaml.safe_load; `name` equals the directory;
`description` is a non-empty string; voice skills (*-voice) end their
description with the "Not affiliated with or endorsed by ..." sentence.
Tip: a description containing ": " must be wrapped in double quotes.
"""
import glob, os, sys
import yaml

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
errors = []
paths = sorted(glob.glob(f'{REPO}/*/SKILL.md'))
for p in paths:
    slug = os.path.basename(os.path.dirname(p))
    text = open(p).read()
    if not text.startswith('---'):
        errors.append(f'{slug}: no frontmatter'); continue
    try:
        fm = yaml.safe_load(text.split('---')[1])
    except yaml.YAMLError as e:
        errors.append(f'{slug}: invalid YAML ({str(e).splitlines()[0]})'); continue
    if fm.get('name') != slug:
        errors.append(f"{slug}: name is {fm.get('name')!r}")
    desc = fm.get('description')
    if not isinstance(desc, str) or not desc.strip():
        errors.append(f'{slug}: missing description')
    elif slug.endswith('-voice') and 'Not affiliated with or endorsed by' not in desc:
        errors.append(f'{slug}: voice description lacks the Not affiliated line')
for e in errors:
    print(e)
print(f'{len(paths)} skills checked, {len(errors)} problems')
sys.exit(1 if errors else 0)
