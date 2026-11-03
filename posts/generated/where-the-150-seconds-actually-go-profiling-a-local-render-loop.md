---
title: "Where the 150 seconds actually go: profiling a local render loop"
slug: "where-the-150-seconds-actually-go-profiling-a-local-render-loop"
author: "mujin"
source: "devto_python"
published: "Tue, 03 Nov 2026 13:33:30 +0000"
description: "I generate on a 4GB GTX 1650, SD1.5 in fp32 with model offload. One 512x768 image takes about 150 seconds. That number is useless on its own — it tells me no..."
keywords: "time, loop, not, per, one, load, seconds, encode"
generated: "2026-11-03T13:55:05.591156"
---

# Where the 150 seconds actually go: profiling a local render loop

## Overview

I generate on a 4GB GTX 1650, SD1.5 in fp32 with model offload. One 512x768 image takes about 150 seconds. That number is useless on its own — it tells me nothing about what to change. So I timed the loop in pieces. Splitting the 150 seconds into model load, sampling steps, and PNG encode The first version is a stopwatch and a cProfile dump, wrapped around the three phases I care about. It fits in a screen: import cProfile , pstats , time , io from PIL import Image def timed ( pipe , prompt , seed , out ): t = {} t [ " load " ] = time . perf_counter () pipe . enable_model_cpu_offload () t [ " load " ] = time . perf_counter () - t [ " load " ] t [ " sample " ] = time . perf_counter () img = pipe ( prompt = prompt , width = 512 , height = 768 , generator = torch . Generator (). manual_seed ( seed )). images [ 0 ] t [ " sample " ] = time . perf_counter () - t [ " sample " ] t [ " encode " ] = time . perf_counter () img . save ( out , format = " PNG " ) t [ " encode " ] = time . perf_counter () - t [ " encode " ] return t pr = cProfile . Profile () pr . enable () t = timed ( pipe , prompt , seed , " out.png " ) pr . disable () print ( t ) pstats . Stats ( pr ). sort_stats ( " cumulative " ). print_stats ( 15 ) On my card the split comes out roughly as: model load and offload setup takes a noticeable slice, sampling dominates, PNG encode is small but not zero. I am not going to quote a breakdown I did not log per-phase — what matters is that the stopwatch gives you three numbers instead of one, and cProfile names the function inside the dominant phase. What the profile changed Two fixes actually cut wall-clock: One: stop reloading the model. The load phase was being paid every run because the script was re-entered fresh. Keeping the pipe alive across the loop and only offloading weights between calls removed the repeated setup cost from every image after the first. Two: fix the sampling call, not the sampler. The cumulative profile put the time inside the denoise loop, which is expected. The real change was making the loop's inputs stable — same resolution, same step count, no per-call resizing — so the offload pattern stopped thrashing between CPU and GPU. The 150 seconds is the floor I accept at 512x768 fp32; I stopped trying to shave the loop itself and started removing everything around it. The "optimization" that only moved cost to disk: caching intermediate latents and re-encoding. cProfile stopped attributing time to sampling and started attributing it to file writes. Wall-clock barely changed. I reverted it. If a change moves time from the sampler to the disk without lowering the total, it is bookkeeping, not speed. The single per-run number worth writing to a file Per image, append one line: seed, wall_seconds, phase_split . That is it. Not loss, not step count — wall seconds and where they went. The reason is the 77 pieces I generated and pinned. At one line per run, a slow week shows up as a drift in that column before I have to guess why. If the sampling phase grows, it is the loop or the hardware. If load grows, it is the environment. If encode grows, it is the disk. One number, three phases, and the trend is visible without a session of re-profiling. The rest of the pipeline — the ERC-721, hand-built Seaport listings, the restock daemon, the fact-gated copywriter, the ~271-test suite — does not need this number, but the render loop is the only part I cannot make faster by writing better code, so it is the only part I measure every run. The collection this feeds is live at https://thunderous-sunflower-a910b4.netlify.app — 7 of 77 minted, 70 to go, 5 per wallet, mint at 0.00063 ETH on Base, preload about 0.0000008 ETH per piece. Takeaway for today: add a one-line CSV append to your render loop that records wall seconds per phase. It costs a few lines and turns "why was this week slow" into a column you can read.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/mujin/where-the-150-seconds-actually-go-profiling-a-local-render-loop-4akb

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
