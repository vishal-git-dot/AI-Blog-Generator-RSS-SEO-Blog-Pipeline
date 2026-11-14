---
title: "Claude Sonnet 4.5 retires on 30 November: find it in your code"
slug: "claude-sonnet-45-retires-on-30-november-find-it-in-your-code"
author: "Karthik Upadrasta"
source: "devto_ai"
published: "Sat, 14 Nov 2026 05:40:06 +0000"
description: "Anthropic retires Claude Sonnet 4.5 ( claude-sonnet-4-5-20250929 ) on 30 November 2026 . After that, requests to that model ID on Anthropic's API fail. Anthr..."
keywords: "claude, sonnet, anthropic, your, check, retires, november, code"
generated: "2026-11-14T05:48:05.832765"
---

# Claude Sonnet 4.5 retires on 30 November: find it in your code

## Overview

Anthropic retires Claude Sonnet 4.5 ( claude-sonnet-4-5-20250929 ) on 30 November 2026 . After that, requests to that model ID on Anthropic's API fail. Anthropic recommends Claude Sonnet 5.5 as the replacement ( Anthropic's notice ). The ID rarely sits in one place. Check: application code and SDK calls .env.example and other environment defaults Terraform variables and Helm values notebooks and eval scripts fallback paths that only run when something else fails The free way rg -n "claude-sonnet-4-5" --hidden -g '!node_modules' It misses IDs built from parts ( f"claude-sonnet-{ver}" ) and aliases, so read the hits around your config loaders too. On Bedrock or Google Cloud? Those platforms set their own retirement dates, which can differ from Anthropic's. Check your platform's page. The automatic way We built SunsetLint , a GitHub App that runs this check against 59 retirement rules (Anthropic, OpenAI, Google Gemini), each taken from the provider's own notice. It opens one issue per repo with file, line, date and replacement, and it's read-only. Here's what it posts on our demo repo: issue #1 . Free for public repos and 3 private repos.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/genztechnologies/claude-sonnet-45-retires-on-30-november-find-it-in-your-code-2amn

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
