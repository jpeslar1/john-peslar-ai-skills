# David Ogilvy Source Map

Research date: 2026-09-09
Refresh cadence: every 12 months (the corpus is historical and will not drift; next: 2027-09)

## Corpus quality warning

This was the weakest-sourced corpus in the voice-dna collection, and this revision improves it without pretending to fix the underlying problem: the two canonical books are still unread. Every item is still `documented`, meaning widely republished and consistently attributed, or in the case of the new items, either the agency's own official curation or a swipe-file reproduction of an actual advertisement. None of it is `verified` in this project's sense, and none of it can be, short of buying and reading the books, because Ogilvy died in 1999 and has no site of his own. Ogilvy is one of the most misquoted figures in advertising, and quote sites propagate errors between each other. His own memo says "Check your quotations." Do that before any of these lines appears in client-facing work.

## Primary sources

| Source | URL | What it gives | Access |
|---|---|---|---|
| Confessions of an Advertising Man (1963) | archive.org (lending only) | The register, the reader-respect doctrine, the headline economics | In print, purchase; a lending scan exists but was deliberately not used, see below |
| Ogilvy on Advertising (1983) | archive.org (lending only) | The rules with examples, the long-copy argument, the picture-and-caption rules | In print, purchase; a lending scan exists but was deliberately not used, see below |
| The Unpublished David Ogilvy (1986) | - | The internal memos, including "How to Write" (1982) | In print, purchase |
| ogilvy.com official quotations reissue | https://www.ogilvy.com/ideas/ogilvy-75-quotations-david-ogilvy | Agency-curated short quotations, sourced by the agency to named books and internal reports | Open, fetched directly this session |
| ogilvy.com campaign history | https://www.ogilvy.com/ideas/ogilvy-75-75-years-iconic-campaigns | The agency's own dated list of his campaigns, by client and year | Open, fetched directly this session |
| Swipe file archive, Rolls-Royce collection | https://swiped.co/collections/rolls-royce-ad-campaign-ogilvy/ | Reproduced headlines and a first-person Ogilvy quotation about his working method | Open, fetched directly this session |
| Swipe file archive, Hathaway | https://swiped.co/file/man-hathaway-shirt-ad-david-ogilvy/ | Campaign background and the eye-patch story; body copy text itself required cross-referencing elsewhere | Open, fetched directly this session; body copy not confirmed on this specific page |
| Reproductions of the 1982 memo (Boing Boing, Open Culture, Farnam Street, and others) | https://boingboing.net/2015/04/23/david-ogilvys-1982-memo.html | The ten hints, consistently reproduced across sources | Open, fetched directly this session |

## What was actually fetched

**2026-09-09, original build:** Nothing primary. The corpus was assembled from search results and one quotation aggregator. Two attempts to have a page-reading tool reproduce the memo verbatim were declined by that tool on copyright grounds, which is why the memo items were drawn from fragments that appeared consistently across multiple independent reproductions.

## What was fetched on 2026-09-09 (this revision)

