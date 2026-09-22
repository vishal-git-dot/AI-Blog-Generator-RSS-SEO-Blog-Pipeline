---
title: "How we built a free global cleaning jobs marketplace, and opened 958 live cleaning contracts to anyone"
slug: "how-we-built-a-free-global-cleaning-jobs-marketplace-and-opened-958-live-cleaning-contracts-to-anyone"
author: "Mark Natthan"
source: "devto_webdev"
published: "Tue, 22 Sep 2026 21:00:40 +0000"
description: "Most people never think about who cleans the offices, schools, hospitals and shops they walk through every day. We did, and we found an industry worth hundre..."
keywords: "cleaning, free, contracts, people, they, what, public, built"
generated: "2026-09-22T21:06:11.061203"
---

# How we built a free global cleaning jobs marketplace, and opened 958 live cleaning contracts to anyone

## Overview

Most people never think about who cleans the offices, schools, hospitals and shops they walk through every day. We did, and we found an industry worth hundreds of billions that still runs on word of mouth, paper and middlemen taking a cut from the people doing the actual work. So we built CQD New Gen , a free global marketplace for the cleaning industry. Cleaners find verified work near them. Businesses hire trusted cleaners fast. Nobody pays a subscription, a commission or a posting fee, so cleaners keep 100 percent of what they earn. This is a short write up of the interesting technical parts, and of one thing we opened up for free that we think is genuinely useful. The stack Vite and React with server side rendering for a fast, crawlable single page app Supabase over PostgREST for data, so most of the app is just typed REST calls Vercel for hosting, with a manual production promote step from the build repo A programmatic SEO layer that generates a page per city and per market, so the site currently serves close to 6,000 indexable pages The SSR plus programmatic pages combination is what lets a brand new marketplace get discovered organically, without paying for ads. Every city and every market becomes its own landing page with real local content. The part we are proud of: opening the data Public cleaning contracts are published by governments and public bodies all over the world, but they are scattered across dozens of portals, in different formats, in different languages. A small cleaning business has no realistic way to see them all. So we aggregate them. Right now the platform tracks 958 live cleaning contracts across 55 countries , plus 400 live public tenders across 21 countries , de-duplicated and ranked into one clean feed. Anyone can browse it free at the contracts digest . We also built a renewal radar that infers when existing contracts are coming up for re-tender, from the end dates in official award notices, so a cleaning business can prepare a bid before a contract goes back out to the market. What we learned SSR is not optional for organic marketplaces. If your inventory pages are not server rendered, you are invisible to search and to AI answer engines. That is your whole free distribution channel gone. Free instant indexing is underused. A single IndexNow POST pushes thousands of URLs straight to Bing, Yandex, Naver, Seznam and Yep at zero cost. Google ignores it, but the rest matter more than people think, especially for AI answer surfaces. Zero commission is a distribution strategy, not just a pricing choice. When the people who use your product keep all their money, they tell other people. That is the cheapest growth there is. If you run or work in a cleaning business anywhere in the world, take a look and tell us what is missing: www.cqdnewgen.ai . We are building in public and we read everything.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/mark_natthan_87bbeb4db57d/how-we-built-a-free-global-cleaning-jobs-marketplace-and-opened-958-live-cleaning-contracts-to-41l1

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
