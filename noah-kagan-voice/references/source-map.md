# Noah Kagan Voice Source Map

Research date: 2026-10-18
Refresh cadence: every 6 months (next: 2027-04)

## Primary sources

| Source | URL | What it gives | Access |
|---|---|---|---|
| noahkagan.com blog (formerly OkDork; okdork.com URLs redirect here) | https://noahkagan.com/ | 2026 posts in his current voice; each has a "The short version:" block and a "Want the one email I send..." insert; 26 excerpts from 6 posts | Open; text pulled from the raw HTML `<article>` body |
| "Brutally Honest Business Advice to My Younger Self" (Sep 21 2026) | https://noahkagan.com/brutally-honest-business-advice-to-my-younger-self/ | Number-then-"But before that:" opener; chiasmus rules; "Business Marriage"; the shrug kaomoji | Open |
| "I'm back as AppSumo CEO. It sucked." (Sep 5 2026) | https://noahkagan.com/im-back-as-appsumo-ceo/ | The one-line confession opener; "holy schnikeys"; "Oh shit, now I'm accountable."; "Get that in, Jason." | Open |
| "AppSumo is at war. Return buyers are down 40%." (Sep 5 2026) | https://noahkagan.com/appsumo-is-at-war/ | The burger-menu analogy; "chief repeating officer"; Triple B | Open |
| "There are no awards for life. Notes from turning 44." (Sep 5 2026) | https://noahkagan.com/no-awards-for-life-turning-44/ | Vulnerable register ("waiting for someone to clap"); hype skepticism (OpenClaw) | Open |
| "AI made my goals easier. It also killed the fun." (Oct 15 2026) | https://noahkagan.com/2026-goals-check-in/ | "Leadership is moving things forward. Complaining is having a strong opinion from the sideline." | Open |
| "How to Quit Your 9-5 (The Smart Way)" (Sep 21 2026) | https://noahkagan.com/how-to-quit-your-9-5-the-smart-way/ | Validation framework: collect money upfront, freedom number, "Think NOW, not HOW."; the Reid Hoffman shrug | Open |
| "Why I got Fired from Facebook (a $100 Million dollar lesson)" (OkDork, Sep 29 2012) | https://noahkagan.com/why-i-got-fired-from-facebook-a-100-million-dollar-lesson/ | 2012 register: "Can I be real with you? Real real?", "shit-canned", "Lesson learned:"; 3 excerpts | Open; now hosted on noahkagan.com |
| Million Dollar Weekend book site | https://milliondollarweekend.com/ | First-person positioning copy ("I've built 8 businesses..."); 1 excerpt | Open; the first chapter is email-gated and was not fetched |
| Noah Kagan YouTube, "I Met 25 Billionaires… Here's 6 Lessons They Taught Me" (video FRbeL6rEWjY, undated) | https://www.youtube.com/watch?v=FRbeL6rEWjY | Solo monologue: 1% claim, "You Must Be Your Own Boss", the 834-years math, "Uncle Noah loves you"; 4 excerpts | Open video; DOCUMENTED (yt-dlp auto-captions, no punctuation in source) |
| Noah Kagan YouTube, "die with $0" interview (video mzXJDP9Hoic) | https://www.youtube.com/watch?v=mzXJDP9Hoic | Captions downloaded but almost entirely Bill Perkins speaking; not used | Open video; not excerpted |
| Noah Kagan Presents podcast (Apple/Spotify) | linked from each blog post ("Listen to this episode") | Audio versions of the posts | Public audio; no transcript fetched |
| @noahkagan on X | https://x.com/noahkagan | Not retrieved | Timeline endpoints returned "Rate limit exceeded"; no status IDs located via search; zero posts collected |

## What the corpus rests on

Thirty of thirty-four excerpts are verbatim from text he published under his own name: twenty-six from six noahkagan.com posts dated September 5 to October 15, 2026 (his current voice, six weeks old at research time), three from the 2012 OkDork Facebook post (the raw early register), and one from the first-person copy on his book site. Four are documented-grade YouTube auto-captions from one solo monologue video. The written sample is recent, dense, and drawn entirely from channels he controls; the 2012 post shows the register has been stable for fourteen years. Confidence in wording is high for items 1-30 and moderate for 31-34. There is no X sample, so short-form claims are inferred from blog sentence habits.