- `https://swiped.co/file/rolls-royce-ad-by-david-ogilvy/`, `https://swiped.co/file/worst-kept-secret-rolls-royce-ogilvy/`, `https://swiped.co/file/13550-rolls-royce-ogilvy/`, `https://swiped.co/file/under-bonnet-rolls-royce-ogilvy/`, and `https://swiped.co/file/no-chauffeur-rolls-royce-david-ogilvy/` all fetched directly and scraped cleanly. Together they supplied four Rolls-Royce headlines and, most valuably, a first-person Ogilvy quotation about his own research method on the "At 60 miles an hour" ad (corpus item 34).
- `https://swiped.co/file/man-hathaway-shirt-ad-david-ogilvy/` fetched directly and scraped cleanly, but the page carries campaign background rather than the ad's running body copy. The body-copy text used in corpus items 26-27 came from a WebSearch synthesis across secondary reproductions (Medium, sitepoint.com, and others), not from a single page fetched by this session. This is flagged explicitly in the corpus and should be treated as the weakest-sourced group added this revision.
- `https://boingboing.net/2015/04/23/david-ogilvys-1982-memo.html` fetched directly and scraped cleanly. It reproduces the full ten-hint memo and supplied one line missing from the earlier build ("If it is something important, get a colleague to improve it.").
- `https://www.ogilvy.com/ideas/ogilvy-75-quotations-david-ogilvy` and `https://www.ogilvy.com/ideas/ogilvy-75-75-years-iconic-campaigns` both fetched directly from ogilvy.com itself and scraped cleanly. The quotations page names its own sources (the two books, How to Create Advertising That Sells, Principles of Management, internal Creative Council reports); the campaign history page gave dated, agency-confirmed facts, including that "The Guinness Guide to Oysters" was his first ad, not Rolls-Royce or Hathaway as internet folklore sometimes has it.
- `https://www.entrepreneur.com` was not used for Ogilvy (that route was for the Dan Kennedy corpus). `archive.org` listings for both books were located and confirmed to be lending-only scans; per this project's constraint, that access mode was not used to extract text.
- YouTube caption route was not usable this session: `yt.py search` worked and returned candidate videos (e.g. ADWEEK's "David Ogilvy: Essentials"), `yt.py tracks` succeeded and reported an auto-generated (ASR) caption track, but `yt.py tx` failed with `IpBlocked` (HTTP 429-class YouTube IP block) on the first attempt. Not retried, per the session's tooling constraint. No video material was added this session as a result.

## Known gaps

- **No book text, still the top gap.** Both canonical books remain unread. This revision added agency-curated quotations and actual ad copy, which is a real improvement, but it is not the same as sampling his running prose from the books. The voice fingerprint in SKILL.md is still built from aphorisms, a memo, and ad headlines rather than from continuous book prose.
- **Hathaway body copy is the weakest-sourced group in this revision.** It was assembled via search synthesis across secondary reproductions, not fetched by this session from one archival page. Confirm against a photographed scan before treating it as exact.
- **No video or spoken register.** YouTube transcript access was blocked this session by an IP-level 429 (see above). This is a new, concrete finding this revision (previously the corpus simply had no video route attempted); the gap itself is not closed.
- **Wording variance.** Several items, particularly "If it doesn't sell, it isn't creative", appear in slightly different forms across sources. The corpus records the most common form and flags the variance. This revision surfaced one more: the Rolls-Royce "At 60 miles an hour" ad is dated 1958 by swiped.co and 1959 by ogilvy.com's own campaign history. Both are cited; neither is silently preferred.
- **Attribution risk.** At least one widely circulated Ogilvy quotation collection includes lines he did not write. Anything not traced to a book, a memo reproduction, a dated advertisement, or the agency's own official reissue should be treated as unattributed.
- **Only two ad campaigns given real depth.** Rolls-Royce and Hathaway got focused research this revision. Schweppes, Dove, Puerto Rico, and Britain tourism are mentioned in the corpus at the level of a single background fact each, not sampled as copy. A refresh could pull actual headlines for each from the swipe-file archive the same way this revision did for Rolls-Royce.

## Refresh instructions

1. Read Ogilvy on Advertising and Confessions of an Advertising Man. Replace the aphorism corpus with short cited quotations including page references, and drop the `documented` labels for anything actually verified against the printed page.
2. Confirm the Hathaway body copy (items 26-27) against a photographed scan of the actual 1951 ad, ideally via a library archive or a museum collection rather than another aggregator.
3. Pull actual headlines for Schweppes, Dove, Puerto Rico Tourism, and Visit Britain from swiped.co the way this revision did for Rolls-Royce, following the same collection-page pattern (`https://swiped.co/collections/...` where one exists, or searching `site:swiped.co <client name> ogilvy`).
4. Retry `yt.py tracks` / `yt.py tx` on the ADWEEK "David Ogilvy: Essentials" video or a similar clip once the IP block has cleared, to add a spoken or archival-footage sample; note it will be ASR-based (`documented`, not `verified`) even if it succeeds.
5. Resolve the 1958-vs-1959 Rolls-Royce dating discrepancy against a primary trade-press source before it matters for client-facing accuracy.
6. Remove or re-source any line that cannot be traced to a book, a memo, a dated advertisement, or the agency's official reissue.
7. Keep the historical framing note on item 1. It is a 1955 line and should not be presented as live audience guidance.
