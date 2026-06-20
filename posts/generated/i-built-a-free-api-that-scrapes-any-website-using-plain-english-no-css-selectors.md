---
title: "I Built a Free API That Scrapes Any Website Using Plain English - No CSS Selectors"
slug: "i-built-a-free-api-that-scrapes-any-website-using-plain-english-no-css-selectors"
author: "Paras Tejpal"
source: "devto_python"
published: "Sat, 20 Jun 2026 13:51:12 +0000"
description: "I've wasted days of my life maintaining CSS selectors. You know the drill - you write the perfect scraper, it works great for a week, then the site does a fr..."
keywords: "free, selectors, you, opticparse, api, your, vision, json"
generated: "2026-06-20T14:15:47.238230"
---

# I Built a Free API That Scrapes Any Website Using Plain English - No CSS Selectors

## Overview

I've wasted days of my life maintaining CSS selectors. You know the drill - you write the perfect scraper, it works great for a week, then the site does a frontend redesign, your selectors break, and you spend another afternoon hunting through the DOM again. So I built Opticparse - a completely different approach. How It Works Instead of selectors, Opticparse: Opens a real Chromium browser (via Playwright) Navigates to your URL and waits for JavaScript to load Screenshots the page Sends the screenshot to a vision AI model Returns structured JSON based on your natural language query curl -X POST https://opticparse.onrender.com/api/vision-scrape \ -H "X-API-Key: YOUR_KEY" \ -H "Content-Type: application/json" \ -d '{ "target_url": "https://news.ycombinator.com", "extraction_query": "Extract all story titles and upvote counts as a JSON array" }' No selectors. No XPath. No DOM inspection. The AI figures out where everything is from the screenshot. The AI Provider Rotation The smartest part: if one AI provider rate-limits, the next one kicks in automatically. Provider order: Groq - llama-3.2-11b-vision (fastest free inference, < 1s) GitHub Models - gpt-4o (free 150 req/day fallback) OpenRouter - gpt-4o (additional free credits) Zero downtime, effectively unlimited free capacity. The Stealth Mode Cloudflare and other WAFs detect headless browsers by checking navigator.webdriver . I added a simple init script to neutralize this: await context . add_init_script ( " Object.defineProperty(navigator, ' webdriver ' , {get: () => undefined}); " ) Combined with a real Chrome user agent, this bypasses most basic bot detection. Try It Free Available on RapidAPI with a free tier - no credit card needed. GitHub (MIT): https://github.com/parastejpal987-cmyk/opticparse What websites have you tried to scrape that kept breaking? Let me know in the comments!

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/parastejpal987cmyk/i-built-a-free-api-that-scrapes-any-website-using-plain-english-no-css-selectors-14fa

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
