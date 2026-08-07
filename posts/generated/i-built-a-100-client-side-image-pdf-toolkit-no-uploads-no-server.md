---
title: "I built a 100% client-side image & PDF toolkit — no uploads, no server"
slug: "i-built-a-100-client-side-image-pdf-toolkit-no-uploads-no-server"
author: "ZephyrTran"
source: "devto_webdev"
published: "Fri, 07 Aug 2026 07:05:15 +0000"
description: "I kept reaching for online tools to compress an image, convert a PDF, or grab audio from a video — and every one of them uploads your file to a server. For a..."
keywords: "image, pdf, client, side, uploads, server, tools, audio"
generated: "2026-08-07T07:23:56.537225"
---

# I built a 100% client-side image & PDF toolkit — no uploads, no server

## Overview

I kept reaching for online tools to compress an image, convert a PDF, or grab audio from a video — and every one of them uploads your file to a server. For anything remotely personal, that felt wrong. So I built Snapvi : a set of free image / PDF / video tools that run entirely in the browser . Your file never leaves your device. A few things I learned building it: canvas + toBlob covers a surprising amount: format conversion (incl. WebP), resizing, cropping, collage — all client-side. pdf-lib and pdf.js handle merge / split / compress / page-numbering / PDF↔image without a backend. Web Audio decodeAudioData + a small JS MP3 encoder (lamejs) extracts audio from a video to MP3/WAV locally. For the AI tools (background removal, image upscaler , sharpener ) I run the models in-browser via TensorFlow.js — the image still never uploads. The trade-off is the model download + slower on weak phones, which I gate with size caps and a "fast vs max" toggle. Lossless EXIF/GPS stripping is just parsing the JPEG APP segments and dropping them — no re-encode. Turned that into a metadata remover . It's a static site on Cloudflare Pages, so hosting is basically free and there's no server to leak anything. Happy to answer anything about the client-side approach — what would you want to see run in-browser next?

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/zephyrtran/i-built-a-100-client-side-image-pdf-toolkit-no-uploads-no-server-133f

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
