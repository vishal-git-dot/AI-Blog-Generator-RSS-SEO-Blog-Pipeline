---
title: "# I got tired of hunting for free ML/robotics papers across 5 sites, so I built an aggregator"
slug: "i-got-tired-of-hunting-for-free-mlrobotics-papers-across-5-sites-so-i-built-an-aggregator"
author: "Ansh Kansagra"
source: "devto_python"
published: "Tue, 28 Jul 2026 19:12:38 +0000"
description: "I'm a final-year Electronics & Communication Engineering student about to start a robotics-focused master's. For the last two years, "finding a paper" has me..."
keywords: "free, pdf, api, robotics, then, ieee, mdpi, open"
generated: "2026-07-28T19:39:37.247439"
---

# # I got tired of hunting for free ML/robotics papers across 5 sites, so I built an aggregator

## Overview

I'm a final-year Electronics & Communication Engineering student about to start a robotics-focused master's. For the last two years, "finding a paper" has meant checking arXiv, then IEEE, then MDPI, then Google Scholar, then still not being sure if the PDF link I found was actually free or just a paywall in disguise. So I built Cortexa — a free, open-access-only search engine for robotics, ML, deep learning, computer vision, VLSI, and adjacent research. No login wall to search, no scraped paywalled content pretending to be free. Stack: Next.js 16 (App Router), TypeScript, Tailwind CSS v4, Supabase (Postgres + Auth + Storage), deployed on Vercel with daily cron ingestion. Where the papers come from: arXiv's Atom API, CrossRef (MDPI, individually open-access IEEE Transactions articles, and other OA publishers), and OpenAlex — about 22,800 papers indexed as I write this, growing daily. The bug that actually taught me the most: early on, some "View free PDF" links were opening raw XML instead of a PDF. Turned out CrossRef and OpenAlex sometimes list a publisher's metadata API endpoint as the "PDF" link, not the paper itself. I ended up writing a small validator that rejects anything shaped like an API call ( api.* hosts, /content/article/ paths, httpAccept query params) before it's ever shown as a download link — a good reminder that "the API said it's a PDF" and "it's actually a PDF" are different claims. Licensing was the part I didn't expect to spend so much time on. "Open access" isn't one thing — MDPI is 100% OA by policy, but IEEE and most other publishers only have it OA when the author specifically paid for it. So every non-MDPI paper only gets ingested if its own CrossRef record carries a verified Creative Commons license, regardless of which journal it's technically in. That's how the index includes individually-open-access articles from otherwise-paywalled IEEE Transactions journals without misrepresenting the paywalled majority of that same journal as free. It's live at automata-index.vercel.app (yes, the rename to Cortexa is still in progress — long story). Free, no ads yet, built solo. If you're in robotics/ML/AI research and want to kick the tires or tell me what's missing, I'd genuinely like to hear it.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/ansh_kansagra/-i-got-tired-of-hunting-for-free-mlrobotics-papers-across-5-sites-so-i-built-an-aggregator-1104

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
