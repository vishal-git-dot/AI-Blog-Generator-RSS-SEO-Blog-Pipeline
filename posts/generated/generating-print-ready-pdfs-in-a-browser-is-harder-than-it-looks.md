---
title: "Generating Print-Ready PDFs in a Browser Is Harder Than It Looks"
slug: "generating-print-ready-pdfs-in-a-browser-is-harder-than-it-looks"
author: "Hannah Whitfield"
source: "devto_webdev"
published: "Fri, 24 Jul 2026 19:21:41 +0000"
description: ""Export to PDF" sounds like a solved problem until the output has to go to an actual printer and come back as a physical book. Screen PDFs and print PDFs are..."
keywords: "not, print, browser, screen, you, than, has, cmyk"
generated: "2026-07-24T19:37:11.866786"
---

# Generating Print-Ready PDFs in a Browser Is Harder Than It Looks

## Overview

"Export to PDF" sounds like a solved problem until the output has to go to an actual printer and come back as a physical book. Screen PDFs and print PDFs are different artefacts with different requirements. RGB is not CMYK Browsers work in RGB. Printers work in CMYK. The conversion is lossy and not symmetric — saturated RGB colours, particularly bright blues and greens, have no CMYK equivalent and come back visibly duller. Nothing in the browser warns you. The proof looks right on screen and wrong on paper, which is an expensive way to discover the problem. Practical mitigation: design within a CMYK-safe palette from the start rather than converting at the end. Muted colours survive the round trip; neon does not. Bleed and trim Print requires content to extend past the trim line — typically 3mm on each edge — so that cutting tolerance does not leave white slivers. A "210×297mm" PDF is wrong for print; you need 216×303mm with trim marks. CSS gets you part of the way: @page { size : 216mm 303mm ; /* A4 + 3mm bleed each side */ margin : 0 ; } But @page support is uneven and bleed marks generally are not something the browser will draw for you. Image resolution is the most common rejection Screen images are typically 72-96 DPI. Print needs 300 DPI. An image looking crisp in the browser is roughly a quarter of the resolution a printer wants, and print services reject or flag these. Worth validating at upload — compute effective DPI from the intrinsic pixel dimensions against the placed physical size and warn immediately, rather than at export when the user has already done the work. Pagination is the genuinely hard part Reflowable HTML has no concept of a page. Getting a recipe to not break across a page boundary means measuring rendered content and making layout decisions, which the browser will not do for you. break-inside: avoid helps for simple blocks and is not sufficient for real layout control. What actually worked: render content off-screen, measure real heights, then assign blocks to pages in code — essentially reimplementing pagination rather than asking CSS to do it. Fonts must be embedded An unembedded font substitutes at the print shop and your careful typography becomes Helvetica. Whatever generates the PDF must embed subsets — and the font licence has to permit embedding, which not all do. I deal with all of this at Cook Press — recipes in, Etsy-ready hardcover out. Caveat If the output is only ever going to be read on screen, ignore most of this. These constraints exist because a physical printing press is on the other end, and they are pure overhead otherwise.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/hannahjwhitfield/generating-print-ready-pdfs-in-a-browser-is-harder-than-it-looks-25g3

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
