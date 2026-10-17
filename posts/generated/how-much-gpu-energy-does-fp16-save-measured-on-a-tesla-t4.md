---
title: "How much GPU energy does fp16 save? Measured on a Tesla T4"
slug: "how-much-gpu-energy-does-fp16-save-measured-on-a-tesla-t4"
author: "bsharma173860-oss"
source: "devto_python"
published: "Sat, 17 Oct 2026 15:00:10 +0000"
description: "How much GPU energy does fp16 actually save over fp32? Spec sheets give TDP and peak FLOPS, not joules per job, so I measured it on a Tesla T4 using the GPU'..."
keywords: "energy, gpu, torch, runs, joules, run, cuda, every"
generated: "2026-10-17T15:18:37.846879"
---

# How much GPU energy does fp16 save? Measured on a Tesla T4

## Overview

How much GPU energy does fp16 actually save over fp32? Spec sheets give TDP and peak FLOPS, not joules per job, so I measured it on a Tesla T4 using the GPU's own NVML energy counter. The job import sys , torch dtype = { " fp16 " : torch . float16 , " fp32 " : torch . float32 }[ sys . argv [ 1 ]] a = torch . randn ( 8192 , 8192 , device = " cuda " , dtype = dtype ) for _ in range ( 100 ): b = a @ a torch . cuda . synchronize () fp16 and fp32 runs alternate (so temperature and clock drift hit both sides), 5 measured runs each, medians reported, Mann-Whitney test between the two. Results: the whole job Setup fp16 fp32 GPU energy saved No cooling between runs 475 J, 8.6 s 2.53 kJ, 39.7 s 81.2% Every run starts at ≤65 °C 426 J, 7.8 s 2.21 kJ, 33.8 s 80.8% ≤65 °C + 3 warm-up runs 413 J, 8.4 s 2.50 kJ, 40.1 s 83.5% Same, a second session 392 J, 7.9 s 2.29 kJ, 36.1 s 82.9% p = 0.008 every time: every fp16 run beat every fp32 run. Results: just the matmuls Measuring inside the process, without Python start-up and CUDA set-up, 20 matmuls took about 73 J and 1.1 s in fp16 against about 486 J and 7.4 s in fp32: roughly 85% less GPU energy and 6.6× faster. import torch , joules with joules . Session ( gpus = [ 0 ]) as s : with s . phase ( " fp16 " ) as p : ... # your code print ( p . energy_j , p . duration_s ) Why the gap is so large The T4 is Turing: fp16 matmuls run on the tensor cores, but there is no TF32, so fp32 runs on the ordinary CUDA cores. Energy is power × time, so most of the saving comes from finishing sooner. fp32 also sat throttled 93% of the time at the T4's 70 W cap, against about 60% for fp16. On an A100, H100 or L4, fp32 matmuls can use TF32, so expect a much smaller gap there. Measure it rather than assume it. Run it yourself pip install -U landauer-gap joules compare --names fp16,fp32 --baseline fp32 --runs 5 --warmup 3 --cool-to 65 --gpus 0 \ "python3 bench.py fp16" "python3 bench.py fp32" Full write-up with power and throttling tables: https://wattops.dev/blog/fp16-vs-fp32-gpu-energy-t4 Disclosure: I built joules, the open-source CLI used here.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/bsharma173860oss/how-much-gpu-energy-does-fp16-save-measured-on-a-tesla-t4-4e08

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
