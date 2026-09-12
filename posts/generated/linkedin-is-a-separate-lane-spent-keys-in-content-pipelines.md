---
title: "LinkedIn is a separate lane: spent keys in content pipelines"
slug: "linkedin-is-a-separate-lane-spent-keys-in-content-pipelines"
author: "Robert"
source: "devto_webdev"
published: "Sat, 12 Sep 2026 10:00:00 +0000"
description: "The LinkedIn channel in Orqestra now tracks spent source keys independently from the blog and the dev.to daily log. Before this change, used_source_keys() fi..."
keywords: "linkedin, blog, set, spent, channel, now, log, lane"
generated: "2026-09-12T10:25:42.908887"
---

# LinkedIn is a separate lane: spent keys in content pipelines

## Overview

The LinkedIn channel in Orqestra now tracks spent source keys independently from the blog and the dev.to daily log. Before this change, used_source_keys() filtered against a single global set, which meant a source event consumed by a short note was blocked from the blog and from LinkedIn as well. The fix is in used_source_keys(), which now filters by lane. An outage described briefly in the daily log can still surface as full coverage on the blog, and again as a LinkedIn post, without the second or third pass being blocked by the first. Four files changed, with 688 lines added and 87 removed. The three-channel schedule, dev.to every day, the blog for search and pillar coverage, LinkedIn three times a week, was set on 2026-09-06 and is now enforced in code rather than by hand. The record does not say what the global set was originally designed to prevent. If your pipeline shares one spent-key set across output channels, a key consumed by a short post will block the same event on LinkedIn or anywhere else: scope the record to the channel. Originally published at neuragrowth.co . NeuraGrowth is a one-person digital-products studio; this is the log of what its pipeline does and where it breaks.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/robswierk/linkedin-is-a-separate-lane-spent-keys-in-content-pipelines-1373

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
