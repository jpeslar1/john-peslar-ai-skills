# Lara Acosta Voice Source Map

Research date: 2026-08-24; inbox refresh 2026-10-18
Refresh cadence: every 6 months (next: 2027-04)

## Primary sources

| Source | URL | What it gives | Access |
|---|---|---|---|
| LinkedIn profile and posts | https://www.linkedin.com/in/laraacostar/ (10 individual post URLs cited in voice-corpus.md) | Core LinkedIn corpus: hooks, rehooks, tactical lists | Login wall |
| X profile | https://x.com/Laraacostar (2 posts cited in voice-corpus.md) | Short-form register on X | Login wall |
| Kleo interview and bio | https://kleo.so/blog/lara-acosta | Her own words on story-first content, underdog bio | Open |
| VeryGoodCopy micro-interview | https://www.verygoodcopy.com/microinterviews-3-1/lara-acosta | Her own words on writing philosophy, scarcity mentality | Open |
| Email, The Known Club cohort 3 launch sequence (May 2026) | 8 emails from lara@literallyacademy.com | Verified verbatim sales-email register: subject lines, CTAs, sign-offs | Primary, author-delivered; private copy (operator's inbox) |
| Email, daily nurture drip (Sep 11 - Oct 17 2026) | 20 emails from lara@theknownclub.com ("Lara Acosta", The Known Club, via Kit) | Evergreen and nurture register: mindset stories, tactical frameworks (S.M.P.V., three engines, broad → narrow → niche, 4-3-2-1), free-resource gifts, algorithm analysis, client-win proof | Primary, author-delivered; private copy |
| Email, Literally Academy "Founders' Vault" launch (Sep 28 - Oct 4 2026) | 10 emails from lara@theknownclub.com | Full 7-day sunset-launch sequence: announcement, price ladder, case study, framework, "this is hard", resend, future-pace, last call, 4-hours-left, fixed footer block | Primary, author-delivered; private copy |
| Email, promos (Sep 15 - Oct 11 2026) | 6 emails from lara@theknownclub.com | Video-promo template ("I recorded a brand NEW video"), fake-"Re:" resend, live-workshop seat email, 1:1 coaching offer | Primary, author-delivered; private copy |
| Style-analysis corroboration only | magicpost.in, connectsafely.ai, buldrr.com | Context only; contain author-reconstructed examples, NOT used for quotes | Open |

## What the corpus rests on

The post and interview excerpts (20 items) come from her own LinkedIn and X post pages plus two interviews where she is quoted directly; confidence is high on wording but the sample leans older (2022-2025) since public post pages were fetched individually rather than pulled from a live, current feed. The email corpus (91 items from 44 emails) is the strongest part of this skill: emails Lara wrote and sent to the operator's inbox, copied verbatim. It is primary source in the strictest sense (author-written, author-sent, no intermediary), and after the October 2026 refresh it covers all three of her email registers: launch sequence (May 2026 cohort launch and the Sep-Oct 2026 Literally Academy sunset), daily nurture/evergreen, and promo. Private delivery is an access detail, not a quality problem; a third party who wants to re-check a line needs the inbox, and the refresh instructions cover re-pulling.

## Known gaps

- **No video or Stories sample.** She is active on video-first formats (LinkedIn video with 1M+ impression posts, YouTube trainings she links from nearly every promo email, Reels, Instagram where she passed 100k followers in Oct 2026); none were reviewed. The voice here is text-only. This is the largest remaining gap.
- **Post sample skews older.** Most LinkedIn/X posts cited are from 2022-2024, with one from 2025. Her current 2026 feed was not re-pulled; the emails quote several of her 2026 post hooks second-hand, but the posts themselves were not fetched.
- **Sender and brand changed between passes.** May 2026 emails came from lara@literallyacademy.com (Literally Academy); by Sep 2026 all sends come from lara@theknownclub.com (The Known Club) via Kit, and Literally Academy was shut down and sunset-sold as the "Founders' Vault". Searches on the old domain return nothing after 2026-05-17; use the new domain.
- **Follower/revenue figures not independently verified.** "360k followers", "$3.5M from LinkedIn", "3x 7-figure businesses", "Forbes 30 Under 30" come from her own emails and bio, not an audited source. Quote them as her claims.
- **Email sample ends 2026-10-17.** Anything sent after that date is unsampled.

## Refresh instructions

1. Pull her recent LinkedIn posts (profile above) and X feed; add 5-10 new verbatim excerpts with URLs to `voice-corpus.md`.
2. Re-check hook lengths, arrow formatting, and CTA norms against current posts; her format evolves with LinkedIn's algorithm.
3. Treat aggregator "example posts" as reconstructions unless matched against an original post URL. Drop any quote that can no longer be verified at its source.
4. Pull new emails from the operator's inbox first (primary): from the admin-dev repo, `set -a; source .env; set +a; python3 scripts/gmail_read_dwd.py search --max 100 'from:theknownclub.com after:YYYY/MM/DD'`, then `gmail_read_dwd.py read <id>` per message. Strip Kit tracking URLs, zero-width spaces, and the footer (address, unsubscribe). Add the batch as its own dated subsection, label each send launch / nurture / evergreen / promo, and continue the item numbering. Check whether the sender domain changed again.
5. Still missing after two passes: a spoken sample. Pull captions from one of the YouTube trainings she links (yt-dlp) and add a "documented" spoken section.

## Pattern notes

### 1. Underdog time-jump
Low point and current state contrasted in two dated lines. The skill uses the USER's own arc, never her biography.

### 2. Fluff-free line discipline
Every sentence precise, applicable, and short; over-explaining is the cardinal sin. This is the universal editing pass for the voice.

### 3. Hook plus rehook
8-10 word mobile-first hooks with a parenthetical or contrast rehook on line 2, and value that re-grips every few lines ("a master hook. In every. single. line.").

### 4. Story-to-you pivot
First person for the story, second person for the lesson; "my content is never about me, it's about them."

### 5. Anti-comparison and anti-guru framing
She dismantles visible-success illusions ("What you see / What you SHOULD see") and positions against generic guru advice with her own lived data.

### 6. Emotion resolved into a directive
Vulnerability (fear of being seen, the broke-student room) always flips into an imperative for the reader within a couple of lines.

### 7. CTA norms
Repost-for-resource asks, newsletter P.S. with the recurring fluff-free tagline, warm FAQ-style P.S. questions; no hashtag piles or engagement-bait polls.

### 8. Delusional self-belief (added 2026-10-18)
The dominant mindset theme of the fall-2026 drip: "delusional" reclaimed as a virtue, journaling goals in the past tense, "do it scared", "waiting to feel ready is the most expensive thing you will ever do". Nurture emails resolve this into one concrete repetition target (100 cold emails, 100 Looms, 100 posts).

### 9. Attention game vs revenue game (added 2026-10-18)
Her core business argument in email: impressions and follower counts are a different game from revenue; the three engines (offer, marketing, funnel) sit behind content; most selling happens in email, not on LinkedIn. The skill should refuse "post more" as advice and route to offer, positioning, or funnel instead.

### 10. Evergreen line bank (added 2026-10-18)
She reuses proven lines verbatim across months ("I built my entire account by emulating the best in the game…", "If your post fails, no one saw it. Try again tomorrow."). Repetition across sends is a feature of the voice, not a flaw; the skill can reuse a user's own best lines the same way.
