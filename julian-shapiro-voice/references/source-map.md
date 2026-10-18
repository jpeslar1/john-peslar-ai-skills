# Julian Shapiro Voice Source Map

Research date: 2026-10-19
Refresh cadence: every 6 months (next: 2027-04)

## Primary sources

| Source | URL | What it gives | Access |
|---|---|---|---|
| Writing Well handbook, Intro | https://www.julian.com/guide/write/intro | Writing as a laxative for the mind, the bat signal, notetaking as map-drawing | Open; curl with a desktop UA; undated (guide pages show no publish date) |
| Writing Well handbook, Ideas | https://www.julian.com/guide/write/ideas | Novelty x Resonance formula, the half-told story, hooks as goodwill, "Anything can be interesting when framed by an intriguing question" | Open; undated |
| Writing Well handbook, First Drafts | https://www.julian.com/guide/write/first-draft | Speedrun the terrible first draft, self-indulgent writing, curiosity over expertise | Open; undated |
| Writing Well handbook, Rewriting | https://www.julian.com/guide/write/rewriting | The thirteen-year-old test, simple language licenses complex ideas, succinctness as a ratio, the $15 book arithmetic | Open; undated |
| Writing Well handbook, Style | https://www.julian.com/guide/write/style | The wormhole self-demonstration, "fraudulent voice" | Open; undated |
| Start a Startup handbook, Intro | https://www.julian.com/guide/startup/intro | "zero fluff" framing, 6-step startup process, credentials | Open; undated |
| Blog: "What to do with your life" (Oct 8 2016) | https://www.julian.com/blog/life-planning | The withheld test hook, "I will never start another startup" | Open; dated on page |
| Blog: "Creativity faucet" (Jan 22 2021) | https://www.julian.com/blog/creativity-faucet | Backed-up pipe analogy, Creativity Faucet and Relentless Juxtaposition coinages | Open; dated on page |
| Blog: "How to tell great stories" (Jul 17 2021) | https://www.julian.com/blog/storytelling | Storytelling as strategic withholding | Open; dated on page |
| Blog: "Memorized Rules" (Jul 22 2021) and "Pick better life goals" (Oct 31 2020) | https://www.julian.com/blog/memorized-rules ; https://www.julian.com/blog/vanity-metrics | "A funny lie of adulthood", crisp opening lines | Open; dated on page |
| X @Julian, "My day job is growing startups" thread (Jan 25 2021) | https://x.com/Julian/status/1353764328030130179 | Credential colon opener, growth-marketing timeline, Twitter-followers bullet list | Open via `https://api.fxtwitter.com/Julian/status/<id>` |
| X @Julian, "An intro to startup growth" thread (Oct 5 2021) | https://x.com/Julian/status/1445282615972429827 | Definitional "1/" opener, PLG definition with footnote asterisk | Open via fxtwitter |
| X @Julian, "I read 3,000 startup pitch decks" thread (Nov 4 2024) | https://x.com/Julian/status/1853510703388524979 | It's-done question hook, "Here's the kicker", "experimentation factory" closer | Open via fxtwitter |
| Monthly newsletter archive | https://www.julian.com/archived/newsletter | Newsletter register | Password-protected; NOT sampled |
| The Brains podcast; swyx mixtape clip | https://brainspodcast.com (and the swyx clip page) | Spoken voice | No transcripts published; NOT sampled |

## What the corpus rests on

All 30 excerpts are verbatim from channels he writes himself: 17 from five Writing Well handbook pages, 4 from dated blog posts (2016-2021), 1 from the Start a Startup handbook intro, and 8 from three of his own X threads (2021-2024), each tweet fetched individually by status ID via fxtwitter or the X syndication single-tweet endpoint. This is a two-channel corpus, which the research brief accepts when one main long-form channel (julian.com) is paired with one secondary (X). Nothing comes from a quote aggregator or an unroll service. The handbook register and the thread register are both covered and read as one voice at two compressions. There is no spoken sample and no newsletter sample. Confidence in wording is high for every item; confidence in dating is high for the blog posts and tweets and absent for the handbook pages, which carry no publish date.

