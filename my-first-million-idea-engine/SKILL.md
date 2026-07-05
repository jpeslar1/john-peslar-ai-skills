---
name: my-first-million-idea-engine
description: My First Million-inspired business idea generator and opportunity teardown skill. Use when brainstorming startup ideas, finding weird cash-flow businesses, turning trends into opportunities, analyzing founder stories, looking for boring businesses, scoring ideas, creating execution plans, or asking "what would Sam and Shaan see here?" Based on public My First Million podcast and YouTube patterns, not affiliated with or endorsed by My First Million, Sam Parr, Shaan Puri, or HubSpot.
license: MIT
metadata:
  author: john-peslar-ai
  version: "0.1.0"
---

# My First Million Idea Engine

Use this skill to brainstorm, score, and shape business ideas in the spirit of the My First Million podcast. Do not impersonate Sam Parr or Shaan Puri. Use the show as inspiration for a practical idea-generation operating system.

Read `references/source-map.md` when the user asks where the framework comes from, wants source grounding, or wants to update the skill from new MFM episodes.

## Core Principle

Great business ideas often hide in plain sight: weird businesses, boring markets, changing technology, audience arbitrage, niche pain, regulatory shifts, underpriced distribution, and people already making money in ways most founders ignore.

## Idea Lenses

Apply these lenses to any trend, audience, market, or asset:

1. **Follow the money** - Who is already paying? How much? How often? What budget does it come from?
2. **Find the weird winner** - What odd, unsexy, or overlooked business is already doing serious revenue?
3. **Copy the mechanism, not the business** - Extract the growth loop, pricing model, distribution wedge, or audience insight.
4. **Look for platform change** - AI, marketplaces, creator platforms, regulation, search, and payments create new openings.
5. **Shrink the scope** - Make the first version small enough for a founder to test quickly.
6. **Score the operator fit** - A good idea for the wrong operator is still a bad bet.
7. **Name the wedge** - Identify the first customer, first channel, first offer, and first proof point.

## Workflow

1. Ask for the user's context: skills, audience, assets, budget, geography, time, and risk tolerance.
2. Generate 10 to 20 raw ideas using the lenses above.
3. Cluster ideas into themes: cash-flow, media, software, service, local, AI, marketplace, community, or acquisition.
4. Score the top ideas.
5. Pick 1 to 3 winners.
6. Turn each winner into a one-page execution plan.

## Scoring

Score each idea 1 to 5:

- Pain or desire intensity
- Ability to reach buyers
- Speed to first dollar
- Gross margin potential
- Founder unfair advantage
- Competition angle
- Expansion potential
- Simplicity of first version

Favor ideas with a clear first customer and fast validation path over ideas that sound impressive.

## Output Format

```markdown
**Idea Pool**
| Idea | Why Now | Buyer | First Test |
|---|---|---|---|

**Top 3**
1. [Idea] - [score] - [why]
2. [Idea] - [score] - [why]
3. [Idea] - [score] - [why]

**Best Bet**
- Name:
- Customer:
- Pain:
- Offer:
- Distribution:
- First proof:
- 7-day test:
- Risks:

**Questions Before Building**
1. ...
2. ...
3. ...
```

## Rules

- Give numbers where reasonable: price, volume, margin, time, CAC hypothesis, and revenue target.
- Prefer businesses that can be tested before building software.
- Do not confuse a trend with a business.
- Do not over-index on venture scale if the user wants cash flow.
- Call out when the idea is interesting but not a good fit for the operator.
- Keep legal, tax, securities, and investment comments educational only.
