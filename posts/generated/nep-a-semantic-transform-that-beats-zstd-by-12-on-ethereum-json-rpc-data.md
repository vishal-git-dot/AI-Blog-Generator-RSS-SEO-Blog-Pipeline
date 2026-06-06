---
title: "NEP: A Semantic Transform That Beats zstd by 12% on Ethereum JSON-RPC Data"
slug: "nep-a-semantic-transform-that-beats-zstd-by-12-on-ethereum-json-rpc-data"
author: "Lourens Wasserman"
source: "devto_python"
published: "Sat, 06 Jun 2026 03:15:58 +0000"
description: "If you've ever looked at what Ethereum JSON-RPC responses actually contain, you'll notice most of the data is structured waste: hex strings that could be raw..."
keywords: "zstd, nep, ethereum, json, blocks, block, compression, stage"
generated: "2026-06-06T04:00:30.106656"
---

# NEP: A Semantic Transform That Beats zstd by 12% on Ethereum JSON-RPC Data

## Overview

If you've ever looked at what Ethereum JSON-RPC responses actually contain, you'll notice most of the data is structured waste: hex strings that could be raw bytes, field names repeated thousands of times per block, addresses appearing dozens of times in full 42-character form. NEP (Neurop Encoding Protocol) is a deterministic 4-stage binary transform that cleans all of this up before zstd runs. The result: 12% better compression than plain zstd, 200/200 block wins, fully lossless. What it does Ethereum JSON → NEP encode → zstd → storage Ethereum JSON ← NEP decode ← zstd ← storage Four stages, each targeting a specific source of bloat: | Stage | What it removes | |---|---| | Hex → binary | Every "0x..." field halved in size | | Schema stripping | JSON keys replaced with 2-byte IDs | | Address deduplication | 42-char addresses → 2-byte index on repeat | | Delta encoding | Numeric sequences compressed to deltas | After these 4 stages the binary blob is ~46% of the original JSON size — before zstd even starts. Results Tested on 200 real mainnet blocks, all consecutive, fetched live: | Method | Mean ratio | vs zstd | Lossless | |---|---|---|---| | zstd-9 | 5.71x | baseline | — | | NEP + zstd-9 | 6.18x | +8% | 200/200 ✓ | | NEP + zstd + dict | 6.38x | +11.7% | 200/200 ✓ | Every single block. Every output round-trip verified. The NeuropBlocks angle The interesting part: I rebuilt the entire NEP pipeline using 5 general-purpose composable primitives from the NeuropBlocks library instead of the hand-written encoder. Same results, zero custom code: hex_decode — hex strings → raw bytes deduplicate_by — address lookup table delta_encode — 7 numeric sequences delta_decode — lossless verification pack_integers — tx type bits into 4-bit slots NeuropBlocks + zstd-22 beats the dedicated encoder at high compression levels (20/20 blocks, +5.14% including 112KB dictionary overhead). General primitives composing to outperform a purpose-built tool. ## Reproduce it yourself No API key. No pre-built files. Fetches live mainnet data. bash # Clone git clone https://github.com/Louw115/nep-ethereum-compression cd nep-ethereum-compression # Install pip install zstandard brotli # Run (fetches real blocks, prints per-block table, saves results) python nep_reproduce.py # Or run the composable blocks demo python nep_blocks_demo.py Runs in three stages (20 / 100 / 200 blocks). Each stage prints a full per-block table with raw bytes, ratio, and lossless flag. Cache builds progressively — Stage 2 only fetches the delta blocks. At scale At Ethereum's current chain size (~800 TB): Plain zstd: ~141 TB NEP + zstd + dict: ~127 TB ~14 TB saved. At $0.02/GB object storage that's ~$280K on the existing chain alone, before bandwidth savings on live RPC responses. The chain grows ~80 GB/day. Repo: github.com/Louw115/nep-ethereum-compression Happy to answer questions on methodology or the NeuropBlocks composition approach in the comments.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/lbwasserman/nep-a-semantic-transform-that-beats-zstd-by-12-on-ethereum-json-rpc-data-3am5

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
