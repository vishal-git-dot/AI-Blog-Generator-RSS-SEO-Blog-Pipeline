---
title: "I Built a 2.8KB Cookieless Analytics Tool After Google Analytics Hid 35% of My Traffic"
slug: "i-built-a-28kb-cookieless-analytics-tool-after-google-analytics-hid-35-of-my-traffic"
author: "Azaan Ali Raza"
source: "devto_ai"
published: "Tue, 23 Jun 2026 19:57:49 +0000"
description: "Last month my Next.js SaaS showed 1,200 visitors in Google Analytics. AmazeMatrix showed 1,847. That's 35% of my traffic GA simply missed because of ad block..."
keywords: "you, analytics, blockers, privacy, but, want, how, built"
generated: "2026-06-23T20:12:47.955851"
---

# I Built a 2.8KB Cookieless Analytics Tool After Google Analytics Hid 35% of My Traffic

## Overview

Last month my Next.js SaaS showed 1,200 visitors in Google Analytics. AmazeMatrix showed 1,847. That's 35% of my traffic GA simply missed because of ad blockers and cookie consent rejections. I am 20, building from Meerut, and I was making product decisions on broken data. So I deleted GA and built my own. The problem I launched AmazeMatrix in early 2026 with GA4 installed. Three things broke immediately: The cookie banner killed UX. 60% of Indian users clicked "Reject". My bounce rate jumped. Ad blockers ate my data. Over 40% of internet users run blockers that kill analytics cookies by default. Speed. GA's script was 45KB. My LCP went from 1.9s to 3.1s on mobile. I tried the privacy tools everyone recommends: Plausible — $9/mo, super clean, but no heatmaps, no Core Web Vitals Fathom — $15/mo, managed, but no AI insights, no India pricing OpenPanel — $2.50/mo, great product analytics, but I still needed timeline annotations for deploys I didn't want 4 tools. I wanted one lightweight snippet that gave me traffic, speed, and why things changed. Investigation: how cookieless actually works I spent a week reading how the good ones do it. Three patterns: No persistent cookies. Instead of storing an ID for months, you generate a daily rotating hash from IP + user agent + salt that changes every 24h. You can count uniques today, but you can't track someone forever. Server-side or edge capture. If the browser never sets a cookie, ad blockers have nothing to block. Relative coordinates for heatmaps. Instead of sending screenshots (heavy), you send x/y as percentages of the element. That's under 0.2KB per click. That was the blueprint. Solution: I built AmazeMatrix Tech stack I chose because I live in Next.js 16: Frontend: Next.js App Router, Tailwind, Framer Motion Edge: Cloudflare Workers / Vercel Edge DB: Neon Postgres + Drizzle ORM Auth: Better Auth AI: Gemini SDK Billing: Razorpay (because Stripe doesn't work for most Indian founders) The entire snippet is 2.8KB gzipped: 3 lessons I learned building privacy analytics Don't fingerprint, rotate. I first tried a persistent hash. It felt creepy and broke privacy laws. Daily rotating hash gives me accurate daily uniques without storing PII. Privacy-first is not a marketing line, it's an architecture choice. Heatmaps don't need images. Everyone sends full-page screenshots. I send {x: 0.42, y: 0.18, el: '#pricing'}. That's 18 bytes. Multiply by 10k clicks and you save megabytes. Founders don't want another dashboard, they want answers. The most used feature is not the graph. It's the AI chat. "How is page speed affecting sales?" gets more clicks than any chart. How you can try it I kept it stupid simple: Sign up, get siteId Paste 2 lines See data in 10 seconds Free for first 7 days I'm building in public on X and Threads as [@razavi_azaan]. If you want the self-host Docker compose, comment "self-host" and I'll DM it.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/azaanaliraza/i-built-a-28kb-cookieless-analytics-tool-after-google-analytics-hid-35-of-my-traffic-36o1

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
