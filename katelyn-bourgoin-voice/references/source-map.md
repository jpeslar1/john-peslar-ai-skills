# Katelyn Bourgoin Source Map

Research date: 2026-09-09
Refresh cadence: every 6 months (next: 2027-03)

## Primary sources

| Source | URL | What it gives | Access |
|---|---|---|---|
| Why We Buy newsletter / blog | https://customercamp.co/blog/ | The core corpus: newsletter issues teaching one buyer-psychology or cognitive-bias concept per post | Open, server-rendered, scrapes cleanly |
| Choice Closure | https://customercamp.co/choice-closure/ | Five-part newsletter shape, "How To Apply This" section, identity-transformation language | Open |
| The Labor Illusion | https://customercamp.co/the-labor-illusion/ | Brainy Tweetable pull-quote device, luxury/Hermès case, mechanism statements | Open |
| The Trigger Technique (part 3 of a series) | https://customercamp.co/the-trigger-technique-2/ | Her named framework (trigger events, cornerstone insights), buyer-interview methodology | Open |
| Dunning-Kruger Effect | https://customercamp.co/dunning-kruger-effect/ | Reveal-the-term hook, named sub-concepts (Mount Stupid, Slope of Enlightenment), her own product plug in first person | Open |
| X profile | https://x.com/katebour | Current bio line, short-form identity register | Open (raw HTML fetch works for bio/profile header; full timeline requires login) |
| LinkedIn profile | https://ca.linkedin.com/in/katebour | Headline, recommendations, current company (UNIGNORABLE) | Login wall for full content; only a paraphrased summary was retrievable |
| Demand Curve podcast interview | https://www.youtube.com/watch?v=V4SHt99AXqM | Spoken register on buyer psychology, trigger events, Jobs to Be Done sourcing (Bob Moesta, Clayton Christensen) | Open, human-authored (non-ASR) caption track |
| Earned Secrets with Varun podcast interview | https://www.youtube.com/watch?v=q1FD9zUeqTQ | Spoken register on "ownable ideas" and buyable positioning | Open, auto-generated (ASR) caption track only |
| Customer Camp site / Why We Buy brand | https://customercamp.co | Company/brand context, product names (Wallet-Opening Words, Clarity Calls, PAINKILLER, Ouchy Pain Finder) | Open |
| UNIGNORABLE / Ownable Ideas | https://beunignorable.com | Her current company, referenced in her X bio | Open, not deep-fetched this session |

## What was actually fetched

- Four customercamp.co newsletter posts were pulled as raw text on 2026-09-09: "Choice Closure" (2024-09-11), "The Labor Illusion" (2024-06-26), "The Trigger Technique" (2025-01-08, clean-text version), and "Dunning-Kruger Effect" (undated deep-dive, confirmed "Written By Katelyn Bourgoin" at the foot of the post). All four scraped cleanly as readable prose with a plain HTTP fetch; the site is server-rendered.
- A fifth file (`posts1.txt`, raw Divi/WordPress HTML with shortcodes for the same Trigger Technique post) was available but not used: the clean-text version was complete, so the raw HTML was redundant noise.
- Her X profile page (`x.com/katebour`) was fetched directly and returned a readable bio header ("Idea owners get richer // Founder of @beunignorable, the Ownable Ideas company", 150.4K followers) even though the full tweet timeline is behind a login wall for unauthenticated fetches.
- Her LinkedIn profile was only reachable through a paraphrasing fetch tool, which returns an AI-generated summary, not her original words. That summary is not quoted anywhere in the corpus; it only confirms headline facts (location, current company, follower count).
- Two YouTube podcast interviews were pulled by videoId: `V4SHt99AXqM` (Demand Curve, "Buyer's Psychology w/ Katelyn Bourgoin") has a human-authored English caption track (`generated=False`), so its excerpts are treated as verbatim. `q1FD9zUeqTQ` (Earned Secrets with Varun) has only an auto-generated caption track (`generated=True`), so its excerpts are labeled `documented` and may contain ASR transcription errors (e.g. "revvelatory" for "revelatory" in the raw transcript).
- A blog index page at customercamp.co/blog/ was fetched to find additional post titles for future refreshes (Normalcy Bias, Baader-Meinhof Phenomenon, Framing, Warm-Glow Giving, Self-Serving Bias, Base Rate Fallacy); several guessed slug URLs for these (e.g. `/base-rate-fallacy/`, `/self-serving-bias/`, `/warm-glow-giving/`, `/framing/`) 404'd on the exact slug guessed and were not pursued further this session.

## Known gaps

- **No confirmed verbatim LinkedIn post text.** LinkedIn is described by secondary sources as her primary short-form platform (98K-220K combined followers across LinkedIn and X depending on source), but the profile is behind a login wall for this session's tools and only a paraphrased summary came back. The LinkedIn Content Expert playbook in SKILL.md is inferred from her newsletter habits and her confirmed X bio line, not from sampled LinkedIn posts. This is the single biggest gap in this skill.
- **No confirmed verbatim X/Twitter post text, only her bio.** The X profile header fetched cleanly, but the tweet timeline itself requires a logged-in session and was not retrievable. Nothing in this corpus is claimed to be a sampled tweet.
- **No book or paid-course text.** She has published paid frameworks (Wallet-Opening Words, PAINKILLER, Clarity Call Cheatsheets, Unignorable challenge). None of that gated content was accessed; only free newsletter posts and public podcast/profile text were used.
- **Newsletter sample skews 2024-2025 and is only 4 of ~100+ published issues.** Only four posts were fetched this session (Choice Closure, The Labor Illusion, The Trigger Technique, Dunning-Kruger Effect). The archive is much larger; several additional post slugs were identified from the blog index but not fetched (see above).
- **The Earned Secrets podcast quotes are ASR-only.** No human-caption or verbatim text source was found for her "ownable idea" framework talking points; treat item 27-31 wording as approximate, not exact.
- **No confirmed authorship check on every customercamp.co post.** Only the Dunning-Kruger Effect post explicitly showed a "Written By Katelyn Bourgoin" byline in the fetched text; the other three were assumed to be hers based on consistent first-person voice, matching brand, and matching structural pattern across the same domain, but the byline line itself was not independently confirmed for those three.

## Refresh instructions

1. Re-fetch https://customercamp.co/blog/ and pull 3-4 more individual posts not already in the corpus, prioritizing recent issues to check whether the five-part newsletter shape has changed.
2. Attempt an authenticated or logged-in fetch of linkedin.com/in/katebour and x.com/katebour to get real short-form post text; without that, the short-form playbooks stay inferred rather than sampled.
3. Search for a talk or podcast with a confirmed human (non-ASR) caption track specifically on the Trigger Technique or Ownable Idea framework, to upgrade the `documented` items in the corpus toward `verified`.
4. Re-check whether the "20-30%" style research citations she quotes elsewhere in her archive (not sampled this session) have been updated with newer studies.
5. Confirm current follower counts and company name (UNIGNORABLE / beunignorable.com) are still accurate before reusing bio-level facts.
