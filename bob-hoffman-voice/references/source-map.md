# Bob Hoffman Voice Source Map

Research date: 2026-10-19
Refresh cadence: every 6 months (next: 2027-04)

## Primary sources

| Source | URL | What it gives | Access |
|---|---|---|---|
| The Ad Contrarian blog (Blogger) | https://adcontrarian.blogspot.com/ | 540 posts, 2013-11 to 2021-01, full HTML bodies; items 1-18 | Public. JSON feed `https://adcontrarian.blogspot.com/feeds/posts/default?alt=json&max-results=100&start-index=N` returns full content, title, date, permalink |
| Nobody Gives A Flying Shit About Your Brand (2015-05-13) | https://adcontrarian.blogspot.com/2015/05/nobody-gives-flying-shit-about-your.html | The dull-inventory opener; consumer indifference as base case | Public |
| There's No Bullshit Like Brand Bullshit (2015-02-17) | https://adcontrarian.blogspot.com/2015/02/theres-no-bullshit-like-brand-bullshit.html | Yes/No setup-then-reversal; Pepsi/Nike/McDonald's loyalty lines | Public |
| The First Rule Of Social Media (2014-10-13) | https://adcontrarian.blogspot.com/2014/10/the-first-rule-of-social-media.html | Toasters-and-paper-clips inventory; made-up-number alert | Public |
| 10 Compelling Reasons To Target Millennials (2015-08-11) | https://adcontrarian.blogspot.com/2015/08/10-compelling-reasons-to-target.html | The bait-and-reveal (over-50s) | Public |
| What If Targeting Doesn't Work? (2015-07-30) | https://adcontrarian.blogspot.com/2015/07/what-if-targeting-doesnt-work.html | "-o-graphics" coinages; one-cut media planning | Public |
| Data Is A Frame, Not A Picture (2015-10-12) | https://adcontrarian.blogspot.com/2015/10/data-is-frame-not-picture.html | Question volley; the frame-not-picture line | Public |
| Tons Of Data And Not An Ounce Of Sense (2016-07-18) | https://adcontrarian.blogspot.com/2016/07/tons-of-data-and-not-ounce-of-sense.html | The flat moral close | Public |
| The Six Stages Of Digital Delusion (2019-11-25) | https://adcontrarian.blogspot.com/2019/11/the-six-stages-of-digital-delusion.html | Headquarters opener; numbered stage list | Public |
| The Only Test Of Brand Purpose (2019-06-24) | https://adcontrarian.blogspot.com/2019/06/the-only-test-of-brand-purpose.html | Purpose test (taxes) | Public |
| The Universal Creative Brief (2015-04-27) | https://adcontrarian.blogspot.com/2015/04/the-universal-creative-brief.html | Ironic exclamation; agency satire | Public |
| How adtech helped to radicalize us (Campaign UK piece, republished 2021-09) | https://adcontrarian.blogspot.com/2021/09/how-adtech-helped-to-radicalize-us.html | Long-form argumentative register (read, not excerpted) | Public |
| The Ad Contrarian newsletter archive index | https://www.bobhoffmanswebsite.com/newsletters | Issue list #1-#338 (2016-2025) with createsend links; items 19-31 | Public Wix page; older issues at `createsend.com/t/d-<ID>`, 2022+ issues at `typeagroup.createsend.com/campaigns/reports/viewCampaign.aspx?...ID=<ID>` |
| Newsletter #336 Nobody Learns Anything (2025-03-30) | https://createsend.com/t/d-210AD93101C5BC6E2540EF23F30FEDED | "Annoying dickheads like me"; dashed bottom-line list | Public, fetches clean with curl |
| Newsletter #335 Let's Pretend (2025-03-23) | https://createsend.com/t/d-1590BA1E4BB2BA6A2540EF23F30FEDED | "Let's pretend" anaphora; Roscoe; precision targeting thesis | Public |
| Newsletter #334 Online Adv Hits Rock Bottom (2025-02-16) | https://createsend.com/t/d-DA28B0CF6ED8263E2540EF23F30FEDED | "What if I told you" moral-spine opener | Public |
| Newsletter #337 It's Supposed To Be Fun (2025-04-06) | https://createsend.com/t/d-4BB74B692D3F5E202540EF23F30FEDED | Personal register: the fun part and the torture part | Public |
| Newsletter #338 It's A Free Book (2025-05-03) | https://createsend.com/t/d-23FA5E4886C948502540EF23F30FEDED | Mock-generous promotion; blogweasel close | Public |
| Newsletter #278 The Three-Word Brief rerun (2022-03-20) | https://createsend.com/t/d-D10C440F1B773C602540EF23F30FEDED | His core fame-not-brand-meaning essay; the DMV line | Public |
| Newsletter #245 Google's Secret Project (2021-04-18) | http://createsend.com/t/d-8103DA99AD729E9B2540EF23F30FEDED | Early newsletter register (read, not excerpted) | Public |

