---
title: "How I built 15 browser tools with zero backend"
slug: "how-i-built-15-browser-tools-with-zero-backend"
author: "Chilam Chan"
source: "devto_webdev"
published: "Wed, 16 Sep 2026 04:06:18 +0000"
description: "Every "free online tool" I reached for wanted an upload, an account, or both. So I built 15 that need neither — and the constraint that made that possible tu..."
keywords: "you, browser, tools, just, backend, tool, can, nothing"
generated: "2026-09-16T04:17:07.149090"
---

# How I built 15 browser tools with zero backend

## Overview

Every "free online tool" I reached for wanted an upload, an account, or both. So I built 15 that need neither — and the constraint that made that possible turned out to be the best decision in the project: no backend at all. Here's what runs where. The browser can do more than we give it credit for Image work (HEIC→JPG, compress, resize, strip EXIF): <canvas> + createImageBitmap , and WASM ( heic2any ) for formats the browser can't decode natively. PDF split/merge: pdf-lib , entirely client-side. QR codes, password generation, JSON formatting, word counting: plain JS + crypto.getRandomValues and Intl.Segmenter . Nothing touches a server. "Your files never leave your device" isn't a privacy promise you have to trust — it's just how the thing works. Open DevTools → Network and watch: no request fires when you convert a file. Why no-backend is a superpower for a solo dev $0 to run. A zero-dependency static site generator emits plain HTML; Cloudflare Pages serves it free. 272 pages (15 tools × 16 languages + hub) cost nothing. Nothing to operate. No servers, no uploads to secure, no data to leak, no scaling. The whole "ops" surface is a git push. It's genuinely private , which is a real differentiator when every competitor uploads your file to "process" it. The tradeoffs (being honest) No accounts, no cross-device sync, no server-side history. For utilities, that's fine — you do one thing and leave. Some formats (TIFF, exotic codecs) the browser just won't decode; you draw the line and say so. SEO is the whole growth engine, since there's no viral loop. That's the part I'm still figuring out. If you're sitting on a "should this be a SaaS or just a tool" decision: a surprising amount can be just a tool , and shipping it that way is faster, cheaper, and more private. Tools are here if useful: https://boring-tools-6ip.pages.dev — happy to go deeper on any part of the stack in the comments.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/chilam_chan_68a518a731328/how-i-built-15-browser-tools-with-zero-backend-4ffi

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
