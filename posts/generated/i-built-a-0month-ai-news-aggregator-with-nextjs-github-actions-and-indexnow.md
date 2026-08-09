---
title: "I built a $0/month AI news aggregator with Next.js, GitHub Actions and IndexNow"
slug: "i-built-a-0month-ai-news-aggregator-with-nextjs-github-actions-and-indexnow"
author: "alanaicode"
source: "devto_webdev"
published: "Sun, 09 Aug 2026 06:48:40 +0000"
description: "Every morning I used to open a dozen tabs — Hacker News, arXiv, a few vendor blogs, two newsletters — just to figure out what actually happened in AI the day..."
keywords: "git, you, indexnow, vercel, day, json, actions, export"
generated: "2026-08-09T07:03:35.998025"
---

# I built a $0/month AI news aggregator with Next.js, GitHub Actions and IndexNow

## Overview

Every morning I used to open a dozen tabs — Hacker News, arXiv, a few vendor blogs, two newsletters — just to figure out what actually happened in AI the day before. It took 30 minutes and I still missed things. So I built a pipeline that does it for me, and it costs $0/month . Here is the whole architecture. The stack Layer Choice Why Collection GitHub Actions (cron) Free minutes on public repos, no server to babysit Processing Plain Python (stdlib only) Zero dependency drift, cold start is instant Storage JSON committed to the repo Git is the database and the changelog Rendering Next.js static export Pre-rendered HTML, perfect Lighthouse scores Hosting Vercel free tier Push to deploy, global CDN included Indexing IndexNow New URLs hit Bing/Yandex in seconds, not days The result is live at AI Nexus Daily if you want to see the output before reading the how. 1. Collection runs in CI, not on a server The single biggest cost saving is refusing to run a server. A scheduled workflow is enough: name : build on : schedule : - cron : ' 0 10 * * *' push : branches : [ master ] jobs : build : runs-on : ubuntu-latest steps : - uses : actions/checkout@v4 - run : python generate.py - name : Commit results run : | git config user.name "bot" git config user.email "bot@users.noreply.github.com" git add -A git diff --staged --quiet || git commit -m "chore: daily rebuild" git push Public repositories get unlimited Actions minutes. A daily job that runs for 40 seconds will never cost anything. 2. Commit the data, don't host a database generate.py writes data/items.json and commits it. That gives you three things for free: Versioning — git log data/items.json is a full audit trail of every change. Rollback — a bad scrape is one git revert away. Deploy trigger — the commit itself makes Vercel rebuild. No webhook, no token. The moment you reach for Postgres for a few thousand rows of read-mostly JSON, you have signed up for a monthly bill and a backup strategy you don't need. 3. Static export, not SSR Feed content changes once a day. Server-side rendering it on every request means paying (in latency and in function invocations) for work that is identical 40,000 times in a row. // next.config.js module . exports = { output : ' export ' , trailingSlash : true , } Static export also means the site keeps serving even if the build pipeline breaks — the last good HTML is still on the CDN. 4. The part most people skip: telling search engines Getting crawled is the actual bottleneck for a new content site. Sitemaps are passive — you publish one and hope. IndexNow is active: you ping the endpoint and Bing, Yandex and Seznam come fetch the URL, usually within minutes. Two requirements that cost me an afternoon: The key file must be reachable at the domain root. On Next.js that means public/<key>.txt , not the repo root. Putting it in the repo root gives you a confident 404. The key file content must be exactly the key , no trailing newline drama, no HTML wrapper. import json , urllib . request payload = { " host " : " ainexusdaily.vercel.app " , " key " : " YOUR_KEY_HERE " , " keyLocation " : " https://ainexusdaily.vercel.app/YOUR_KEY_HERE.txt " , " urlList " : [ " https://ainexusdaily.vercel.app/ " ], } req = urllib . request . Request ( " https://api.indexnow.org/indexnow " , data = json . dumps ( payload ). encode (), headers = { " Content-Type " : " application/json; charset=utf-8 " }, ) print ( urllib . request . urlopen ( req ). status ) # 200 or 202 Google does not participate in IndexNow, so keep the sitemap for them. But getting indexed on Bing the same day still beats waiting a week for everyone. What I would do differently Start with the static export. I began with SSR out of habit and spent a day removing it. Commit the data from day one. My first version regenerated everything on each run, so I had no way to see what changed — which turned out to be the interesting part. Add IndexNow before writing any content. Indexing latency compounds; a page published on day 1 and indexed on day 8 lost a week of traffic it will never get back. Cost breakdown Item Monthly GitHub Actions (public repo) $0 Vercel Hobby $0 Domain ( .vercel.app subdomain) $0 Database none needed Total $0 The whole thing has been running unattended for weeks. If you want to see what it produces daily, it is at ainexusdaily.vercel.app . Happy to answer questions about any layer of this in the comments — especially the IndexNow part, since the docs are thin and the failure mode is silent.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/alanaicode/i-built-a-0month-ai-news-aggregator-with-nextjs-github-actions-and-indexnow-4akj

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
