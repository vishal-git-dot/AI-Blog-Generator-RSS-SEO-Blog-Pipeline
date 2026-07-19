---
title: "Your LLM can't actually watch video. Here's the smallest fix (MIT)"
slug: "your-llm-cant-actually-watch-video-heres-the-smallest-fix-mit"
author: "Leo Huang"
source: "devto_python"
published: "Sun, 19 Jul 2026 03:01:16 +0000"
description: "Every model card says "multimodal". Then you hand the model a real video file and discover what that means in practice: ChatGPT reads the subtitle track, Cla..."
keywords: "video, real, model, claude, frames, llm, can, you"
generated: "2026-07-19T03:25:16.526181"
---

# Your LLM can't actually watch video. Here's the smallest fix (MIT)

## Overview

Every model card says "multimodal". Then you hand the model a real video file and discover what that means in practice: ChatGPT reads the subtitle track, Claude doesn't accept video files at all. The model narrates a video it mostly never saw. I unpack viral videos daily for my own content work, so I couldn't route around this. I built a small tool instead. The mechanism claude-real-video converts a video into three things an LLM can genuinely read: Scene-aware sampled frames — ffmpeg scene scores decide where to sample, so you get a frame when the picture changes, not every N seconds. An --adaptive flag handles slow deformations (a real user bug report: fixed thresholds missed squash/stretch morphs entirely). A timestamped transcript — whisper by default; if faster-whisper is installed it runs in-process and several times faster, with automatic fallback. One MANIFEST timeline — frames and transcript merged into a single file, so the model follows the video in order instead of guessing from fragments. A --text-anchors flag force-samples frames at subtitle cues so on-screen text never falls between frames. Then you point any LLM at the output folder — Claude, GPT, Gemini, or a local model. No API of mine in the middle, everything runs on your machine. Usage pip install claude-real-video crv "video.mp4" -o out Honest limitations Not real-time — a 90-second video takes about 1–2 minutes all-in on an M-series Mac. Frame sampling can still miss motion between frames; the flags above patch the worst cases, both born from real GitHub issues. It's MIT, currently at 1,731 stars with ~8k installs last month, which taught me the problem was never just mine: https://github.com/HUANGCHIHHUNGLeo/claude-real-video

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/huangchihhungleo/your-llm-cant-actually-watch-video-heres-the-smallest-fix-mit-2igp

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
