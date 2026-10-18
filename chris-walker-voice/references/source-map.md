# Chris Walker Source Map

Research date: 2026-08-24; Passetto-era refresh 2026-10-18
Refresh cadence: every 6 months (next: 2027-04)

## Primary sources

| Source | URL | What it gives | Access |
|---|---|---|---|
| LinkedIn (chriswalker171) | https://www.linkedin.com/in/chriswalker171/ | The core corpus. Six full posts fetched 2021-2024 (first pass) plus 15 post permalinks and the profile About section (refresh) | Profile and post permalinks render logged out with a desktop user agent (full text plus JSON-LD datePublished); only the activity feed and company posts page are login-walled |
| "What's next for me" post (Jan 9 2024) | https://www.linkedin.com/posts/chriswalker171_whats-next-chris-walker-announces-new-activity-7150577094471696384-h0sd | Passetto launch announcement with numbers ($218MM analyzed, $670k revenue) | Open |
| "9+ months" rebuttal (Jan 8 2024) | https://www.linkedin.com/posts/chriswalker171_marketing-sales-b2b-activity-7150123889350561793-mxAs | Demand Creation / Demand Capture / Pipeline Conversion split | Open |
| "Prove the ROI" post (Jan 22 2024) | https://www.linkedin.com/posts/chriswalker171_gtm-marketing-sales-activity-7155286414224453632-tgkP | Content syndication math | Open |
| "Signal-based selling" post (Mar 12 2024) | https://www.linkedin.com/posts/chriswalker171_gtm-marketing-sales-activity-7173297907582877696-fxeU | Right Fit / Right Time framing | Open |
| "88% Google Ads cut" post (Jul 11 2024) | https://www.linkedin.com/posts/chriswalker171_gotomarket-b2b-marketing-activity-7217166322420318209-ki_j | Full CAC arithmetic; CEO/CFO escalation | Open |
| GTM Live (formerly Revenue Vitals) RSS | https://anchor.fm/s/1caa9814/podcast/rss | 620 episodes; RV230-RV240 (Jan-Apr 2025) are his last hosted episodes; descriptions are Passetto-written | Open |
| YouTube: "The 3 Pillars of GTM Success" (GTM Live ep 42, Jan 2025) | https://www.youtube.com/watch?v=A8lov65xWgo | Passetto-era spoken register: cost of growth, revenue factory, no silver bullet | Open video; DOCUMENTED (auto-captions) |
| YouTube: "AI Is Ending Knowledge Work / Enter The Frequency Era" (ABM Answered, Jul 8 2026) | https://www.youtube.com/watch?v=AoIyoITdj9I | ENCODED-era spoken register; OUT OF SCOPE for the skill, documented for reference | Open video; DOCUMENTED |
| passetto.com | https://www.passetto.com/ | Confirms Walker is not bylined there; Passetto is now a measurement tool | Open |
| Refine Labs site | https://www.refinelabs.com/ | Hybrid Attribution Framework announcement, Refine Labs-era positioning | Open |
| mcgaw.io interview | https://mcgaw.io/blog/strategy-over-tech-with-chris-walker-ceo-of-refine-labs/ | Spoken register, "process over tech" framing | Open |
| Goldcast hot-takes session | https://www.goldcast.io/blog-post/demand-generation-hot-takes | Spoken register, contrarian one-liners | Open |
| Dreamdata interview (2024) | https://dreamdata.io/blog/chris-walker-b2b-marketing-2024 | Spoken register, sales-velocity framework | Open |
| provencontent.com dark social article | https://provencontent.com/dark-social-secrets-unveiled/ | Quoted line on intent data timing | Open |
| Fame.so State of Demand Gen breakdown | https://www.fame.so/post/state-of-demand-gen-chris-walker-podcast | Podcast line, quoted secondhand | Open |
| Third-party playbook analyses (context only, not quoted as Walker) | antoinebuteau.com, marvinsangines LinkedIn breakdown | Background context on his content patterns; not a source of verbatim excerpts | Open |

## What the corpus rests on

