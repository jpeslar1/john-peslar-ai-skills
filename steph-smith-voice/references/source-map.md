# Steph Smith Voice Source Map

Research date: 2026-10-19
Refresh cadence: every 6 months (next: 2027-04)

## Primary sources

| Source | URL | What it gives | Access |
|---|---|---|---|
| Steph Smith blog RSS (Ghost), full bodies of the 15 most recent posts (Mar 2019 to Nov 2020) | https://blog.stephsmith.io/rss/ | Complete essays: How to Be Great, Writing is Thinking, Antifragility at Work, Another Year Under the Sun, An Ode to Excel, Finding Top Talent, Untranslatable Words, When Do You Become a Developer; items 1-15 | Open; RSS returns full `content:encoded` |
| Steph Smith blog, older posts as HTML (Dec 2018 to Feb 2019) | https://blog.stephsmith.io/the-guide-to-remote-work/ , https://blog.stephsmith.io/you-dont-need-to-quit-your-job-to-make/ , https://blog.stephsmith.io/learning-to-code-apps/ , https://blog.stephsmith.io/a-year-of-sponge/ | The remote-work guide, the "don't quit your job to make" essay, Year of Sponge; items 16-18 | Open HTML with a desktop UA; dates in `article:published_time` |
| Blog post sitemap | https://blog.stephsmith.io/sitemap-posts.xml | Confirms the full catalogue is 25 posts (20 read, 11 quoted) | Open |
| X @stephsmithio single posts via fxtwitter JSON (`api.fxtwitter.com/stephsmithio/status/<id>`) | e.g. https://x.com/stephsmithio/status/1500986096745779200 | Verbatim post text with ISO dates, 2020-2026: the generation-defining-stats thread, Doing Content Right launch, Internet Pipes pricing ask, data-viz thread, Groq announcement; items 19-26 | Open, no login; the profile timeline endpoint returned 429 this session, so only 15 cached posts were available |
| Internet Pipes landing page (her product, first-person copy) | https://internetpipes.com/ | "Who created this?" and "What is Internet Pipes?" sections; items 27-28 | Open |
| Doing Content Right landing page (her book and course) | https://doingcontentright.com/ | Product copy and chapter promises; item 29 | Open |
| a16z Podcast, "The a16z Podcast Returns" (7 Nov 2022), machine transcript | https://podscripts.co/podcasts/a16z-podcast/the-a16z-podcast-returns (episode page: https://a16z.com/podcast/the-a16z-podcast-returns) | Her ~2-minute spoken relaunch monologue as new host; items 30-31 | Open; ASR, so documented-grade (her surname is rendered "Stepsman") |
| stephsmith.io home | https://stephsmith.io/ | Bio and project list (Internet Pipes, 50 Days of Fun, book, Eunoia, MYGA, FeMake); context only, not quoted | Open |

Not available this session: the X profile timeline (`syndication.twitter.com/srv/timeline-profile/screen-name/stephsmithio` returned "Rate limit exceeded"); a16z.com author and episode pages are JS-rendered with no transcript visible to curl; the Every.to transcript of her "AI & I" interview is paywalled; an Elpha AMA page returned empty. No yt-dlp attempt was made.

## What the corpus rests on

Twenty-nine of thirty-one excerpts are verbatim from channels she writes herself: eighteen from eleven essays on blog.stephsmith.io (2018-2020, full bodies from RSS and HTML), eight from her own X account via fxtwitter single-status JSON (2020-2026), and three from the first-person landing copy of her own products. Two are documented-grade ASR from a podscripts.co machine transcript of a scripted monologue she narrates on the a16z Podcast. Nothing comes from a quote aggregator or a secondary summary. The essay register is strongly covered but ends in November 2020; the X register is thinly covered (15 posts cached, 8 quoted); the spoken register is a single scripted sample. Confidence in wording is high for items 1-29 and moderate for 30-31. Confidence that the essay register still matches her current writing is moderate, because her 2021-2026 output is on X, in paid products, and spoken.

