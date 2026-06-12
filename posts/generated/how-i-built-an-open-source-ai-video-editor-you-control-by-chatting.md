---
title: "How I built an open-source AI video editor you control by chatting"
slug: "how-i-built-an-open-source-ai-video-editor-you-control-by-chatting"
author: "Boran Oktay DABAK"
source: "devto_python"
published: "Fri, 12 Jun 2026 15:23:31 +0000"
description: "A few months ago I had a folder full of long videos — podcast recordings, talks, screen recordings — and one simple goal: turn them into short vertical clips..."
keywords: "you, your, video, captions, tool, make, transcript, key"
generated: "2026-06-12T15:28:32.966851"
---

# How I built an open-source AI video editor you control by chatting

## Overview

A few months ago I had a folder full of long videos — podcast recordings, talks, screen recordings — and one simple goal: turn them into short vertical clips with captions. Every tool I tried wanted me to either drag clips around a timeline for an hour, or upload my raw footage to someone's cloud and pay per export. So I built my own, and I just open-sourced it. It's called VibeClip, and the core idea is simple: you edit by typing what you want . What it does You drop in a long video and it cuts it into vertical 9:16 shorts with word-synced captions. Then you refine each clip by chatting: cut the silences make it mrbeast style split it and add gameplay underneath make the captions bigger and yellow undo No timeline scrubbing. You describe the edit, it happens. The architecture Three pieces: 1. Transcription — faster-whisper (local). Everything starts with an accurate word-level transcript. faster-whisper runs on your own machine, needs no API key, and gives per-word timestamps that are the backbone of both caption sync and silence detection. 2. The "brain" — an LLM (your key). This is the only thing that touches the network. The model does two jobs: scoring the strongest moments in the transcript (hook / flow / value, not a keyword scan), and turning a plain-language request like "make it punchier" into a sequence of concrete edit actions. 3. Rendering — ffmpeg (local). Every cut, 9:16 reframe, caption burn, zoom and audio duck is an ffmpeg operation. No cloud render farm. The chat layer is a tool-calling agent. When you type "cut the silences" the model never touches the video — it calls a tool that operates on the transcript timestamps, and the actual pixels are produced by replaying cached intermediates through ffmpeg. One undo reverts a whole multi-step plan, because every mutation is a snapshot. Decisions I'd make again Bring-your-own-key. VibeClip never ships with an API key. You plug in OpenAI, Gemini, Claude, DeepSeek, or point it at any OpenAI-compatible endpoint (Ollama, LM Studio). I'm not a proxy taking a cut of every render, and there's no lock-in — when a cheaper model drops you switch one line in .env. Local-first. A video tool sees your unreleased footage. "Trust me, we delete it" isn't a great pitch. Transcription and rendering both run on your machine; the only thing that leaves is the transcript text you send to your own LLM. AGPL, not MIT. If someone runs a modified version as a hosted service, the improvements have to come back to the commons. A paid hosted version may come later for people who don't want to self-host, but the open tool is the real product, not a teaser. Things that were harder than expected Caption sync. Whisper word timestamps are good but not perfect; landing captions on the right frame after silence-removal cuts meant treating the transcript timeline as the single source of truth and deriving the video from it, never the other way around. Multi-provider JSON. OpenAI's json_object response format is silently ignored by some providers and errors on others. The fix: only send it where it's supported, and tolerantly parse fenced/prose-wrapped JSON everywhere else. No libass on some ffmpeg builds , so captions are rendered with Pillow and overlaid instead of relying on the subtitle filter. Try it It's a docker compose up away, or run it with uv / pip. You only add one LLM key. Repo: https://github.com/oktaydbk54/vibeclip Site: https://vibeclip.dev It's early and rough in places. If you self-host AI tools or make short-form content, I'd genuinely love your feedback — and PRs and issues are very welcome.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/oktaydbk54/how-i-built-an-open-source-ai-video-editor-you-control-by-chatting-1k37

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