## Known gaps

- **Zero X posts were fetchable.** @noahkagan timeline endpoints returned "Rate limit exceeded" and web search surfaced no concrete status IDs, so no tweets were collected. Any short-form or tweet-length output in this voice is inferred from his blog sentence habits, not sampled.
- **Million Dollar Weekend was not quoted.** The first chapter is email-gated on milliondollarweekend.com; Goodreads and Amazon quote pages were not used. Only the site's marketing copy in his first person is captured (item 30). Book lines must not be quoted as verbatim from memory.
- **One solo video only.** The "die with $0" video (mzXJDP9Hoic) captions were downloaded but are almost entirely the guest, Bill Perkins, speaking, so they were not used. The spoken register rests on one monologue.
- **Upload date for FRbeL6rEWjY was not read** (yt-dlp metadata calls were avoided under HTTP 429 pressure).
- **Classic 2013-2016 OkDork posts were not fetched** beyond the Facebook post. The okdork.com Wayback index is large (600+ URLs, alphabetical); the mid-2010s register is unsampled.
- **The podcast was not transcribed.** Episodes are audio versions of the blog posts and were not fetched.
- **Anything published after 2026-10-18 is unsampled.**

## Refresh instructions

1. Re-crawl https://noahkagan.com/ for new posts; pull each article body (`curl -s <url>` and extract `<article>`), and add 5-10 verbatim excerpts with URLs and dates, continuing the item numbering. Keep "The short version:" blocks as a structural reference.
2. For X, locate recent status IDs (search results, a feeder-style mirror, or a logged-in human export) and fetch each with `curl -s 'https://cdn.syndication.twimg.com/tweet-result?id=<id>&token=a'`; aim for 10-15 posts and add a "Short-form (X)" section so the short-form register moves from inferred to sampled.
3. Pull captions from one or two more solo monologue videos (skip interview episodes where the guest talks): `yt-dlp --write-auto-sub --sub-lang en --skip-download -o '%(id)s' 'https://www.youtube.com/watch?v=<id>'`; wait and retry on HTTP 429. Read the upload date with `yt-dlp --print upload_date <url>` once rate limits clear. Label all caption text documented-grade.
4. Fetch two or three 2013-2016 OkDork posts via the Wayback Machine (https://web.archive.org/web/*/okdork.com/*) to confirm the mid-2010s register and add them as a labelled section.
5. Re-verify that every URL above is still live. Never carry a quote forward that was not re-read at its source.

## Pattern notes

### 1. One-sentence confession opener
"Three Sundays ago I did not want to go to work on Monday." / "Can I be real with you? Real real?" The Ghostwriter playbook makes line one a confession the user actually holds; the Hook Creator writes it as the first of six hook types.

### 2. The number nobody publishes
$100M a year, 20+ dead startups, return buyers down 40%, a $100,000 paycheck, 834 years. The Ghostwriter and Newsletter playbooks require at least one self-disclosed figure in the first third, flagged [VERIFY] if the user cannot confirm it.

### 3. Story, then bolded rule
Numbered sections tell what happened in 3-6 short sentences and end on one repeatable line. This is the unit of every list post in the Ghostwriter playbook.

### 4. Chiasmus and near-rhyme rules
"Intensity gets the ball rolling. Sustainability gets the ball winning." / "Think NOW, not HOW." / "let your hate, motivate." At least one rule per post should take this shape; more than one per section is the over-imitation tell.

### 5. Validation before building
"Collect money upfront: the promise of payment is not validation… that's a polite rejection." and the freedom-number path over the cliff-jump myth. The Newsletter playbook attaches the simplest repeatable plan rather than a named framework.

### 6. Caps, crude word, self-correction
One or two CAPS words per sentence instead of exclamation marks; one "holy schnikeys" or "Holy shit." per post as a release valve; a bold claim walked back in the same breath ("That's an exaggeration, but..."). The emotional register section uses these three to fix drafts that read polished or mean.
