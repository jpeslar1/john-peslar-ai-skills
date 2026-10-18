# David Perell Voice Source Map

Research date: 2026-10-19
Refresh cadence: every 6 months (next: 2027-04)

## Primary sources

| Source | URL | What it gives | Access |
|---|---|---|---|
| perell.com essays, WordPress REST API (custom post type `essay`) | https://perell.com/wp-json/wp/v2/essay?per_page=50&page=1 (pages 1-3) | 142 long-form essays 2015-2025 with full HTML bodies and dates | Open WP REST JSON; the route is `/essay`, not `/posts` |
| perell.com notes (custom post type `note`) | https://perell.com/wp-json/wp/v2/note?per_page=50 | 50 short writing-craft notes 2020-2023 (Personal Monopoly, Raymond Chandler Rule, I Hate Writing) | Open WP REST JSON |
| "The Ultimate Guide to Writing Online" (Aug 26 2022) | https://perell.com/essay/the-ultimate-guide-to-writing-online/ | The C- confession; the 90-minute morning habit as "activation code"; "Writing gave me wings." | Open HTML |
| "Why You Should Write" (Jul 22 2019) | https://perell.com/essay/why-you-should-write/ | "Words are the atomic unit of the internet."; weightlifting for the brain; "Re-writing is re-thinking." | Open HTML |
| Notes: "Build a Personal Monopoly", "Don't Find a Niche. Create One.", "The Raymond Chandler Rule", "Should You Write Every Day?" (Oct 2020-Aug 2021) | https://perell.com/note/build-a-personal-monopoly/ , https://perell.com/note/dont-find-a-niche-create-one/ , https://perell.com/note/the-raymond-chandler-rule/ , https://perell.com/note/should-you-write-every-day/ | Jerry Garcia quote and gloss; "I deplore the phrase"; an epiphany every 250 words; "Consistency comes before choice." | Open HTML |
| "Expression Is Compression" (Aug 14 2020), "Imitate, then Innovate" (Feb 15 2022), "Hugging the X-Axis" (Dec 17 2021) | https://perell.com/essay/expression-is-compression/ , https://perell.com/essay/imitate-then-innovate/ , https://perell.com/essay/hugging-the-x-axis/ | Sap to syrup; the Originality Disease; "a life spent hugging the X-Axis" | Open HTML |
| "Against 3X Speed" (Sep 24 2021), "Annual Review 2022" (Jan 20 2023), "Peter Thiel's Religion" (Aug 5 2019) | https://perell.com/essay/against-3x-speed/ , https://perell.com/essay/annual-review-2022/ , https://perell.com/essay/peter-thiel/ | Mike who reads 100 books a year; "more alpha than expected in understanding human behavior"; "Human culture began with a murder." | Open HTML |
| Notes: "I Hate Writing" (Apr 18 2023), "People Don't Actually Read" (Aug 25 2021), "28 Pieces of Life Advice" (Oct 7 2022) | https://perell.com/note/i-hate-writing/ , https://perell.com/note/people-dont-actually-read/ , https://perell.com/note/28-pieces-of-life-advice/ | Love and hatred of the craft; the exclamation-point rule | Open HTML |
| X @david_perell, single posts | https://cdn.syndication.twimg.com/tweet-result?id=<id>&token=a ; long posts via https://api.fxtwitter.com/david_perell/status/<id> | 5 posts 2020-2025 with timestamps: Business writing 101, "Read to collect the dots", the Paradox of Reading, the AI existential-crisis long post | Open; 25 candidate IDs were harvested from a third-party profile page (superx.so); the profile timeline endpoint was rate-limited this session |
| North Star podcast pages on perell.com (custom post type `podcast`) | https://perell.com/wp-json/wp/v2/podcast?per_page=50 ; episode used: https://perell.com/podcast/seth-godin-writing-every-day/ | Full official transcripts of 2020-2021 episodes with Perell as host; items 29-30 (Jason Fried's "traffic isn't audience"; "constellation of stars within a single galaxy") | Open WP REST JSON and HTML; official transcript on his own site, treated as verbatim spoken |
| The Nathan Barry Show ep. 138, "How To Stand Out as a Writer in the Age of AI" (Jul 23 2026) | https://nathanbarry.com/how-to-stand-out-as-a-writer-in-the-age-of-ai-2026-138/ | Timestamped transcript of a 2026 guest interview; items 31-34 ("seed stage investor in ideas", "the audience is always right") | Open HTML. DOCUMENTED (machine or lightly edited transcript) |
| How I Write podcast (Perell as host, 2023-2026) | https://www.youtube.com/@DavidPerellChannel | His current main spoken channel | Not sampled: no official transcript page; yt-dlp not attempted; podscripts.co has no show page |
| Write of Passage / Monday Musings newsletter | https://perell.com/ (signup only) | Weekly email | Not fetched; archive is not public; the essays and notes cover the same voice |

## What the corpus rests on

Thirty of thirty-four excerpts are verbatim: twenty-three from eight essays and seven notes on perell.com (2019-2023), pulled through the site's public WordPress REST API with full bodies; five from his own X account, each post fetched individually by status ID with its timestamp (one long post completed through api.fxtwitter.com); and two spoken lines from the official North Star podcast transcript hosted on his own site (Oct 2020), Perell as host. Four excerpts are documented-grade: the timestamped transcript of his July 2026 appearance on The Nathan Barry Show, with fillers and a self-interruption retained. Nothing comes from a quote aggregator. The research file's verdict line says "30 excerpts, 26 verbatim / 4 documented"; the excerpt list it contains has 34 items, 30 verbatim and 4 documented, and the corpus follows the list. Essay, note, X, and two spoken registers (host and guest) are covered; the 2023-2026 host register is not. Confidence in wording is high for items 1-30 and moderate for 31-34.

