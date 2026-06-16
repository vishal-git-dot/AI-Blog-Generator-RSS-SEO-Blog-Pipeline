---
title: "The Inline HTML Almost Nobody Uses"
slug: "the-inline-html-almost-nobody-uses"
author: "Dimon"
source: "devto_webdev"
published: "Tue, 16 Jun 2026 16:54:33 +0000"
description: "Everyone knows <b> , <i> , <a> , and <code> . But HTML has a whole second cast of inline elements that most developers go entire careers without typing once ..."
keywords: "you, ins, abbr, var, mark, one, dfn, not"
generated: "2026-06-16T17:05:59.750966"
---

# The Inline HTML Almost Nobody Uses

## Overview

Everyone knows <b> , <i> , <a> , and <code> . But HTML has a whole second cast of inline elements that most developers go entire careers without typing once — <ins> , <dfn> , <abbr> , <var> , <q> , <mark> . Not because they're broken or deprecated. They're rare because the use cases are genuinely narrow, and when one does come up, the reflex is to reach for a <span class="something"> instead. I bumped into this building out a prose/content section for a UI system — once you start styling text properly, you notice how many real semantic elements you'd been ignoring. So here's the whole forgotten cast, in a single sentence that legitimately uses eleven of them: Here's what that actually is: <p> The experiment revealed <mark> a significant energy spike </mark> in the reactor core. Previous readings of <del> 42.7 terawatts </del> were revised to <ins> 51.3 terawatts </ins> after recalibration. The formula <var> E </var> = <var> mc </var><sup> 2 </sup> governs the conversion, where H <sub> 2 </sub> O serves as the coolant medium. <abbr title= "Void Energy Reactor Interface" > VERI </abbr> logs confirm the anomaly. As Dr. Vasquez noted, <q> the readings exceed all theoretical models </q> ( <cite> Void Research Quarterly </cite> ). This phenomenon, known as <dfn> energy cascade </dfn> , occurs when containment thresholds are breached. The <s> original safety protocols </s> have since been replaced. </p> The cast, and where you'd actually use each Edits and corrections. <ins> and <del> are added and removed content — they pair up for change tracking, and both accept datetime and cite attributes so the edit is machine-readable. <s> is the one people conflate with <del> : it marks content that's no longer accurate or relevant (a stale price, an outdated claim), which is a different statement than "this was deleted." Two elements exist precisely because those mean different things. Notation. <sub> and <sup> are for cases where the position carries meaning — chemical formulas (H₂O), exponents (I²R), ordinals, footnote markers — not for "make it small and raised." <var> is a variable in math or code, which is why P , I , and R above are each wrapped in one. Reference and meaning. <mark> is a relevance highlight — it's literally what search engines use to highlight your query in the results. <abbr title="…"> gives an abbreviation its expansion, surfaced as a tooltip. <dfn> marks the one spot where a term is defined (its introducing instance, not every later mention). <cite> is the title of a work — a book, paper, album — and notably not a person's name, which is the thing nearly everyone gets wrong. And <q> is an inline quotation where the browser inserts the quotation marks for you: correct for the document's language, and correctly nested if you put a quote inside a quote. You never type a " again. Why bother Every one of these throws a bit of meaning into the page that a styled <span> silently discards. Screen readers announce them. <q> localizes its punctuation. <abbr> exposes the long form. <ins> / <del> are a real, parseable changelog. A <span class="highlight"> looks the same and means nothing. The only honest reason to avoid them is that the browser defaults are inconsistent and, frankly, ugly — <mark> is highlighter-yellow, <q> 's marks are whatever, half of them are unstyled. But that's a few lines of CSS, not a law of physics. Give <mark> a brand-tinted background, <ins> a green underline, <abbr> a dotted one, <q> colored quote marks, <dfn> an italic weight — and suddenly an entire sentence of semantic richness reads as clean, deliberate typography. Most of these you'll reach for maybe once a year. But once a year correctly — with the meaning intact and the styling handled — beats a <span> that's lying about what it is.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/dimonb19a/the-inline-html-almost-nobody-uses-205d

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
