---
name: regal-gentleman-barber-brief
description: Use this Regal Gentleman-inspired barber consultation lens to turn hairstyle goals and reference photos into a precise, realistic men's haircut brief, especially for medium-length changes, tapers, and transformations. Not affiliated with or endorsed by Regal Gentleman, Liam Jennings, or its barbers.
license: MIT
metadata:
  author: john-peslar-ai
  version: "0.1.0"
---

# Regal Gentleman-Inspired Barber Brief

Use this skill when the decision is less about trends and more about the conversation in the barber chair. It is an independent interpretation of Regal Gentleman's public transformation and education content. It does not claim to be a particular barber's opinion. Read [the source map](references/source-map.md) when current source context or attribution is needed.

## Core lens

A useful haircut recommendation has to translate into a result a barber can execute. Reference photos are helpful only when they show a realistic match for texture, density, and starting length. Name the shape, the retained length, the transition, and the growth path.

Treat large changes as a sequence when possible. A cut can make the present look sharper while leaving enough length to grow into the next option.

## Use this skill for

- Preparing for a barber appointment
- Moving from long or overgrown hair to a controlled medium or short style
- Deciding between a taper, fade, scissor-led cut, or a length-preserving clean-up
- Choosing and annotating reference photos

## Workflow

1. Define the starting point and commitment level: maintenance interval, how much length is safe to lose, styling ability, and whether a future grow-out matters.
2. Separate the decision into top, sides, corners, crown, neckline, fringe, and sideburns. Do not collapse it into “short sides, long top.”
3. Create a barber brief in visible terms. If the client has good reference photos, explain exactly what each photo contributes and what should not be copied.
4. Include a growth path. State how the cut should look at appointment day, two to four weeks, and when the next trim would be useful.
5. Give a quick styling plan that makes the intended silhouette visible, plus a fallback for days without heat styling.

## The brief must answer

- Where should the side transition begin and end?
- Is the desired result blended, disconnected, or scissor-led?
- Which areas should retain weight to avoid an overly round or overly severe profile?
- How should the fringe and crown move naturally?
- Is the neckline tapered, natural, or squared?
- What should the barber not take too short?

## Output format

```text
Appointment goal:
[one sentence]

Starting-point assessment:
[what is usable now and the main constraint]

Exact barber brief:
- Top: ...
- Sides and corners: ...
- Crown and fringe: ...
- Neckline and sideburns: ...
- Avoid: ...

Reference-photo notes:
[what to point to, and what not to expect from it]

Growth and styling plan:
[what it should look like now, later, and how to style it]
```

## Guardrails

- Do not promise a transformation that ignores the person’s starting length, texture, or hairline.
- Do not advise someone to cut their own major transformation or give unsafe clipper instructions.
- Do not make medical claims about recession, shedding, or scalp health from photos.
- Do not state or imply that any Regal Gentleman barber personally recommends the cut.
- Always flag that a barber should adjust length and technique in person.
