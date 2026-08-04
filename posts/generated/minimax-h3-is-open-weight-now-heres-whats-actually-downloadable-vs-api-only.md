---
title: "MiniMax H3 Is Open-Weight Now — Here's What's Actually Downloadable vs API-Only"
slug: "minimax-h3-is-open-weight-now-heres-whats-actually-downloadable-vs-api-only"
author: "RouteAI"
source: "devto_ai"
published: "Tue, 04 Aug 2026 08:33:48 +0000"
description: "MiniMax released H3, a general-purpose multimodal video generation system, on July 31, and confirmed shortly after that the weights are open — live on Huggin..."
keywords: "video, open, minimax, model, not, generation, text, image"
generated: "2026-08-04T08:46:37.699999"
---

# MiniMax H3 Is Open-Weight Now — Here's What's Actually Downloadable vs API-Only

## Overview

MiniMax released H3, a general-purpose multimodal video generation system, on July 31, and confirmed shortly after that the weights are open — live on Hugging Face as MiniMaxAI/MiniMax-H3, with a ComfyUI-repackaged mirror shipping native support the same day. Important upfront: the open-weight license reportedly excludes the EU, UK, South Korea, and the United States from its applicable territory. Commercial use elsewhere is free but requires displaying "MiniMax H3" in your product UI, and revenue above $20M/year needs separate written authorization. If you're in one of the excluded regions, check the license on the Hugging Face model card directly before planning to use this — don't take a secondhand summary (including this one) as the final word on your specific situation. What's actually open vs. what stays API-only: the system has three layers — a hosted preprocessing/orchestration layer (Context-IR) that stays behind MiniMax's API, the core generator (H3-Base) which is what's open-sourced, and a 2K regeneration pass (Regenerate-2K) that also stays API-hosted. So "open-sourced" here means the core generator, not the full commercial pipeline. The technical specifics, for anyone evaluating whether this is runnable on their own hardware: it's a 33B dense single-stream Transformer, shipped as two task-specific checkpoints — fl2va (text/image-driven generation) and ref2va (reference-driven generation) — around 21GB each in their smallest quantized form. Full precision runs about 123.6GB; the smallest working combination is reportedly around 42.5GB. ComfyUI's own guidance suggests a 12GB card plus CPU offloading can run it, though expect that to be a slow, not snappy, experience. Native local generation is 768px on the short edge — the 2K output comes from a separate in-context regeneration pass that isn't part of the open weights. Rough shape of getting it running (check the official model card for exact, current commands — this is illustrative, not copy-paste-guaranteed given how fast these release details can shift): from huggingface_hub import snapshot_download # Download only the checkpoint you actually need — # fl2va for text/image-driven generation, ref2va for reference-driven snapshot_download( repo_id="MiniMaxAI/MiniMax-H3", allow_patterns=["fl2va/*"], # or "ref2va/*" local_dir="./minimax-h3" ) # From here, follow the model card's specific inference instructions — # this is a 33B video model, not a drop-in chat completion call, # and exact loading code depends on which runtime (ComfyUI, diffusers-style # pipeline, etc.) you're using. Why the release got attention beyond "another model dropped": Artificial Analysis reportedly ranked H3 #1 in video editing and top-three in both text-to-video and image-to-video, and noted that releasing the weights would make it the leading open-weight model in the category by a clear margin (Artificial Analysis, July 2026). Worth balancing that against the same benchmark reportedly showing H3 trailing Gemini Omni Flash in text-to-video, and behind both Seedance 2.0 and Gemini Omni Flash in image-to-video (South China Morning Post, July 2026) — it's a strong result in one specific category (editing), not a clean sweep. TL;DR: MiniMax open-sourced H3's core generator (not the full hosted pipeline) — a 33B video generation model that understands text/image/video/audio together and outputs video with native audio. Strong specifically at video editing per third-party benchmarks, not uniformly #1 everywhere. License excludes the EU, UK, South Korea, and US — check the official terms before planning commercial use. To learn more, please visit： RouteAI

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/routeai_official/minimax-h3-is-open-weight-now-heres-whats-actually-downloadable-vs-api-only-441k

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
