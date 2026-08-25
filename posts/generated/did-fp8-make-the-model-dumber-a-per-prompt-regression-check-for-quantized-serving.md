---
title: "Did FP8 make the model dumber? A per-prompt regression check for quantized serving"
slug: "did-fp8-make-the-model-dumber-a-per-prompt-regression-check-for-quantized-serving"
author: "Jahn"
source: "devto_python"
published: "Tue, 25 Aug 2026 18:12:24 +0000"
description: "FP8 gave us a clean 1.5x on Qwen3-8B serving throughput on an RTX PRO 6000 Blackwell (1,725 to 2,597 tok/s at concurrency 32, vLLM). The uncomfortable questi..."
keywords: "one, identical, you, run, wrong, json, prompt, same"
generated: "2026-08-25T18:46:02.101774"
---

# Did FP8 make the model dumber? A per-prompt regression check for quantized serving

## Overview

FP8 gave us a clean 1.5x on Qwen3-8B serving throughput on an RTX PRO 6000 Blackwell (1,725 to 2,597 tok/s at concurrency 32, vLLM). The uncomfortable question is always the same: did the model get dumber. This post is the exact check we ran before recommending the switch, with numbers, so you can run the same one. Why "run an eval suite" is usually the wrong first answer Standard benchmarks (MMLU and friends) are noisy instruments for quantization deltas at 8B scale. Score movement inside the error bars tells you nothing about whether YOUR prompts changed behavior. What you actually want to know is narrower: on the workload you serve, does the FP8 checkpoint produce materially different outputs than BF16, and are any of the differences wrong. That is answerable directly, cheaply, and per prompt. The method Both configurations run the same fixed workload: 20 prompts covering reasoning, code, summarization, translation, extraction, classification, math, and instruction following. Greedy decoding, temperature 0, 256-token cap, streamed. Greedy matters: it removes sampling noise, so any output difference is attributable to the numerics. Then a three-stage comparison: Byte equality. outputs_bf16[i] == outputs_fp8[i] . Anything identical is settled. Similarity triage. For non-identical pairs, difflib.SequenceMatcher.ratio() sorts near-identical wording drift from real divergence. Side-by-side review under a written rubric. Every non-identical pair gets read. The rubric asks one question: is there a factual or numerical claim that one precision gets right and the other gets wrong. Wording changes, reordering, and equally-defensible readings are recorded but not counted as regressions. The core loop is small: import difflib , json bf16 = json . load ( open ( " vllm_bf16_conc1.texts.json " )) fp8 = json . load ( open ( " vllm_fp8_conc1.texts.json " )) for i , ( a , b ) in enumerate ( zip ( bf16 , fp8 )): if a == b : print ( i , " identical " ) continue r = difflib . SequenceMatcher ( None , a , b ). ratio () print ( i , f " similarity { r : . 3 f } " ) # non-identical pairs go to side-by-side review What it found on Qwen3-8B FP8 7 of 20 outputs byte-identical. 9 differed only in wording or formatting; equivalent content on review. 3 minor regressions: a repeated word in a poem, one list item drifting off topic, one questionable tool suggestion. 1 extraction prompt was ambiguous and produced two defensible readings. Zero cases where FP8 gave a wrong factual or numerical answer that BF16 answered correctly. That last line is the acceptance bar. Minor stylistic wobble is expected from a numerics change; a flipped fact is a blocker. This profile passed, so the 1.5x was free for this workload. Two honest caveats. First, this validates a prompt profile, not the model in general: different domains, longer contexts, or sampled decoding need their own pass. Second, greedy-decoding equality is a strict signal but not a complete one; if you serve with sampling, run the review stage on sampled pairs too and expect more (benign) divergence. The wrinkle that almost blocked the whole thing Getting FP8 to run at all on workstation-class Blackwell (sm_120) required routing around a kernel assertion in the default FP8 path. If you are on the same silicon and vLLM refuses to load the FP8 checkpoint, that is a known class of problem rather than something wrong with your setup. The full report this check belongs to, with the raw CSVs, environment manifest, and the one-command reproduction script, is here: https://conatus.jahn.ai/ai-engineering/sample-report

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/conatusai/did-fp8-make-the-model-dumber-a-per-prompt-regression-check-for-quantized-serving-595f

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
