---
title: "Teaching Generative Audio Models Non-Western Rhythms: Fine-Tuning ACE-Step 1.5 with LoRA on 6/8 South Indian Percussion"
slug: "teaching-generative-audio-models-non-western-rhythms-fine-tuning-ace-step-15-with-lora-on-68-south-indian-percussion"
author: "Boobalan Arjunan"
source: "devto_ai"
published: "Fri, 16 Oct 2026 10:55:15 +0000"
description: "State-of-the-art music generation models like ACE-Step 1.5 are technical marvels, but they carry a known systemic blindspot: they were trained predominantly ..."
keywords: "ace, step, lora, audio, standard, southindiaparailora, models, south"
generated: "2026-10-16T11:05:26.348583"
---

# Teaching Generative Audio Models Non-Western Rhythms: Fine-Tuning ACE-Step 1.5 with LoRA on 6/8 South Indian Percussion

## Overview

State-of-the-art music generation models like ACE-Step 1.5 are technical marvels, but they carry a known systemic blindspot: they were trained predominantly on Western 4/4 structures. When you prompt foundation models for traditional South Indian acoustic percussion like Parai, Thappu, or high-energy Dappankuthu , the output falls flat. The reason is musical and mathematical: our folk drumming relies on 6/8 compound time signatures (tha-ki-tta, tha-ki-tta) and rapid acoustic transient spikes that standard cross-attention layers fail to resolve on standard binary grids. To solve this, I fine-tuned and open-sourced SouthIndiaParaiLoRA on top of the ACE-Step 1.5 foundation architecture. 🔬 Engineering & Training Setup Base Architecture : ACE-Step 1.5 ( acestep-v15-x1-base & turbo compatible) Dataset : 393 studio-quality stems of authentic Parai, Thappu, Thappattam, and Urumi loops (80 – 172 BPM) Hardware : 30 epochs on an NVIDIA A40 (48GB VRAM) via RunPod LoRA Configuration : Rank 64, Alpha 128 Optimization : Slashed final loss by 75.5% (from a 1.97 baseline down to 0.48 ) 🛠️ How to Run in ACE-Step Playground & ComfyUI The model weights are released in standard .safetensors format: 1. ACE-Step Playground Clone the engine: ACE-Step-1.5-PlayGround--Engine Drop adapter_model.safetensors and adapter_config.json into: checkpoints/SouthIndiaParaiLoRA/final/ Launch the WebUI and select SouthIndiaParaiLoRA from the LoRA dropdown. 2. ComfyUI Workflow Load adapter_model.safetensors directly into your standard ACE-Step 1.5 LoRA loader node. 🎯 Example Prompt Prompt: High energy South Indian dappankuthu street festival drumming, massive thappu ensemble, authentic 6/8 compound folk rhythm at 145 BPM, urumi and parai dynamic groove Lyrics: [Instrumental] LoRA Scale: 0.85 🎧 Model Weights & 7 Audio Demos The adapter weights and 7 pre-rendered audio demos across different tempos and rhythmic variations are available under Apache 2.0 on Hugging Face: 👉 [Hugging Face Model Card & Demos] (https://huggingface.co/boobalanit/ACE-Step-1.5-SouthIndiaParaiLoRA) I'd love to hear feedback from fellow researchers, audio engineers, and developers experimenting with ACE-Step or regional music synthesis!

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/boobalan_arjunan/teaching-generative-audio-models-non-western-rhythms-fine-tuning-ace-step-15-with-lora-on-68-7nn

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
