---
title: "# I built 62 free browser tools in one website — no uploads, no sign-ups, works offline"
slug: "i-built-62-free-browser-tools-in-one-website-no-uploads-no-sign-ups-works-offline"
author: "Sophia Anjum"
source: "devto_webdev"
published: "Sat, 11 Jul 2026 13:21:49 +0000"
description: "I got tired of a routine most of us know too well: you need to merge two PDFs, or shrink an image, or make a QR code — so you Google it, land on some ad-cove..."
keywords: "your, tools, you, two, site, free, image, pdf"
generated: "2026-07-11T13:38:52.451104"
---

# # I built 62 free browser tools in one website — no uploads, no sign-ups, works offline

## Overview

I got tired of a routine most of us know too well: you need to merge two PDFs, or shrink an image, or make a QR code — so you Google it, land on some ad-covered site, and it asks you to upload your file to their server and maybe "create a free account" before giving you the result. For a 10-second task. And now your file lives on someone else's computer. So I built the site I wished existed: Tools Guru — 62 free tools in one place, where everything runs locally in your browser. Nothing is ever uploaded. No account. No limits. Install it as an app and it works with your WiFi turned off. What's inside The tools cover pretty much everything I kept needing: 📄 PDF tools — merge PDFs, split by page range, images → PDF, text → PDF. Your documents never leave your device, which honestly is the whole point for anything sensitive — contracts, IDs, invoices. 🖼️ Image tools — compressor, resizer, image → Base64, color picker, CSS gradient generator... and the two I'm most proud of, which I'll get to in a second. 📝 A full resume maker — 20 recruiter-style templates (sidebar, timeline, two-column, with-photo layouts), live preview, pixel-perfect PDF and Word export. The kind of thing other sites paywall behind $9.99/month. 🧮 Calculators & converters — EMI, loan, GST, SIP, BMI, age, date difference, unit converter, temperature, binary/hex, Roman numerals, Morse code with actual sound playback... ⚙️ Developer utilities — JSON formatter, regex tester with live highlighting, hash generator, Base64/URL/HTML encoding, timestamp converter, CSV ⇄ JSON, markdown preview, a live HTML/CSS/JS playground. 🎲 Generators — passwords with strength meter, QR codes, barcodes, UUIDs, color palettes, random name picker for giveaways. Plus everyday stuff: text-to-speech with downloadable audio, stopwatch, event countdowns, a calorie finder, live weather. The two tools that were genuinely hard to build Most of the 62 are honest, simple utilities. Two of them nearly broke me: The AI background remover. Every background remover online uploads your photo to a server. Mine runs the AI entirely in your browser — two different segmentation models (ISNet and RMBG-1.4, ~280 MB of neural network weights combined) executed locally via ONNX Runtime and transformers.js. Your photo never leaves your machine, and after the first visit it works completely offline. Getting there meant solving problems like: pre-downloading the models silently when you first open the site (so the tool is instant when you need it), writing files into the exact Cache Storage buckets the AI libraries look up, working around Chrome's Background Fetch API silently stalling on CDN redirects, and discovering that my own service worker was wiping the downloaded models on every site update. If people are interested, I'll write a separate deep-dive post on the engineering. The AI image generator — type a description, get an image, free, no account. Same philosophy: as little server as possible, no data hoarding. Why "nothing uploaded" is the hill I'll die on Three reasons this became the core rule for all 62 tools: Privacy that's structural, not promised. I don't have to convince you I delete your files — I never receive them. Open DevTools, watch the network tab, verify it yourself. Speed. No upload → process → download round-trip. A 20 MB PDF merges in about a second because it never travels anywhere. It works offline. The site is a PWA. On a flight, in a dead zone, during an internet outage — every tool keeps working. I need your feedback (the real reason for this post) The site is live and free: toolsguru.shop I built this solo, and 62 tools means 62 places I might have gotten something wrong. If you have two minutes, I'd genuinely love to hear: Which tool did you try first, and did it do what you expected? What's broken or awkward? Especially on mobile — be brutal, it's the only useful kind of feedback. What's missing? If there's a tool you keep re-Googling that isn't here, tell me and there's a good chance I'll build it. For the curious: throw a difficult photo at the background remover — hair, fur, glass — and tell me which of the two engines handled it better. I'll be in the comments. Every suggestion gets read, and honestly the roadmap for the next 10 tools will probably come from this thread. Stack: vanilla JS, transformers.js + ONNX Runtime WASM for the AI tools, Service Worker + Cache Storage for offline, deployed on Vercel. No frameworks, no backend, no database — the entire product is static files and your browser.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/sophia_anjum_0509b2bb7049/-i-built-62-free-browser-tools-in-one-website-no-uploads-no-sign-ups-works-offline-3cia

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