## Known gaps

- **No spoken-word source.** yt-dlp was not attempted; the Brains podcast and the swyx clip page publish no transcripts, and his Lenny's Newsletter interview has no public transcript located. Every voice claim here is about his written register.
- **X sample is three threads.** The syndication timeline endpoint returned "Rate limit exceeded" on every attempt, so standalone tweets were not sampled; the 8 X items come from threads located by web search and fetched by ID. One located tweet (the 2019 TechCrunch column announcement, status 1104162903060471809) returns 404 and was dropped.
- **Handbook pages are undated.** julian.com guide pages carry no publish date in the HTML and are labeled undated; the handbooks have been revised over time, so wording may drift between refreshes.
- **Newsletter archive is password-walled** (julian.com/archived/newsletter); the newsletter register is unsampled and should not be inferred.
- **Pitch-deck thread coinages (billboarding, PLA, genesis narrative) are noted in the research but not excerpted**; quote them only after re-fetching the thread.
- **Anything published after 2026-10-19 is unsampled.**

## Refresh instructions

1. Re-fetch each handbook page (`curl -sL -A "Mozilla/5.0" https://www.julian.com/guide/write/<page>` for intro, ideas, first-draft, rewriting, style, and the startup guide pages) and diff against the corpus; if wording changed, update the item and note the revision date. Add 3-5 excerpts from any guide pages not yet sampled (e.g. the growth handbook).
2. Re-fetch `https://www.julian.com/blog` and add 2-4 verbatim excerpts from any new dated post, continuing the numbering in the julian.com section.
3. Pull the X syndication timeline (`https://syndication.twitter.com/srv/timeline-profile/screen-name/Julian`) when it is not rate-limited, or locate new threads via web search for `x.com/Julian/status`; fetch each tweet via `https://api.fxtwitter.com/Julian/status/<id>` and add 5-8 verbatim posts, including the billboarding / PLA / genesis-narrative tweets from the pitch-deck thread.
4. Close the spoken gap: run `yt-dlp --write-auto-sub --skip-download --sub-lang en "<url>"` once on a long podcast appearance (Lenny's Podcast or similar), add 3-5 excerpts under a new "## Documented excerpts" heading, and add a spoken-register bullet to the stats.
5. If the newsletter archive becomes public, add a labelled "Newsletter" verbatim section and consider a Newsletter Writer playbook.
6. Re-verify that every URL is still live. Never carry a quote forward that was not re-read at its source.

## Pattern notes

### 1. Formula line
He compresses a topic to an equation or ratio on its own line and claims it ("Writing Quality = Novelty x Resonance / That's my writing framework."). The Ghostwriter sets one formula per chapter; the Contrarian Take Generator uses the inversion thesis in the same slot.

### 2. Analogy per idea
Every abstract claim gets one concrete comparison (laxative, bat signal, map, wormhole, backed-up pipe, the 100-page book). The Ghostwriter requires one analogy per section and forbids two for one idea.

### 3. Withheld answer
Hooks raise a question and tease only part of the answer, exactly as he teaches ("There's a super quick test for it."; "Was there a "secret ingredient"… YES."). The Hook Creator names the withheld half before writing the hook.

### 4. Self-demonstration
He performs the technique in the sentence that teaches it and then points at it ("See, that's an example of style."). The Ghostwriter deploys one self-demonstration early in each piece.

### 5. Credential colon
Threads open with work done, scale, a promise, and a colon ("My day job is growing startups. I've worked with a few hundred by now. Here's how to…"). The Hook Creator and Ghostwriter both use it as the thread root; ghostwritten copy must substitute the user's own work.

### 6. Reader-cost arithmetic and the kicker
He argues for brevity by counting the reader's time and words saved, and he announces the single most important point ("But. Here's the kicker"). The Contrarian Take Generator proves its inversion with the arithmetic; the Ghostwriter places the kicker two-thirds through.
