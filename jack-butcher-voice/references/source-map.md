# Jack Butcher Source Map

Research date: 2026-09-09
Refresh cadence: every 6 months (next: 2027-03)

## Primary sources

| Source | URL | What it gives | Access |
|---|---|---|---|
| VV Blog / Articles index | https://visualizevalue.com/blog | 67 short essays, byline "By Jack Butcher" on most | Open, server-rendered, scrapes cleanly |
| How to Create Visual Leverage | https://visualizevalue.com/blog/how-to-create-visual-leverage | His own description of the visual method: six named techniques | Open |
| Slow Down | https://visualizevalue.com/blog/slow-down | Short-essay register, one-line closer pattern | Open |
| 1% vs. 2% | https://visualizevalue.com/blog/1-vs-2 | Numbered-example structure, a quoted outside line he cites | Open |
| The Formula for Freedom | https://visualizevalue.com/blog/the-formula-for-freedom | Bulleted-list register, his own career history | Open |
| Building a Personal Monopoly | https://visualizevalue.com/blog/building-a-personal-monopoly | Numbered "1/ 2/ 3/" framework register | Open |
| Make Yourself an API | https://visualizevalue.com/blog/make-yourself-an-api | Named-concept essay, definition-then-consequence structure | Open |
| Specificity | https://visualizevalue.com/blog/specificity | Shortest essay sampled, near-visual compression | Open |
| About page | https://visualizevalue.com/about | Site's own description of the daily practice, his bio, the agency-to-VV origin story | Open |
| Visuals archive | https://visualizevalue.com/visuals | "168 originals" - the word-plus-diagram archive. Caption text only, no image content read. Mixed: some captions are his own aphorisms, many are quotations from other people (Alan Watts, Viktor Frankl, Lao Tzu, Carl Sagan, Benjamin Franklin, Charlie Munger, Jimi Hendrix, Miles Davis, Epictetus, George Bernard Shaw, and others) that he has visualized | Open, client-rendered list, plain-text scrape worked for caption text only |
| Changelog / RSS feed | https://visualizevalue.com/feed.xml | Confirmed NOT useful as voice corpus - it is a software changelog for the visualizevalue.com site itself ("Back links match their surface", "Saved visuals load again"), not his content voice | Open, confirmed and excluded |

## What was actually fetched

