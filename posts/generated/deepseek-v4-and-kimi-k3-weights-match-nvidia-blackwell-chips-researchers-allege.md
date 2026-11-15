---
title: "DeepSeek V4 and Kimi K3 weights match Nvidia Blackwell chips, researchers allege"
slug: "deepseek-v4-and-kimi-k3-weights-match-nvidia-blackwell-chips-researchers-allege"
author: "ColdCaseTech"
source: "devto_ai"
published: "Sun, 15 Nov 2026 22:16:17 +0000"
description: "Originally published on ColdCaseTech . Disclosure: this post contains affiliate links. We may earn a commission at no extra cost to you. Then vs. Now (News r..."
keywords: "hardware, tom, chips, techcrunch, models, deepseek, blackwell, not"
generated: "2026-11-15T22:39:51.911803"
---

# DeepSeek V4 and Kimi K3 weights match Nvidia Blackwell chips, researchers allege

## Overview

Originally published on ColdCaseTech . Disclosure: this post contains affiliate links. We may earn a commission at no extra cost to you. Then vs. Now (News report): Then: Unemployment Labs, a nonprofit research group led by former OpenAI researcher Will DePue, reported evidence that open-weight Chinese AI models were trained on Nvidia Blackwell chips. Now: The researchers state their method does not reveal where the chips were, how they were accessed, or prove that export controls were broken. Unemployment Labs, a nonprofit research group, analyzed open-weight models from DeepSeek, Moonshot AI, MiniMax and Ant Group, and found compelling evidence that the most closely watched models, including Moonshot's Kimi K3 releases and DeepSeek's V4 models, bear fingerprints from training on Blackwell chips ( TechCrunch ). The group is led by Will DePue, a former OpenAI researcher, who analyzed the weights of the released models ( TechCrunch ). The researchers hedge their findings, noting that the analysis does not reveal where the chips were or how they were accessed ( Tom's Hardware ). Key Facts Item Detail Source Researcher Unemployment Labs, led by Will DePue TechCrunch Models named DeepSeek V4, Kimi K3.1, MiniMax-M3, Ling-3.1-Flash Tom's Hardware Method Statistical match of weight initialization to chip layouts Tom's Hardware Export status Blackwell GPUs are banned from export to China or Chinese-owned firms TechCrunch Limit Works only on models with open weights Tom's Hardware Timeline 2026-11-13 : TechCrunch reports the Unemployment Labs findings on DeepSeek, Moonshot AI, MiniMax and Ant Group models ( TechCrunch ). 2026-11-14 : Tom's Hardware details the fingerprinting technique and the models it names ( Tom's Hardware ). Details (as Reported) Nvidia's Hopper chips have 132 shader modules, Blackwell B series chips have 148, and Blackwell GB chips have 152 ( Tom's Hardware ). Training begins by initializing weights with pseudo-random adjustments through cuRAND, a process spread across the shader modules and their threads ( Tom's Hardware ). The researchers repeated that initialization with the same chips, software and thread counts, and their weight distribution matched that of DeepSeek, Kimi and others ( Tom's Hardware ). When they changed the shader module and thread counts, the correlation broke down ( Tom's Hardware ). The method identifies chip families and an approximate card count, but cannot pinpoint the exact card variant ( Tom's Hardware ). For DeepSeek V4, the researchers also analyzed the weight values and ruled out AMD cards ( Tom's Hardware ). White House technology adviser Michael Kratsios said earlier this year that Moonshot had used export-banned Nvidia chips, citing U.S. intelligence sources ( TechCrunch ). Epoch AI estimates that about two million advanced chips entered China in 2024 and 2025 through schemes designed to hide their final destination ( TechCrunch ). Epoch also estimates that 275,000 Nvidia AI accelerators were imported to Malaysia in 2024 and 2025 ( TechCrunch ). Run an AI model on your own server. Open models such as DeepSeek can run on a rented server instead of someone else's app, so prompts and data stay on a machine you control. See Contabo's AI server setup (affiliate link) What Is Not Yet Confirmed Whether export control laws were violated is not established, since the chips could have been in an offshore data center ( TechCrunch ). Where the chips were located and how they were accessed are not revealed by the analysis ( Tom's Hardware ). The models were not necessarily trained entirely on Nvidia chips ( TechCrunch ). As far as Tom's Hardware can tell, it is not currently illegal for Chinese companies to rent Blackwell hardware abroad ( Tom's Hardware ). Sources TechCrunch, 2026-11-13 Tom's Hardware, 2026-11-14 Tools related to this case AI voice generation for narration, videos and podcasts: ElevenLabs A low-cost cloud server for testing software and small projects: Contabo Core VPS S3-compatible storage for datasets, media and backups: Contabo Object Storage These are affiliate links: we may earn a commission at no extra cost to you. ColdCaseTech is an independent record of technology's promises: every line links to its source. New cases daily at coldcasetech.com . Follow on X , Bluesky or Telegram .

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/coldcasetech/deepseek-v4-and-kimi-k3-weights-match-nvidia-blackwell-chips-researchers-allege-2191

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
