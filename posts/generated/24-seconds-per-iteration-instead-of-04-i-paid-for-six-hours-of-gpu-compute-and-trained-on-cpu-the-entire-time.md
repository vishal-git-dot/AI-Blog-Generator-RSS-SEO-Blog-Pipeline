---
title: "24 seconds per iteration instead of 0.4. I paid for six hours of GPU compute and trained on CPU the entire time."
slug: "24-seconds-per-iteration-instead-of-04-i-paid-for-six-hours-of-gpu-compute-and-trained-on-cpu-the-entire-time"
author: "Francisco Booth"
source: "devto_python"
published: "Sun, 06 Sep 2026 10:22:30 +0000"
description: "Failure 1 — CUDA silently fell back to CPU My training job launched on Vast.ai and ran to completion. Iteration time was 24 seconds instead of 0.4 seconds. C..."
keywords: "computefence, before, gpu, disk, had, training, pod, cache"
generated: "2026-09-06T10:39:35.962729"
---

# 24 seconds per iteration instead of 0.4. I paid for six hours of GPU compute and trained on CPU the entire time.

## Overview

Failure 1 — CUDA silently fell back to CPU My training job launched on Vast.ai and ran to completion. Iteration time was 24 seconds instead of 0.4 seconds. CUDA had fallen back to CPU silently. PyTorch logged nothing. I had been billed for six hours of GPU compute while training on an unaccelerated CPU thread the entire time. Failure 2 — HF_HOME on ephemeral disk Every fresh pod re-downloaded base model weights to /root/.cache — the ephemeral container disk wiped on pod shutdown. Same download, same cost, every run. The fix is one line. I did not know it for weeks. export HF_HOME=/workspace/.cache/huggingface Failure 3 — Accelerate config mismatch My accelerate config had num_processes: 2. The pod had one GPU. Training launched, appeared to run, and produced garbage output. No error thrown. The configuration simply did not match the hardware. Failure 4 — Dirty dataset 28,432 duplicate rows. 312 conflicting labels. Loss collapsed to 0.693 on step one — the exact cross-entropy value for random guessing on a binary classification problem. I spent three days debugging model architecture and learning rates before I scanned the dataset. The pattern None of these printed an exception. All of them were visible before python train.py if I had known what to check. I spoke to 13 ML engineers on RunPod, Vast.ai, and AWS. Nine had lost checkpoints to ephemeral disk. Eight had shipped silent garbage with no log error. An ML engineer at a major German industrial company told me his team maintains a five or six part manual bash script that they run before every GPU job because no standardised tool exists. When enterprise teams are hand-rolling bash scripts, the problem is real. So I built ComputeFence. Standard install: pip install computefence computefence doctor Zero install on a fresh pod: uvx computefence doctor 30 seconds. Every warning prints the exact fix command. ComputeFence v0.2.5 — Pre-flight diagnostic ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2 WARNINGS · 0 BLOCKERS · 3 PASSED Storage ⚠ HF_HOME is not set — model weights will cache to ephemeral disk Fix: export HF_HOME=/workspace/.cache/huggingface ⚠ Root disk (/) — 14.3 GB free (below 20 GB) Fix: Free up disk or move checkpoints: df -h to check usage ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2 warning(s) found. Review before launching. It checks GPU and CUDA visibility, HuggingFace cache path persistence, Accelerate GPU count versus what is actually on the instance, disk headroom for checkpoints, and checkpoint output directory persistence via --output-dir. It does not check training script correctness, learning rate safety, or anything that only fails during the run. HuggingFace cache and your checkpoint output directory are separate paths — fixing one does not fix the other. ComputeFence catches configuration mistakes before the GPU starts billing. Add it to your pod startup script. Exit code is 0 on warnings and 1 only on hard blockers so training will still launch on warnings: pip install computefence && computefence doctor && python train.py Does it catch anything real? Three operators have run it before paid training jobs on RunPod. One caught HF_HOME writing to ephemeral disk and an Accelerate config mismatch on a RunPod A100. He fixed both before launch. One confirmed the storage warning matched real pod behaviour and said he would not have caught it without the tool. Aaron, an ML engineer who ran ComputeFence on a RunPod A40, said the Accelerate warning would have made him stop and investigate before launching. Still very early. If you run it before your next paid job on RunPod, Vast.ai, Lambda Labs, or any bare metal instance — paste your computefence doctor output in the comments or open an issue on GitHub. I want to know which checks fire on real setups and which are noise. Free. MIT licensed. Works on any bare metal GPU provider. GitHub: github.com/Francisco-Booth/ComputeFence

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/franciscobooth/24-seconds-per-iteration-instead-of-04-i-paid-for-six-hours-of-gpu-compute-and-trained-on-cpu-the-3p41

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
