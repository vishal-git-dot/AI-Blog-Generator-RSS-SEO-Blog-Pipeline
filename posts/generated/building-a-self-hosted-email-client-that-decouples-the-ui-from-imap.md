---
title: "Building a Self-Hosted Email Client That Decouples the UI from IMAP"
slug: "building-a-self-hosted-email-client-that-decouples-the-ui-from-imap"
author: "Maksim Ramzaev"
source: "devto_webdev"
published: "Wed, 01 Jul 2026 09:48:09 +0000"
description: "Full disclosure: I'm the developer of RMS Mail. This is my own project, not a recommendation of someone else's tool. The problem that started it all A few mo..."
keywords: "mail, imap, self, hosted, rms, all, multi, storage"
generated: "2026-07-01T09:59:55.960302"
---

# Building a Self-Hosted Email Client That Decouples the UI from IMAP

## Overview

Full disclosure: I'm the developer of RMS Mail. This is my own project, not a recommendation of someone else's tool. The problem that started it all A few months ago I ran into a stupid problem. My Mac only has a 512GB SSD, while I have around twenty email accounts with years of archived mail. Buying a larger Mac or external storage felt like the wrong solution. Storage on a VPS is dramatically cheaper, so I started looking for a self-hosted mail client. I've been a sysadmin for 15+ years and currently run my own hosting business — about a dozen servers, mine and clients'. So I went through the usual self-hosted options: Roundcube, SnappyMail, Stalwart, the rest of the list. Most felt like software from another era. The newer ones required surprisingly heavy infrastructure, and almost all of them had the same architectural habit — IMAP sits at the center of the app. The real bottleneck wasn't storage Then I realized storage wasn't actually the problem. The real bottleneck was architecture — every search, every bulk operation, every folder switch depended on a remote mail server. The UI wasn't slow because JavaScript was slow. It was slow because every action waited for IMAP. Instead of optimizing that model, I built a different one. IMAP as a sync layer, not the backbone RMS Mail treats IMAP as a synchronization layer. The UI never queries IMAP directly. Mail syncs into a local database where indexing, full-text search, threading, and bulk operations happen independently of the mail server. IMAP's only job is keeping data in sync; the application handles everything else. In practice: searching large archives, moving thousands of messages, and background sync all happen against the local index, with no IMAP round-trip in the critical path. Tech stack Backend : Go Frontend : Next.js Storage : SQLite (single-mailbox edition) or PostgreSQL + Redis + Asynq (multi-account/heavy workloads) Distribution : Docker images — ~73MB frontend, ~19MB backend Runtime memory footprint: Single-mailbox edition (SQLite, no Postgres/Redis): ~90MB total Multi-account/Postgres-backed editions: ~370–700MB, mostly Postgres being Postgres Three editions, one architecture Self-hosted means different things depending on who's running it, so RMS Mail ships as three editions on the same core: Mono (free) — A modern Roundcube replacement. Multi-user webmail for a single domain: each person logs into their own account. SQLite, no external dependencies, starts in under a minute. Mono Pro (paid) — Same multi-user model as Mono, scaled up with Postgres, Redis, and Asynq for heavy, long-term workloads. Unified (freemium) — A genuinely different model: not multi-user, but multi-account for a single person. One workspace, many mailboxes — built for managing ~20 accounts myself, with a combined inbox and project groups. Optional AI features Since this tends to be the first thing self-hosted/privacy-focused folks ask about: RMS Mail includes optional summarization, categorization, translation (45 languages), and a chat interface that can drive the app's processes in plain text. There's also a Telegram integration (control your inbox from chat) and an MCP integration (control it from your IDE). All of it is opt-in — bring your own API key (9 providers supported) or point it at a local Ollama instance. A single environment variable strips every AI-related code path and UI element if you don't want it at all. On the source code Worth being upfront about: the source is closed. All three editions ship as Docker images, not as public repositories. I know that's a harder sell in self-hosted circles specifically, where open source is often the default expectation — happy to discuss the reasoning, or hear whether that's a dealbreaker for people who'd otherwise want this. Where things stand The project is a few months old and actively developed — 11 releases so far, all three editions at stable status. Current priorities: core stability, multi-gigabyte mailbox performance, low-latency search, and infrastructure reliability. Repo (deployment files, Docker Compose configs, documentation): github.com/max-ramas/rms-mail-public Product page: rms-ds.com/en/products/rms-mail I'd especially like feedback from people managing large mailboxes or running self-hosted infrastructure themselves. If you think I solved something the wrong way, I want to hear why.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/maxramas/building-a-self-hosted-email-client-that-decouples-the-ui-from-imap-4bcn

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
