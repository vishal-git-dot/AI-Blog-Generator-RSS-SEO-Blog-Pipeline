---
title: "Your CSS Grid cards look misaligned. `subgrid` is the fix you didn't know existed."
slug: "your-css-grid-cards-look-misaligned-subgrid-is-the-fix-you-didnt-know-existed"
author: "Parsa Jiravand"
source: "devto_webdev"
published: "Thu, 16 Jul 2026 08:21:26 +0000"
description: "Here is a layout I have built more times than I can count. You have a row of cards in a CSS Grid. Each card has a header, a body with variable-length content..."
keywords: "grid, card, subgrid, you, row, footer, rows, cards"
generated: "2026-07-16T08:22:50.506086"
---

# Your CSS Grid cards look misaligned. `subgrid` is the fix you didn't know existed.

## Overview

Here is a layout I have built more times than I can count. You have a row of cards in a CSS Grid. Each card has a header, a body with variable-length content, and a footer with a button. The card with three lines of copy has its button sitting higher than the card with one line. You want all the footer buttons to sit on the same horizontal line. So you try the usual fixes. You add flex: 1 to the body so it pushes the footer down. It pushes the footer to the bottom of its own card , but each card is a different height, so the buttons still don't align. You try a fixed height on the body. It works until someone adds a sentence of copy and the text overflows. You write four lines of JavaScript — querySelectorAll , getBoundingClientRect , find the max, set minHeight on each — and add a ResizeObserver to re-run it when the viewport changes. That last approach works. It is also the wrong tool for a layout problem. The real problem is structural: CSS Grid controls only direct children . Your card elements can participate in the outer grid's columns. But the content sections inside the cards — the header, body, footer — can't. Each card is its own formatting context, blind to the parent grid's row tracks. subgrid changes that. What subgrid actually does When you apply grid-template-rows: subgrid to a grid item that spans multiple rows, the item stops defining its own row tracks. Instead, it inherits the parent grid's tracks for the span it occupies. Its children slot into the parent's rows directly. .cards { display : grid ; grid-template-columns : repeat ( 3 , 1 fr ); grid-template-rows : auto 1 fr auto ; gap : 1.5rem ; } .card { display : grid ; grid-row : span 3 ; /* occupy 3 row tracks in the parent */ grid-template-rows : subgrid ; /* inherit those 3 tracks */ } With this in place, every .card-header sits in the first shared row track — sized to the tallest header across all cards. Every .card-body occupies the second track, a 1fr that expands consistently. Every .card-footer sits in the third track — sized to the tallest footer. No JavaScript. No fixed heights. The grid algorithm does the measurement. The card alignment problem, solved Here's the before and after: Before — each card sizes independently: .cards { display : grid ; grid-template-columns : repeat ( 3 , 1 fr ); gap : 1.5rem ; } .card { display : flex ; flex-direction : column ; } .card-body { flex : 1 ; /* pushes footer to the bottom of *this* card only */ } After — cards share the parent's row tracks: .cards { display : grid ; grid-template-columns : repeat ( 3 , 1 fr ); grid-template-rows : auto 1 fr auto ; gap : 1.5rem ; } .card { display : grid ; grid-row : span 3 ; grid-template-rows : subgrid ; } /* .card-header, .card-body, .card-footer need no special sizing rules */ The content sections slot into the shared tracks automatically. Every header aligns. Every footer aligns. The 1fr body row stretches uniformly across the entire row of cards. Subgrid on both axes You can opt into the parent's columns, rows, or both: .card { display : grid ; grid-column : span 2 ; grid-row : span 3 ; grid-template-columns : subgrid ; /* inherit parent columns */ grid-template-rows : subgrid ; /* inherit parent rows */ } A card spanning two columns can now place its own children across both of those parent column tracks. This is useful in dense dashboard layouts — a wide stat card with an icon and a value that need to align with adjacent narrow cards' content. Where subgrid actually belongs in your codebase Subgrid solves a specific problem: nested content that should align with the outer grid's tracks . Common candidates: Card grids — headers, body copy, and footers that must share horizontal baselines Definition lists — term and value pairs in a two-column layout where nested fieldsets or groups must align with the outer columns Form layouts — labels and inputs inside grouped sections that need to respect the outer grid's column widths Navigation lists — icon, label, and badge in each row should share columns even when the rows are separate components It does not replace flex-direction: column with flex: 1 in every card. That pattern is still appropriate when you only care that the footer reaches the bottom of its own card. Reach for subgrid the moment you hear yourself say "the buttons should all be on the same line." Browser support subgrid is Baseline 2023 : Chrome 117, Firefox 71 (Firefox shipped it years earlier, in 2019, which proved demand existed), Safari 16. Every browser you are targeting for a new project supports it. No polyfill, no fallback grid, no build-time transform. The takeaway CSS Grid gave you a powerful coordinate system for your outer layout. subgrid extends that coordinate system into nested content that needs to participate in the same tracks. The alignment problem that has been driving you toward JavaScript — measuring heights, iterating over siblings, wiring up resize listeners — is a layout problem. The layout language has the answer now. Use it. Thanks for reading! Let's stay connected: ⭐ GitHub — follow me and star the projects: github.com/parsajiravand 📸 Instagram — frontend best practices, daily: @bestpractice___ 💼 LinkedIn — linkedin.com/in/parsa-jiravand ✉️ Email (work & contract inquiries): bestpractice2026@gmail.com

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/parsajiravand/your-css-grid-cards-look-misaligned-subgrid-is-the-fix-you-didnt-know-existed-k94

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
