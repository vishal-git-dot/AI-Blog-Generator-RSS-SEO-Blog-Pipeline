---
title: "I built a free browser-based image & utility toolkit — here's what I learned"
slug: "i-built-a-free-browser-based-image-utility-toolkit-heres-what-i-learned"
author: "toolzip"
source: "devto_webdev"
published: "Mon, 31 Aug 2026 13:12:04 +0000"
description: "Why I Built ToolZip A few months ago, I needed to compress some images for a client project. I searched for a free online tool, found one, uploaded my files ..."
keywords: "toolzip, files, true, what, tools, generator, api, ean"
generated: "2026-08-31T13:15:26.830392"
---

# I built a free browser-based image & utility toolkit — here's what I learned

## Overview

Why I Built ToolZip A few months ago, I needed to compress some images for a client project. I searched for a free online tool, found one, uploaded my files — and then realized I had no idea what they were doing with those files on their servers. That bothered me. So I built ToolZip — a collection of browser-based tools where everything runs locally . No files ever leave your device. What It Does ToolZip currently has 18 tools across several categories: Image tools Compress JPG & PNG (using browser-image-compression ) Convert HEIC → JPG (iPhone photos, using heic2any ) Convert WEBP → JPG/PNG Resize, crop, rotate Developer tools JSON formatter with error highlighting and line numbers URL encoder/decoder with query string parser Base64 encoder/decoder (supports images too) Unix timestamp converter (live current time display) Color converter (HEX ↔ RGB ↔ HSL with palette generator) Utilities QR code & barcode generator Password generator (Web Crypto API) Special characters & emoji copy tool 3D file viewer (OBJ, GLB, FBX, STL, BVH, PLY) Tech stack: Next.js 14 (App Router), deployed on Vercel, all processing via Canvas API and Web Workers. The Hardest Part: EAN-13 Barcodes I want to share one specific challenge that took way longer than expected: rendering EAN-13 barcodes with the EAN-5 add-on correctly . The library I used ( bwip-js ) has a known bug where enabling includetext: true causes the text digits to overlap with the bars when an add-on code is present. My first instinct was to set includetext: false and manually position the text. But this removed the guard bars (the longer bars at the edges and center of an EAN-13 barcode) — which are actually encoded as part of the includetext rendering logic. The solution: Keep includetext: true (to preserve guard bars), extract and remove the glyph paths from the SVG, then re-render the digits as <text> SVG elements at the correct positions. // Server-side (Next.js API route) const rawSvg = bwipjs . toSVG ({ bcid : ' ean13 ' , text : ' 9791190333146 07810 ' , scale : 2 , height : 10 , includetext : true , // ← must stay true (guard bars) guardwhitespace : true , }); // Remove digit glyphs, re-add as <text> elements // with correct x positions calculated from bar positions For the EAN-5 add-on digits, I had to render them as strings , not numbers — because 07810 rendered as a number becomes 7810 (leading zero disappears). Small detail, big headache. 😅 The 3D Viewer Challenge Another interesting part was building the 3D file viewer. I initially loaded Three.js via CDN and referenced it as window.THREE . This caused intermittent failures because the script hadn't finished loading when the component initialized. Fix: Switch to npm import. import * as THREE from " three " ; Simple, but it took me an embarrassingly long time to diagnose. For BVH (motion capture) files, the challenge was different. BVH bone coordinates are in centimeter scale (hundreds of units), so I had to: Add root bones to a group Calculate bounding box from bone positions directly Apply scale Then call group.updateWorldMatrix(true, true) Then create SkeletonHelper(group) Order matters — creating the helper before updating the matrix results in incorrect bone positions. What I'd Do Differently 1. Lazy load tool components from the start All 18 tools currently live in one large JSX file (~5,000 lines). It works, but as the tool count grows this will affect initial load time. I'm planning to split them into separate files with dynamic imports. 2. Server-side generation for complex outputs The barcode generator taught me that some things are better handled server-side. Browser rendering of the same library can differ from Node.js rendering in subtle ways. I moved barcode generation to a Next.js API route, which resolved all inconsistencies. 3. Test with real files earlier I discovered most BVH and FBX edge cases only after users started uploading their actual files. A broader test dataset would have saved time. Traffic & SEO Notes ToolZip launched about a week ago. Here's what I've noticed so far: Google Search Console shows the sitemap was accepted (13+ pages indexed) No organic traffic yet — expected for a new domain The "no server upload" angle resonates well in communities like Reddit I'm writing Korean blog posts targeting local SEO as well, since that's my primary market for now. What's Next Hash generator (MD5, SHA-256 via Web Crypto API) Regex tester Markdown preview More 3D formats (MMD/PMX for the anime community) If you try ToolZip and something doesn't work as expected, I'd genuinely appreciate feedback — either here in the comments or at hello@toolzip.app . Live site: toolzip.app

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/toolzip_7e9a28bbade/i-built-a-free-browser-based-image-utility-toolkit-heres-what-i-learned-2flj

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
