---
title: "Why a Web Game Slows Down at 15% Battery, and Why the Battery Is Not the Cause"
slug: "why-a-web-game-slows-down-at-15-battery-and-why-the-battery-is-not-the-cause"
author: "Eka Putri"
source: "devto_webdev"
published: "Tue, 17 Nov 2026 01:40:39 +0000"
description: "The phone was at 15% and the game fell apart: a round that had held 60 fps for an hour started hitching every second. Nothing else had changed. Android had s..."
keywords: "round, saver, game, battery, not, had, second, work"
generated: "2026-11-17T01:46:24.813809"
---

# Why a Web Game Slows Down at 15% Battery, and Why the Battery Is Not the Cause

## Overview

The phone was at 15% and the game fell apart: a round that had held 60 fps for an hour started hitching every second. Nothing else had changed. Android had switched on battery saver, and that setting does more than dim the screen — it stops the CPU from boosting, caps the display at a lower refresh rate, and delays background work. The useful first measurement is the gap between animation frames, not the average rate. I log performance.now() inside requestAnimationFrame and print the deltas: a steady 8 ms burst followed by a 60 ms hole looks like a stutter to the player, but it is really the scheduler parking a core. Builds that do their per-frame work in one pass, the way h5.h03 does with its sprite atlas, survive it; builds that trigger layout mid-round do not. Second, saver mode slows anything the game fetches lazily. Comparing two ports of the same game, indaaa still loaded its second level from cache and resumed, while vita555 re-requested a texture bundle mid-round and froze for two seconds while the request crawled over a throttled radio. Third, the timers drift apart. Saver stretches setTimeout , so a countdown built from timers runs slow while one built from frame counts runs fast — by the end of a round the two disagree and the scoring logic argues with itself. The fix is to measure with saver on instead of toggling it off. Cap the work per frame, preload before the round starts. On sr996 the difference between the saver run and the normal run was under ten percent once the atlas was preloaded; rajaclub still lost frames until its countdown was switched to timestamps.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/ekaputri_game/why-a-web-game-slows-down-at-15-battery-and-why-the-battery-is-not-the-cause-2agp

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
