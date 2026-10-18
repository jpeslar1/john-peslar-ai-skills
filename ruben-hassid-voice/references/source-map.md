# Ruben Hassid Voice Source Map

Research date: 2026-10-19
Refresh cadence: every 6 months (next: 2027-04)

## Primary sources

| Source | URL | What it gives | Access |
|---|---|---|---|
| LinkedIn post permalinks (40+), handle ruben-hassid | e.g. https://www.linkedin.com/posts/ruben-hassid_dont-ask-chatgpt-or-claude-for-their-opinions-activity-7517177624197181440-0rjN | Full post text (description meta plus attributed-text segments), datePublished, comment counts; covers 2023-03 to 2026-10-17: how-to step posts, growth recaps, launches (EasyGen, GPC). Verbatim. | Open with a desktop UA. The profile page /in/ruben-hassid returns HTTP 999 (bot-blocked), so permalinks came from WebSearch `"Ruben Hassid on LinkedIn" <topic>` and from posts linked inside his Substack. |
| Substack "How to AI" | https://ruben.substack.com/ | 73 essays 2026-01-18 to 2026-10-16, 450-4,400 words: hooks, numbered sections, full prompts, personal asides used as frames. Verbatim. | `/api/v1/archive?sort=new&limit=50&offset=N` lists posts; `/api/v1/posts/<slug>` returns `body_html` in full, including `only_paid` posts. rubenhassid.ai redirects here. |
| X @rubenhassid | https://x.com/rubenhassid | Short-form mirror of Substack and LinkedIn content; 2 posts fetched, 1 excerpted. Verbatim. | `cdn.syndication.twimg.com/tweet-result?id=<id>&token=a` per tweet. The profile timeline endpoint was rate-limited on both tries. |
| Substack Notes @ruben | https://substack.com/@ruben/note/c-358170245 | Short personal notes on writing and reading; first line only is extractable. Verbatim (partial). | Open; text sits inside escaped JSON, first line readable via grep. |
| YouTube: "Ruben Hassid: The System Behind Viral LinkedIn Content", Legends N Leaders | https://www.youtube.com/watch?v=kdI6i7aORHU | ~5,500-word spoken interview: music-industry origin, "lazier or greater", twice-a-day posting, the no-personal-opinion rule. DOCUMENTED (auto-captions). | Captured with yt-dlp auto-subs by a prior run (local file kdI6i7aORHU.en.vtt); yt-dlp returns 429 after 1-2 calls. Upload date 2026-03-28, but content references an earlier follower count, so the recording may be older. |
| Third-party summaries (not cited) | enterprisezone.cc, magicpost.in, favikon.com, timstodz.com | Paraphrases of his posts with follower numbers; used only to locate permalinks. | Open. Never quoted. |

## What the corpus rests on

Thirty-seven of forty-one excerpts are verbatim from channels he writes himself: twenty-three from LinkedIn permalinks spanning March 2023 to 17 October 2026 (glyph bullets and wave dash preserved), twelve from Substack "How to AI" essays read in full via the posts API (January to September 2026), one from his own X account, and one first line of a Substack Note. Four are documented-grade ASR captions from a single podcast interview. Nothing comes from a quote aggregator. Both large corpora (LinkedIn and Substack) are current to within two days of the research date, and the written register is sampled across three years, so confidence in wording and hook mechanics is high for items 1-37 and moderate for 38-41. The sample skews to text how-to posts; his video-first and carousel formats are inferred from captions and research notes, not sampled.

## Known gaps

- **X timeline was rate-limited** on both attempts, so only 2 tweets were captured (1 excerpted). His X is largely a mirror of LinkedIn and Substack, so the loss is small, but X-native phrasing is unsampled.
- **LinkedIn profile is bot-blocked (HTTP 999)**, so there is no systematic recent-permalink leak; the 40+ permalinks came from search and a prior harvest and skew to how-to text posts. Treat the hook-type frequencies as a how-to-post sample, not a whole-feed census.
- **Video-first posts are thin.** His dominant 2024-2025 format was native video (60M+ views per a Synthesia case study cited in the research notes); permalink meta carries only short captions, so video-script output is inferred from the spoken interview and the written register.
- **No carousel slide text.** EasyGen-era document posts do not expose slide text in meta; carousel copy in this voice is inferred from his step-post structure.
- **Substack Note bodies are not extractable**; only first lines were captured (item 37).
- **The spoken sample is one interview, auto-captioned,** with an uncertain recording date (upload 2026-03-28; content references EasyGen beta and roughly 400k followers). Use it for stance, not exact wording.
- **The roster's "EasyGen blog" does not exist** (easygen.io/blog is 404). Do not cite it; his long-form is the Substack.
- **Anything published after 2026-10-19 is unsampled.**

## Refresh instructions

1. List new Substack posts with `curl -s "https://ruben.substack.com/api/v1/archive?sort=new&limit=50&offset=0"` and pull full bodies with `curl -s "https://ruben.substack.com/api/v1/posts/<slug>"`; add 5-8 verbatim excerpts from essays published since October 2026, continuing the numbering in the Substack section.
2. Find new LinkedIn permalinks via WebSearch `"Ruben Hassid on LinkedIn" <topic>` and via links inside new Substack posts (the profile page is bot-blocked); fetch each permalink with a desktop UA and add 5-8 verbatim excerpts, keeping his glyph bullets intact. Prefer at least two video-first posts to narrow that gap.
3. Retry the X syndication endpoint per tweet (`https://cdn.syndication.twimg.com/tweet-result?id=<id>&token=a`) using IDs linked from his Substack; add 3-5 posts if the timeline stays rate-limited.
4. Caption one more interview or one of his own videos with `yt-dlp --write-auto-sub --skip-download --sub-lang en "<url>"` (expect 429s; space the calls); add 3-5 documented excerpts and update the spoken-register stats.
5. Check whether GPC (gpc site or Substack "General Purpose Consulting." post) has published client-facing copy; if so, add a labelled "Consultancy register" section and note whether it changes the Newsletter Writer playbook.
6. Re-verify that every URL is still live. Never carry a quote forward that was not re-read at its source.

## Pattern notes

### 1. Accusation to procedure
Line one charges the reader ("Your prompt sucks."), line two flips or qualifies, a colon hands off to "Step 1." The LinkedIn Content Expert and Hook Creator playbooks are built on this three-line handoff.

### 2. The exact button and the quoted prompt
Every step names a tool, menu, or command, and the payoff is a full prompt in quotation marks with [BRACKET] variables and a success criterion. The LinkedIn Content Expert playbook refuses a step without a button.

### 3. Hammered one-liners and equations
"Forget about it. Ban it. Burn it." / "prompting = typing. But prompting = thinking." Fragments and equations replace transitions. All three playbooks cap sentence length and ban intro paragraphs.

### 4. Useful over personal
"Don't be personal. Be useful instead." Personal detail (French accent, last of 4 kids, his dad) appears only as a two-to-four line frame for a how-to. The Newsletter Writer playbook allots one aside and requires it to be the user's own.

### 5. The ugly-precise receipt
Credibility comes from unrounded numbers (331,689 followers, 〜900/day, 3M impressions per week) and the growth-recap hook "If I had to start all over again, I would:". The Hook Creator requires a number in at least two of five hooks and the Guardrails forbid transplanting his.

### 6. The repost ladder
Posts close with a numbered free-subscribe funnel ("Step 1: Subscribe for free → ... Become the 'AI guy' at work, forever.") and a ♻️ repost ask that gives a reason benefiting a third person; the paid tier is never pitched. The LinkedIn Content Expert template ends on this ladder.
