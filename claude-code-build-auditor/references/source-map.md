# Source Map - Claude Code Build Auditor

This skill is based on public lessons from Boris Cherny's Y Combinator talk, "Boris Cherny: Building Claude Code" (`https://www.youtube.com/watch?v=qyPCVqFUyDo`). It is not affiliated with or endorsed by Boris Cherny, Anthropic, Claude Code, or Y Combinator.

## Core Learnings

1. **Delete most instructions before adding new ones**
   - Claude Code deleted over 80% of its system prompt for the model discussed in the talk.
   - The team treats each model generation as different enough to justify prompt and harness ablations.
   - Old instructions often compensate for weaknesses that the new model no longer has.

2. **Ablate prompts, tools, and harness code**
   - Remove the system prompt, then add lines back one by one only when they prove useful.
   - Do the same with tools and harness code.
   - Much of the durable harness should be safety, permissions, static analysis, and UI, not clever over-scaffolding.

3. **Observe repeated failures before adding instructions**
   - Run the model against the real codebase or product.
   - Watch where it stumbles.
   - Add durable instructions only when the same failure repeats.
   - Every instruction is read every run, so each one has a carrying cost.

4. **Treat AI product building as empirical, not theoretical**
   - Models behave differently across generations.
   - The right harness is discovered by trying, observing, measuring, and iterating.
   - Evals outlive prompts for a while, but even evals expire when models saturate them.

5. **Unhobble the model**
   - Product overhang means today's models can do things that products have not yet made possible.
   - Hobbling happens when UI, permissions, workflow, or instructions prevent the model from expressing capability.
   - A good AI product gives the model enough freedom, tools, and feedback to do harder work.

6. **Use higher-level tasks with guardrails**
   - Avoid micromanaging every step.
   - Describe the task, guardrails, and exit criteria.
   - Let the model choose the route when the verification loop is strong.

7. **Verification is the key skill**
   - Give the model a way to verify its work like an engineer would.
   - Examples from the talk include test suites, fuzzing, screenshots, pixel comparison, live progress reports, and long-running runs that keep checking themselves.
   - Harder tasks become viable when verification is concrete.

8. **Use long-running and multi-agent workflows for truly hard work**
   - Dynamic workflows can orchestrate many agents in sequence and parallel.
   - Loops and routines can handle repeated maintenance tasks.
   - Good uses include dead-code cleanup, experiment removal, test coverage, duplicate abstraction cleanup, and large migrations with a strong test suite.

9. **The best builders forget stale priors**
   - Try the current model on problems that seemed impossible before.
   - Keep throwing new model generations at important hard tasks.
   - The practical edge is less "prompt engineering trick" and more empirical task design plus verification.

## Use-Case Translation

- **Architecture decision:** ask if the model and future maintainers can navigate the structure, then remove unnecessary layers.
- **AI bloat:** run an abstraction-police pass for duplicate helpers, speculative config, and files added without necessity.
- **Instructions:** delete first, observe, then add only repeated-failure fixes.
- **Agent comprehension:** give concrete context, boundaries, and verification instead of long prose.
- **Build timing:** use this skill before large agent runs, during drift, after model upgrades, and before shipping.