Items 1-23 (first pass) rest on six LinkedIn posts fetched from his profile (2021-2024) and five podcast or interview quotes pulled from third-party write-ups. The 2026-10-18 refresh added items 101-142: 33 verbatim LinkedIn excerpts fetched from logged-out post permalinks with dates, and 9 documented ASR excerpts from two videos. Items 101-123 are the Passetto era (2024 to early 2025) and are the material this skill emulates; items 124-142 are the ENCODED era (2026) and are kept only to document the pivot. The B2B marketing register is now sampled end to end, 2021 through April 2025, with the Passetto-era gap closed. Confidence in wording is high for LinkedIn items (line breaks normalized) and moderate for ASR.

## Known gaps

- **He left the field.** Walker handed off Revenue Vitals in April 2025, sold his Refine Labs shares in July 2025, and is CEO of ENCODED (neuroperformance) and author of The Frequency Era (April 2026). His 2026 LinkedIn carries no B2B marketing content. The skill is frozen at the 2019 to April 2025 register by operator decision; he will not produce more of it. If the operator ever wants "current Chris Walker", that is a near-rewrite around ENCODED topics, not a refresh.
- **No 2025 LinkedIn posts captured.** The profile exposes only the latest nine posts; search surfaced 2024 and 2026 permalinks but nothing dated 2025, including the Refine Labs exit post.
- **RV240 (Apr 4 2025), his farewell episode, was not transcribed.** It is the best source for his own words on leaving; the audio is an anchor.fm MP3 with no located YouTube mirror.
- **No Passetto-bylined writing exists.** passetto.com blogs are by Carolyn Dilks. The Passetto-era written register rests on LinkedIn only.
- **Items 17-23 remain secondhand.** Podcast quotes from third-party write-ups were not replaced; the refresh added first-hand ASR instead.
- **ASR caveats.** Both video pulls are auto-captions with machine errors ("sauna" for Asana); spot-check before quoting.
- **Anything published after 2026-10-18 is unsampled.**

## Refresh instructions

1. The B2B register is closed: he produces no more of it. A refresh can only backfill 2024-2025 material. Search for 2025 permalinks (`linkedin.com/posts/chriswalker171_...`) and fetch them logged out with a desktop user agent; the date is in JSON-LD.
2. Transcribe RV240 (Apr 2025) from the anchor.fm feed if a transcript or mirror appears; add 3-5 documented excerpts.
3. Replace the secondhand items 17-23 with first-hand ASR from GTM Live episodes RV200-RV240 using `yt-dlp --write-auto-sub --skip-download --sub-lang en` on the YouTube mirrors.
4. Do NOT fold ENCODED-era material into the emulated sections. If the operator decides to build a current-Walker voice, make it a separate skill.
5. Re-verify URLs are live; never carry a quote forward that was not re-read at its source.

## Pattern notes

### 1. One thesis, relentlessly

The same core argument re-cut through new datasets, customer numbers, and predictions for 6+ years. New posts are new angles on the standing thesis, never new thesis.

### 2. Data vindication

Claims are framed as already proven: "The same thing I've been saying for 6 years, now confirmed in a MASSIVE data set." Numbers are precise and slightly odd, with arithmetic derived in public.

### 3. Old Way vs. New Way

Binary contrast structures: lead gen vs. demand gen, software-based vs. self-reported attribution. The legacy playbook is timestamped to a specific year to declare it obsolete.

### 4. Ask the buyer

Self-reported attribution is the tiebreaker authority: "The most accurate way to get attribution is simply by asking them!"

### 5. Preemptive objection handling

The "p.s." disarms the anticipated counterattack before commenters raise it. Objections are reframed as outdated thinking rather than debated.

### 6. Escalation to the C-suite

Marketing problems are repositioned as CEO/CFO/board KPI-stack problems the marketing team cannot fix alone. The Passetto era (2024-2025) is this pattern at full strength: finance vocabulary (CAC payback, cost of growth, revenue factory), the Create Demand / Capture Intent / Convert Pipeline / Expand Accounts split, and "it's time for CEOs and CFOs to apply pressure here."

### 7. What survived the pivot (added 2026-10-18)
Structure and proof style are constant across Refine Labs, Passetto, and ENCODED: one-line hard-claim opener, hyphen-led bullet lists with no space after the hyphen, a horizontal separator before the turn, one to three ALL CAPS words, a "p.s." carrying the escalation or the plug, and precise slightly odd numbers with arithmetic shown. He writes plain hyphens, never em dashes, which already matches the operator's copy rule. The topics changed completely; the skeleton did not.
