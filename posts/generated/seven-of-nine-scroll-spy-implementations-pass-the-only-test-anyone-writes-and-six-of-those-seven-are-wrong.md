---
title: "Seven of Nine Scroll-Spy Implementations Pass the Only Test Anyone Writes, and Six of Those Seven Are Wrong"
slug: "seven-of-nine-scroll-spy-implementations-pass-the-only-test-anyone-writes-and-six-of-those-seven-are-wrong"
author: "Devanshu Biswas"
source: "devto_webdev"
published: "Sat, 29 Aug 2026 20:21:30 +0000"
description: "A scroll-spy lights the table-of-contents entry for the heading you are reading. One integer to settle. The property everyone tests is: exactly one entry is ..."
keywords: "entry, reading, line, scroll, test, lit, never, every"
generated: "2026-08-29T20:45:19.188484"
---

# Seven of Nine Scroll-Spy Implementations Pass the Only Test Anyone Writes, and Six of Those Seven Are Wrong

## Overview

A scroll-spy lights the table-of-contents entry for the heading you are reading. One integer to settle. The property everyone tests is: exactly one entry is lit · it never jumps backwards · it is on screen Across 21,909 whole pixels of scroll over three real documents, seven of nine implementations satisfy that at every single pixel. Six of those seven are wrong. See it: https://dev48.infy.uk/design/day74-scroll-spy.html What the test cannot see A heading that is in the table of contents never lights at all — 8 of 34 entries, each named on the page. The test only asks about the entry that is lit. It never asks whether every entry can be. And the two properties are provably incompatible The textbook implementation uses a reading line: the lit section is whichever contains a line partway down the viewport. That is not buggy. It satisfies the reading line is inside the lit section at 100% of pixels . And that property is provably incompatible with every entry lights on any page whose last headings sit inside the final screen — once you cannot scroll further, the reading line can never reach them. So one of the two must break. The interesting question is which, and by how much: implementation overflow test what is actually broken reading line ✅ 8 of 34 entries never light clamped threshold ✅ breaks the reading-line property by the least it can five others ✅ wrong in ways the test cannot see // the incompatibility, stated plainly // last heading top > scrollHeight - viewportHeight => unreachable by any // reading line at a fixed offset. No amount of tuning the offset fixes it. The lesson If your only assertion is "exactly one is lit and it's on screen", you are testing the property that every plausible implementation satisfies — including the ones that silently drop a quarter of your headings. Assert which entry, and assert that every entry is reachable. 146 verifier asserts, 130 in-page checks, 0 failures.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/dev48v/seven-of-nine-scroll-spy-implementations-pass-the-only-test-anyone-writes-and-six-of-those-seven-558g

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