## Known gaps

- **The long-form corpus ends in November 2020.** No essay or newsletter in her own words after that date was retrievable; her later writing lives on X (only 15 cached posts), inside paid products (Internet Pipes, Doing Content Right, Trends.co reports), or in spoken form (a16z Podcast, Sydlis, My First Million). The essay-register claims in SKILL.md describe 2018-2020 writing.
- **X sample is small.** The syndication timeline endpoint was rate-limited this session; the eight quoted posts come from a prior cache and the thread items may not show every post in each thread. Do not extend a thread from memory.
- **No LinkedIn posts sampled.** No permalinks were located this session.
- **Spoken sample is one scripted monologue**, documented-grade ASR with a name error; conversational interview speech is not represented, so any claim about how she talks in interviews is unsupported.
- **Doing Content Right and Internet Pipes text is paid.** Only landing-page copy and her own tweet about the book were used.
- **a16z.com is JS-rendered** with no transcript tab visible to curl; podscripts.co ASR was the only transcript route found.
- **Anything published after 2026-10-19 is unsampled.**

## Refresh instructions

1. Re-fetch https://blog.stephsmith.io/rss/ and https://blog.stephsmith.io/sitemap-posts.xml; if any post is dated after Nov 2020, add 3-5 verbatim excerpts and continue the numbering in the essay section.
2. Retry the X timeline (`https://syndication.twitter.com/srv/timeline-profile/screen-name/stephsmithio`) once the rate limit clears, or pull single statuses via `https://api.fxtwitter.com/stephsmithio/status/<id>`; add 8-10 verbatim posts from 2024-2026 so the X register is no longer the weak channel, and complete the three thread items (19-21, 24) with their later posts.
3. Pull 3-4 more a16z Podcast episodes she hosts from https://podscripts.co/podcasts/a16z-podcast/ and add 4-6 documented items of interview-mode speech, labelled ASR; if a YouTube version exists, caption it with `yt-dlp --write-auto-sub --skip-download --sub-lang en "<url>"` and compare wording.
4. Search LinkedIn for "Steph Smith" posts with permalinks; if found, add a labelled "LinkedIn (verbatim)" section of 3-5 items.
5. Re-fetch https://internetpipes.com/ and https://doingcontentright.com/ and confirm items 27-29 still match character for character; landing copy changes without notice.
6. Re-verify that every URL is still live. Never carry a quote forward that was not re-read at its source, and never add anything from a quote aggregator.

## Pattern notes

### 1. Stat, then reframe
A dated figure with a unit and a source is followed by a one-line interpretation ("Per day!", "What are the generation-defining stats of today?"). The Hook Creator playbook requires the reframe line under every stat hook and kills any hook that works without its number.

### 2. The pivot question
Paragraphs turn on a question she then answers ("So then the question then becomes, how does one activate this process?"). The Newsletter Writer uses one per section to move the argument.

### 3. Admit the limits, conclude anyway
"The labeling was at best subjective and at worst inconsistent" precedes the conclusion rather than hiding in a footnote. The Newsletter Writer and Ghostwriter both require the honest admission before the takeaway.

### 4. Aphorism after the build
Long sections land on a 5-10 word line ("Writing and thinking are two peas in a powerful pod", "People are mostly good"). All three playbooks end sections and pieces on a compression.

### 5. Credit and invite, never sell hard
Sources are named (Bezos, @sydlis, r/dataisbeautiful) and closers invite participation ("Comment with a trend I missed!"). The Newsletter Writer replaces the CTA with an invitation plus one named resource.

### 6. Humble-analytical hedging
"I think", "Perhaps", "I must admit", "arguably" appear in a quarter of the items while the claims stay data-backed. The Ghostwriter treats hedges as features and the Emotional register fix adds one when a draft reads authoritative.
