---
name: linkedin-signal-miner
description: Find LinkedIn buying signals and turn them into warm outreach angles, lead lists, comment strategies, and follow-up workflows. Use when the user wants to identify prospects from posts, comments, job changes, funding news, hiring, pain language, competitor complaints, tool adoption, or content engagement. Trigger on "LinkedIn signals", "buying intent", "warm outreach", "social selling", "prospect list", "comment strategy", "lead mining", or "find people to DM".
license: MIT
metadata:
  author: john-peslar-ai
  version: "0.1.0"
---

# LinkedIn Signal Miner

Use this skill to turn LinkedIn activity into useful prospecting intelligence. Focus on signals that imply pain, urgency, budget, timing, or authority.

Read `references/signal-categories.md` when building a signal library or daily mining workflow.

## Signal Types

- **Pain signal** - They complain about a problem the offer solves.
- **Trigger event** - They changed roles, raised money, launched a product, or started hiring.
- **Tool signal** - They mention using or replacing a relevant tool.
- **Competitor signal** - They complain about a competitor or ask for alternatives.
- **Expansion signal** - They are growing team, region, budget, or channel.
- **Content engagement signal** - They comment on posts about the problem.
- **Authority signal** - They own the budget or influence the decision.

## Workflow

1. Define ICP and offer.
2. List likely trigger events.
3. Write search phrases and post patterns.
4. Classify signals by strength.
5. Build the outreach angle from the signal.
6. Write a non-generic comment or DM.
7. Track replies and refine the signal library.

## Signal Strength

| Score | Meaning |
|---:|---|
| 5 | Direct pain plus authority plus timing |
| 4 | Clear pain or trigger with likely authority |
| 3 | Relevant interest but unclear urgency |
| 2 | Weak fit or weak timing |
| 1 | Generic engagement only |

## Output Format

```markdown
**ICP**
[summary]

**Best Signals**
| Signal | Why It Matters | Search Pattern | Strength |
|---|---|---|---:|

**Outreach Angles**
1. ...
2. ...
3. ...

**DM Templates**
[templates tied to specific signals]

**Daily Workflow**
1. ...
2. ...
3. ...

**Disqualifiers**
[who not to contact]
```

## Rules

- Do not write fake personalization.
- Anchor every message to a real observed signal.
- Lead with relevance, not flattery.
- Prefer helpful comments before DMs when the relationship is cold.
- Track which signals convert, not just which signals are easy to find.
