# Ann Handley Voice Source Map

Research date: 2026-10-19
Refresh cadence: every 6 months (next: 2027-04)

## Primary sources

| Source | URL | What it gives | Access |
|---|---|---|---|
| annhandley.com blog (Total Annarchy archive) | https://annhandley.com/wp-json/wp/v2/posts?per_page=40&page=1 (pages 1-3) | 120 full essays 2019-2026; newsletter issues republished with the "A version of this story appeared in Total Annarchy" preamble | Open. curl with a fake Chrome UA gets an HTTP/2 stream error (exit 52/92); default curl UA or python urllib works |
| Total Annarchy newsletter signup | https://annhandley.com/newsletter/ | Fortnightly newsletter; signup page only, issues live on the blog | Open with default UA |
| Essay: SEO That Gets At The Heart of the Question (Oct 12 2026) | https://annhandley.com/seo-that-gets-at-the-heart-of-the-question/ | Newest sampled issue; sweaty-palms scene, "the moment behind the query", "make them feel seen" | Open |
| Essay: Don't Outsource This Part of Writing (Aug 24 2026) | https://annhandley.com/dont-outsource-this-part-of-writing/ | Reluctant-return opener; "What do I lose if I hand this over?" | Open |
| Essay: AI Slop, Accusations, And A Better Way (Aug 10 2026) | https://annhandley.com/ai-slop/ | Mock-trial image, "PEOPLE. Come on.", "use em dashes. They are blameless." | Open |
| Essay: Why Care About The Stupid Em Dash Anyway? (Jun 29 2026) | https://annhandley.com/why-care-about-the-em-dash/ | Hinge vs fog machine; Batman bath towel; "Is this a hill I want to die on?" | Open |
| Essay: Surprising Things I've Learned Writing 1000 Words a Day (Oct 2025) | https://annhandley.com/1000-words-a-day/ | 1K A Day; "obligation, not a habit"; "one 2×4 at a time" | Open |
| Essay: The One Email Metric You Need to Track (Feb 25 2023) | https://annhandley.com/the-one-email-metric-to-track/ | OWBR coinage and pronunciation guide; "harbinger" joke | Open |
| LinkedIn posts (annhandley) | e.g. https://www.linkedin.com/posts/annhandley_so-many-people-sent-me-this-graphic-this-activity-7482823969113288704-0cnS | Full post text and JSON-LD datePublished, logged out; 8 posts 2022-2026 sampled | Permalinks render with a desktop UA; the /in/annhandley/ profile authwalls (HTTP 999). Permalinks found via WebSearch `"Ann Handley" "on LinkedIn:" <topic>` and a third-party hero page |
| LinkedIn Pulse: Why I Write (Apr 22 2018) | https://www.linkedin.com/pulse/why-i-write-ann-handley | "I write to find my squad"; the "More articles by" list points to newer Pulse pieces | Open with desktop UA |
| MarketingProfs author page | https://www.marketingprofs.com/authors/36/ann-handley | Her MarketingProfs columns | BLOCKED: 403 for every UA tried |
| Everybody Writes (2nd ed. 2022) and Content Rules | n/a | Books | Not fetched; no public excerpt located |

## What the corpus rests on

All 28 excerpts are verbatim and written by her: 19 from the full bodies of essays on annhandley.com (most of them archived Total Annarchy issues, 2019 to October 2026), 8 from public LinkedIn post permalinks (2022 to 2026), and 1 from a 2018 LinkedIn Pulse article. Nothing comes from a quote aggregator and nothing is documented-grade; there is no ASR material at all. The newsletter register is covered in depth across seven years; the LinkedIn sample is smaller and skews to 2026 and the em-dash theme. Confidence in wording is high for every item.

## Known gaps

- **MarketingProfs columns not represented.** The author page and column URLs return 403 on every fetch. Her professional-column register is inferred from the newsletter.
- **Book text not sampled.** No public excerpt of Everybody Writes or Content Rules was located. Her own newsletter summaries of book ideas (the Ugly First Draft, "write the hairs") stand in; do not quote the books as verbatim.
- **No spoken sample.** Keynotes and podcast appearances (for example Jay Acunzo's How Stories Happen) were not captioned; all 28 items are written. Spoken-style output is inferred.
- **LinkedIn sample is thin and skewed.** The profile and /recent-activity/ pages authwall, so permalinks came only from WebSearch and a third-party hero page: 10 posts located, 8 used, concentrated in 2026 and on the em-dash theme.
- **Anything published after 2026-10-19 is unsampled.**

## Refresh instructions

1. Re-pull the blog through WordPress: `curl -s 'https://annhandley.com/wp-json/wp/v2/posts?per_page=40&page=1'` (default curl UA, not a fake Chrome UA) and continue through pages 2-3; convert `content.rendered` HTML to text locally. Add 5-10 verbatim excerpts from the newest issues, continuing the numbering, and note the newsletter preamble date where it differs from the republish date.
2. Find new LinkedIn permalinks with WebSearch `"Ann Handley" "on LinkedIn:" <topic>`; fetch each permalink with a desktop UA and read the full text from `attributed-text-segment-list__content` and the date from the JSON-LD `datePublished`. Add to the LinkedIn section.
3. Check the LinkedIn Pulse "More articles by" list at https://www.linkedin.com/pulse/why-i-write-ann-handley for newer long-form pieces (for example the Aug 27 2026 Amazon book-destruction article) and sample one if the register differs.
4. If a spoken register is wanted, caption a keynote or podcast appearance with `yt-dlp --write-auto-sub --skip-download --sub-lang en <url>` and add 3-5 documented excerpts under a "Documented excerpts (ASR captions)" heading, flagged as such.
5. Retry https://www.marketingprofs.com/authors/36/ann-handley once per refresh; if it opens, add 2-3 column excerpts in their own section.
6. Re-verify that every URL is still live. Never carry a quote forward that was not re-read at its source.

## Pattern notes

### 1. Scene, bridge, callback
Every sampled essay opens on a small physical scene from her own week, bridges to the lesson with a deliberately plain sentence, reuses the scene as the metaphor, and calls it back in the last line. The Newsletter Writer and Ghostwriter playbooks interview for the user's scene before anything else.

### 2. Parenthetical second voice
The joke lives in parentheses and stage directions while the main sentence stays clear. Every playbook budgets the asides to the funniest moments so the tell does not become a tic.

### 3. Exasperation without profanity
Indignation is performed with caps and food oaths ("PEOPLE. Come on.", "holy ravioli") and resolved into a joke within two lines. The LinkedIn Content Expert playbook requires the indignation to resolve before the close.

### 4. Coin it
Ideas get names with pronunciation guides or acronyms with plain expansions (OWBR, AMYL, 1K A Day). The Newsletter Writer asks for one coinage per issue and the Guardrails forbid transplanting hers.

### 5. Declarative pair
Craft rules are taught as two plain metaphors or two short sentences ("A useful em dash is a hinge. It turns the sentence."). The Ghostwriter states the lesson this way right after the bridge.

### 6. Reader turn
Posts and issues end on a question to the reader or an open reply invitation, and the reply rate is the metric she tracks. Every playbook template ends on a callback or a question, never a summary.
