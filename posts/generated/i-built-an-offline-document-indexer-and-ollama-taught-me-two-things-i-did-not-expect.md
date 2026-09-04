---
title: "I built an offline document indexer, and Ollama taught me two things I did not expect"
slug: "i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect"
author: "ᗩᒪᕮ᙭ ᑕᗩᗰᗩᑕᕼO ᑕᗩSTIᒪᕼO"
source: "devto_python"
published: "Fri, 04 Sep 2026 03:28:41 +0000"
description: "I had a folder with a few hundred scanned documents I could not upload anywhere. Confidential, mostly images of paper with no text layer, useless for search...."
keywords: "not, one, model, you, ollama, every, two, things"
generated: "2026-09-04T03:55:40.883763"
---

# I built an offline document indexer, and Ollama taught me two things I did not expect

## Overview

I had a folder with a few hundred scanned documents I could not upload anywhere. Confidential, mostly images of paper with no text layer, useless for search. Opening them one by one was the only way to find anything. So I built the step that comes before the AI assistant, rather than trying to replace it. What it does You point it at a folder. It scans, runs OCR only on the pages that have no text layer (it checks per file and skips the rest), slices oversized PDFs, reads every page, and classifies each one into an item with a type, a date where one exists, an author and a summary. Then it writes four Markdown files next to your originals: an index of every item, a chronological timeline, a review report naming every gap and failure it hit, and a set of instructions ready to paste into an AI project. The originals are never touched, everything lands in a separate output folder. Classification runs on an open model through Ollama, on the machine itself. The host is fixed to 127.0.0.1 in code and never read from configuration, which was the property I actually needed. There is also a deterministic rules engine that uses no model at all, for machines that cannot run one. Stack is Python 3.12, FastAPI, HTMX, SQLite and Ollama. 456 tests, CI on Windows, interface in English, Portuguese and Spanish. GPL-3. Two things surprised me while building it, and they are probably more useful to you than the project. 1. num_gpu: -1 does not mean "use all the GPU" I had a card with several GB of VRAM free while the model ran at CPU speed for the layers that had spilled into RAM. I was passing options.num_gpu = -1 , which reads like "use as much GPU as possible". It does not do that. It hands the decision to Ollama's own scheduler, which is deliberately conservative. It sizes the KV cache for OLLAMA_NUM_PARALLEL concurrent requests, four by default on the versions I tested, which is four times the cache a single threaded classifier will ever use. Then it keeps a safety margin on top and rounds down to a whole number of layers. Two independent things fixed it. Server settings, not request options. num_gpu is per request, but the sizes that decide how much fits are per server environment variables, read once by ollama serve at startup. One loaded model, one parallel slot, flash attention on and a quantised KV cache freed enough VRAM for several more layers, with no effect on output. The cache holds attention state, not the answer. Compute the layer count yourself. Read block_count and embedding_length from the model metadata, work out the per layer cost at your context size, and pass an explicit num_gpu . One trap that cost me an afternoon: measure free VRAM with nothing loaded. If you measure while the model you are sizing is already resident, you budget against a number that already includes it. You ask for fewer layers than fit, Ollama reloads smaller, less is free next time, and you ratchet a model that fit right off the GPU. 2. The bigger model lost I benchmarked five models over the same windows of a 31 page document, every one running fully on an 8 GB card: Model Size Type field filled s/window qwen3.5:4b 3.0 GB 100% 30.8 gemma4:e4b 3.1 GB 79.5% 38.5 qwen3.5:9b 5.3 GB 79.5% 86.2 qwen3:8b 5.4 GB 100% 108.8 granite4.2:8b 5.7 GB 100% 116.9 The 4b beat the 9b of its own family, on quality and on speed at the same time. Describing a page is reading and format discipline, not deep reasoning, so size buys nothing for this task and costs a lot of time. It is the default now. There was a related bug worth mentioning. Models with a thinking channel dump the whole answer into thinking and return an empty response when you do not explicitly disable it. My code only read response , so every window came back with zero items. Sending think: false fixed it, and reading thinking as a fallback covers the rest. What I am asking for People running it on hardware that is not mine. It was built and tested on essentially one machine, so I am certain things break on other GPUs, other Windows versions and file formats that never passed through here. An issue, a PR, or just a note saying what went wrong all help. Two limits, so nobody wastes an afternoon. It is Windows only and structurally so, since it reads WMI, the registry and Performance Counters directly. And the quality score it reports measures the engine's declared self confidence and how completely it filled the fields, not whether it was right. An engine can score 100 and still misfile a document. That is written into the code that computes the score, not just the README. https://github.com/alexccastilho/gclaude-indexer

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/alexccastilho/i-built-an-offline-document-indexer-and-ollama-taught-me-two-things-i-did-not-expect-4ho5

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
