---
title: "Cursor's Breach Started With a Vendor's Leaked Key"
slug: "cursors-breach-started-with-a-vendors-leaked-key"
author: "Rohan Tech official"
source: "devto_ai"
published: "Sun, 15 Nov 2026 05:42:33 +0000"
description: "On November 13, Cursor published the full story behind its October security incident — and the first domino fell outside Cursor's own walls. An access key Cu..."
keywords: "cursor, traces, fireworks, key, its, security, incident, access"
generated: "2026-11-15T05:48:55.493583"
---

# Cursor's Breach Started With a Vendor's Leaked Key

## Overview

On November 13, Cursor published the full story behind its October security incident — and the first domino fell outside Cursor's own walls. An access key Cursor had issued to its inference vendor, Fireworks AI, was exposed at Fireworks. The attacker used it to copy coding-agent traces out of a storage bucket the two companies shared. The bucket was read-only, and most of the traces in it dated from 2025, from sessions that weren't running in Privacy Mode. The traces were the real problem Here's the uncomfortable bit: some of those traces held credentials that had never been redacted. The attacker found them, and those credentials opened the door to Cursor's internal SaaS tools. On October 29, that access was used to plant modified copies of Anthropic's Claude Code extension — versions 2.1.312 and 2.1.313 — in the cache behind Cursor's extension marketplace. The tampered builds sat there for about 11 hours, and Cursor says up to 5,000 users may have received them. Anthropic didn't publish those copies; they were slipped in through the compromised access. Where things stand now Cursor says the incident is contained. The last attacker activity it saw was on November 1, and it was blocked. The Fireworks key has been revoked, all inference traffic has moved off Fireworks, and the marketplace has been rebuilt. You can read Cursor's own account in its post, An update on our recent security incident . The takeaway for anyone building with coding agents? Your session traces can hold live secrets, and your model vendors are part of your attack surface whether you planned for it or not. I wrote up the full timeline, the response steps, and what developers should check in the complete piece here: Cursor Traces Its Security Breach to a Fireworks Key

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/rohan_techofficial_81a0f/cursors-breach-started-with-a-vendors-leaked-key-5g5a

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
