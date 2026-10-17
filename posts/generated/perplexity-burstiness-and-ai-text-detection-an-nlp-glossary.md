---
title: "Perplexity, Burstiness, and AI Text Detection: An NLP Glossary"
slug: "perplexity-burstiness-and-ai-text-detection-an-nlp-glossary"
author: "Wajahat Ali Shahani"
source: "devto_ai"
published: "Sat, 17 Oct 2026 20:12:06 +0000"
description: "What do "perplexity," "burstiness," and "watermarking" actually mean when people throw them around in AI-detection debates? We wrote a plain-English glossary..."
keywords: "text, perplexity, detector, model, burstiness, detectors, human, not"
generated: "2026-10-17T20:22:56.710777"
---

# Perplexity, Burstiness, and AI Text Detection: An NLP Glossary

## Overview

What do "perplexity," "burstiness," and "watermarking" actually mean when people throw them around in AI-detection debates? We wrote a plain-English glossary of the core NLP vocabulary, grounded in the primary papers. Here is the short version of the terms that matter most, with why each one is in the conversation. Perplexity Perplexity measures how "surprised" a language model is by a text: the average probability it assigns to each next token, inverted. Low perplexity means the text reads as highly predictable to a model. Because model-generated text tends to be fluent and statistically bland, detectors and researchers often treat very low perplexity as a machine-likeness signal. The Google ML Glossary defines it as "a measurement of how well a probability model predicts a sample." Caveat: careful, edited human prose - legal writing, textbook prose, some Wikipedia intros - also scores low on perplexity. Low perplexity is a register signal, not proof of authorship. (We saw exactly this failure mode in our 8-text detector test : a human Wikipedia paragraph scored 99% AI.) Burstiness Burstiness describes variation in sentence length and structure across a text - the rhythm of a human draft: some terse sentences, some long winding ones. Classical work by Benedetto, Caglioti, and Loreto (Physical Review Letters, 2002) showed that compressed-length features of human language vary in characteristic ways that simple generated text does not. Modern detectors use stylistic features in this family; when people say detectors look for "human rhythm," burstiness is usually what they mean. Tokenization Models do not read words; they read subword units produced by tokenizers (BPE, WordPiece). Detectors that operate on token probabilities inherit everything about how the tokenizer splits text - which is partly why detector behavior shifts across languages and domains. Watermarking Green et al. (2023) proposed embedding statistical "green lists" of plausible next tokens during generation, so watermarked text carries a detectable signature. Kirchenbauer et al. (arXiv:2301.10226, ICML 2023) extended this to bit-encoded payloads. Watermarking is a provenance technique, not a detector of human text - and its signals can be attacked: Sadasivan et al. showed paraphrasing (including recursive paraphrasing) can substantially reduce watermark detectability (arXiv:2303.11156, TMLR). Membership inference & zero-shot detection Zero-shot detectors (Liang et al., arXiv:2304.02819, Patterns) estimate the likelihood a token sequence came from a model, without detector-specific training. The same paper found widely used detectors disproportionately mis-flagged non-native English writers - constrained prose reads as machine prose. GLTR & the original detector toolkit GLTR (Gehrmann, Strobelt, Rush; ACL 2019 demo, arXiv:1906.04043) visualizes token-rank distributions to help humans spot machine text. It is a teaching tool as much as a detector, and its paper is a clean entry point into the whole feature family. The honest takeaway Every term above describes a statistical property of text , and every detector is a model built on such properties. Confidence percentages describe the model, not the writer's laptop. The practical workflow is review, not screening. Full glossary with all citations: Perplexity, Burstiness, and AI Text Detection: an NLP glossary The test data behind the caveats: 8 Texts, 1 Detector Cross-posted from RewriteAI with a canonical link to the original.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/wajahatshahani/perplexity-burstiness-and-ai-text-detection-an-nlp-glossary-3khp

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
