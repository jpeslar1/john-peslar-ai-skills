---
name: ai-workflow-architect
description: Design practical AI workflows, agents, automations, SOPs, and human approval loops for business operations. Use when turning a manual process into an AI-assisted workflow, mapping tools and data sources, deciding what to automate versus keep human, creating an implementation plan, or auditing an existing process for AI leverage. Trigger on "automate this", "AI workflow", "AI agent", "SOP", "manual process", "operations automation", "Claude workflow", "Codex workflow", or "where can AI save time?"
license: MIT
metadata:
  author: john-peslar-ai
  version: "0.1.0"
---

# AI Workflow Architect

Use this skill to turn messy business operations into practical AI workflows. Optimize for reliable execution, clear handoffs, and fast implementation, not impressive diagrams.

Read `references/workflow-map.md` when the user wants a full workflow map, SOP, or implementation spec.

## Core Principle

AI automation works when the workflow is explicit: clear trigger, clean inputs, defined decisions, bounded tool access, human approval points, and measurable output quality.

## Workflow

1. **Map the current process**
   - Trigger
   - Inputs
   - Tools
   - Human decisions
   - Outputs
   - Failure points
   - Time spent

2. **Classify each step**
   - Automate: repetitive, rule-based, low-risk
   - Assist: judgment-heavy but draftable
   - Human approval: customer-facing, financial, legal, reputational, or irreversible
   - Do not automate: unclear, high-risk, or low-volume

3. **Design the AI workflow**
   - Agent role
   - Data sources
   - Tool permissions
   - Prompts or skills needed
   - Memory or knowledge base needed
   - Human review gates
   - Logging and audit trail

4. **Write the implementation plan**
   - Week 1: manual-assisted version
   - Week 2: partial automation
   - Week 3+: deeper integration only after quality proof

## Output Format

```markdown
**Current Workflow**
[summary]

**Automation Map**
| Step | Current Owner | AI Role | Human Gate | Risk |
|---|---|---|---|---|

**Recommended Agent Design**
- Trigger:
- Inputs:
- Tools:
- Knowledge:
- Output:
- Approval:
- Logs:

**Implementation Plan**
1. ...
2. ...
3. ...

**Risks**
- ...

**First Test**
[smallest useful workflow to run this week]
```

## Rules

- Start with the smallest workflow that proves value.
- Never remove human approval from high-risk steps until quality is measured.
- Prefer plain files, tables, forms, and checklists before complex infrastructure.
- Name what can break.
- Include observability: logs, status, error handling, and review queues.
