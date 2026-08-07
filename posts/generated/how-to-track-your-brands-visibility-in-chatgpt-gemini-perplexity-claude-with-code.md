---
title: "How to Track Your Brand's Visibility in ChatGPT, Gemini, Perplexity & Claude (With Code)"
slug: "how-to-track-your-brands-visibility-in-chatgpt-gemini-perplexity-claude-with-code"
author: "Krutika Galvankar"
source: "devto_webdev"
published: "Fri, 07 Aug 2026 13:05:09 +0000"
description: "AI search engines like ChatGPT, Gemini, Perplexity, and Claude are changing how people discover brands. Instead of clicking through Google results, users now..."
keywords: "webscore, your, geo, result, brand, sdk, console, log"
generated: "2026-08-07T13:15:09.531592"
---

# How to Track Your Brand's Visibility in ChatGPT, Gemini, Perplexity & Claude (With Code)

## Overview

AI search engines like ChatGPT, Gemini, Perplexity, and Claude are changing how people discover brands. Instead of clicking through Google results, users now ask AI — and the AI picks who to mention. The question is: is your brand being mentioned? Most tools to answer are built for marketers, not developers. So I built webscore-sdk — an npm package that lets you measure this programmatically. What is GEO? GEO (Generative Engine Optimization) is the practice of improving your brand's visibility in AI-generated answers. Think of it like SEO, but instead of ranking on Google, you're trying to get mentioned when someone asks ChatGPT "what's the best tool for X?" Two key metrics matter: Mention rate — % of relevant prompts where your brand appears Citation rate — % of prompts where your website is linked Install npm install webscore-sdk Quickstart import { WebScore } from ' webscore-sdk ' const client = new WebScore ( ' your_api_key ' ) const result = await client . geo . scan ( ' https://yoursite.com ' ) console . log ( result . mentionRate ) // e.g. 67 console . log ( result . citationRate ) // e.g. 42 console . log ( result . sentiment ) // "positive" console . log ( result . score ) // 0–100 GEO score Get a free API key at webscore.dev . Free Tier The free plan includes 10 GEO scans to try it out — no credit card required. Paid plans with higher limits are coming soon. npm: webscore-sdk Live tool: webscore.dev API docs: webscore.dev/api-docs Would love feedback on the prompt methodology or the mention/citation split. Drop a comment below!

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/krutika_galvankar/how-to-track-your-brands-visibility-in-chatgpt-gemini-perplexity-claude-with-code-published-4ij7

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
