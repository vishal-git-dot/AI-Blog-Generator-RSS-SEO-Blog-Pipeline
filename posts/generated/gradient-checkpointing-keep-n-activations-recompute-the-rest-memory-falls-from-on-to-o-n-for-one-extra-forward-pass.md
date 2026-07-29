---
title: "Gradient checkpointing: keep N activations, recompute the rest — memory falls from O(N) to O( N) for one extra forward pass"
slug: "gradient-checkpointing-keep-n-activations-recompute-the-rest-memory-falls-from-on-to-o-n-for-one-extra-forward-pass"
author: "Devanshu Biswas"
source: "devto_python"
published: "Wed, 29 Jul 2026 18:59:12 +0000"
description: "Train a deep network and the thing that blows up your VRAM usually isn't the weights — it's the activations . Backprop needs every layer's forward output to ..."
keywords: "segment, forward, recompute, memory, gradient, activations, only, one"
generated: "2026-07-29T19:24:36.663598"
---

# Gradient checkpointing: keep N activations, recompute the rest — memory falls from O(N) to O( N) for one extra forward pass

## Overview

Train a deep network and the thing that blows up your VRAM usually isn't the weights — it's the activations . Backprop needs every layer's forward output to compute that layer's gradient, so the naive training step stores all of them, and activation memory grows as O(N) with depth (and with batch size, and with sequence length). Gradient checkpointing trades a little compute for a lot of that memory: keep only a handful of activations and recompute the rest on demand during the backward pass. It changes nothing about the math — the gradients and trained weights come out bit-for-bit identical — only the memory schedule. I built a demo that computes the whole trade live. Here's the idea. Backprop needs the forward activations The chain rule for a layer's weight gradient contains that layer's input. For y = W·x , dL/dW = dL/dy · xᵀ — you literally need x at backward time. So the naive pass keeps a tape of every activation: acts = [] h = x for layer in layers : h = layer ( h ) acts . append ( h ) # keep EVERY activation -> O(N) memory The trade: throw them away, recompute on demand Split the net into segments and store only the segment boundaries — the checkpoints . Run the interior forward under no_grad so nothing is retained, then re-run that segment's forward during the backward pass, when the values are actually needed. with torch . no_grad (): # forward WITHOUT storing interior activations h = segment ( x ) # ...later, in backward, when we need them: h = segment ( x_checkpoint ) # RECOMPUTE on demand (graph on this time) Compute is cheap and parallel; memory is scarce — so trading a few microseconds of recompute to free a tensor for the whole step is a win. The segment mechanism The backward loop walks segments in reverse, recomputing one at a time from its stored checkpoint. Because only the current segment's activations are ever materialised, only one segment's worth is alive at once — and that's the entire saving. for k in reversed ( range ( len ( segs ))): h = checkpoints [ k ]. detach (). requires_grad_ () out = segs [ k ]( h ) # recompute this segment (graph built now) out . backward ( grad ) # backprop through it only grad = h . grad # hand the gradient to the previous segment Why √N — minimize s + N/s At any instant you're holding the s stored checkpoints plus the N/s interior activations of the segment being recomputed. So peak memory is s + N/s , and minimizing it is one derivative: # d/ds (s + N/s) = 1 − N/s² = 0 -> s = √N -> peak ≈ 2√N peak ( 64 , 8 ) # 16 sqrt(64) segments -> O(√N), a 4× cut peak ( 64 , 64 ) # 65 store all -> O(N) peak ( 64 , 1 ) # 65 store none -> one huge segment, still O(N) Both extremes cost ~N; only the middle collapses. N=64 drops from 64 to 16 units; N=10,000 drops from 10,000 to ~200 — a 50× cut, and the deeper the net the bigger the win. The cost is one extra forward pass: recompute roughly doubles the forward work, and since backward already costs ~2× a forward, a step goes from ~3 to ~4 forward-equivalents — about +30% wall-clock (Chen et al., 2016). What you'd actually ship You don't hand-roll the reverse loop. PyTorch wraps a block with checkpoint , splits a Sequential into ~√N segments with checkpoint_sequential , and HuggingFace exposes model.gradient_checkpointing_enable() . The one correctness rule: recompute must reproduce the forward exactly, so seed or freeze anything random — dropout, batch-norm stats — or pass use_reentrant=False . It's worth contrasting with gradient clipping, which actually rescales the gradient and changes the update. Checkpointing changes nothing you can measure in the result — only where the memory goes. Its relatives push further: activation offloading moves activations to CPU RAM, reversible layers reconstruct inputs for near-zero storage, and FlashAttention applies the same recompute trick to attention itself. Set the depth and segment count and watch peak memory bottom out at 2√N: https://dev48v.infy.uk/dl/day48-gradient-checkpointing.html

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/dev48v/gradient-checkpointing-keep-n-activations-recompute-the-rest-memory-falls-from-on-to-on-74k

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
