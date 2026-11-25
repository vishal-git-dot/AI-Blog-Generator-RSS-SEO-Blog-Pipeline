---
title: "Why #fragment URLs matter for true zero-knowledge"
slug: "why-fragment-urls-matter-for-true-zero-knowledge"
author: "Юра"
source: "devto_webdev"
published: "Wed, 25 Nov 2026 21:12:33 +0000"
description: "Ever wonder how self-destructing notes actually keep your secrets safe? Per RFC 3986, anything after # in a URL stays strictly in your browser and never hits..."
keywords: "your, zero, knowledge, never, server, fragment, true, how"
generated: "2026-11-25T21:26:57.089677"
---

# Why #fragment URLs matter for true zero-knowledge

## Overview

Ever wonder how self-destructing notes actually keep your secrets safe? Per RFC 3986, anything after # in a URL stays strictly in your browser and never hits server logs. BurnNote uses this exact mechanism alongside zero-knowledge AES-256-GCM to handle self-destructing notes and up to 50MB encrypted files. Because keys live exclusively client-side, the server never sees them—meaning true end-to-end privacy for sharing sensitive credentials, API keys, or configs with your team. How Zero-Knowledge Ephemeral Sharing Works Client-Side AES-256-GCM: The 256-bit key is generated inside your browser via Web Crypto API and placed in the URL #fragment (never transmitted to the server). Preview & Bot Shield: Link-preview bots (Slack, Telegram, Discord) cannot accidentally consume the secret before your recipient clicks. Atomic Deletion: Upon first read or file download (up to 50MB), the encrypted record is permanently erased from PostgreSQL. Try it free with no signup required: https://burnnote-vault.vercel.app/?utm_source=devto

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/_e498b2d7ee4ac62198933/why-fragment-urls-matter-for-true-zero-knowledge-6ll

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
