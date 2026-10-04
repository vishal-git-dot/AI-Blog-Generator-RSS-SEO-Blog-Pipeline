---
title: "Your 'vectorized' SVG may still be a bitmap — 4 checks, with measurements"
slug: "your-vectorized-svg-may-still-be-a-bitmap-4-checks-with-measurements"
author: "MakeInterview"
source: "devto_webdev"
published: "Sun, 04 Oct 2026 04:46:18 +0000"
description: "When you "vectorize" an image, the result is supposed to be paths — geometry you can scale, recolor, and cut. A surprising number of tools, including Inkscap..."
keywords: "image, bitmap, you, png, paths, svg, inkscape, vector"
generated: "2026-10-04T05:17:20.177723"
---

# Your 'vectorized' SVG may still be a bitmap — 4 checks, with measurements

## Overview

When you "vectorize" an image, the result is supposed to be paths — geometry you can scale, recolor, and cut. A surprising number of tools, including Inkscape's own Trace Bitmap, instead wrap the original bitmap in an <svg> tag, so the file is a picture inside a vector wrapper. It looks fine at 100% and falls apart everywhere else. You can tell which one you got in about a minute. Here are four checks, then the numbers from a benchmark I ran. Check 1 — count the <image> elements Open the SVG in a text editor and search for <image . A non-zero count means a raster picture is embedded, and the file is at least partly a bitmap in a vector wrapper. Zero is a good sign, but not the whole story (see check 3). Check 2 — compare bytes with and without the bitmap Strip every <image> element and compare the file sizes. The delta is exactly how many bytes of picture were hiding inside. # bytes with the embedded bitmap removed python3 - << ' EOF ' import re s = open("out.svg").read() print(len(s.encode()), "->", len(re.sub(r"<image \b .*?</image>|<image \b [^>]*/>", "", s).encode())) EOF If the file drops by 70% when you remove the image, the image was the artwork. Check 3 — is the visible shape actually made of paths? Path count is the giveaway. If the artwork you see has rich color but the <svg> contains 4 <path> elements, those paths are not drawing your picture — the embedded bitmap is. Check 4 — render it huge Rasterize the SVG at 20× and zoom in. Real vector paths hold a clean edge; an embedded bitmap goes soft and pixelated the moment you pass the source resolution. What the measurement actually showed I ran three tracers on three inputs on one Apple-silicon Mac, twice each on two dates (2026-09-28 and 2026-09-29). The harness recorded offline: true — not one call left the machine. Two inputs kept identical SHA-256 hashes across both runs and produced byte-identical Inkscape and potrace output, so the columns below are reproducible. Input Tool Bytes Bytes excl. bitmap <path> elements Distinct colours Embedded <image> apple-touch-icon.png (180×180) Inkscape 1.4.4 Trace Bitmap 29,689 20,869 7 7 1 apple-touch-icon.png potrace 1.16 1,322 1,322 1 1 0 apple-touch-icon.png any2svg engine (VTracer 0.6.15) 1,027 1,027 3 3 0 og-image.png (1200×630) Inkscape 1.4.4 Trace Bitmap 550,602 460,883 8 8 1 og-image.png potrace 1.16 21,718 21,718 88 1 0 og-image.png any2svg engine 32,583 32,583 236 93 0 synthetic-flat.png (800×600) Inkscape 1.4.4 Trace Bitmap 6,759 1,605 4 4 1 synthetic-flat.png potrace 1.16 771 771 1 1 0 synthetic-flat.png any2svg engine 3,068 3,068 6 6 0 Three things fall out of this: Inkscape's stock Trace Bitmap exported exactly one embedded <image> every time — all three inputs, both dates. The bare <image> count is not a perfect verdict on its own, but here it fired on every single run. potrace is honest but 1-bit. It never embeds a bitmap, and it never produces more than one colour layer. Perfect for a stencil, useless for a logo. Path count tracks "is this really a vector". The icon that came out as 3 paths and the photo-derived banner that came out as 236 paths are genuinely editable; the 7-path Inkscape file is a 20 KB bitmap with a thin vector coat of paint. Why this bites harder than it looks CNC, laser, and vinyl cutters consume the paths , not the pixels. A raster-in-a-wrapper produces a toolpath around the image bounds, not the shape you wanted. Web use means shipping a 550 KB "SVG" that could have been 30 KB, then watching it blur on a retina display. Editing is the loudest tell: try to recolor a single region of an embedded bitmap inside a vector editor. You can't, because there is no path there to select. Getting a real one If you'd rather generate than audit: potrace is the right tool for flat, high-contrast art. For photos, logos, and multi-colour artwork you want a colour tracer that emits genuine filled paths. Full disclosure: I build one — pic2svg , the engine in the table above. It's a hosted tracer (image posted to the API, traced there), free to trace and preview, with a paid tier for downloads. But the point of this post is the checklist, not the pitch: run checks 1–4 on whatever tool you already use, and you'll know in a minute whether you're holding vectors or a picture in a costume. The raw measurements and the exact commands are published at pic2svg.com/offline-vector-converter-benchmark if you want to reproduce or dispute them.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/makeinterview/your-vectorized-svg-may-still-be-a-bitmap-4-checks-with-measurements-5g6h

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
