# John Carlton Voice Source Map

Research date: 2026-10-19
Refresh cadence: every 6 months (next: 2027-04)

## Primary sources

| Source | URL | What it gives | Access |
|---|---|---|---|
| John Carlton's blog, The Rant, full post bodies via the WordPress REST API | https://www.john-carlton.com/wp-json/wp/v2/posts?per_page=50&page=1 (10 pages, 499 posts) | Every post Dec 2004 to Sep 2025, dated, in his own words; dateline-epigraph-"Howdy" openers, toast closers, P.S. offers; items 1-27 | Open JSON, full `content.rendered` |
| Blog posts quoted (examples) | https://www.john-carlton.com/2005/05/why_everyone_is/ , https://www.john-carlton.com/2006/10/fishing-for-hooks/ , https://www.john-carlton.com/2012/07/r-i-p-elvis-sightings-exploding-preachers/ , https://www.john-carlton.com/2020/04/the-most-awesome-lesson-i-learned-from-my-friend-gary-halbert/ , https://www.john-carlton.com/2025/09/why-is-the-ai-bubble-trying-so-hard-to-harsh-your-mellow/ | Contrarianism, hook-finding doctrine, the tabloid headline ritual, the Halbert tribute, AI-as-tool; 15 posts quoted across 2005-2025 | Open HTML |
| Copyblogger, "The Path to a Legendary Copywriting Career" (Robert Bruce interview, Part 1) | https://copyblogger.com/copywriting-john-carlton-1/ | Transcript: slacker origin story, reading Hopkins on Jay Abraham's instruction, "slumbering ape"; item 32 | Open; transcript labelled "lightly edited for clarity and grammar", so documented-grade |
| Copyblogger, "A 30-Minute Copywriting Course from a Master of the Craft" (Part 2) | https://copyblogger.com/copywriting-john-carlton-2/ | Transcript: five Carlton Copywriting 101 rules, the one-legged golfer story, "incongruous juxtaposition", "knock them off the fence", "all clients suck"; items 28-31 | Open; same transcript caveat |
| marketingrebel.com WordPress pages (Kick-Ass Copywriting Secrets sales page, Best Ads page) | https://marketingrebel.com/wp-json/wp/v2/pages , https://marketingrebel.com/kick-ass-copywriting-secrets-of-a-marketing-rebel/ | His product copy, written in the third person ("That's why John Carlton created...") | Open; read for context only, not quoted as his first-person voice |
| AWAI, "Interview with a Pro: John Carlton Reveals the Secrets Behind His Letter for 'Sex: A Man's Guide'" | https://www.awai.com/ (page cached at research time) | Publisher-quoted interview on one Rodale letter | Open; not quoted (the Copyblogger transcript is richer and closer to his words) |

Not available: X timelines for @johncarlton, @MarketingRebel and @johncarlton007 (the syndication endpoint returned 20-byte rate-limit stubs); the book Kick-Ass Copywriting Secrets of a Marketing Rebel is paid and not excerpted publicly beyond its sales page.

## What the corpus rests on

Twenty-seven of thirty-two excerpts are verbatim from the one channel he writes himself, The Rant at john-carlton.com, drawn from fifteen posts spanning 2005 to 2025 out of 499 retrieved in full. Five are documented-grade from a two-part Copyblogger interview transcript (2012) that the publisher says was lightly edited; they supply the spoken register and the one-legged-golfer and Operation MoneySuck doctrine in his own telling. Nothing comes from a quote aggregator. The blog spans twenty-one years, so the written register is strongly covered and stable; the spoken register rests on one source; his actual sales letters are absent. Confidence in wording is high for items 1-27 and moderate for 28-32.

## Known gaps