Session tooling: `fetch.py` (plain HTTP GET, HTML stripped to text) against visualizevalue.com. Ten blog URLs were attempted; eight returned clean, byline-confirmed text (listed in the table above as the eight essay rows) and two returned 404 (guessed slugs that do not match the site's actual routing; not retried further - see gaps). The About page and the Visuals archive were fetched cleanly as plain text. The RSS feed (`vv-feed.xml`, pre-cached in scratchpad) was read in full and confirmed to be a site changelog, not voice content, so nothing from it went into the corpus.

One essay, "How Exceptional People Think," carries the byline "Guest Author: Polina Marinova Pompliano" on visualizevalue.com. It was read and explicitly excluded from the corpus - it is not Jack Butcher's writing even though it is hosted on his site.

WebSearch was used twice to locate secondary descriptions of the visual style (a Design Discipline masterclass writeup and general profile pieces). Those results are paraphrases by third-party writers, not verbatim Jack Butcher quotes, so nothing from them was quoted in the corpus. They informed the "Diagram grammar" section in SKILL.md only as corroborating, secondary-source context, and are marked as such there.

## Known gaps

- **No image content was ever read.** Every tool available this session (`fetch.py`, WebFetch, WebSearch) returns HTML/text, not rendered images. His native output is a diagram plus a short caption, and this research saw only the caption text (where a caption exists as page text) or, for the "168 originals" archive, a bare list of lines with no image, no alt text, and no visual layout information attached. The "Diagram grammar" subsection in SKILL.md is built from (a) his own essay "How to Create Visual Leverage," which describes his visual techniques in prose, and (b) secondary-source descriptions of the aesthetic (black-and-white, one font, geometric shapes) that were not independently verified against an actual image. Treat every diagram-composition claim in SKILL.md as inferred, not observed.
- **The Visuals archive mixes his own lines with other people's quotations, and this was not resolved caption-by-caption.** The scrape returns caption text only, with no attribution line, no image, and no way to tell from the text alone whether a given caption is his own aphorism or a line he has visualized from someone else. Where a caption text is a well-known quotation from a named historical or public figure (Alan Watts, Viktor Frankl, Lao Tzu, Carl Sagan, Benjamin Franklin, Charlie Munger, Jimi Hendrix, Miles Davis, Epictetus, George Bernard Shaw, Mary Kay Ash, Virginia Satir, and several others recognized on sight), it was excluded from the corpus entirely - it is not his voice, full stop. Where a caption text closely matches the title or the body wording of one of his own byline-confirmed essays (for example "Slow down.," "Failure = feedback.," "Truth, Perception"), it is included in the corpus at `documented` tier: the domain and the pattern strongly support his authorship, but the individual visual caption itself was never confirmed word-for-word against a human-authored source the way the essay excerpts were. A number of short, plausible-sounding original lines on the Visuals page were left out entirely because they could not be confidently sorted into either bucket - excluding them was the conservative choice, not an oversight.
- **No X/Twitter corpus.** @jackbutcher's short-form feed is very likely his primary distribution channel for the word-plus-diagram format and would be the strongest source for confirmed, attributable one-liners. It sits behind X's anti-scraping wall; WebSearch returned only secondary commentary about the account, never his tweet text itself. This is the single biggest gap. Fix on refresh with a logged-in fetch or a licensed X API pull.
- **No spoken/podcast corpus.** Multiple interviews exist (Creator Lab, The Learning Leader Show, Nathan Barry's podcast, a Justin Odisho interview) but none were transcribed this session; `yt.py` was not run against them. His stage/interview register and any looser, spoken description of his process are not represented here.
- **Only 8 of 67 blog essays were sampled**, and two attempted URLs 404'd (their slugs were guessed from title text, not confirmed via a sitemap or listing page with links). The blog's `/blog` index lists all 67 titles as plain text without hyperlinks in this scrape, so slugs for the untried essays are unconfirmed. Notably absent from the sample: "Failure is Feedback," "The First Step," "Luck Surface Area," "Frame," "Money is Time," "Process > Prize," "Do less, do more," "Writing is a Technology," and "Price vs. Value" - all on-brand, compression-heavy titles that would likely have strengthened the corpus.
- **No course or product copy sampled.** Visualize Value sells six courses and a membership; none of that sales/instructional copy was pulled. The register there (direct-response, benefit-led) may differ from the free essay register sampled here.
- **Sample skews 2021-2022.** All eight essays fetched date from August 2021 to January 2023 (per the blog index dates). No 2023-2026 long-form writing was confirmed; the About page and Changelog show the brand is still active as of July 2026, but recent essay-register samples are missing.

## Refresh instructions

1. Re-fetch `https://visualizevalue.com/blog` for the current article count and get real hyperlinks (not just title text) so essay slugs no longer have to be guessed.
2. Attempt a logged-in or API-based pull of @jackbutcher on X to close the single-form-factor gap - this is his native medium and the highest-value fix available.
3. Pull one podcast transcript (Creator Lab or The Learning Leader Show episode 379) via `yt.py` for the spoken register, checking `generated=True/False` before labeling anything `verified`.
4. Re-check the Visuals archive page for a captions-on/attribution toggle (the scrape showed a "Captions on" UI control that was not activated in this session) - if it exposes per-visual attribution, redo the corpus classification with real data instead of pattern-matching.
5. Confirm whether any course/membership copy is fair game to sample for the Ghostwriter and Sales Closer playbooks.
