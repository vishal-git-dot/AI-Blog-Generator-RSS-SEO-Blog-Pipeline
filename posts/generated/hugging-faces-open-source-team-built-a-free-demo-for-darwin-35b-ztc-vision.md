---
title: "Hugging Face's Open-Source Team Built a Free Demo for Darwin-35B-ZTC-Vision"
slug: "hugging-faces-open-source-team-built-a-free-demo-for-darwin-35b-ztc-vision"
author: "AI OpenFree"
source: "devto_ai"
published: "Wed, 28 Oct 2026 04:49:12 +0000"
description: "TL;DR Apolinário (multimodalart) of the Hugging Face open-source team contacted VIDRAFT about our open model Darwin-35B-ZTC-Vision . He thanked us for open-s..."
keywords: "model, hugging, demo, vision, face, darwin, team, ztc"
generated: "2026-10-28T05:00:43.287496"
---

# Hugging Face's Open-Source Team Built a Free Demo for Darwin-35B-ZTC-Vision

## Overview

TL;DR Apolinário (multimodalart) of the Hugging Face open-source team contacted VIDRAFT about our open model Darwin-35B-ZTC-Vision . He thanked us for open-sourcing it and said the team had built an interactive demo for it on Hugging Face Spaces, running on free ZeroGPU hardware. He also offered to transfer the demo to us. We accepted, and the Space is moving to our FINAL-Bench organization. Anyone can now try a 35B vision decision model in a browser, with no GPU and no setup. Model: huggingface.co/FINAL-Bench/Darwin-35B-ZTC-Vision Demo: huggingface.co/spaces/hugging-apps/darwin-35b-ztc-vision (moving to FINAL-Bench; Hugging Face redirects the old address after a transfer) What happened? On 27 October 2026, Apolinário opened a discussion on the model page. He wrote that the team "were excited about this work" and had built an interactive demo app of it. He asked which account the Space should move to, so that it could "give your work more visibility, discoverability" and let people try the model. We asked for the FINAL-Bench organization and thanked the team. We did not ask for this. The Hugging Face team found the model, built the demo and offered it to us. What does Darwin-35B-ZTC-Vision do? It is a vision decision model . It does not write text. You give it up to four images, a short state and a typed question. In one forward pass it returns a calibrated probability for every option: Question type Example Output noul (yes or no) "Is there a defect on this part?" P(yes), P(no) choice "Which of the two photos has the higher quality?" one probability per option score "Rate the image quality from 1 to 5" one probability per level Item Value Size 35B mixture of experts, about 3B active parameters per token Backbone Darwin-35B-A3B-Opus Images per request up to 4 License Apache 2.0 Downloads (Hugging Face counter, 28 Oct 2026) 8,940 Because the model returns probabilities instead of a text answer, an application can set its own threshold. For example, it can send a part to a human inspector when P(defect) is between 0.3 and 0.7. What does the demo do? The demo is a Gradio app. You upload one to four images, pick a question type, type the question and options, and get a probability for each option. It has example images for counting, spatial relations, image quality and anomaly detection. To fit the model on Spaces, the Hugging Face team wrote its own loader. The demo container has a RAM limit of about 97 GB. A standard load of the 69 GB checkpoint goes over that limit. Their loader reads the weights one tensor at a time and puts each one on the GPU right away. The numbers are the same as the reference BF16 path; only the loading order changes. This is real engineering work by the Hugging Face team, and we thank them for it. How did the model do on S1MB? The model has a complete result on the vision track of S1MB (System One Mosaic Benchmark): all 20 required vision tasks, with zero failed decisions. The maintainer merged the result on 19 October 2026. The live S1MB vision leaderboard has the current rankings. How do I run it myself? With the demo, you only need a browser. To run it on your own hardware, you need a CUDA GPU with about 75 GB of free memory (BF16) and the code that ships with the model: import sys from pathlib import Path from huggingface_hub import snapshot_download path = Path ( snapshot_download ( " FINAL-Bench/Darwin-35B-ZTC-Vision " )) sys . path . insert ( 0 , str ( path )) from autojev.model import DecisionModel , answer The model card has the full usage example. FAQ Is this a Hugging Face certification? No. The Hugging Face open-source team built a demo for the model and gave it to us. It is not a certification or a ranking. Is the demo free? Yes. It runs on Hugging Face ZeroGPU, which gives Spaces shared GPUs at no cost. If many people use it at the same time, you may have to wait in a queue. Where will the demo live? In the FINAL-Bench organization on Hugging Face, next to the model. The current address will redirect after the transfer. Can I use the model commercially? The model is released under Apache 2.0. Does it generate captions or descriptions? No. It only returns probabilities over the options you give it. For text output, use a generative vision language model. Links Model: FINAL-Bench/Darwin-35B-ZTC-Vision Demo Space: hugging-apps/darwin-35b-ztc-vision Text sibling: FINAL-Bench/Darwin-27B-ZTC-v9 VIDRAFT: vidraft.net Originally published on VIDRAFT AI Media .

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/ai_openfree_b23025ef075cf/hugging-faces-open-source-team-built-a-free-demo-for-darwin-35b-ztc-vision-995

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
