---
title: "I wanted the diff, not a screenshot: a small URL-change API"
slug: "i-wanted-the-diff-not-a-screenshot-a-small-url-change-api"
author: "SignalWatch"
source: "devto_webdev"
published: "Thu, 24 Sep 2026 04:05:26 +0000"
description: "I kept wanting one thing: paste a public URL, and get a unified diff when the text changes — in email, Slack, or a JSON webhook I can point at n8n. Screensho..."
keywords: "not, you, what, diff, url, public, text, can"
generated: "2026-09-24T04:09:17.205595"
---

# I wanted the diff, not a screenshot: a small URL-change API

## Overview

I kept wanting one thing: paste a public URL, and get a unified diff when the text changes — in email, Slack, or a JSON webhook I can point at n8n. Screenshot tools are built for that inbox moment ("something changed, go look"). Self-hosting changedetection.io is the right answer if you want a container. I wanted the hosted, boring version: visible text, a CSS selector, an ignore regex, and a signed webhook. So I built SignalWatch . What it does Polls a public URL (15 min on the free plan) Hashes the visible text, optionally scoped to a CSS selector Strips noise with an ignore regex, ignore-line-order, and a minimum change ratio Sends email, a Slack/Discord message with a diff block, or HMAC-signed JSON Keeps the event history so the dashboard can show what actually moved What it does not do It does not render JavaScript, log in, or take screenshots. If the price only exists after client-side rendering, it will not see it. There is a public monitor on the Hacker News front page so you can see real diffs without an account: live sample . Free tier is 3 monitors, no card. I would like to know what you would watch with it, and which noise filter you actually need.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/signalwatch/i-wanted-the-diff-not-a-screenshot-a-small-url-change-api-1aoh

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
