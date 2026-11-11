---
title: "Hitting 200 Strokes: What the Signature Maker Does at Its Stroke Limit"
slug: "hitting-200-strokes-what-the-signature-maker-does-at-its-stroke-limit"
author: "OnePassApps"
source: "devto_webdev"
published: "Wed, 11 Nov 2026 05:29:38 +0000"
description: "Hitting 200 Strokes: What the Signature Maker Does at Its Stroke Limit I work on OnePassApps, and this is our own app, measured on our own site. Our guide fo..."
keywords: "one, stroke, app, strokes, signature, not, limit, export"
generated: "2026-11-11T05:37:22.169249"
---

# Hitting 200 Strokes: What the Signature Maker Does at Its Stroke Limit

## Overview

Hitting 200 Strokes: What the Signature Maker Does at Its Stroke Limit I work on OnePassApps, and this is our own app, measured on our own site. Our guide for the Signature Maker makes a promise we had never actually tested: "A signature holds up to 200 strokes and 40,000 points." Every post this account has written about that app so far quoted that line and moved on. This one is the test. What I measured, and where: the live app at app.onepassapps.com/apps/signature-maker, in one browser, one signed-out session, one build, on 11 November 2026. Every number below came out of that session. The counter is live. The panel counts strokes as you draw them and says so out loud: "1 stroke. Ctrl+Z undoes." Add strokes and it becomes "199 strokes. Ctrl+Z undoes." I started the pass with one long stroke already on the canvas, so the counter read one ahead of the strokes I was adding. The 201st stroke did not land. The app said: "This signature has reached its stroke limit. Undo a stroke or clear the canvas to keep drawing." That message appeared the first time I tried to add a stroke past the limit, and it stayed on screen. The counter then froze. It read exactly 200 for the next 20 strokes I tried to draw, fifteen in one pass and five in another. It never read 201, and the export size did not move either. Exporting still works at the ceiling. The export line kept reading "Exports at 1198 × 182 px, trimmed to the ink with a small margin." and the PNG at 2x downloaded as 52,090 bytes, measuring 1198 x 182 pixels. Reaching the limit stops drawing; it does not break the export. The other half of the guide's number, and where I got to. The guide also names 40,000 points. I dispatched 41,000 pointer-move events inside a single stroke. The app counted that as one stroke, never showed a point-limit message, and the vector export of that stroke held 3,999 curve commands - roughly 12,000 coordinate pairs - in 151,856 bytes, with viewBox "4 66 599 30", exactly one path element and no image tag. So whatever the app held internally, the SVG for that stroke was about 12,000 points, well short of 40,000. I am not claiming what happens at 40,000 points: I did not reach them, and I would rather say so than guess. Limits, stated plainly: one browser, one signed-out session, one build, one day, 11 November 2026. Strokes were driven with a mouse, so the pressure-aware width path, where a pen that reports pressure changes the line width, was not exercised. The counts are the app's own, read from its panel. The byte sizes are the downloaded files. The SVG figures are parsed out of the file itself. I did not use the Copy PNG button, I made no account, I uploaded nothing, and I changed nothing on the site. The guide, the app and the earlier post on this app are linked below. That earlier post measured the export formats in detail and left this ceiling untested; this post is the test it left open. The Signature Maker Its guide The earlier post on this app: export formats, the PNG margin and the SVG

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/onepassapps/hitting-200-strokes-what-the-signature-maker-does-at-its-stroke-limit-7hf

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
