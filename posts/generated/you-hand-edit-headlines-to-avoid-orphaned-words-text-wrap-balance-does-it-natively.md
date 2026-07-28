---
title: "You hand-edit headlines to avoid orphaned words. `text-wrap: balance` does it natively."
slug: "you-hand-edit-headlines-to-avoid-orphaned-words-text-wrap-balance-does-it-natively"
author: "Parsa Jiravand"
source: "devto_webdev"
published: "Tue, 28 Jul 2026 08:41:41 +0000"
description: "Here is a small but persistent annoyance in frontend work: <h1> The Practical Guide to Building Resilient Web </h1> The browser broke the headline at "Web" b..."
keywords: "text, wrap, balance, width, browser, pretty, line, every"
generated: "2026-07-28T08:43:31.570619"
---

# You hand-edit headlines to avoid orphaned words. `text-wrap: balance` does it natively.

## Overview

Here is a small but persistent annoyance in frontend work: <h1> The Practical Guide to Building Resilient Web </h1> The browser broke the headline at "Web" because it ran out of space. Now you have one word sitting alone on the second line. You fix it by shortening a word, tweaking max-width , or inserting a <br> that will be wrong at a different viewport width anyway. This is not a rare edge case. It happens every time a heading is near the container edge, and every fix that works at one width breaks at another. text-wrap: balance is the native solution. What text-wrap: balance does text-wrap: balance tells the browser to distribute the text as evenly as possible across all lines, rather than filling each line greedily until it overflows. The browser picks the break points; you don't guess. h1 , h2 , h3 { text-wrap : balance ; } Before, with the default greedy wrapping: The Practical Guide to Building Resilient Web After, with text-wrap: balance : The Practical Guide to Building Resilient Web Both lines are closer to equal in length. The orphan disappears. No <br> , no max-width in ch units, no viewport-specific overrides. The property is limited to short content — the browser caps the lookahead at around six lines. That is intentional: the algorithm is quadratic, and running it on a 500-word block would be expensive. Headlines and pull quotes are exactly the right target. 🎮 Try it yourself ▶️ Open the interactive playground → Runs right in your browser — poke at it and watch the concept react live. text-wrap: pretty for body text Long-form paragraphs have their own orphan problem: a single word stranded at the start of the last line. text-wrap: balance is too aggressive for running text — balancing a 10-line paragraph would shift nearly every line. text-wrap: pretty is the calibrated version. p , li , blockquote { text-wrap : pretty ; } pretty uses a lookahead only on the last few lines of a block, pulling one word back if it would otherwise sit alone. The result looks identical to balance for the last line, but the rest of the paragraph is untouched. /* Recommended defaults */ h1 , h2 , h3 , h4 , h5 , h6 { text-wrap : balance ; } p , li , figcaption , blockquote { text-wrap : pretty ; } This pair covers both problems with two rules and no JavaScript. Comparison with the old workarounds <br> tags. Work at one width. Wrong at every other width. Require you to re-edit content when the container changes. &shy; soft hyphens. Depend on hyphenation, which is language-sensitive and not always what you want for brand names or technical terms. max-width tweaks. Force the heading into a narrower box to avoid the bad break. Move the break to a different width. Still wrong somewhere. JavaScript rebalancing (e.g. react-text-balancer ). Measures the element after render and inserts zero-width spaces or spans to approximate balance. Requires a ResizeObserver, adds DOM complexity, and causes a repaint. text-wrap: balance does none of this. The browser solves the line-breaking problem during layout, before anything is painted. There is no DOM surgery, no observer, no flash of unbalanced content. A real-world example A marketing page card with a headline and a description: <article class= "card" > <h2> Automate Your Deployment Pipeline Without the Overhead </h2> <p> Learn how to wire up a zero-downtime deploy in an afternoon using tools your team already has installed. </p> </article> .card h2 { text-wrap : balance ; font-size : clamp ( 1.25rem , 2.5vw , 1.75rem ); } .card p { text-wrap : pretty ; } The h2 distributes across lines evenly regardless of the card's width — useful in a grid where card widths vary by column count. The p avoids a trailing orphan without disrupting the rhythm of the rest of the paragraph. Both properties do their jobs silently while the layout shifts. Browser support text-wrap: balance is Baseline 2024 : Chrome 114 (June 2023), Firefox 121 (December 2023), Safari 17.4 (March 2024). text-wrap: pretty shipped slightly later: Chrome 117, Firefox 128, Safari 17.4. Both degrade gracefully — unsupported browsers use the default greedy wrapping. The text is still readable; it just may have an orphan. That is the correct fallback behavior for a visual refinement. There is no polyfill needed and nothing to install. 🧠 Test yourself Think it clicked? Take the 7-question quiz → Instant feedback, a hint on every question, and an explanation for each answer — right or wrong. The takeaway Search your stylesheets for <br> tags inside headings, or for max-width values expressed in ch units that exist specifically to force a nicer headline break. Each one is a layout constraint solving a problem CSS can now handle natively. Add text-wrap: balance to your heading selectors and text-wrap: pretty to your body text selectors. The browser finds the right breaks at every viewport width, for every heading length, without any JavaScript or content edits on your part. Thanks for reading! Let's stay connected: ⭐ GitHub — follow me and star the projects: github.com/parsajiravand 📸 Instagram — frontend best practices, daily: @bestpractice___ 💼 LinkedIn — linkedin.com/in/parsa-jiravand ✉️ Email (work & contract inquiries): bestpractice2026@gmail.com

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/parsajiravand/you-hand-edit-headlines-to-avoid-orphaned-words-text-wrap-balance-does-it-natively-286f

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
