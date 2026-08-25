---
title: "Building a local video search CLI with ffmpeg and OpenCLIP"
slug: "building-a-local-video-search-cli-with-ffmpeg-and-openclip"
author: "Harry Xu"
source: "devto_python"
published: "Tue, 25 Aug 2026 12:45:27 +0000"
description: "I often remember the shot I want before I remember its filename. That gap is what binquery is for. It is a local Python CLI that indexes video clips and turn..."
keywords: "not, does, binquery, demo, quality, what, footage, venv"
generated: "2026-08-25T12:56:12.655430"
---

# Building a local video search CLI with ffmpeg and OpenCLIP

## Overview

I often remember the shot I want before I remember its filename. That gap is what binquery is for. It is a local Python CLI that indexes video clips and turns a sentence into a ranked shortlist for a human to review. It deliberately stops before editing: no timeline generation, no automatic cut, and no render. The smallest reproducible trial You can test the complete installed command path without supplying footage: python3 -m venv .venv .venv/bin/pip install binquery .venv/bin/binquery demo --out /tmp/binquery-demo The demo generates a synthetic 30-second video locally, then exercises splitting, indexing, validation, and querying. The first run may download OpenCLIP model weights. This is an end-to-end pipeline smoke test, not evidence of semantic search quality on real footage. Why keep the architecture small? The current design uses: ffmpeg to sample three frames from each clip OpenCLIP ViT-B-32 to build the local visual index plain JSON and NumPy files for metadata and vectors a JSON result containing clip paths, scores, and ranking signals There is no database, vector service, or daemon to operate. Querying an existing index does not resample the footage or rebuild the full index. The trade-off is straightforward: three frames keep indexing understandable and bounded, but they can miss important content in long or visually varied clips. I would rather expose that limitation than market a synthetic demo as a quality benchmark. Ranking signals are not explanations The output includes fields such as score , gate , and reasons . Here, reasons means ranking signals recorded by the pipeline. It should not be interpreted as a reliable semantic explanation of why a clip is correct. That distinction matters because a plausible-looking explanation can create more confidence than the underlying retrieval quality deserves. The shortlist is meant to reduce what a person must inspect, not replace editorial judgment. What binquery does not do It does not build a timeline or export a finished edit. It does not claim that the synthetic demo measures retrieval quality. It does not turn every indexed metadata field into a user-facing search filter. It does not hide the first-run model download. What I want feedback on I would especially value criticism of: the three-frame sampling strategy, the CLI and JSON output contracts, packaging and first-run installation failures, and useful ways to evaluate ranking quality without committing private footage to the repository. The project is MIT licensed and available on GitHub . Version 0.3.0 is also on PyPI with a corresponding GitHub Release . AI assistance disclosure: AI tools assisted parts of development, review, and preparation of this article. I personally checked the repository changes, tests, release artifacts, published package, and the factual claims above. Remaining limitations and unverified behavior are documented rather than presented as measured results.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/harry_xu_74d04f7a971995d5/building-a-local-video-search-cli-with-ffmpeg-and-openclip-3a5g

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
