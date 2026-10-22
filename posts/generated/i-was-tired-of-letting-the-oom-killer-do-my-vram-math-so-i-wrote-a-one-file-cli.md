---
title: "I was tired of letting the OOM killer do my VRAM math, so I wrote a one-file CLI"
slug: "i-was-tired-of-letting-the-oom-killer-do-my-vram-math-so-i-wrote-a-one-file-cli"
author: "TECHDEV"
source: "devto_python"
published: "Thu, 22 Oct 2026 04:00:04 +0000"
description: "My workflow for trying a new local model used to be: download 4 GB, watch the progress bar, then read failed to allocate 3412 MiB like it was a fortune cooki..."
keywords: "file, ggufit, only, one, model, weights, cache, count"
generated: "2026-10-22T04:08:58.349199"
---

# I was tired of letting the OOM killer do my VRAM math, so I wrote a one-file CLI

## Overview

My workflow for trying a new local model used to be: download 4 GB, watch the progress bar, then read failed to allocate 3412 MiB like it was a fortune cookie. The math that would have saved me fits on a napkin — weights, plus KV cache, plus overhead — but nobody does it before downloading, because the tools that do it live in a browser tab and want you to type in the parameter count by hand. The file is sitting right there on your disk. It knows its own parameter count. So I wrote ggufit : one Python file, standard library only, no install. Point it at a .gguf file and it reads the actual header — tensor table, quantization types, layer count, KV heads — and answers the only question that matters: $ python3 ggufit.py llama-3.1-8b-q4_k_m.gguf --gpu "RTX 4060" ... Verdict: TIGHT — only 0.14 GB headroom; one Chrome tab away from OOM Two things most calculators get wrong, fixed here: KV cache is not a footnote. At 32k context, an 8B model's KV cache costs as much as its weights. ggufit computes it from the real architecture (GQA-aware, so small-kv-head models get the smaller number they deserve). Your 8 GB card doesn't have 8 GB free. The database compares against usable VRAM after driver/display/OS reserve, not the number on the box. Haven't downloaded the model yet? That's the best use case: $ python3 ggufit.py --params 8B --quant q4_k_m --ctx 32768 --gpu "RTX 4060" Verdict: WON'T FIT — short by 3.36 GB try: shorten context to ~5160 tokens (7.39 GB total) try: offload ~80% of layers to CPU/RAM (keep ~6 of 32 on GPU) It also does --table (verdict against every card in the DB), --json with exit code 2 on won't-fit so you can chain it in front of llama-server , and --list-gpus . The weights number is measured from the file; everything estimated is labeled as estimated, because a guess wearing a lab coat is still a guess. Repo: https://github.com/techdevfun/ggufit — MIT, PRs welcome, especially new cards for the database (vendor spec sheet numbers only, please).

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/techdevfun/i-was-tired-of-letting-the-oom-killer-do-my-vram-math-so-i-wrote-a-one-file-cli-4lge

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
