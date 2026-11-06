---
title: "Both URLs followed main, so my residual could mix two dates"
slug: "both-urls-followed-main-so-my-residual-could-mix-two-dates"
author: "pm25coder"
source: "devto_python"
published: "Fri, 06 Nov 2026 22:18:04 +0000"
description: "A reader left a note under my last post that I have not been able to put down. He said, in effect: pin the revision before you fetch the config and the model..."
keywords: "not, two, same, one, config, seven, you, api"
generated: "2026-11-06T22:54:48.604063"
---

# Both URLs followed main, so my residual could mix two dates

## Overview

A reader left a note under my last post that I have not been able to put down. He said, in effect: pin the revision before you fetch the config and the model metadata, because both of the URLs in your example follow a mutable head independently, and a nonzero residual can describe a mixed observation rather than a missing term in the formula. He is right, and it is not a theoretical race. The snippet he was reading asks two URLs: https://huggingface.co/{repo}/raw/main/config.json https://huggingface.co/api/models/{repo} Both follow main . Two reads, two chances for the branch to move between them, and then a comparison between a number computed from one and a number computed from the other. The residual in that post was the gap between the parameter count a model card claims and the parameter count the checkpoint's own config implies. If the two reads landed on different commits, that gap could be describing a mix of two states instead of a property of one. So this week I measured what it costs to stop doing that. Why the snippet has two URLs at all I did not fetch two URLs because I like two URLs. The API response cannot answer "how many parameters does this checkpoint store", because the config object inside it does not carry the fields that answer it. Across seven repos, api/models/{repo} returned a config object with three keys — architectures , model_type , tokenizer_config — and four for Phi-3-mini, which adds auto_map . None of the seven carried vocab_size , num_hidden_layers or hidden_size . Those three live in config.json , and I could not reach them from the metadata call. So the shape is forced: one call for what the API knows, one call for the file the API does not inline. The only open question is which revision the second call names. What the two paths returned today Seven repos, four model families, all ungated, read in one sitting: repo sha (first 12) safetensors.total main vs pinned HuggingFaceTB/SmolLM2-135M-Instruct 12fd25f77366 134,515,008 same HuggingFaceTB/SmolLM2-360M-Instruct a10cc1512eab 361,821,120 same HuggingFaceTB/SmolLM2-1.7B-Instruct 31b70e2e869a 1,711,376,384 same Qwen/Qwen2.5-0.5B-Instruct 7ae557604adf 494,032,768 same Qwen/Qwen2.5-1.5B-Instruct 989aa7980e4c 1,543,714,304 same microsoft/Phi-3-mini-4k-instruct f39ac1d28e92 3,821,079,552 same allenai/OLMo-1B-hf aee7752d9c08 1,176,764,416 same "Same" is not a shrug in that column. Both paths answered 200, both returned the same config values (I compared vocabulary size, layer count, hidden size, tie flag, dtype and architecture string), both returned the same byte count — 861, 846, 908, 659, 660, 967 and 632 — and both carried the same ETag header. Seven out of seven. That last part is what I did not expect, and it is exactly the trap. An equality that holds today, with nothing behind it that keeps it holding. The ETag earns you one true sentence: these two paths currently resolve to the same object. It does not promise they will at the moment your script runs tomorrow, because neither path is asking for a particular commit. Only the sha does that, for the plain reason that the sha is the request. What pinning costs, and a correction In the reply I sent that reader, I wrote that pinning the revision costs one extra request. Measured properly, that sentence is missing its condition, so let me put the condition back. If your script already calls api/models/{repo} — mine did, because it needed safetensors.total — then the sha arrives in that very response, sitting next to the total. Pinning then costs zero extra requests: the same two calls, with one of them naming a sha instead of main . The extra request only appears in the other case: a script whose only read is raw/main/config.json , because all it wants is the config. That one goes from one call to two. So the honest version is: zero if you were already asking the API for anything, one if you were not. I wrote down the second half as if it were the whole answer. Not a large error, but it is the kind that survives because it sounds like a cost, and costs are the thing you are allowed to round. The order that removes the ambiguity Three steps, and no new dependency: GET api/models/{repo} and keep sha — plus safetensors.total if your comparison needs it. GET raw/{sha}/config.json , and recompute what the checkpoint stores from the config you just pinned. Compare the two numbers. After that, if the comparison still fails, the difference is real: you can no longer be comparing two dates by accident. The change is one string in a URL. What it buys is that every number in your table belongs to the same commit, and that someone who re-runs your script next month gets the same artifact you described — or an error, which is also an answer. What I did not measure Whether any of these seven repos actually moved between two of my reads. I cannot replay the past, and the identical ETag s only say the paths agree now. The failure my reader described is plausible and cheap to prevent; I did not observe it. Gated repos. All seven I tried were ungated and answered 200. A gated repo may treat raw/{sha} differently from raw/main , and I do not know which way. The web UI's metadata. I read the API and the raw file, not the page. Whether main had moved at all since the post my reader was reading. That post is a day old; its own reads are not reproducible now, which is the whole point. Seven repos is not a survey. It is seven repos, named above, so you can run the same seven and check me.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/pm25coder/both-urls-followed-main-so-my-residual-could-mix-two-dates-5c40

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
