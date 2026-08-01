# Kellen-style outbound feedback patterns

This reference distills recurring outbound copy feedback patterns from Kellen Casebeer of The Deal Lab (https://thedeallab.com/). Use it to produce feedback that feels like the extracted Kellen feedback without impersonating him.

## Core beliefs

1. Brevity usually wins.
   - Aim for 40-80 words when possible.
   - Use 3-5 short lines, often one sentence each.
   - Split longer emails into brief, normal brief, and slightly longer test versions.

2. Framing beats wording.
   - The question is not “is this sentence polished?”
   - The question is “what frame does this put the buyer in?”
   - Strong frames make the recipient think: “That sounds like my situation.”

3. Buyer psychology matters more than sender credibility.
   - Buyers care about their pain, opportunity, risk, status, priorities, and internal incentives.
   - They rarely care about the sender’s company, process, or claims until relevance is established.
   - Sender-centric “we” lines often add nothing.

4. Agitation plus empathy beats soft politeness.
   - Disrupt status quo.
   - Be fair, not apologetic.
   - Agitation should feel observant and honest, not gotcha-y.
   - “Chippy empathy” can work: self-aware, slightly cheeky, but not needy.

5. Skepticism is the default state.
   - Big guarantees, stacked proof, and “we booked X meetings” often trigger doubt.
   - Overclaiming makes the email feel like a commodity vendor pitch.
   - Reduce certainty until the buyer has a reason to believe.

6. The first line must stand alone.
   - Do not rely on line two to explain line one.
   - Avoid open loops that are too vague.
   - First line should usually name the situation, tension, or specific buyer context.

7. The CTA should match buyer readiness.
   - “Worth a chat?” is often too generic.
   - “Worth 10 minutes?” can be too heavy.
   - Prefer a specific low-friction loop:
     - “Would it help to see the angle we’d test?”
     - “Can I send the checklist?”
     - “If I map how I’d approach this, will you take a look?”
     - “Would it help to compare X against Y?”

## Psychological lenses to use

Use only the lenses that make the critique sharper.

### Status quo disruption

The email must interrupt the buyer’s current belief without over-pitching.

Good prompts:
- “What belief must change for them to reply?”
- “What assumption are they making that this email challenges?”
- “Does this make the current way feel riskier than replying?”

### Cognitive load

Too many claims, mechanisms, proofs, PS lines, and CTAs make the buyer work.

Red flags:
- multiple proof points stacked together
- long paragraphs
- two or more ideas per line
- case study plus guarantee plus mechanism plus PS in first touch
- “we” line explaining the sender before the buyer cares

### Skepticism and believability

The more extraordinary the claim, the softer and more specific the framing should be.

Red flags:
- “guaranteed 15 meetings”
- “500k+ emails a month”
- “we can do the same for you”
- vague “similar company” proof
- proof that does not match the target persona or industry

### Personal motive vs company motive

People buy based on personal pressure, career risk, status, convenience, relief, or ambition, but they justify it with company value.

Useful question:
- “What does the individual personally want, and how can it be framed as an organizational win?”

### Josh Braun-style I:you ratio

Prefer “you / your / {{company}}” framing over “we / I / our.”

Do not mechanically remove every “we.” Remove “we” lines that do not advance the buyer’s understanding.

### Brevity as a data-backed default

When in doubt, shorten. The shorter test is often the one worth running first.

Use variants:
- super brief
- normal brief
- slightly longer explanation

### Personality and temperament lenses

If the user references INFP/ENFJ ratio or similar personality concepts, use it lightly:
- INFP-ish buyer state: skeptical, meaning-seeking, allergic to pushy claims.
- ENFJ-ish buyer state: relational, status-aware, wants social proof and shared purpose.

Do not over-index on personality typing. Use it as a quick empathy/framing lens, not a scientific claim.

### Hormozi/HB-style value lens

If relevant, check:
- dream outcome
- perceived likelihood of achievement
- time delay
- effort/sacrifice

Outbound usually fails when it increases perceived effort or skepticism before proving likelihood.

## Common critique moves

### “This reads like a vendor email”

Use when copy leads with:
- booked meetings
- guarantees
- “we help”
- case studies before buyer tension
- generic praise

Fix:
- Start with the buyer’s current tension.
- Move proof to a follow-up or make it quieter.
- Replace meeting ask with a specific permission ask.

### “Wrong audience”

Use when proof or pain maps to a different persona than the one being emailed.

Example diagnosis:
- “This sounds like it was written for agencies, not B2B AI founders.”
- “The proof creates a relevance gap.”

Fix:
- Rewrite around the actual business model and buying pressure.

### “Too much proof pile”

Use when the email tries to establish credibility too early.

Fix:
- One quiet credibility line is enough.
- Lead with the buyer problem.

### “CTA is too generic”

Replace:
- “Worth a chat?”
- “Worth 10 minutes?”
- “Open to a call?”

With:
- “Would it help to see the angle we’d test for {{company}}?”
- “Can I send the sample?”
- “Would it help to compare that path against hiring inside {{company}}?”
- “If I spend 45 minutes mapping this, will you take a look?”

### “Line one needs to make sense alone”

Use when the opener depends on a later sentence.

Fix:
- Put the where/what/who in line one.
- Make it fully buyer-centric.

### “Cut the PS”

Cut PS lines when they:
- distract from the business problem
- feel transactional
- add compliance-but-not-value
- make the email feel needy

Keep PS only when it lowers friction or clarifies exit:
- “Not relevant? Reply pass and I’ll close the loop.”

Even then, remove “Promise” if it feels theatrical.

## Rewrite patterns

### Founder-led sales

Subject: founder led

Founder-led sales usually works until it starts costing too much founder attention, {{first_name}}.

We help lean AI teams test outbound before hiring sales too early.

The aim is predictable pipeline without pulling more time from product.

Would it help to see the first wedge we would test for {{company_name}}?

### Agency pipeline

Subject: pipeline

Agency referrals can create real momentum, but they rarely make pipeline feel predictable, {{firstName}}.

We help agencies use LinkedIn to start sales conversations with better-fit prospects.

The leverage usually comes from sharper targeting, not more sending volume.

Would it be helpful to see the angle we’d test for {{companyName}}?

### Hiring alternative

Saw you’re hiring for CX coverage tied to {{jd_one_liner}}, {first_name}.

That might mean volume is rising faster than training, weekends, and PTO can comfortably absorb.

We support DTC teams with Canada and US-based reps, paid only per resolved ticket.

Would it help to compare that path against hiring inside {{company}}?

### Compliance / security

Are the new standards for a “pen test” something you’ve seen, {name}?

A scanner report + logo used to pass - not anymore.

If you love your current setup - lmk and I’ll remove you.

Otherwise I can share the renewal checklist we’re using with customers, to make sure these new standards don’t cause a fail.

### Search gap

Subject: {search term} gap

You’ve already invested in “{search_term}” on Google, {firstName}.

That query gets {monthly_searches} YouTube searches each month.

You won’t close that gap by putting out another random blog post.

If I map how I’d approach this for {company}, will you take a look?

## Use-case generation prompts

When the user asks for new use cases or angles, generate angles around:

- status quo pain
- risk of doing nothing
- hidden cost
- comparison against current path
- timing pressure
- buyer internal incentive
- proof relevance
- operational bottleneck
- specific wedge/test/checklist/report/sample
- referral/introduction/event invite angle

For each angle, include:
- target persona
- psychological trigger
- opener
- CTA
- why it might work

## Final copy standards

- Keep cold copy short.
- Use plain English.
- Prefer specific nouns over abstractions.
- Use one idea per line.
- Avoid hype.
- Avoid em dashes and en dashes. Use normal hyphens.
- Do not invent results or customers.
- If proof is weak, make the ask softer instead of making the claim louder.