## What the corpus rests on

All thirty-one excerpts are verbatim from Hoffman's own writing: eighteen from the Ad Contrarian blog (2014-2019), read through the blog's own JSON feed, and thirteen from seven issues of The Ad Contrarian newsletter (2021-2025), read from the Campaign Monitor archive his site links to. Zero items are documented-grade; no ASR, journalist transcription, or quote aggregator was used. Confidence in wording is high throughout. The written register is sampled across twelve years and two channels and is strikingly consistent; there is no spoken sample at all.

## Known gaps

- **No spoken-register sample.** No talk, podcast, or interview was collected. His EU Parliament talk exists as newsletter #314, but the createsend "viewCampaign" URL variant returned only the Campaign Monitor wrapper, not the body. Any claim about how he speaks is inferred from the written register.
- **Books not excerpted.** BadMen, Adscam, The Three Word Brief, Marketers Are From Mars, and Inside The Black Box have no fetchable publisher-hosted excerpt. Newsletter #278 reruns the Three-Word Brief essay in full, which covers that thesis verbatim; the others are unsampled.
- **X account @AdContrarian not sampled.** The syndication timeline endpoint was rate-limited during research. The blog and newsletter are his primary channels, so this is a minor gap.
- **2022+ newsletter issues use a different archive URL.** Issues after 2022 live at the `typeagroup.createsend.com/.../viewCampaign.aspx` variant, which returned only the wrapper on one attempt; the 2025 issues sampled here were reached through `createsend.com/t/d-<ID>` links. Confirm which pattern works on refresh.
- **Cited studies are his citations, not independently checked.** Adlook, Nielsen, and the abuse-site reporting he references appear as he reports them; treat figures as his published claims.
- **Anything published after 2026-10-19 is unsampled.**

## Refresh instructions

1. Re-fetch https://www.bobhoffmanswebsite.com/newsletters and pull any issue after #338 (2025-05-03) with `curl -L <createsend link>`; add 5-8 verbatim excerpts and extend the newsletter section numbering.
2. If a `viewCampaign.aspx` link returns only the Campaign Monitor wrapper, look for the matching `createsend.com/t/d-<ID>` short link on the index page, or try `https://web.archive.org/web/2025/<url>`.
3. Attempt a spoken sample once: find the EU Parliament talk or a podcast appearance on YouTube and run `yt-dlp --write-auto-sub --skip-download --sub-lang en -o "<slug>/%(id)s" <url>`; if it returns HTTP 429, use the show's published transcript page. Label the result documented and add a spoken-register stat.
4. Retry `https://syndication.twitter.com/srv/timeline-profile/screen-name/AdContrarian` to sample X; if still rate-limited, skip, the channel is secondary.
5. Re-verify every URL in the Primary sources table is live before carrying any quote forward; the Blogger JSON feed is the fastest check for blog items.

## Pattern notes

### 1. Setup, then gut-punch
Parallel declaratives or a list build a premise; one short line in its own paragraph reverses it ("Oh, wait a second... that's not Millennials, that's people over 50. Sorry."). The Contrarian Take Generator returns the turn line first so the punch can be judged on its own.

### 2. The dull inventory
Ordinary objects and ordinary worries (toasters, socks with holes, rent to pay) make consumer indifference concrete. The Ghostwriter playbook uses it as the preferred opener.

### 3. Scare quotes on jargon
"Engaging", "content", "precision", "brand purpose": the quotes do the mocking and no further comment is added. All three playbooks cap the move to avoid the every-noun tell.

### 4. Grant every premise
"Let's pretend..." frames give the target everything it asks for before the fact arrives. The Contrarian Take Generator opens report takedowns this way.

### 5. The made-up-number alert
Illustrative figures are flagged as invented in the same breath ("97% of product categories (made-up number alert)"). The skill borrows this as its honest alternative to [VERIFY] when a number is for scale, not proof.

### 6. The flat moral
One undecorated sentence of real conviction closes the piece and nothing follows it ("tons of data and not an ounce of fucking sense"). The Newsletter Writer ends each section on it and the issue on a two-line dismissal.
