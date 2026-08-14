---
title: "Fixed dt spike at tutorial card dismiss."
slug: "fixed-dt-spike-at-tutorial-card-dismiss"
author: "Weird Codes"
source: "devto_webdev"
published: "Fri, 14 Aug 2026 18:44:00 +0000"
description: "Devlog: Performance Fix - Tutorial Card Dismiss Commit SHA: 9e00951468a361cd1127092072208ac6b63e947d Author: pj90 (weirdcodesofficial) Date: 2026-08-14 18:21..."
keywords: "tutorial, card, lasttime, spike, time, dismiss, when, game"
generated: "2026-08-14T19:00:48.691001"
---

# Fixed dt spike at tutorial card dismiss.

## Overview

Devlog: Performance Fix - Tutorial Card Dismiss Commit SHA: 9e00951468a361cd1127092072208ac6b63e947d Author: pj90 (weirdcodesofficial) Date: 2026-08-14 18:21:24 UTC Message: performance-fix: fixes dt spike at tutorial card dismiss. Summary Fixed a delta time ( dt ) spike that occurred when dismissing the tutorial card. The issue was that lastTime was only being updated conditionally when there was no active tutorial card, causing a large time gap on the next frame after dismissal. Changes File Modified: src/main.js Before // tutorial card dismiss होने पर dt spike न आए if ( ! tutorial . hasActiveCard ()) lastTime = ts ; After // lastTime हमेशा update — pause/tutorial/shaashtra किसी में भी spike न आए lastTime = ts ; Technical Details Issue : The conditional update of lastTime was causing delta time spikes because when the tutorial card was active, lastTime wasn't being updated. Upon dismissal, the accumulated time difference would create a large dt value in the game loop. Solution : Unconditionally update lastTime on every frame to ensure consistent delta time calculations, preventing spikes regardless of pause/tutorial/shaashtra states. Impact : Smoother gameplay experience without frame rate anomalies when dismissing the tutorial card. Files Changed src/main.js (+2 lines, -2 lines) Game Context This optimization is part of the MOKSHA project—an HTML5 browser game based on Sanatan Shastras and Karmic philosophy. The fix ensures the game maintains stable performance during tutorial interactions.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/weirdcodesofficial/fixed-dt-spike-at-tutorial-card-dismiss-4efp

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