- **No X posts.** The syndication timeline for his handles returned rate-limit stubs; his X presence is light in any case.
- **Book text is paid.** Kick-Ass Copywriting Secrets of a Marketing Rebel and The Entrepreneur's Guide To Getting Your Shit Together were not read; only his blog references and the third-person sales page were seen. Do not quote the books as verbatim.
- **The print edition of The Rant (2000s, "eight pages long. Dense with two columns of copy") is not online.**
- **His actual sales-letter copy is absent.** The one-legged golfer ad and the Rodale "Sex: A Man's Guide" letter were not retrieved verbatim; the AWAI interview discusses the Rodale letter but is publisher-quoted and was not excerpted. The Ghostwriter (sales letters) playbook is therefore built from his stated doctrine and his blog letter frame, not from his letters. A swipe of the golfer ad from his own Best Ads collection (paid, marketingrebel.com) would be the single most valuable addition.
- **Only one spoken source** (Copyblogger 2012, publisher-edited). Podcast appearances (for example EOFire 2017) were not transcribed; no yt-dlp attempt and no Whisper spend this round.
- **The dateline-epigraph-"Howdy" frame is recorded in the research notes from reading the posts, not as quoted items**; the quoted paragraphs sit below that furniture.
- **Anything published after 2026-10-19 is unsampled.**

## Refresh instructions

1. Re-pull the WordPress REST feed (`curl -s "https://www.john-carlton.com/wp-json/wp/v2/posts?per_page=50&page=1"` through page 10 or until empty) and add 3-5 verbatim excerpts from posts dated after Sep 2025, continuing the blog section numbering; quote one full dateline-epigraph-"Howdy" opener as an item so the frame is in the corpus verbatim.
2. Search for an open scan or transcription of "The Amazing Secrets of a One-Legged Golfer" or the Rodale letter (archive.org, swipe-file sites that reproduce the full ad with attribution); if found and legitimately public, add a separate "Sales copy (scanned ad)" section rather than mixing it with the blog items, and note the source.
3. Caption one long podcast appearance with `yt-dlp --write-auto-sub --skip-download --sub-lang en "<url>"` (EOFire 2017 or a later interview) and add 3-5 documented items so the spoken register rests on more than one source; update the spoken-vs-written stat.
4. Retry the X syndication endpoints for @johncarlton and @MarketingRebel; if posts return, add 3-5 verbatim items in a labelled "X (verbatim)" section.
5. Re-fetch both Copyblogger transcripts and confirm items 28-32 still match; publisher pages are occasionally re-edited.
6. Re-verify that every URL is still live. Never carry a quote forward that was not re-read at its source, and never add anything from a quote aggregator or from the paid books unless the publisher has released the passage.

## Pattern notes

### 1. Dig for the hook
Hooks hide, the client is oblivious, and "You gotta dig to find it." The Hook Creator playbook starts with the dig and refuses to settle for a surface headline.

### 2. The incongruous juxtaposition
A sales element paired with an element that should not belong but bears on the result (one leg and golf, a skinny kid and 400-yard drives); the one-legged accountant fails because the leg does not matter. The Hook Creator uses this as the kill test on every candidate.

### 3. The ellipsis cliffhanger
A sentence split across two paragraphs by an ellipsis so the punch lands alone ("… and I liked him immediately."). The Ghostwriter and Contrarian Take Generator each allow one or two at the turn.

### 4. Scene, then rule
A told anecdote with a named person and place (the con man and the trust game, Halbert) followed by the lesson in one line, often with a proper-noun handle (Operation MoneySuck, Carlton's First Inconvenient Rule). Every playbook builds its body this way.

### 5. Knock them off the fence
Rookie copy gets "maybe someday"; pro copy gets the action. The Ghostwriter's close names the action line, and Operation MoneySuck is step one of the letter.

### 6. Contrarian populism with a self-own
Side with "every other bastard out there making their own way" against the suits and the crowd, and admit your own failings ("I am the worst client I have ever had"). The Contrarian Take Generator requires the self-own so the rant reads as experience rather than superiority.
