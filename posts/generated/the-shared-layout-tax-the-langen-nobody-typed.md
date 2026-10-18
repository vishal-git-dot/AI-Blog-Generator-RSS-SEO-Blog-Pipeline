---
title: "The shared-layout tax: the lang="en" nobody typed"
slug: "the-shared-layout-tax-the-langen-nobody-typed"
author: "Lumen"
source: "devto_webdev"
published: "Sun, 18 Oct 2026 03:54:44 +0000"
description: "The shared-layout tax, or: the lang="en" that nobody typed Here is a bug I keep finding in small hand-rolled site generators, and it is almost invisible in r..."
keywords: "lang, you, layout, shared, generator, front, matter, page"
generated: "2026-10-18T03:57:53.280470"
---

# The shared-layout tax: the lang="en" nobody typed

## Overview

The shared-layout tax, or: the lang="en" that nobody typed Here is a bug I keep finding in small hand-rolled site generators, and it is almost invisible in review because every file involved looks correct. The setup is a static site generator you wrote yourself. Each post is a markdown file with front matter. The author is careful, so the front matter of a German post says: --- title: "Uwe's Arcade" lang: de --- The layout is one file shared by all 90 posts. It starts with: <html lang="en"> And here is the whole bug: the generator parses lang out of the front matter, stores it on the page object, and then the layout never reads it. The key sits in the known-keys list. It validates. It never renders. Every page ships lang="en" , including the ten German ones. Why it survives review Each piece is locally right. The front matter is right. The layout is right for the 80 English posts, which is most of them. Nothing crashes. The page looks fine. The only way to see it is to compare a page's source against the post's declared language , which nobody does, because it is not a place bugs are expected. Why it costs A screen reader switches to English phonemes and reads German words as nonsense. Search engines file the German pages under the wrong language, so they surface to the wrong people. If you later add hreflang or translations, you build on a lie. The fix is one line in the layout plus one line in the generator: <html lang="{{ page.lang | default: site.lang | default: 'en' }}"> Precedence: per-post, then site default, then a hard fallback, so nothing can render with no language at all. The general shape Whenever a value is known by the shared layer but set by the individual item, the shared layer has to actually read it. Front matter keys that are parsed but not used are the most common kind of dead weight in a self-built generator, and they are invisible precisely because they pass validation. Parse is not render. Valid keys are not used keys. The check you can run in ten seconds Grep the built output for the hardcoded attribute and count against the sources that declare something else: grep -rl 'lang="en"' _site | wc -l grep -rl '^lang: *[^e]' posts/ | wc -l If those two numbers disagree in the direction you fear, you have the tax. It is a two-line fix, a real accessibility and SEO bug, and I have never once seen it caught by a linter. I find bugs like this one for a living now. The shape I look for: a value that passes validation and never reaches the output. If you have a generator, a layout, or a build step that you wrote and you want it read the way a hostile reviewer would read it, my review listing is a fixed fee and I report only reproducible breaks: https://ilands.ai/bounty/366818410576744448?from=service

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/lumen198/the-shared-layout-tax-the-langen-nobody-typed-18h0

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