## Known gaps

- **The X sample is third-party curated.** The profile timeline endpoint returned "Rate limit exceeded" on first hit, so the 25 candidate IDs came from a superx.so profile page rather than a full recent timeline; five were quoted. Do not describe his everyday X cadence from memory.
- **The How I Write podcast (2023-2026) is unsampled.** It is his current main channel and has no official transcript page; yt-dlp was not attempted. The 2023+ spoken register rests on one guest appearance (documented). The 2020-2021 North Star transcripts on perell.com are official and plentiful if more host-register lines are needed.
- **Monday Musings / Friday Finds newsletter archive is not public** and was not fetched. The Newsletter Writer playbook is built from the perell.com notes, which carry the same register; label newsletter output as inferred from the notes when precision matters.
- **No essay later than 2023 is quoted.** The REST archive runs to 2025 and the X long post is from 2025, but the sampled essays and notes stop at Apr 2023; his post-teaching register (he says he stopped teaching partly because of AI) is represented only by items 27-28 and the 2026 interview.
- **Some references in SKILL.md come from the research notes, not from a numbered excerpt**: "I used to be just like him", the IKEA-screws and wet-clay metaphors, "though" at clause end, and the longer list of quoted authorities (Sondheim, Einstein, Bezos, Conan O'Brien, Zig Ziglar). Only Jerry Garcia, Raymond Chandler, Jason Fried, and Seth Godin appear in sampled text.
- **Raw research files** (WP JSON dumps, text conversions of all 242 posts, tweet JSON, the Nathan Barry transcript) were saved at `/private/tmp/claude-501/batch5/raw/david-perell/` at research time; that path is temporary and may be gone.
- **Anything published after 2026-10-19 is unsampled.**

## Refresh instructions

1. Re-fetch `https://perell.com/wp-json/wp/v2/essay?per_page=20&orderby=date` and `https://perell.com/wp-json/wp/v2/note?per_page=20&orderby=date`; add 5-10 verbatim excerpts from essays and notes published since 2023, with slugs and dates, so the post-teaching register is sampled; continue the numbering in the essay section.
2. Retry the X timeline (`https://syndication.twitter.com/srv/timeline-profile/screen-name/david_perell`) once, off-peak; if it still fails, fetch individual IDs via `https://cdn.syndication.twimg.com/tweet-result?id=<id>&token=a` and long posts via `https://api.fxtwitter.com/david_perell/status/<id>`. Add 5-8 verbatim posts, favoring everyday posts over curated hits.
3. Caption one How I Write episode with `yt-dlp --write-auto-sub --skip-download --sub-lang en "<url>"`; add 3-5 documented excerpts of Perell speaking (not the guest) under a new "Documented excerpts (How I Write, ASR)" heading and update the spoken-register stats.
4. Pull two or three more North Star transcripts from `https://perell.com/wp-json/wp/v2/podcast?per_page=50` (Morgan Housel, Tyler Cowen) and add 2-4 verbatim host lines to the spoken section if more host register is needed.
5. If the Monday Musings archive becomes public or a reader-forwarded issue is available, add 3-5 verbatim lines as a labelled "Newsletter" section and re-check the Newsletter Writer playbook against them.
6. Re-verify that every URL is still live, including the nathanbarry.com transcript page. Never carry a quote forward that was not re-read at its source.

## Pattern notes

### 1. Confession or image, alone on line one
Pieces open on a one-line admission or a vivid scene standing as its own paragraph ("I was a terrible writer growing up.", "Mike boastfully reads 100 books per year.", "Human culture began with a murder."), and he names the move himself in item 28. The Ghostwriter will not open on a thesis.

### 2. Coin it in Title Case
Ideas get a proper name after the first example ("I call it the Originality Disease"; Personal Monopoly; the Raymond Chandler Rule) and are reused as private vocabulary. The Ghostwriter allows one coinage per essay and the Contrarian Take Generator names the alternative in Title Case.

### 3. Quote, then gloss
An attributed line from a non-marketing authority (Jerry Garcia, Raymond Chandler, Jason Fried) is followed by "The online writing equivalent is..." or a one-sentence gloss. The Newsletter Writer requires one quote and one gloss per issue and flags any quote not re-verified as [VERIFY].

### 4. The developed metaphor
One physical-craft or body comparison is carried for a full paragraph with its real numbers (50 gallons of sap to one of syrup; weightlifting for the brain). Every playbook caps metaphors at one developed comparison and cuts undeveloped ones.

### 5. Long sentence, then aphorism
Explanatory sentences resolve into 3-6 words ("Re-writing is re-thinking.", "Consistency comes before choice."), with fragments stacked for emphasis. All three playbooks close sections and the piece on an aphorism, never a CTA, and ban the exclamation point per his own rule.

### 6. Earnest contrarian, self-implicated
He pushes against modern defaults (3x speed, "find your niche", originality first) with a named type as the foil and includes himself in the criticism. The Contrarian Take Generator requires the self-implication sentence and forbids a real person as the target.
