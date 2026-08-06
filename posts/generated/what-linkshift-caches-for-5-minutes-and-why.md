---
title: "What LinkShift caches for 5 minutes, and why"
slug: "what-linkshift-caches-for-5-minutes-and-why"
author: "Piotr Zielinski"
source: "devto_webdev"
published: "Thu, 06 Aug 2026 14:10:52 +0000"
description: "I built LinkShift to help people avoid breaking links during migration. One thing that matters a lot in a redirect system is cache behavior. In the codebase,..."
keywords: "map, minutes, cache, linkshift, people, matters, redirect, behavior"
generated: "2026-08-06T14:24:40.418532"
---

# What LinkShift caches for 5 minutes, and why

## Overview

I built LinkShift to help people avoid breaking links during migration. One thing that matters a lot in a redirect system is cache behavior. In the codebase, there are three useful layers to think about: redirect context, keyed by hostname link map context, keyed by map ID edge hostname routing Under normal operation, a successful write invalidates the relevant cache right away. If invalidation fails, live traffic can stay stale for up to 5 minutes. There is also a short negative cache for missing or deleted link map IDs, around 60 seconds. That matters because a deleted map referenced by a rule should fail closed and move on to the next rule, not keep hammering the database. The practical lesson is simple: if your product rewrites traffic, document the worst-case stale window honestly. “Usually immediate” is fine. “Up to 5 minutes if invalidation fails” is better. I added a short note in the docs about this because it comes up whenever people test migrations, redirects, or edge behavior.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/p-zielinski/what-linkshift-caches-for-5-minutes-and-why-1ddc

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
