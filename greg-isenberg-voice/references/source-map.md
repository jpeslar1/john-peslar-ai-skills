# Greg Isenberg Voice Source Map

Research date: 2026-10-18
Refresh cadence: every 6 months (next: 2027-04)

## Primary sources

| Source | URL | What it gives | Access |
|---|---|---|---|
| Late Checkout newsletter archive (Substack, 2023) | https://latecheckout.substack.com/archive | Weekly letters in his voice: hot-take lists, personal anecdotes, the "Greg's bookmarks" sign-off block; 14 excerpts from 4 letters | Open; the Substack JSON API (`/api/v1/posts/<slug>`) returns the full `body_html` without login |
| "The most important post I've written in a while" (Oct 1 2023) | https://latecheckout.substack.com/p/the-most-important-post-ive-written | Life-vision letter: the quiet-Slack scene, "Technicolor detail," "what's your line?" | Open |
| "I'M FEELING SPICY TODAY" (Sep 23 2023) | https://latecheckout.substack.com/p/im-feeling-spicy-today | Numbered hot takes: Solo Burnouts, MRR charts are whack, boring business is boring | Open |
| "Why I no longer hire from Harvard & Google" (Oct 6 2023) | https://latecheckout.substack.com/p/why-i-no-longer-hire-from-harvard | Money receipt (Instagram, WhatsApp), Counter Strike clans, "parties on the internet" | Open |
| "How I (almost) made $4M on Loom" (Oct 15 2023) | https://latecheckout.substack.com/p/how-i-almost-made-4m-on-loom | The confessed miss; the stacked "They never talked about" lines | Open |
| gregisenberg.com blog (Greg's Letter web versions, 2025) | https://www.gregisenberg.com/blog | 2025 essays: "Everyone should start a business," "One thing!," "The Greatest Adventure Ever"; 6 excerpts | Open |
| "Everyone should start a business" (May 29 2025) | https://www.gregisenberg.com/blog/everyone-should-start-a-business | "That's backwards," the repetition triplet, "funding your experiments" | Open |
| "One thing!" (Apr 15 2025) | https://www.gregisenberg.com/blog/one-thing | Asymmetric bets; "One thing, baby. One thing!!" | Open |
| "The Greatest Adventure Ever" (Apr 3 2025) | https://www.gregisenberg.com/blog/the-greatest-adventure-ever | "At 20, you're dangerous"; cash-flow positive over Series A; the spaced-hyphen habit | Open |
| @gregisenberg on X | https://x.com/gregisenberg | Short takes, lowercase two-liners; 4 posts from Jan 18-19 2026 | Per-tweet only, via `https://cdn.syndication.twimg.com/tweet-result?id=<id>&token=a`; the profile timeline endpoint is IP rate-limited |
| feeder.co mirror of @gregisenberg | https://feeder.co/discover/12d985a353/x-com-gregisenberg | Tweet IDs and truncated text for Jan 2026 posts; used only to locate IDs, never quoted | Open; stale (Jan 2026) |
| The Startup Ideas Podcast, "$5T opportunity: AI Roll Ups" (YouTube, c. Sep 28 2026) | https://www.youtube.com/watch?v=ZT4mpjx0JnE | Spoken register: big-number cold open, "If you're new here," 5,000-likes CTA, "Take care."; 5 excerpts | Open video; DOCUMENTED (yt-dlp auto-captions; HTTP 429 on first attempt, succeeded on retry) |
| gregisenberg.com home | https://www.gregisenberg.com/ | Self-description one-liners; context only, not excerpted | Open |

## What the corpus rests on

Twenty-four of twenty-nine excerpts are verbatim from channels he writes himself: fourteen from four 2023 Late Checkout letters (full body via the Substack JSON API), six from three 2025 Greg's Letter essays on gregisenberg.com, and four X posts from January 2026 fetched one at a time through the syndication endpoint. Five are documented-grade YouTube auto-captions from a single podcast episode. The written sample is consistent across 2023 and 2025 and drawn entirely from his own channels; the short-form (X) sample is thin at four posts, and the spoken sample is one episode. Confidence in wording is high for items 1-24 and moderate for 25-29.

## Known gaps

- **X is thinly sampled.** Profile timeline endpoints (syndication timeline, Nitter mirrors) are IP rate-limited or blocked; only tweet IDs located through the feeder.co mirror could be fetched individually. Four posts, all from January 2026, and no 2026-Q3 or Q4 posts. The lowercase two-liner register rests on this small sample.
- **One podcast episode only.** YouTube captions returned HTTP 429 on the first attempt and succeeded on retry for a single episode; no second episode was captured. The intro and outro formula is evidenced once.
- **The current Greg's Letter email issues were not obtained.** The post-Substack newsletter has no stable public archive beyond the gregisenberg.com/blog web versions; no 2026 letter text was sampled.
- **LinkedIn was not collected.** Login wall; the Zevari MCP route would need user context confirmation and was not used.
- **The 2023 Substack letters use em dashes occasionally** per the research notes, but none fall inside the sampled excerpts, so the native dash habit is inferred from the pattern notes rather than shown in the corpus.
- **Anything published after 2026-10-18 is unsampled.**

## Refresh instructions

1. Re-fetch the Substack archive list at https://latecheckout.substack.com/api/v1/archive?sort=new&limit=20 and pull any letter body with `curl -s https://latecheckout.substack.com/api/v1/posts/<slug>`; add 5-10 verbatim excerpts with URLs and dates, continuing the item numbering.
2. Re-crawl https://www.gregisenberg.com/blog for new Greg's Letter web versions and excerpt 3-5 lines from each new essay.
3. For X, locate recent status IDs (feeder.co mirror, search results, or a logged-in human export) and fetch each with `curl -s 'https://cdn.syndication.twimg.com/tweet-result?id=<id>&token=a'`; aim for 10-15 posts so the short-form register is properly evidenced.
4. Pull captions from one or two more podcast episodes: `yt-dlp --write-auto-sub --sub-lang en --skip-download -o '%(id)s' 'https://www.youtube.com/watch?v=<id>'`; wait and retry on HTTP 429. Label all caption text documented-grade.
5. Re-verify that every URL above is still live. Never carry a quote forward that was not re-read at its source.

## Pattern notes

### 1. Hot take, justification, kicker
Each numbered item is a claim ("Solopreneurs = Solo Burnouts."), a short justification, and a jab or question ("Anyone else?"). The Ghostwriter and Newsletter Writer playbooks make this three-beat unit the building block of every list.

### 2. Concrete fantasy scene for abstract advice
The life-vision letter puts the reader in a quiet Slack with a "cha-ching" channel before naming the principle. The Ghostwriter playbook interviews for one prop and places the scene before the list.

### 3. Money receipt with casual math
Two companies and two numbers ($1B with 13 employees, $19B with 55), or a personal miss priced out ($25k into $3M-$4M). The Hook Creator playbook uses it as an opener; every figure must be real or flagged [VERIFY].

### 4. Repetition triplet, then the turn
"The tools are basically free now. The distribution is basically free. The barriers are basically gone." followed by a one-line reversal. Used once per piece in the Ghostwriter and Newsletter playbooks to build momentum into the principle.

### 5. Consensus, then the slap
"Everyone says X. That's backwards." / "People are saying X. Couldn't be less true." The Contrarian Take Generator opens on the quoted orthodoxy and lands the slap in one short sentence, then gives the mechanism.

### 6. Slogan close and question back
Posts end on 2-4 words ("Less is more.", "One thing, baby.", "Bottom line > top line.") or a question ("How cool is that?", "So, what's your line?"). All four playbooks use one of these as the default closer; on X the closer is the lowercase punchline line.
