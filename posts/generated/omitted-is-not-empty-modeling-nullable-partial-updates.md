---
title: "Omitted Is Not Empty: Modeling Nullable Partial Updates"
slug: "omitted-is-not-empty-modeling-nullable-partial-updates"
author: "LkSvn"
source: "devto_webdev"
published: "Mon, 27 Jul 2026 19:19:44 +0000"
description: "While adding Job Opportunity editing to my Candidate Tracker, one optional description produced three different behaviors: omit the property to preserve the ..."
keywords: "null, domain, update, not, partial, optional, value, provide"
generated: "2026-07-27T19:42:31.392733"
---

# Omitted Is Not Empty: Modeling Nullable Partial Updates

## Overview

While adding Job Opportunity editing to my Candidate Tracker, one optional description produced three different behaviors: omit the property to preserve the stored value; provide a string to replace it; provide null to clear it. The first version mixed undefined and null across the domain, Prisma adapter, application service, and form action. That made clearing a value ambiguous. The final convention uses string | null for persisted domain entities and optional properties for partial update commands. PostgreSQL NULL , Prisma null , and the domain now use the same absence representation. At the update boundary, omission still means “do not change.” The broader lesson is that update types describe commands and state transitions. They should distinguish every behavior the application needs instead of merely reusing an entity shape without considering omission.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/lksvn/omitted-is-not-empty-modeling-nullable-partial-updates-9po

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
