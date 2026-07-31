---
title: "Show HN: Gander, an Android file viewer that asks for no permissions at all"
slug: "show-hn-gander-an-android-file-viewer-that-asks-for-no-permissions-at-all"
author: "mokshablr"
source: "hackernews"
published: "Fri, 31 Jul 2026 05:45:13 +0000"
description: "Hi HN, I built an Android file viewer that opens PDF, Word, Excel, PowerPoint, images, video, audio, Markdown and code, and asks for no permissions at all. I..."
keywords: "file, viewer, android, permissions, gander, asks, all, powerpoint"
generated: "2026-07-31T08:56:54.065473"
---

# Show HN: Gander, an Android file viewer that asks for no permissions at all

## Overview

Hi HN, I built an Android file viewer that opens PDF, Word, Excel, PowerPoint, images, video, audio, Markdown and code, and asks for no permissions at all. I have always been uneasy about opening files people send me. On Android you either install a 400 MB office suite and sign in or use a small free viewer that wants storage access and ends up uploading your file to a server to render it. Also the hassle of having to download different apps for different file formats was really annoying. Gander holds no permissions, not even INTERNET so the OS itself guarantees the file cannot leave the phone. PDFs use Pdfium, media uses Media3, and Office formats are rendered by bundled JS libraries in a WebView and so no request goes to any server. It is a viewer only. Complex PowerPoint decks come out approximately right, spreadsheet charts are not drawn, and old binary .doc and .ppt are unsupported. I'll work on it as issues come up :P It is 14 MB, MIT licensed and uploaded on Github releases. Do try it! I would love some feedback especially on files that render badly or need new support. Comments URL: https://news.ycombinator.com/item?id=49119425 Points: 36 # Comments: 15

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://github.com/mokshablr/gander

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
