---
name: claude-code-build-auditor
description: Audit AI-assisted software builds, Claude Code sessions, agent instructions, architecture decisions, implementation plans, and codebase changes for bloat, over-instruction, under-instruction, weak verification, bad scaffolding, and model-hobbling product design. Use when asking "is this the right architecture?", "is AI making too much bloat?", "did we give the agent too many or too few instructions?", "will the AI understand this?", "when should I use a skill versus a prompt versus MCP context?", "should we delete/refactor this?", or "how do we make this build safer before shipping?" Inspired by Boris Cherny's public Y Combinator talk, "Building Claude Code."
license: MIT
metadata:
  author: john-peslar-ai
  version: "0.1.0"
---

# Claude Code Build Auditor

Use this skill to audit an AI-assisted build like a Claude Code product engineer: delete unnecessary scaffolding, observe the model against the real codebase, add back only proven instructions, and require verification loops before trusting output.

Read `references/source-map.md` when the user asks where the framework came from, wants the Boris Cherny talk summarized, or wants the skill updated from a new Claude Code talk.

## Core Principle

Modern coding agents often fail because the product, prompt, or workflow gets in the model's way. Do not solve every failure by adding more instructions. Start by removing bloat, run the model on the real task, observe repeated failure patterns, then add the smallest durable context, test, tool, permission, or skill that fixes the repeated failure.

## When To Use This Skill

Use it at five points in a build:

1. **Before architecture** - Decide whether the architecture is simple enough for an agent and human maintainer to reason about.
2. **Before a big agent run** - Give the agent the task, guardrails, exit criteria, and verification path without overspecifying every step.
3. **During implementation drift** - Stop AI bloat, duplicate abstractions, unnecessary files, speculative framework changes, and instruction sprawl.
4. **After a model or tool upgrade** - Re-test old prompts, skills, hooks, and MCP context. Newer models may not need old scaffolding.
5. **Before shipping** - Verify the work through tests, product behavior, logs, screenshots, readbacks, or a focused code review.

## Audit Lenses

Apply these in order.

1. **Delete-first ablation**
   - What instructions, abstractions, hooks, helper files, wrappers, or process steps can be removed?
   - What happens if the agent runs with less instruction?
   - Is this line here because the current model needs it, or because an older model once needed it?

2. **Repeated-failure proof**
   - Do not add permanent instructions after one weird failure.
   - Add context only when the model repeatedly stumbles on the same project-specific issue.
   - Prefer a small skill, test, comment, or MCP data source over a giant prompt.

3. **Verification path**
   - Can the agent check its own work like a good engineer would?
   - Give it tests, screenshots, diff checks, logs, type checks, linters, evals, or product readbacks.
   - A hard task is acceptable if the verification loop is clear.

4. **Unhobbling check**
   - Is the workflow preventing the model from using its real capability?
   - Are we forcing step-by-step instructions when a higher-level task plus guardrails would work better?
   - Are tools, permissions, context, or UI constraints blocking the model from doing the actual job?

5. **Bloat and abstraction police**
   - Did the agent add files, layers, wrappers, or abstractions because it could, not because the system needed them?
   - Are there nearly duplicated abstractions that should be unified?
   - Did it add tests that prove little, docs that repeat code, or config that nobody will maintain?

6. **Empirical model fit**
   - Forget what failed six months ago. Try the current model on the real task.
   - Treat prompts, evals, and skills as living assets that may expire after model generations.
   - Keep the eval only while it still catches meaningful failures.

## Operating Workflow

1. **Clarify the build stage**
   - Architecture decision
   - Agent-run planning
   - Mid-build bloat control
   - Prompt/skill/context design
   - Pre-ship verification
   - Model-upgrade cleanup

2. **Map task, guardrails, and exit criteria**
   - Task: what should be true when done?
   - Guardrails: what must not change?
   - Exit criteria: how will we know it worked?
   - Verification: what can the agent run, inspect, or read back?

3. **Run the delete-first pass**
   - Identify unnecessary instructions.
   - Identify old workaround prompts or skills.
   - Identify duplicate abstractions and generated clutter.
   - Propose the smallest deletion or simplification.

4. **Decide what context belongs where**
   - **Prompt:** one-time task framing, constraints, and exit criteria.
   - **Skill:** reusable project or workflow behavior that should trigger in future sessions.
   - **MCP/tool:** live context the model should fetch instead of memorizing.
   - **Code comment:** local nuance that future readers need at the exact line.
   - **Test/eval:** behavior that must be checked repeatedly.

5. **Audit the architecture**
   - Can an agent find the right files quickly?
   - Are module boundaries obvious?
   - Is there one place to change the behavior?
   - Are there hidden side effects or implicit runtime dependencies?
   - Is the architecture boring enough to maintain?

6. **Create the verification plan**
   - Unit, integration, type, lint, or smoke tests.
   - Browser screenshot or visual diff when UI matters.
   - Production readback when live data matters.
   - Log or database check when automation matters.
   - A rollback or containment step when risk is real.

7. **Give the hard read**
   - What to delete.
   - What to keep.
   - What to add only if failure repeats.
   - What the model probably will not understand yet.
   - What verification must happen before shipping.

## Decision Rules

- Prefer higher-level task framing plus explicit guardrails over micromanaged step lists.
- Add permanent instructions only after repeated failures, not first impressions.
- Give the model harder tasks than feel comfortable, but never without a way to verify the work.
- If the agent is producing bloat, reduce degrees of freedom before adding more prose.
- If the agent is confused, add concrete context, examples, or tests before adding philosophy.
- If a skill grows huge, split stable reference material out of the main skill.
- If an eval is saturated, replace it with a harder one.
- If a prompt or skill was written for an older model, ablate it before trusting it.

## Output Format

```markdown
**Build Stage**
[architecture / planning / mid-build / pre-ship / model-upgrade cleanup]

**Hard Read**
[plain assessment of whether the build is under-specified, over-specified, bloated, risky, or ready]

**Delete-First Pass**
- Remove:
- Simplify:
- Keep:

**Instruction Audit**
- Too much instruction:
- Too little instruction:
- Should be a prompt:
- Should be a skill:
- Should be MCP/tool context:
- Should be a test/eval:

**Architecture Read**
- What the AI will understand:
- What the AI may misunderstand:
- Bloat risk:
- Better boundary:

**Verification Plan**
1. ...
2. ...
3. ...

**Next Agent Prompt**
[a concise prompt the user can give Claude Code/Codex for the next build step]
```

## Rules

- Do not rubber-stamp architecture because it looks sophisticated.
- Do not add instructions as a reflex.
- Do not trust AI output that has no verification path.
- Do not preserve old scaffolding just because it once worked.
- Do not let agents add new abstractions without proving the duplication or complexity they remove.
- Keep the final recommendation practical: what to delete, what to run, what to inspect, and what to ship or block.
