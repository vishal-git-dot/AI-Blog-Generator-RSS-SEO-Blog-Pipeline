---
title: "I have 591 pages. Google indexed one. Here's how I'm debugging it."
slug: "i-have-591-pages-google-indexed-one-heres-how-im-debugging-it"
author: "Bcrypto"
source: "devto_ai"
published: "Tue, 11 Aug 2026 19:00:50 +0000"
description: "I run a directory site with 2,499 real vendor listings across Beirut, Dubai, Riyadh, Doha, Cairo and Casablanca. It has 591 programmatic landing pages and 1,..."
keywords: "you, pages, page, one, what, not, indexed, google"
generated: "2026-08-11T19:08:47.095046"
---

# I have 591 pages. Google indexed one. Here's how I'm debugging it.

## Overview

I run a directory site with 2,499 real vendor listings across Beirut, Dubai, Riyadh, Doha, Cairo and Casablanca. It has 591 programmatic landing pages and 1,182 URLs in its sitemap. I checked what Google had actually indexed. The homepage. That was it. Not 591. Not 200. One. This post is what I checked, what I ruled out, and the one diagnostic that actually decides what to do about it — because I got that last part wrong at first, and I suspect a lot of people do. First instinct: something's broken on the site That's where I went, and it's usually where everyone goes. So I worked the checklist. robots.txt — correct. Allows everything, references the sitemap. Sitemap — valid XML, 1,182 URLs, auto-generated, submitted. Hub page — present. Something links into the page set; they aren't orphans. Internal linking — 62 cross-links per page. Not a dead end. Structured data — JSON-LD on every page. Server-rendered content — real listings in the initial HTML. Not a JS shell. Here's the fastest way to check that last one, and it's the one people skip: curl -s https://yoursite.com/some-page | wc -w If that number is small, that's roughly what a crawler sees. Your framework hydrating beautifully in a browser is irrelevant to a bot that doesn't run JavaScript. I've measured client sites with 10 words in the initial HTML that looked perfect to a human. All six checks passed. Which meant the problem wasn't on the page. The wrong conclusion I nearly published My first explanation was: the site has no inbound links and no brand mentions anywhere, so Google has no reason to crawl it deeply. Authority problem. Go get links. That's a coherent story. It might even be right. But I nearly wrote it up as fact, and it turns out there's a specific piece of data that decides it — and until you look at that data, you're guessing. The diagnostic that actually matters Google Search Console → Indexing → Pages → "Why pages aren't indexed". Two statuses look similar and mean opposite things: Discovered – currently not indexed Google knows the URL exists but hasn't spent crawl budget on it. This is the authority/crawl-scheduling case. Links and internal-linking improvements genuinely help here. Crawled – currently not indexed Google fetched the page, looked at it, and decided not to index it. This is a quality judgement . For programmatic pages — city × category templates where only a couple of fields change — this usually means it read them as thin or near-duplicate. If it's the second one, backlinks will not fix it. You can build links for six months and stay at one indexed page, because the pages themselves are what got rejected. The fix is consolidation: fewer, substantially different pages with real unique content, rather than more thin ones. Same symptom. Opposite remedies. The export is free and takes two minutes, and I was about to skip it in favour of a narrative that felt right. The trap in programmatic SEO Programmatic SEO makes the satisfying work and the useful work feel identical. Generating 600 pages is a fun afternoon. It produces a number that goes up. It looks like progress. And if your pages are being rejected rather than not reached , generating another 600 moves you from one indexed page to one indexed page. I could have shipped a second batch and felt productive the whole time. What I'd check on any site, in order site:yourdomain.com in Google. Compare the count to how many pages you think you have. The gap is the actual story, and most people never look. View source with JS disabled. If there's a loading spinner where your content should be, that's what you've published. GSC → Indexing → Pages. Get the real status before choosing a fix. Check whether you're blocking AI crawlers. Plenty of robots.txt files disallow GPTBot , ClaudeBot or PerplexityBot inherited from a template, and then people wonder why assistants never cite them: curl -s https://yoursite.com/robots.txt | grep -iE "gptbot|claudebot|perplexity" Grep your bundles for keys. Unrelated to indexing, but while you're in there — anything starting sk_live , AKIA , or a service-role JWT that reached the browser is public regardless of what your backend does. Where I've got to The GSC export is the next thing I do, and it decides whether the next month is spent earning citations or consolidating pages. I'm writing this before I have that answer deliberately, because the interesting part isn't the resolution — it's that the symptom looked obvious and pointed at two incompatible fixes. If you've got a programmatic site sitting at a fraction of its expected index coverage, check which status you have before you spend a month on the wrong one. I automated the on-page half of these checks into a free scanner while debugging this — preflightscan.vercel.app , no signup. It won't tell you your GSC status; nothing can except GSC.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/bcrypto/i-have-591-pages-google-indexed-one-heres-how-im-debugging-it-5cel

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
