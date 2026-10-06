---
title: "AccessBuild Day 3: Auto-Scanning Is Live. Here's What I Learned."
slug: "accessbuild-day-3-auto-scanning-is-live-heres-what-i-learned"
author: "Okeke Chukwudubem"
source: "devto_python"
published: "Tue, 06 Oct 2026 12:53:16 +0000"
description: "Day 3 of AccessBuild. The API is no longer just a calculator. It has a memory now. What I Built Today Yesterday, the API could only score elements you pasted..."
keywords: "day, what, real, tree, scan, api, now, supabase"
generated: "2026-10-06T13:06:53.999444"
---

# AccessBuild Day 3: Auto-Scanning Is Live. Here's What I Learned.

## Overview

Day 3 of AccessBuild. The API is no longer just a calculator. It has a memory now. What I Built Today Yesterday, the API could only score elements you pasted in manually. Today, it parses real Android UI tree XML, extracts every interactive element, scores it, and saves the result to Supabase. The new /scan endpoint accepts a raw UI tree dump. It walks through every node, classifies each element as button/input/icon/link, checks for accessibility labels, and returns a grade from A to F. Then it writes the audit to the database. The Stack Grew Up Day 1 Day 3 FastAPI FastAPI In-memory only Supabase PostgreSQL Manual element list Android UI tree XML One-off test Persistent, repeatable audits No history /audits/recent endpoint No stats /stats endpoint The First Real Scan I ran the first auto-scan on a test banking login screen. Five interactive elements. Only two had labels. Result: D — 40% accessible Recommendation: "Urgent. Most elements are invisible to screen readers. Immediate fixes required." That's the point. A real banking app with that score would be unusable by blind customers. And now the audit is saved in the database for future reference. What Broke The deploy failed multiple times. First, Render couldn't find the port. Then it couldn't find models.py . Then the build cache held onto old code. Each error taught me something about how Render handles deployments. The fix: update the start command to use $PORT , create the missing files, clear the build cache, and redeploy. Three hours of debugging. Ten minutes of actual feature work. What Works Now /scan — Auto-scan from Android UI tree XML /stats — Aggregate statistics from Supabase /audits/recent — Recent audit history Supabase persistence — Every audit saved Full pipeline: request → parse → score → save → respond What's Next (Day 4) Build a public dashboard showing audited apps and scores Connect real app scanning to my Phone Agent's UI tree output Start scanning Nigerian banking apps for real The Repo 👉 github.com/Dexter2344/accessbuild-api Day 3 is done. The API has a memory now. — Dexter

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/okeke_chukwudubem_5f3bf49/accessbuild-day-3-auto-scanning-is-live-heres-what-i-learned-59h8

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
