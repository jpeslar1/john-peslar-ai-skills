# Jay Clouse Voice Source Map

Research date: 2026-10-19
Refresh cadence: every 6 months (next: 2027-04)

## Primary sources

| Source | URL | What it gives | Access |
|---|---|---|---|
| Creator Science essays, Ghost RSS feed (full bodies) | https://creatorscience.com/rss/ | 13 Jay-bylined essays, Jan-Oct 2026, complete text with pubDate per item; the feed is capped at 15 items | Open. Ghost site; `/rss/` returns `content:encoded` full HTML. `/wp-json` 404s (not WordPress) |
| "Proof of Effort" (Oct 16 2026) | https://creatorscience.com/proof-of-effort/ | The volume-vs-effort essay: "I'm not speaking from a mountaintop here", the tree-falls-in-the-forest sale line, "choose not to" | Open HTML |
| "Attention Maximizers vs. Trust Maximizers" (Sep 12 2026) | https://creatorscience.com/attention-vs-trust/ | The two-camps frame with declared bias; crowd vs. audience; the Vegas street performer; "indifference is death" | Open HTML |
| "Single-serving effort is why the Red Queen is going to catch you" (Jul 19 2026) | https://creatorscience.com/single-serving-effort/ | Reader-question opener; "if you feel like you mailed it in, we can feel it too"; permission-then-push close | Open HTML |
| "Midslop" (Feb 8 2026) | https://creatorscience.com/midslop/ | The bot-drafted post he did not publish; "I create midslop myself"; "There's no black and white, right or wrong answer here" | Open HTML |
| "AI-rbitrage" (Feb 1 2026) | https://creatorscience.com/airbitrage/ | The 2021 NFT loss opener; FOMO vs. obsession; "your actual voice is still your best competitive advantage" | Open HTML |
| "2025 Year In Review" (Jan 4 2026) | https://creatorscience.com/year-in-review-2025/ | "My biggest failure in 2025 was thinking of 2025 as a failure"; revenue down 8%, expenses up 5%; credibility and revenue entangled | Open HTML |
| "Why people aren't buying (and how to fix it)" (Apr 18 2026) | https://creatorscience.com/why-people-arent-buying/ | Fear described physically: "my whole body clenches and my field of vision narrows" | Open HTML |
| LinkedIn posts via profile permalinks (Oct 7-16 2026) | https://www.linkedin.com/in/jayclouse plus permalinks such as https://www.linkedin.com/posts/jayclouse_the-easier-it-becomes-to-create-the-more-activity-7516862361522245632-3jqj | 7 posts: the two AI rules, crowd vs. audience, the $101,666 launch arrow chain, the 66,000-person list, the 3am parenting post, the Jessica Lackey case study | Open with a desktop UA, no login. Full text sits in `<meta name="description">`, date and author "Jay Clouse" in JSON-LD. `/recent-activity/` login-walls; `site:linkedin.com/posts jayclouse` search returned nothing, the profile page was the index |
| Creator Science Podcast, solo episode "9 Things I'm Doing Differently in My Business" (Mar 26 2026) | https://creatorscience.com/podcast/9-things-2026/ | Full site-published transcript, Jay alone, timestamped, about 55KB: the pawn-in-their-game rant, "sorry for the rant", slow growth as a slog, villagers | Open HTML; transcript inline under "Full transcript". DOCUMENTED (site-published, likely ASR-cleaned) |
| Creator Science Podcast, solo episode "12 Ways To Stand Out In 2026" (Feb 10 2026) | https://creatorscience.com/podcast/12-ideas-2026/ | Full site-published transcript, about 38KB: "as a sensitive boy", leaning on people offline and online | Open HTML. DOCUMENTED |
| Creator Science podcast index | https://creatorscience.com/podcast/ | 100+ episode pages; the solo episodes (10-year-plan, 2025-growth-strategy, 11-lessons-2021, 2024-preview) are the voice-relevant ones | Open |
| X @jayclouse | https://x.com/jayclouse | Short-form; he describes himself as weak at it | Not sampled: `syndication.twitter.com/srv/timeline-profile/screen-name/jayclouse` returned "Rate limit exceeded" this session and was not retried |

## What the corpus rests on

Twenty-nine of thirty-five excerpts are verbatim from channels he writes himself: twenty-two from seven essays on creatorscience.com (Jan-Oct 2026), copied from the full bodies in the site's own RSS feed, and seven from his own LinkedIn posts (Oct 2026), read from each permalink's page metadata with the author confirmed in JSON-LD. Six are documented-grade: the Creator Science Podcast's own published transcripts of two solo episodes (Feb and Mar 2026), which are site-published and likely ASR-cleaned, so wording is close but not byte-exact. Nothing comes from a quote aggregator and no ghostwriter credit appears on the site. The essay register, the LinkedIn register, and a spoken sample are all covered; the newsletter and the essay archive are the same corpus. Confidence in wording is high for items 1-29 and moderate for 30-35.

