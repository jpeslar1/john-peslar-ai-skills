# Fletch (Anthony Pierri and Robert Kaminski) Voice Source Map

Research date: 2026-10-19
Refresh cadence: every 6 months (next: 2027-04)

## Primary sources

| Source | URL | What it gives | Access |
|---|---|---|---|
| Anthony Pierri LinkedIn posts | https://www.linkedin.com/in/anthonypierri exposes recent `/posts/anthonypierri_...` links; 2023 permalinks found via WebSearch "Anthony Pierri on LinkedIn" | Long argumentative posts (Attio ads teardown, homepage product marketing, the positioning formula) plus one-line captions on image posts | Open with a desktop UA; full text in the page body plus JSON-LD `datePublished` |
| Anthony Pierri, Attio ads teardown (Oct 7 2026) | https://www.linkedin.com/posts/anthonypierri_this-is-going-to-sound-very-old-man-yells-activity-7513618199494594560-pJIS | Pre-rant disclaimer, "Objection 1:", the customer disclosure, the event CTA | Open |
| Anthony Pierri, "When is it safe to stop talking about the product" (Aug 23 2023) | https://www.linkedin.com/posts/anthonypierri_when-is-it-safe-to-stop-talking-about-the-activity-7100229185603858432-jVFq | Permission question answered with "$203B 🤯" | Open |
| Rob Kaminski LinkedIn posts | https://www.linkedin.com/in/heyrobk (handle is heyrobk, not robertkaminski) | Framework posts Sep-Oct 2026: $1M ARR caution, Obese Startup Methodology, mirror pairs, the three homepage questions, the energy test | Open with a desktop UA |
| Rob Kaminski, "THE OBESE STARTUP METHODOLOGY" (Oct 13 2026) | https://www.linkedin.com/posts/heyrobk_ai-has-brought-us-a-new-methodology-for-building-activity-7515821581042892800-rnV- | The parody framework with the deadpan "Probably." landing | Open |
| The Fletch Newsletter (beehiiv) | https://fletchpmm.beehiiv.com/p/how-to-write-an-h1 ; /p/you-re-building-your-icp-wrong ; /p/the-pitfalls-of-becoming-a-platform | Three 7-13K-character essays (Feb-Apr 2026): H1 writing, firmographics versus energy (M1/M2/M3), the platform trap; house byline "Fletcher Fletchington" | Open HTML; JSON-LD `datePublished` |
| fletchpmm.com homepage and FAQs | https://www.fletchpmm.com/ ; https://www.fletchpmm.com/faqs | House voice: sprint deliverables, blunt caveats ("Nobody is going to read a 100 page slide PowerPoint"), "we rely on you to be the subject matter experts on your customers" | Open (static HTML) |
| fletchpmm.com Before/After library | https://www.fletchpmm.com/before-after (600-plus pages via sitemap) | The visual teardown format; mostly rewritten client copy | Open; not excerpted (client copy, not the founders' prose) |
| Podcasts: Exit Five "How to Master B2B Positioning with Anthony Pierri"; MKT1 positioning teardown | https://exitfive.com/podcast/how-to-master-b2b-positioning-with-anthony-pierri-fletch-pmm/ ; https://newsletter.mkt1.co/p/positioning-and-messaging-teardown | Spoken register | Not transcribed this round |

## What the corpus rests on

Thirty-one of thirty-one excerpts are verbatim from channels the two founders write themselves or publish as a house: ten from Anthony Pierri's LinkedIn (three long 2023 posts plus October 2026 posts), twelve from Rob Kaminski's LinkedIn (September-October 2026), seven from The Fletch Newsletter on beehiiv under the house pseudonym, and two from fletchpmm.com house copy. Every item carries its speaker. Nothing comes from a quote aggregator and nothing is documented-grade; there is no spoken sample. The LinkedIn register is well covered for both people, the newsletter register rests on three essays, and the visual one-slide arguments are represented only by their captions. Confidence in wording is high for all 31 items.

## Known gaps

- **Rob's archive is shallow.** His handle is `heyrobk` (`linkedin.com/in/robertkaminski` returns a stub), all sampled posts are from Sep-Oct 2026, and WebSearch does not index his older permalinks, so his pre-2026 tone is unsampled.
- **Anthony's visual arguments are not recoverable.** Most of his October 2026 posts are one-line captions on images ("AITA?", "We've officially hit bottom"); the teardown lives in the slide. The three 2023 long posts fill the gap, but the image-caption register is under-represented in text.
- **Newsletter authorship is pseudonymous.** The beehiiv sitemap lists only three posts, all bylined "Fletcher Fletchington"; which founder wrote which essay is not stated, so newsletter lines are attributed to Fletch, not to Anthony or Rob.
- **No spoken excerpts.** Podcast appearances (Exit Five, MKT1, Lenny-style interviews) were not transcribed, so spoken cadence is inferred from the written staircase.
- **Before/after pages are client copy.** The 600-plus teardown pages are rewritten client messaging, useful as a format reference but not quotable as the founders' own voice.
- **Anything published after 2026-10-19 is unsampled.**

## Refresh instructions

1. Fetch `https://www.linkedin.com/in/anthonypierri` and `https://www.linkedin.com/in/heyrobk` with a desktop user agent, harvest fresh `/posts/<handle>_...` permalinks, and add 4-6 verbatim posts per person with dates from JSON-LD or the activity ID; keep the speaker tag on every source line.
2. Search `site:linkedin.com/posts heyrobk` and `site:linkedin.com/posts anthonypierri` with topic words (positioning, homepage, ICP, platform) to locate older long posts, especially any Rob post before 2026.
3. Re-fetch the beehiiv sitemap at `https://fletchpmm.beehiiv.com/sitemap.xml` and add 3-5 verbatim excerpts from any new essay; note if a byline other than "Fletcher Fletchington" appears.
4. Caption one podcast appearance with `yt-dlp --write-auto-sub --skip-download --sub-lang en "<url>"` if a video exists (the Exit Five episode is the first candidate); add 3-5 documented excerpts under a new "Documented excerpts (ASR captions)" heading with the speaker tagged, and update the spoken-register stat.
5. Re-fetch `https://www.fletchpmm.com/` and `/faqs` for changed house copy; replace items 30-31 if the wording has moved.
6. Re-verify that every URL is still live. Never carry a quote forward that was not re-read at its source.

## Pattern notes

### 1. The staircase
One idea per line, blank line between, ellipses bridging the break ("Okay fair enough... / ...but is it possible"). The LinkedIn Content Expert playbook builds every post this way and forbids prose paragraphs.

### 2. Quote, then diagnose
A founder's or the market's words go in quotation marks and the real problem is named under them ("Companies SHOULD be doing X" means a marketing problem). The Hook Creator and Objection Handling Expert playbooks both open on the quoted line.

### 3. The forced choice
"Option 1 / Option 2" with one obviously true, left for the reader to pick. The Objection Handling Expert closes on it so the reply never has to say "you're wrong."

### 4. Parody with a deadpan landing
A fake methodology or cheatsheet delivered straight for three to five steps, then one word ("Probably.", "That's it."). The Hook Creator writes the landing alongside the hook so they match.

### 5. The three questions and the energy test
Every page is tested against What is it, Who is it for, When would I use it; every ICP against whether the market already spends energy on the job. Both are mandatory checks in the LinkedIn Content Expert and Objection Handling Expert playbooks.

### 6. Two speakers, one register
Anthony heckles and discloses ("as an Attio customer btw"); Rob mirrors and numbers. The Output Format labels which register each variant leans toward, and the customer-disclosure rule governs any named teardown.
