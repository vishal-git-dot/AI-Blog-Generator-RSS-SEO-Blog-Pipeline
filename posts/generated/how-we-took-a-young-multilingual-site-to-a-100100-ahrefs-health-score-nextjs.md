---
title: "How we took a young multilingual site to a 100/100 Ahrefs health score (Next.js)"
slug: "how-we-took-a-young-multilingual-site-to-a-100100-ahrefs-health-score-nextjs"
author: "mihai"
source: "devto_webdev"
published: "Sat, 18 Jul 2026 18:59:34 +0000"
description: "Last week our agency site hit a 100/100 "Health Score" with 0 errors on Ahrefs' Site Audit — on a domain that's only a couple of months old. Here's exactly w..."
keywords: "every, page, pages, site, next, ahrefs, static, content"
generated: "2026-07-18T19:11:40.226334"
---

# How we took a young multilingual site to a 100/100 Ahrefs health score (Next.js)

## Overview

Last week our agency site hit a 100/100 "Health Score" with 0 errors on Ahrefs' Site Audit — on a domain that's only a couple of months old. Here's exactly what we did, in case it helps someone else building on Next.js. The stack Next.js (App Router), fully static where possible, deployed on Vercel. ~1,000 articles across 6 languages, generated at build time. No CMS bloat — content lives in typed data files, so every page is fast and crawlable. What actually moved the needle 1. Real structured data, not decoration. One interlinked @graph (Organization + WebSite) defined once, referenced by every page. Each page adds BreadcrumbList , and content pages add BlogPosting / FAQPage . Clean, valid, no orphan nodes. 2. hreflang done right. 6 locales, each page enumerates its live siblings + x-default . We generate every locale's static params so internal links never 404 — and gate not-yet-live locales with robots: { index: false, follow: true } instead of breaking the graph. 3. Core Web Vitals as a hard rule. The LCP heading is static — we skip hero animations because they cost ~12–15 mobile PageSpeed points. Images are all sized + have alt text (Ahrefs flagged 0 missing). 4. Internal linking as a system. Every article links to a few topical siblings + the money pages, with keyword anchors. Result: 0 orphan pages, PageRank flows to the pages that matter. 5. Multi-engine indexing with IndexNow. A daily GitHub Action diffs the live sitemap vs a state file and pings only new URLs to Bing / Yahoo / DuckDuckGo / Yandex / Seznam. New pages get indexed in hours, not weeks. (Google doesn't use IndexNow — that's still sitemap + crawl.) 6. Freshness signals. dateModified + sitemap <lastmod> update whenever content actually changes, and we surface an "updated" date on-page. The honest part Technical SEO gets you eligible to rank — it doesn't rank you. Our Domain Rating is still 0; authority (real backlinks) is the slow part. But a clean, fast, well-structured site means every bit of authority we earn converts faster. I run MPO Web Studio — we build fast, custom-coded sites. Happy to answer any Next.js/SEO questions in the comments.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/mpowebstudio/how-we-took-a-young-multilingual-site-to-a-100100-ahrefs-health-score-nextjs-34lj

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