## Known gaps

- **X was not sampled.** The syndication timeline endpoint was rate-limited (shared quota with parallel agents) and not retried. He says repeatedly that he deprioritizes short-form and that his X output is weak, so the omission costs little for a Voice DNA; do not describe his X habits from memory.
- **LinkedIn is a thin, recent slice.** Only the roughly nine permalinks exposed on the logged-out profile page (all Oct 2026) were reachable. The six-lessons launch carousel (item 26) is an eight-page image document; only its text intro was read. Do not extend it from memory.
- **Podcast transcripts are documented-grade.** They are the site's own published transcripts, likely ASR-cleaned, so treat items 30-35 as close wording, not exact. Only two solo episodes were read; interview episodes, which would show his questioning style, were not sampled.
- **No book material.** His book on trust was a proposal in progress per the 2025 Year In Review; nothing is published. Do not quote it.
- **Pre-2026 essays are unsampled.** The Ghost RSS feed is capped at 15 items and no public Content API key was found, so his 2017-2025 writing was not read. The 2026 set alone supports the verdict.
- **Family names are from the research notes, not quoted excerpts.** His wife Mallory and his daughter are mentioned in the notes; only "our daughter" and the 3am post appear in sampled text.
- **Anything published after 2026-10-19 is unsampled.**

## Refresh instructions

1. Re-fetch `https://creatorscience.com/rss/` and add 5-10 verbatim excerpts from essays published since October 2026, with canonical URLs and dates; continue the numbering in the essay section. If the site exposes a Ghost Content API key (`/ghost/api/content/posts/?key=...`), page back through pre-2026 essays and add a labelled "Earlier essays" section.
2. Reload `https://www.linkedin.com/in/jayclouse` with a desktop UA, harvest the new permalinks, and read each post's `<meta name="description">` and JSON-LD; add 5-8 verbatim posts. If an authenticated session is available, read the carousel image pages for item 26 and note the change.
3. Retry the X syndication timeline (`https://syndication.twitter.com/srv/timeline-profile/screen-name/jayclouse`) once, off-peak; if it returns, add 5-8 verbatim posts under a new "Verbatim excerpts (X)" heading and update the stats for short-form.
4. Read one more solo episode transcript from `https://creatorscience.com/podcast/` (the 10-year-plan or 2025-growth-strategy episodes) and one interview episode for his questioning register; add 3-5 documented excerpts. If a raw audio or video source is preferred over the site transcript, caption it with `yt-dlp --write-auto-sub --skip-download --sub-lang en "<url>"` and label the result ASR.
5. If the trust book is announced or excerpted by the publisher, add 2-3 verbatim lines as a labelled section; until then keep it out of the corpus.
6. Re-verify that every URL is still live. Never carry a quote forward that was not re-read at its source.

## Pattern notes

### 1. Confessional number first
Essays and posts open on a first-person admission carrying a figure or a specific moment ("I lost a lot of money in 2021.", "I've been up since 3am.", "~66,000 people on my email list"). The Ghostwriter playbook will not start without the user's own admission and will not substitute a bold claim about the reader.

### 2. Two camps, declared bias
He names both sides of a strategy choice, refuses to rank them ("neither is better or worse; they're just different games"), then says which one he is, in a parenthetical. The Ghostwriter and Newsletter Writer playbooks place the bias in a parenthetical after a fair statement of both camps.

### 3. The number, then its cost
Every figure is complicated within two sentences ("It was a massive success. And it was also a massive lift."). The Build-in-Public Writer chains revenue to cost to margin with arrows and then states the lift and the waste.

### 4. Parenthetical honesty
Caveats, self-corrections, and winks live inside parentheses ("(myself included)", "(some worked, some were a waste of time)"). Every playbook caps these at one to three per piece; the Punctuation Override converts his em dashes into the same parentheses.

### 5. Permission, then push, then aphorism
Closers validate the reader ("You're not a failure for..."), issue one directive, and end on a short line ("indifference is death.", "The only way to do hard things is to do hard things."). The Ghostwriter and Newsletter Writer templates end on exactly this three-beat shape.

### 6. The reader's voice as the moat
He argues against volume, hook formulas, and FOMO and for the writer's own voice and slow trust-building ("If you don't want to compete on volume, the best thing you can do is choose not to."). The Newsletter Writer uses one coined two-word label per issue and one named creator as evidence, never a stat or a formula.
