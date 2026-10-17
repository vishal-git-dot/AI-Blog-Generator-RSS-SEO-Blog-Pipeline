---
title: "GroundTruth OSINT: free live global monitoring — 170 feeds, 3D globe, daily brief, no signup"
slug: "groundtruth-osint-free-live-global-monitoring-170-feeds-3d-globe-daily-brief-no-signup"
author: "OSINT Watch"
source: "devto_webdev"
published: "Sat, 17 Oct 2026 15:13:33 +0000"
description: "A month ago I posted about a side project: a free live global monitoring dashboard. Since then it's been rebranded, rebuilt, and grown a lot. Here's where it..."
keywords: "live, what, free, global, globe, feeds, signup, sources"
generated: "2026-10-17T15:18:37.847613"
---

# GroundTruth OSINT: free live global monitoring — 170 feeds, 3D globe, daily brief, no signup

## Overview

A month ago I posted about a side project: a free live global monitoring dashboard. Since then it's been rebranded, rebuilt, and grown a lot. Here's where it stands. GroundTruth OSINT — https://groundtruthosint.com A free, no-signup dashboard that pulls 170 live reporting feeds — official sources (White House, combatant commands), major outlets, specialists — and correlates them into a single global picture on a 3D globe, refreshed every 15 minutes. The philosophy: detect, correlate, assess. Show what multiple sources report, label the source types, don't editorialize. Raw global awareness without the TV news spin. What's in it: Live 3D globe with 150 tracked events, clickable markers (sources, plain-language "So what," market-impact context) Ranked reports page with keyword + priority search and a triage queue Shareable deep links to any event — send someone straight to a story "New since your last visit" highlighting so you see what changed Optional layers: live wildfire data (NASA FIRMS), earthquakes (USGS M4.5+), severe weather Free daily morning brief — top events in your inbox at 6:30 AM ET, just an email, no account No signup, no paywall, works on mobile The stack: one Cloudflare Worker + D1. Feed polling, clustering, and priority scoring all happen server-side on a 15-minute cycle; the browser just renders. The globe is canvas-rendered with pre-baked marker sprites (learned the hard way that per-frame shadowBlur melts mobile GPUs). Snapshot-backed API took cold loads from 38s to ~1.5s. The honest part: it costs $5/month to run plus feed bandwidth. There's a small donation link on the site — that's the entire business model. The tool is free, no tiers, no gates. What's next: user-defined watch keywords (track your topics, not just the global picture), better source-diversity scoring. It's live: https://groundtruthosint.com — I'd genuinely love feedback from devs: what would you track that it doesn't? Any feeds I'm missing? Disclosure: the linked site has a small donation link that helps cover operating costs.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/osintwatchapp/i-rebuilt-my-free-osint-dashboard-170-feeds-3d-globe-daily-email-brief-no-signup-kb5

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
