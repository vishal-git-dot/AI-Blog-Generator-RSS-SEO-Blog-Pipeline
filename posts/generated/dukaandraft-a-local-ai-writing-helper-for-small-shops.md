---
title: "DukaanDraft: a local AI writing helper for small shops"
slug: "dukaandraft-a-local-ai-writing-helper-for-small-shops"
author: "M N Mustakul Amin Talukdar"
source: "devto_ai"
published: "Sun, 18 Oct 2026 20:21:51 +0000"
description: "This is a submission for the DEV Hacktoberfest Week 2 Challenge . What I Built DukaanDraft is an English-only prototype that turns a local shop's short offer..."
keywords: "model, not, local, shop, facts, test, small, node"
generated: "2026-10-18T20:23:36.865082"
---

# DukaanDraft: a local AI writing helper for small shops

## Overview

This is a submission for the DEV Hacktoberfest Week 2 Challenge . What I Built DukaanDraft is an English-only prototype that turns a local shop's short offer facts into an editable post draft. The workflow is simple: enter a shop name and offer facts, generate a rewrite, compare it with the original facts, edit, and copy. Nothing is posted automatically. The destination labels help organize a draft for WhatsApp, Google Business Profile, or Instagram; they do not change the model prompt yet. The side-hustle idea is a human-reviewed post-writing service for local shops. It is an idea to test, not an existing business. There are no customer, revenue, or willingness-to-pay claims. Demo The fictional test input was: Shop: Fictional Store Offer facts: rice for Rs 50 per kg. The model returned: Fictional Store sells Rice at Rs 50 per Kg. The complete local browser-to-Node-to-model test returned this draft in 3.8 seconds on the test computer. This is one measured result, not a performance guarantee. First use also downloads model weights. The interface keeps the original facts under the editable draft, alongside a warning to check every claim. A small model can still invent details or change a name. In other tests it added "affordable" or changed a shop name, which is why human review is part of the product rather than an afterthought. Code Source code on GitHub The application code is MIT licensed. The model weights keep their own Apache-2.0 license. To run locally with Node.js 20+: npm install npm start Then open http://127.0.0.1:8787 on the same computer. The prototype was tested with Node 22 on Linux. It is not publicly deployed. How I Built It The app uses plain HTML and JavaScript for the form, a small Node HTTP server, and Transformers.js for local inference. The AI core is SmolLM2-360M-Instruct , using the ONNX community conversion . The quantized model runs on the CPU in Node, not through a hosted inference API. No API key or new account is needed to run the app. The server listens only on the local loopback address and accepts local same-origin browser requests. Model files are downloaded from Hugging Face; shop text is processed locally by this application. The first download is hundreds of MB, and model loading needs enough free memory. This is not a phone-only or low-memory-device promise. I kept the scope small: English rewriting, an editable result, original facts for comparison, and an explicit copy action. Earlier API-hosted and browser-only inference approaches were explored but were not verified as working routes and are not the shipped version. Why Does Open Innovation Matter Open weights make it possible to test this idea without an inference-service account or a per-request API dependency. The model can be downloaded, inspected through its published documentation, and run locally. Open-source application code lets someone else change the workflow or replace the model without starting from scratch. That freedom also makes the tradeoffs visible. A small local model is accessible, but it is not automatically accurate enough to write a shop's public claims. The useful next step is to test with real shop owners, measure factual errors, and find out whether a reviewed writing service saves them enough time to pay for it. For now, DukaanDraft is a working local experiment with a clear review step, not a claim of a finished commercial product.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/mrnowshirwan/dukaandraft-a-local-ai-writing-helper-for-small-shops-nn2

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
