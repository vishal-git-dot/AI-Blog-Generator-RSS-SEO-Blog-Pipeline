---
title: "Notes from moving a small side project off a single VPS"
slug: "notes-from-moving-a-small-side-project-off-a-single-vps"
author: "Taylor Gibson"
source: "devto_webdev"
published: "Mon, 14 Sep 2026 21:33:03 +0000"
description: "I had a hobby app running on one small VPS for about three years. It served maybe forty people, most of them me. Last month the host had a bad night and I sp..."
keywords: "had, thing, app, one, not, moving, small, off"
generated: "2026-09-14T21:41:20.586400"
---

# Notes from moving a small side project off a single VPS

## Overview

I had a hobby app running on one small VPS for about three years. It served maybe forty people, most of them me. Last month the host had a bad night and I spent a weekend rebuilding it from a backup that turned out to be eleven days old. So I finally did the thing I had been putting off. The first thing I got wrong was treating this as an infrastructure problem. It was a backup problem. Moving to fancier hosting would not have saved me a single hour that weekend, because the data I lost was gone before the move was ever on the table. Restore drills are boring and they are the only part of this that actually mattered. The second thing: I tried to containerise everything in one pass. Two days in I had a docker-compose file I did not understand and an app that worked slightly worse than before. I threw it away and moved one piece at a time, starting with the database, and that went fine. If you are doing the same thing, the part worth reading properly is the transcoding and file handling, because that is where the surprises live. Three weekends total. The app is not meaningfully faster. But I can lose the whole machine now and be back in twenty minutes, which is the only number I actually cared about. I leaned on the official docs for this.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/mofh5221/notes-from-moving-a-small-side-project-off-a-single-vps-5die

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
