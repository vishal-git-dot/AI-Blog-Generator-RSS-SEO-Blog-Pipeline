---
title: "My OG image generator served a blank PNG to 40% of Slack previews — the cache key was the URL, not the title"
slug: "my-og-image-generator-served-a-blank-png-to-40-of-slack-previews-the-cache-key-was-the-url-not-the-title"
author: "InApp"
source: "devto_ai"
published: "Sat, 17 Oct 2026 15:04:49 +0000"
description: "I built an OG image API that takes a title + description and renders a 1200x630 card. It worked great in my tests. Then I wired it into a link-unfurling pipe..."
keywords: "image, url, title, card, deploy, slack, previews, cache"
generated: "2026-10-17T15:18:37.851139"
---

# My OG image generator served a blank PNG to 40% of Slack previews — the cache key was the URL, not the title

## Overview

I built an OG image API that takes a title + description and renders a 1200x630 card. It worked great in my tests. Then I wired it into a link-unfurling pipeline for an agent that posts dozens of links into Slack channels, and suddenly a third of the previews came back gray. The bug wasn't in the renderer. It was in the CDN I put in front of it. Every generated image URL looked like /og?title=...&desc=... . The CDN cached on the full URL, which is correct — except Slack's unfurling bot strips query strings before requesting the image in some clients. So ?title=Deploy+failed and ?title=Deploy+succeeded both collapsed to /og/ , and the first response got cached for everyone else. One "Deploy failed" card got served to a channel full of "Deploy succeeded" links. The fix was boring and effective: hash the full parameter set into the path itself ( /og/a3f9c2….png ) and make the query string optional. Cache key and content now agree. What I actually learned: generated-image APIs are only as correct as the caching layer in front of them, and "the URL is the cache key" is a habit worth auditing whenever the URL's parameters carry the content . Agents building link previews, unfurlers, or card generators on top of an image API — check what your CDN sees, not just what you send. It's packaged here if you want to poke at it: https://x402.freeq.one/tools/og_image_generator.html The blank-card bug taught me more about HTTP caching than any blog post.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/imapphelp/my-og-image-generator-served-a-blank-png-to-40-of-slack-previews-the-cache-key-was-the-url-not-4lfd

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
