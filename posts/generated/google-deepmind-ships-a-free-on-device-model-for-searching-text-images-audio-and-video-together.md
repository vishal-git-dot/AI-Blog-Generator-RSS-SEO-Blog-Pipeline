---
title: "Google DeepMind Ships a Free On-Device Model for Searching Text, Images, Audio and Video Together"
slug: "google-deepmind-ships-a-free-on-device-model-for-searching-text-images-audio-and-video-together"
author: "Mikhail Savchenko"
source: "devto_ai"
published: "Wed, 07 Oct 2026 05:12:10 +0000"
description: "Google DeepMind has released EmbeddingGemma 2 , an open embedding model that maps text, code, images, audio and video into a single shared vector space so th..."
keywords: "google, text, audio, embeddinggemma, model, million, images, video"
generated: "2026-10-07T05:20:33.236079"
---

# Google DeepMind Ships a Free On-Device Model for Searching Text, Images, Audio and Video Together

## Overview

Google DeepMind has released EmbeddingGemma 2 , an open embedding model that maps text, code, images, audio and video into a single shared vector space so they can be searched together. It follows last year's text-only EmbeddingGemma, which the company says passed 20 million downloads. Built on the Gemma 4 architecture and released under an Apache 2.0 license, EmbeddingGemma 2 has 740 million parameters but is modular: text-only workloads need as little as 270 million parameters, with optional 170 million-parameter vision and 300 million-parameter audio encoders added for full multimodal support. On a Google Pixel 11 Pro, Google reports the quantized model needs roughly 191MB of active RAM for text-only use and about 567MB for the full multimodal version. The model uses Matryoshka Representation Learning to let developers truncate its 768-dimension output vectors down to 512, 256 or 128 dimensions, which Google says cuts local vector database storage by up to 6x. Context has also grown: an 8K token window, four times larger than the original EmbeddingGemma, lets it process up to 5.5 minutes of audio, 29 images, or 58 video frames in a single pass. On benchmarks, Google reports EmbeddingGemma 2 leads sub-1B multimodal embedders on MTEB Code and MAEB while matching or beating some larger specialist models on text, vision and audio tasks. Code retrieval saw the largest jump, improving from 68.76 to 78.68 on MTEB Code — a gain Google positions for local codebase indexing and coding-agent retrieval use cases. Because it shares a tokenizer and audio encoder with Gemma 4, Google is positioning the pair for on-device retrieval-augmented generation: EmbeddingGemma 2 finds relevant text, images or audio clips locally, and Gemma 4 reasons over them, all without a network call. Google points to its AI Edge Gallery apps — Instant Media Search and Video Moments Finder — and the Foresight app as early demonstrations, alongside a MediaPipe Decision Task API for building classification and routing systems on the same embeddings. Model weights are available on Hugging Face and Kaggle, with support already built out for transformers, sentence-transformers, MLX, vLLM, llama.cpp, SGLang, Ollama, LMStudio and Qdrant for vector storage; Unsloth has published fine-tuning guidance.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/mikefluff/google-deepmind-ships-a-free-on-device-model-for-searching-text-images-audio-and-video-together-1l7a

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
