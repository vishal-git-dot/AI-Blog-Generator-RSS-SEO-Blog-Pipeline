---
title: "I Built an AI Publishing Stack for $31/Month — Real Numbers After 15 Posts"
slug: "i-built-an-ai-publishing-stack-for-31month-real-numbers-after-15-posts"
author: "Luna"
source: "devto_webdev"
published: "Fri, 10 Jul 2026 14:31:18 +0000"
description: "I've been building a solo content operation in public for the past month. The goal: run a real publishing workflow — blog posts, analytics, affiliate trackin..."
keywords: "month, real, api, stack, posts, analytics, claude, cloudflare"
generated: "2026-07-10T14:40:05.899479"
---

# I Built an AI Publishing Stack for $31/Month — Real Numbers After 15 Posts

## Overview

I've been building a solo content operation in public for the past month. The goal: run a real publishing workflow — blog posts, analytics, affiliate tracking — entirely on AI automation, and document whether it can pay for itself. The full stack costs $31/month Claude API (~$20) : content drafting, topic generation, quality checks Hetzner CX21 VPS (~$6) : self-hosted n8n for workflow automation .dev domain (~$1) : annualized GitHub Pro (~$4) : private repos + Actions minutes What's actually running on this Auto-publishes 1 post/day (EN + KO) from a topic queue Collects daily view counts via Cloudflare KV Tracks affiliate link clicks with a /go/ redirect layer Sends Telegram alerts when something breaks 15 posts live so far. Every post has real numbers — actual traffic, actual revenue, actual mistakes. No "lessons learned" without the receipts. The parts people ask about most n8n self-hosted : runs on the Hetzner VPS for free. Handles all scheduling, webhook routing, and API calls. Add a 2GB swap file early — n8n can spike on heavy loads. Prompt caching : this one change cut Claude API costs by ~60%. Caching the system prompt and batching overnight runs brought spend from ~$40 to ~$20/month. Cloudflare KV for analytics : Workers increment a view counter on each page load, a nightly cron rolls up daily totals. Free tier covers everything under ~100k reads/day — no separate analytics database needed. Current status The stack works. Whether it earns back the $31 is the question I'm documenting in real time. Full breakdown with every line item: builderlog.net Happy to go deep on n8n setup, Claude API cost optimization, or the Cloudflare Workers + KV pattern.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/moonshot_1341/i-built-an-ai-publishing-stack-for-31month-real-numbers-after-15-posts-4dbd

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
