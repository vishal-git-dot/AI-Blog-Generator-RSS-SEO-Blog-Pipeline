---
title: "Fun-VACE redraw: the control video decides what transfers, and an 8-frame loop makes it long"
slug: "fun-vace-redraw-the-control-video-decides-what-transfers-and-an-8-frame-loop-makes-it-long"
author: "AI-KSK"
source: "devto_ai"
published: "Tue, 24 Nov 2026 22:02:40 +0000"
description: "Wan 2.2 Fun-VACE with an 8-frame overlap loop gives unbounded video redraw, and the controlling insight is that the control video you feed decides what trans..."
keywords: "control, video, pose, vace, redraw, depth, what, transfers"
generated: "2026-11-24T22:10:49.165542"
---

# Fun-VACE redraw: the control video decides what transfers, and an 8-frame loop makes it long

## Overview

Wan 2.2 Fun-VACE with an 8-frame overlap loop gives unbounded video redraw, and the controlling insight is that the control video you feed decides what transfers: pose video transfers pose, depth video transfers dynamics. Watch the episode: https://youtu.be/qX0N0DgZYAk Chinese original: https://www.bilibili.com/video/BV1NNpczEE3Q The core mechanism Fun-VACE's redraw behaviour is determined by the control signal, not by the prompt. That is a cleaner mental model than prompt-based control: Feed an extracted pose video: the output follows the pose. Feed a depth video: the output follows the dynamics and volume. The reference is optional - it supplies style or identity, not motion. Why the 8-frame overlap Long redraw is done in windows. Overlapping eight frames between windows keeps the seam continuous, which is what makes a minute-long redraw look like one shot instead of a series of clips. Dual control The episode covers pose and depth control together - two control streams constraining the same generation. In practice that means a shot can hold a specific body configuration and a specific spatial structure at once. What to check Pose transfer versus depth transfer on the same source - do they really produce different results, as claimed? The window seam at frame 8 boundaries, watched closely. Long runs: does the style drift, even if the pose holds? Where this sits among the VACE episodes Other episodes cover VACE with Lynx identity, VACE with audio, and VACE inside merges. This one is the plainest and most useful: control video in, redraw out, looped. Honest limits Control quality dominates: a bad pose or depth extraction becomes a bad redraw, unfixably. Unbounded loops still accumulate drift. No workflow or weights are bundled with this article.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/ai-ksk/fun-vace-redraw-the-control-video-decides-what-transfers-and-an-8-frame-loop-makes-it-long-4he1

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
