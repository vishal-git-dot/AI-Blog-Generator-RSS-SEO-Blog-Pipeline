---
title: "GoyGram — one Python runtime for both Telegram Bot API and MTProto, with a Rust core and OpSec-first sessions"
slug: "goygram-one-python-runtime-for-both-telegram-bot-api-and-mtproto-with-a-rust-core-and-opsec-first-sessions"
author: "sam Sepiol"
source: "devto_python"
published: "Sun, 30 Aug 2026 20:12:15 +0000"
description: "GoyGram is a Telegram framework for Python. It runs both of Telegram's protocols — Bot API and MTProto — in a single asyncio runtime, and moves crypto and TL..."
keywords: "goygram, one, python, both, telegram, bot, rust, aes"
generated: "2026-08-30T20:50:18.008877"
---

# GoyGram — one Python runtime for both Telegram Bot API and MTProto, with a Rust core and OpSec-first sessions

## Overview

GoyGram is a Telegram framework for Python. It runs both of Telegram's protocols — Bot API and MTProto — in a single asyncio runtime, and moves crypto and TL serialization into a compiled Rust extension. The dual-transport problem aiogram and python-telegram-bot are Bot API only. telethon and pyrogram are MTProto only. GoyGram runs both in one process, one loop, one dispatcher — the transport is picked per operation, and one handler serves both protocols. The Rust core AES-256-IGE and AES-256-GCM run in Rust (LTO, opt-level=3). Benchmarks on one VPS, Python 3.11: cold import: 87 ms (aiogram 3.1 s, pyrogram 477 ms, telethon 298 ms) RSS after import: 12 MB (aiogram 152 MB) AES-256-IGE: 113 MB/s (telethon default 12 MB/s) Zero-overhead dynamic dispatch Methods resolve from the TL schema at load time — no hundreds of generated model files. Raw fields are read lazily. OpSec-first sessions Sessions live in an AES-256-GCM vault keyed to machine-id, keys are zeroized from memory on logout, and login is terminal-only (QR / phone / 2FA) — no token ever touches a browser or desktop client. The rest Multi-session, filters, FSM state machines, transport routing, and an event pipeline. Repo: https://github.com/GoyGram/GoyGram Docs: https://goygram.github.io License: AGPL-3.0

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/sam_sepiol_b877bcc20da75b/goygram-one-python-runtime-for-both-telegram-bot-api-and-mtproto-with-a-rust-core-and-48na

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
