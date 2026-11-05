---
title: "How we made a small stationery site readable to AI assistants"
slug: "how-we-made-a-small-stationery-site-readable-to-ai-assistants"
author: "Ellis"
source: "devto_webdev"
published: "Thu, 05 Nov 2026 05:54:53 +0000"
description: "AI-assistance disclosure: this post was drafted with an AI assistant and edited by the person who runs the site. I run Stationery Times, an independent stati..."
keywords: "stationery, markdown, page, site, text, txt, data, build"
generated: "2026-11-05T06:01:18.141440"
---

# How we made a small stationery site readable to AI assistants

## Overview

AI-assistance disclosure: this post was drafted with an AI assistant and edited by the person who runs the site. I run Stationery Times, an independent stationery reference with no affiliate links. Stationery Times is a static Astro site of sourced guides to pens, inks, paper, notebooks and planners. We wanted AI assistants to be able to read it and cite it correctly. These are the things we built, and nothing here is a guarantee of citations. Answer first. Every guide opens with a 40 to 60 word direct answer and 4 to 5 takeaways. Headings are phrased as the question a person would ask, and each is answered in a bold first sentence. Plain text twins. Each guide has a Markdown copy at the same address with .md on the end, and the server returns Markdown when a client sends Accept: text/markdown . We also publish /llms.txt and /llms-full.txt . Structured data that matches the page. BlogPosting , Product , FAQPage and BreadcrumbList markup is generated from the same data as the visible text, and a build check fails if the schema and the page disagree. Tell crawlers when something changes. We ping IndexNow on every deploy, keep an RSS feed, and our robots.txt allows the major AI crawlers. Build gates. The build fails on answers that are too long, links to missing anchors, future dates and missing Markdown twins, so the rules hold as the page count grows. What we cannot say yet. We have no hands-on test photos, and some guides still lean on sources we plan to replace. We list what we verify with makers and mark what we could not confirm. If you want to see how it looks in practice, the Japan vs US price index is a good example of a data page with an open CSV.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/stationerytimes/how-we-made-a-small-stationery-site-readable-to-ai-assistants-5025

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
