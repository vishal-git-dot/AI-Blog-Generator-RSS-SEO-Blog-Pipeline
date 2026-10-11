---
title: "What is tonGues? A language-exchange messenger with live translation"
slug: "what-is-tongues-a-language-exchange-messenger-with-live-translation"
author: "Frank Milvus"
source: "devto_webdev"
published: "Sun, 11 Oct 2026 12:24:12 +0000"
description: "tonGues is a language-exchange messenger. You chat the way you normally would, and the app translates and transcribes messages in the background — so you and..."
keywords: "language, one, you, messages, what, tongues, exchange, messenger"
generated: "2026-10-11T12:27:52.114067"
---

# What is tonGues? A language-exchange messenger with live translation

## Overview

tonGues is a language-exchange messenger. You chat the way you normally would, and the app translates and transcribes messages in the background — so you and someone who speaks a different language can keep a real conversation going. This is a quick tour of what it does and how it's built. What "language exchange" means here Most messengers assume everyone shares a language. A language-exchange app flips that assumption: the point is that you don't share one. You write in your own language, the other person reads it in theirs, and the original is always one tap away. What it does 💬 Real-time chat — one-to-one and group conversations over WebSockets. 🎙️ Voice and video calls — with background ringing and call notifications. 📷 Rich messages — photos, voice notes, video, and files. 🔤 Live translation — read incoming messages in your own language. 📝 Transcription — turn voice messages into searchable text. ✏️ The usual messenger toolkit — edit, react, reply, forward, pin, search, plus friends and presence statuses. 🖥️ Everywhere — Android, iOS, Windows, macOS and Linux from one Flutter codebase. How it's built Client: Flutter (Dart) — a single codebase for mobile and desktop. Backend: FastAPI + PostgreSQL, with Redis for realtime and presence, object storage for media, and small AI services for speech and translation. Realtime: a WebSocket layer that fans messages out and degrades gracefully when a connection blips. Why we're building in public Building a messenger is mostly about the unglamorous parts — reconnects, delivery guarantees, media uploads that survive a flaky network. We write those up, one change at a time, on our blog and on dev.to. If that's your kind of thing, follow along. 👋 Links App write-ups: https://frankmilvus.github.io/tongues-articles/ dev.to: https://dev.to/frankmilvus — the tonGues team

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/frankmilvus/what-is-tongues-a-language-exchange-messenger-with-live-translation-noj

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
