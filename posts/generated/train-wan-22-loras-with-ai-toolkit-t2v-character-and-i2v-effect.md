---
title: "Train Wan 2.2 LoRAs with AI Toolkit: T2V character and I2V effect"
slug: "train-wan-22-loras-with-ai-toolkit-t2v-character-and-i2v-effect"
author: "AI-KSK"
source: "devto_ai"
published: "Wed, 25 Nov 2026 21:18:13 +0000"
description: "AI Toolkit now supports Wan 2.2 LoRA training through a UI, and this episode builds two beginner-friendly tasks: a T2V character LoRA and an I2V effect LoRA...."
keywords: "lora, training, wan, character, image, low, steps, toolkit"
generated: "2026-11-25T21:26:57.090302"
---

# Train Wan 2.2 LoRAs with AI Toolkit: T2V character and I2V effect

## Overview

AI Toolkit now supports Wan 2.2 LoRA training through a UI, and this episode builds two beginner-friendly tasks: a T2V character LoRA and an I2V effect LoRA. The cloud image lowers setup to a launch command and a web UI. Watch the episode: https://youtu.be/4XVyjeNdBS8 Chinese original: https://www.bilibili.com/video/BV15evPzgEaH Image entry: https://www.compshare.cn/images/P6EGaRs2OeG5?referral_code=A7fTQUYY9lCDFJwA6MMvoq Two training targets T2V: a Tifa character LoRA for identity consistency. I2V: a playful rainbow-spitting effect. Both use Wan 2.2's high- and low-noise models. For a concrete character rather than an abstract concept, training both stages helps reproduce the dataset; the low-noise stage acts like a refiner. Key settings Rank 32, which controls LoRA size. 3,000 steps, saving every 250 steps. Low-VRAM mode with model switching every 20 steps to reduce load/unload overhead. Text encoder kept loaded so cached labels remain valid. 512 training resolution; 512 and 768 are possible with more compute. T2V clips use equal lengths, 33 frames in the test. I2V uses 15-20 clips of the same action. Deployment The episode deploys an AI Toolkit image, opens JupyterLab, runs a startup command, and accesses the UI on port 8675. A 48GB 4090 is recommended. Trial credits are point-in-time platform terms. When is a LoRA ready? The author notes that around 2,000+ steps can already produce a usable model. The saved output appears under the JupyterLab output directory and can be tested in a Wan 2.2 image. Known limits Dataset consistency matters more than step count alone. Low-VRAM training increases model-switch overhead. Caching and text-encoder unloading trade memory against label validity. No workflow JSON, dataset, or LoRA weights are bundled with this article.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/ai-ksk/train-wan-22-loras-with-ai-toolkit-t2v-character-and-i2v-effect-4ge8

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
