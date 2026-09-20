---
title: "Running AI Portrait Segmentation Entirely in the Browser — Bugs Included"
slug: "running-ai-portrait-segmentation-entirely-in-the-browser-bugs-included"
author: "tomcate"
source: "devto_webdev"
published: "Sun, 20 Sep 2026 04:06:40 +0000"
description: "My first post here mentioned that our ID-photo tools run portrait segmentation locally — a passport photo never leaves your machine. A few readers asked how ..."
keywords: "background, photo, mask, img, person, file, createimagebitmap, but"
generated: "2026-09-20T04:23:13.467233"
---

# Running AI Portrait Segmentation Entirely in the Browser — Bugs Included

## Overview

My first post here mentioned that our ID-photo tools run portrait segmentation locally — a passport photo never leaves your machine. A few readers asked how that actually works, so here is the deep dive, including the three bugs that nearly shipped to production. The stack is deliberately boring MediaPipe Selfie Segmentation, compiled to WASM, loading a 244KB tflite model from our own origin (no CDN, no Google API key, works offline once the PWA is installed). The pipeline: File → createImageBitmap → <canvas> → segmenter.segment(canvas) → categoryMask (Uint8Array) → custom mask pass → composite → download Everything after the file picker is client-side JavaScript. The "server" is nginx serving static files — there is nothing to send data to . Bug #1: The mask was inverted, and the specs were no help The segmentation call returns a categoryMask . Intuition says: non-zero pixels = person, zero = background. MediaPipe's convention is the opposite: 0 is the person. We shipped the intuitive version. The result: users uploaded a portrait, picked "blue background", and got a photo where the person was painted solid blue and the background stayed untouched. The bug report was a screenshot of a smurf. The fix is one line — invert the predicate — but the lesson stuck: when a library hands you an opaque byte array, write a 10-line visualization dump before building anything on top of it. We now render the raw mask as grayscale before every mask-processing change. Bug #2: The 1-pixel white halo that took three rounds to kill After recoloring, every hair edge showed a white fringe. Classic cause: the mask boundary is a hard 0/1 cut, but anti-aliased pixels at the boundary are half-person, half-background. Round 1: dilate the person region by 1px. Better, halo narrower. Round 2: 2px. Better still, but now ears looked slightly "eaten". Round 3 — the actual fix was two changes: Dilate the background side by 3px (paint background color slightly into the person), and Remove the feathering entirely. That second one is counter-intuitive. We had added edge feathering (alpha-blend the mask boundary) for softness — but feathering blends the new background color at reduced opacity, which is exactly what a translucent white-ish fringe is. Hard edges beat pretty edges here; hair detail survives better with a slightly aggressive dilate than with a soft, diluted boundary. Bug #3: Safari and createImageBitmap createImageBitmap(file) — the clean, efficient entry point — is unavailable in older Safari. The fallback is an <img> element with objectURL , awaited through img.decode() : const source = typeof createImageBitmap === ' function ' ? await createImageBitmap ( file ) : await new Promise (( res , rej ) => { const img = new Image (); img . onload = () => res ( img ); img . onerror = rej ; img . src = URL . createObjectURL ( file ); }); Both paths end in the same canvas.drawImage , so downstream code never knows the difference. Feature-detect at the edge, normalize immediately. What "local AI" buys you in practice A passport photo with face, ID number, and biometric pattern never touches a server — not because of a policy, but because there is no upload code path at all . F12 → Network proves it live. It works on a plane, behind the great firewall, and on a locked-down corp machine. Model inference at ~100-300ms per photo on a mid-range phone. Users cannot tell it is not a server call. Our "server" cost for this feature is 244KB of static bandwidth. None of this requires a special product. It requires rejecting the default architecture where "AI feature" means "API call". Try it The ID-photo background changer is live (pick any color, standard sizes for Chinese/US/visa formats, print layouts): ToolVault ID Photo If you are building client-side ML: what's the weirdest silent failure you have debugged in a byte array? That mask inversion took us a user screenshot to find — I am curious what yours took. More local-first tools: 166 tools, zero uploads . First post in this series: why we built it .

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/tomcate_9c4562b60a3ac8fe4/running-ai-portrait-segmentation-entirely-in-the-browser-bugs-included-4ioi

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
