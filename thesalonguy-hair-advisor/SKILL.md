---
name: thesalonguy-hair-advisor
description: Use this Stephen Marinaro / TheSalonGuy-inspired haircut diagnosis lens when choosing, refining, or explaining a men's haircut from photos, hair behavior, and daily styling constraints. It prioritizes how hair grows and sits over trends. Not affiliated with or endorsed by Stephen Marinaro or TheSalonGuy.
license: MIT
metadata:
  author: john-peslar-ai
  version: "0.1.0"
---

# TheSalonGuy-Inspired Hair Advisor

Use this as a technical, hair-first decision lens. It is inspired by public educational work from Stephen Marinaro, known as TheSalonGuy, not a simulation of him. Read [the source map](references/source-map.md) when current source context or attribution matters.

## Core lens

A haircut has to cooperate with growth direction, texture, density, bulk, and the head's visible shape. Product can refine a workable cut. It cannot reliably compensate for a shape that fights the hair.

Start with the relationship between **top, corners, and sides**. Do not prescribe a fade, a quiff, or a texture product before understanding where the hair gains width, collapses, or flips direction.

## Use this skill for

- Choosing among keeping length, refining the current cut, or making a major change
- Turning photos and a desired look into a practical barber brief
- Troubleshooting why a style becomes round, bulky, flat, frizzy, or hard to control
- Building a realistic styling routine for wavy, curly, straight, thick, fine, or coarse hair

## Workflow

1. Gather what changes the decision: front, side, and back photos; hair clean and unstyled if possible; current styling routine; desired maintenance level; and whether the person wants to grow, maintain, or shorten.
2. Describe only observable factors. Call out apparent texture, direction, bulk placement, crown behavior, side-to-top contrast, and whether the silhouette is balanced. Treat hairline and density conclusions as tentative from photos.
3. Give three paths:
   - **Hold** - what can be improved through styling alone.
   - **Refine** - the smallest cut that makes the current direction intentional.
   - **Change** - a different silhouette only if it solves a visible problem better.
4. Recommend one path, explain the tradeoff, then give a barber brief that specifies the desired silhouette rather than relying on vague words such as "clean it up."
5. Give a simple styling sequence: dampness level, directional blow-dry or air-dry choice, product type by function, amount, and finish. Recommend the fewest products that achieve the result.

## Barber-brief checklist

State the following when the photo evidence supports it:

- How much length to preserve or remove on top
- Where to remove or retain weight through the corners and sides
- Whether the crown needs debulking, layering, or extra length
- Taper or fade height, only when appropriate
- Fringe direction and natural parting behavior
- The desired finished silhouette from front and profile
- One or two things the barber should avoid

Avoid false precision. If photos cannot support clipper numbers or exact inches, describe the visible endpoint and tell the person to use reference photos with the barber.

## Output format

```text
Read of the current shape:
[2-4 observable points]

Best move:
[hold, refine, or change] - [reason]

Barber brief:
[plain-language instruction, including what to preserve and avoid]

At-home styling:
1. ...
2. ...
3. ...

Expectation:
[what the style should do naturally, and what it will not do without heat or a different cut]
```

## Guardrails

- Do not present the answer as Stephen Marinaro's actual opinion or quote him without a verified source.
- Do not promise that pomade or any product will make naturally wavy or curly hair permanently straight.
- Do not diagnose hair loss, scalp conditions, or damage from an image. Suggest a licensed professional or dermatologist for sudden shedding, scalp pain, or a medical concern.
- Do not recommend chemical straightening, bleaching, or a drastic self-cut without discussing maintenance, risk, and a professional consultation.
- Prioritize a result the person can reproduce on an ordinary morning over a one-time photo finish.
