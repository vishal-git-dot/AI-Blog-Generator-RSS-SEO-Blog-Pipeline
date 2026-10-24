---
title: "MPS backend out of memory: the "max allowed" number on every Mac size"
slug: "mps-backend-out-of-memory-the-max-allowed-number-on-every-mac-size"
author: "Rodion Kazennov"
source: "devto_python"
published: "Sat, 24 Oct 2026 20:02:36 +0000"
description: "The PyTorch error on a Mac carries one number that people search for. This one is from a 16 GB Mac ( AudioLDM2 #20 ): RuntimeError: MPS backend out of memory..."
keywords: "mac, gib, memory, set, ratio, reports, comfyui, mps"
generated: "2026-10-24T20:31:17.908313"
---

# MPS backend out of memory: the "max allowed" number on every Mac size

## Overview

The PyTorch error on a Mac carries one number that people search for. This one is from a 16 GB Mac ( AudioLDM2 #20 ): RuntimeError: MPS backend out of memory (MPS allocated: 18.02 GB, other allocations: 107.10 MB, max allowed: 18.13 GB). Tried to allocate 4.50 MB on private pool. In my earlier note I measured where it comes from on my 48 GB Mac. "max allowed" is PYTORCH_MPS_HIGH_WATERMARK_RATIO , 1.7 by default, times the GPU working set macOS recommends, which torch.mps.recommended_max_memory() returns. One machine can't tell you what that number is on the others, so I read it off other people's errors. Where the numbers come from On 24 October I searched GitHub for issues that quote the error with its "max allowed" value. That gave 250 issues and pull requests, 167 of them with a number in the text. Most values fall into a few groups, and where a reporter named their Mac's memory, the groups line up with the size. Divided by 1.7, each value gives the working set macOS gave the GPU on that machine. Mac memory max allowed, GiB GPU working set, GiB share of memory reports seen 8 GB 9.07 5.33 67 % 27 2023 – 2026 16 GB 18.13 10.67 67 % 18 2023 – 2026 24 GB 27.20 16.00 67 % 9 Jan 2025 – Jan 2026 24 GB 30.19 17.76 74 % 3 Dec 2025 – Sep 2026 32 GB 36.27 21.33 67 % 6 2024 – 2025 36 GB 45.90 27.00 75 % 3 2024 – 2026 48 GB 63.65 37.44 78 % 4, plus mine Sep – Oct 2026 64 GB 81.60 48.00 75 % 7 Dec 2023 – Apr 2025 64 GB 88.13 51.84 81 % 6 Mar – Oct 2026 128 GB 163.20 96.00 75 % 4 2024 – 2025 128 GB 182.78 107.52 84 % 2 Dec 2025 – Jan 2026 Older PyTorch versions label these numbers "GB" and newer ones "GiB". Both are the binary unit: 1.7 × two thirds × 16 GiB is exactly 18.13. What changed Until late 2025 the rule looks simple. macOS gave the GPU two thirds of memory on Macs up to 32 GB and three quarters above that. Reports from late 2025 on show larger shares on the 24 GB, 64 GB and 128 GB Macs. The three 64 GB reports that name their system all say macOS 26. The 8 and 16 GB values haven't moved. My own 48 GB Mac runs macOS 26.5.2 and returns 37.44 GiB, 78 %. Two limits on what this shows: the newer rows rest on two to six reports each, and I can't tell from them whether macOS or the chip made the difference. What it means when you see the error At the default ratio the limit is above physical memory on every row of the table: 1.7 × two thirds is 113 % of memory, and 1.7 × 84 % is 143 %. By the time a job reaches "max allowed", it has been swapping for a while. That matches my own measurement: on my Mac, swap began between 33.5 and 36 GB of footprint, far below the 63.65 GiB limit. The advice at the end of the error, a ratio of 0.0, removes the limit, so the job can swap further. If you'd rather get a clean error than a swapping Mac, set the limit below your memory, for example a ratio of 1.0, which is the working set itself. Set the low ratio with it: on PyTorch 2.14, a high ratio below 1.4 set on its own fails with "invalid low watermark ratio 1.4". PYTORCH_MPS_HIGH_WATERMARK_RATIO = 1.0 PYTORCH_MPS_LOW_WATERMARK_RATIO = 0.8 python your_script.py To see your own Mac's working set: import torch print ( torch . mps . recommended_max_memory () / 2 ** 30 , " GiB " ) The numbers that don't fit About a third of the reports show other limits, such as 1.70 GiB, 3.40 GiB, 6.77 GiB or 3.00 GiB. Those aren't the Mac's default. An app or a user set its own ratio or cap: one video tool caps MPS at 3 GiB even on a 128 GB Mac. Another 20 reports sit at 7.93, and I couldn't tie that value to one Mac size. If your number is far below the table, look in the tool's settings before you blame the Mac. Sources Two reports for each row. The full list of 167 is in the data file. 8 GB, 9.07: noScribe #84 , pytorch #105839 16 GB, 18.13: pinokio #941 , AudioLDM2 #20 24 GB, 27.20: pytorch #145374 , qwen3-optimizer-study #13 24 GB, 30.19: ml-bokeh #3 , ComfyUI #17264 (ratio 1.0, so 17.76) 32 GB, 36.27: ComfyUI-LivePortraitKJ #82 , instructlab #2568 36 GB, 45.90: ACE-Step-1.5 #282 48 GB, 63.65: trellis2-mlx #1 , ask-physics #24 64 GB, 81.60: bobo-fun #8 , ComfyUI-CogVideoXWrapper #312 64 GB, 88.13: EtherReel-releases #7 , ComfyUI #17309 128 GB, 163.20: ComfyUI #9308 , lm-evaluation-harness #1835 128 GB, 182.78: ComfyUI #11584 , ComfyUI-WanVideoWrapper #1856

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/nefayran/mps-backend-out-of-memory-the-max-allowed-number-on-every-mac-size-249e

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
