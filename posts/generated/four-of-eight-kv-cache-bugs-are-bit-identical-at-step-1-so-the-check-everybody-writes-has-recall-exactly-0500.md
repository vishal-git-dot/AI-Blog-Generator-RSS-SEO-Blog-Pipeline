---
title: "Four of Eight KV-Cache Bugs Are Bit-Identical at Step 1, So the Check Everybody Writes Has Recall Exactly 0.500"
slug: "four-of-eight-kv-cache-bugs-are-bit-identical-at-step-1-so-the-check-everybody-writes-has-recall-exactly-0500"
author: "Devanshu Biswas"
source: "devto_python"
published: "Sun, 23 Aug 2026 12:41:05 +0000"
description: "A KV cache is not an approximation. Under causal attention, appending a token cannot move an earlier position's residual stream, keys or values - measured at..."
keywords: "cache, step, one, changed, exactly, which, two, not"
generated: "2026-08-23T12:50:17.230890"
---

# Four of Eight KV-Cache Bugs Are Bit-Identical at Step 1, So the Check Everybody Writes Has Recall Exactly 0.500

## Overview

A KV cache is not an approximation. Under causal attention, appending a token cannot move an earlier position's residual stream, keys or values - measured at exactly 0 per layer - so a cached decode and a full recompute are the same function. Turn the mask off and the cache is still exact at layer 1 and wrong from layer 2, which is the depth at which information can flow backwards. So any deviation is a bug, and the test everyone writes compares the two paths at one step: forward ( M , tokens , { cache }) // all T positions, layer-major, fills the cache decodeStep ( M , cache , tok , pos ) // ONE position over the stored buffer assert ( maxAbs ( cached - recompute ) === 0 ) // exactly, not to a tolerance Bit equality holds over 432 configurations of seed, depth, head count, prompt length, step count and summation order, in each of three numeric formats - 1,296 runs, worst deviation 0.0, every token string matching. Forward and backward are both hand-written (RMSNorm, causal MHA, SiLU MLP, learned positions), the gradient agreeing with independently written central differences to 3.2e-8 over 24 tensors. Dependency-free JavaScript, one file: https://dev48.infy.uk/dl/day69-kv-cache.html Eight bugs, each one changed line the changed line step 1 all steps output changed stale - attend before appending 0.146 0.448 0% posoff - position index one behind 24.9 24.9 100% freeze - buffer stops growing 0.0 24.6 96% evict - an unasked-for sliding window 0.0 0.254 0% posfrozen - prompt length as the offset 0.0 25.5 100% The last four are not 1e-12 apart. They are exactly 0.0, because at step 1 the cache is still just the prefill and every implementation agrees about it. They are bugs in the cache's growth , and step 1 is the one step where nothing has grown. posfrozen - the prompt length used as the position offset instead of the running cache length, which is the commonest way to get this wrong when resuming - is invisible at step 1 and changes the generated text in 100% of runs. Scored as a detector over 240 cases, 180 of which changed the output: the one-step check has recall 0.500 and AUC 0.605 against a chance value of 0.500. The same comparison at every step: recall 1.000, AUC 1.000, no tolerance anywhere. Two rows cut the other way and are kept because they are inconvenient: stale moves the logits immediately and never moves a token, and evict is a genuine bug that never bites. The explanation I set out to confirm "The cache changed my output" is normally blamed on reduction order: a batched prefill and a one-token decode are different shapes, so real kernels sum differently. Both orders are implemented here, with precision split into two knobs - what values are stored in, and what the accumulator runs in. Storing in bfloat16 with a float64 accumulator, which is what every real kernel does, makes the two summation orders agree exactly, at 100% of positions . Lowering the precision removed the discrepancy, because a 1e-16 disagreement lands on the same bfloat16 grid point. Only a bfloat16 accumulator makes order matter - and there, on a near-tied model, tokens flip in 3 of 24 cached runs against 2 of 24 for the no-cache control , two full recomputes differing only in how they add up. Same size, and the cache stays bit-exact in all three formats. Whatever changed the output, it was not the cache. A cache does change the answer in training: reuse a cached prefix and its keys arrive as constants - cosine 0.857 at a prefix of 6 of 12, held-out suffix loss 1.346 against 0.059. 133 verifier assertions, 32 running in the page. One deep-learning idea a day, computed rather than quoted: https://dev48.infy.uk/deeplearningfromzero.php

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/dev48v/four-of-eight-kv-cache-bugs-are-bit-identical-at-step-1-so-the-check-everybody-writes-has-recall-5gkn

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
