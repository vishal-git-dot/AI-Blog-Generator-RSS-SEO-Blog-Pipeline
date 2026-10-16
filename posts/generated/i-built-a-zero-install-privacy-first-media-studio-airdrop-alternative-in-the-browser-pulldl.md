---
title: "I built a zero-install, privacy-first media studio & AirDrop alternative in the browser (PullDL)"
slug: "i-built-a-zero-install-privacy-first-media-studio-airdrop-alternative-in-the-browser-pulldl"
author: "Mahean Ahmed"
source: "devto_webdev"
published: "Fri, 16 Oct 2026 03:34:14 +0000"
description: "Hey developers! 👋 Like many of you, I was constantly frustrated by three everyday digital annoyances: Transferring photos/videos between iPhone, Android, and..."
keywords: "pulldl, audio, photos, drop, video, zero, privacy, media"
generated: "2026-10-16T04:00:24.053111"
---

# I built a zero-install, privacy-first media studio & AirDrop alternative in the browser (PullDL)

## Overview

Hey developers! 👋 Like many of you, I was constantly frustrated by three everyday digital annoyances: Transferring photos/videos between iPhone, Android, and Windows PC without having to email files to myself or connect cables. Online converter sites bloated with shady pop-up ads, malware, and artificial 2GB paywalls. Privacy concerns: Cloud tools that upload private family photos, voice notes, and videos to third-party servers just to convert or compress them. To solve this, I spent the last few months building PullDL — a universal, privacy-first web utility suite that runs heavy processing directly in the browser . 🚀 What makes PullDL different? 1. PullDrop — Universal AirDrop Alternative A zero-install cross-device file transfer engine. You can send large photos, 4K videos, and documents between iOS, Android, Windows, Mac, and Linux: Peer-to-Peer (WebRTC): Files stream directly between devices over local networks whenever possible. End-to-End Encrypted Relay: Works seamlessly even when devices are on different Wi-Fi networks or mobile data. Zero Server Storage: Your files never touch a cloud database. 👉 Try it here: https://pulldl.com/drop 2. Client-Side Video & Audio Processing (WASM) Instead of uploading gigabytes to a remote backend: Batch iPhone HEIC to JPG: Convert Apple HEIC photos instantly in-browser. Discord & Email Video Compressor: Two-pass smart visual encoding to fit video under 25MB or 8MB upload limits. Audio DSP Suite: Sub-bass 8D audio booster, audio joiner, and client-side vocal remover. 3. Universal Public Media Extractor Clean, watermark-free video and audio downloader supporting 1,357+ platforms (YouTube, TikTok, Reddit, Instagram, Facebook, etc.) in original resolutions up to 4K UHD. 🛠️ The Tech Stack Frontend: Next.js (App Router), React, TailwindCSS Media Engine: Client-side WebAssembly (WASM), Web Audio API, Canvas API Networking: WebRTC DataChannels + secure TURN/STUN fallback PWA Ready: Fully installable progressive web app with offline capabilities 🌐 Try it out & Give Feedback! The platform is 100% free with no sign-ups, subscriptions, or intrusive ads: 🔗 Live Platform: https://pulldl.com 🔗 File Drop: https://pulldl.com/drop I would love to get the Dev.to community’s feedback! What tools or features should I add next? Drop your thoughts in the comments below! 👇

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/mahean/i-built-a-zero-install-privacy-first-media-studio-airdrop-alternative-in-the-browser-pulldl-3n93

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
