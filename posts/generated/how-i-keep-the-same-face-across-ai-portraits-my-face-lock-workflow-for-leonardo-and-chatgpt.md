---
title: "How I Keep the Same Face Across AI Portraits: My Face-Lock Workflow for Leonardo and ChatGPT"
slug: "how-i-keep-the-same-face-across-ai-portraits-my-face-lock-workflow-for-leonardo-and-chatgpt"
author: "ZhuAI Studio"
source: "devto_ai"
published: "Sun, 08 Nov 2026 13:00:56 +0000"
description: "The biggest problem with AI portraits isn't quality — it's consistency. Ask any generator for the same person ten times and you'll get ten different faces. T..."
keywords: "face, identity, block, keep, one, your, prompt, same"
generated: "2026-11-08T13:02:50.720649"
---

# How I Keep the Same Face Across AI Portraits: My Face-Lock Workflow for Leonardo and ChatGPT

## Overview

The biggest problem with AI portraits isn't quality — it's consistency. Ask any generator for the same person ten times and you'll get ten different faces. That is the problem a face-lock workflow solves: you lock the identity once, then change only the scene around it. Step 1: Start with one clean reference selfie Your reference photo does most of the heavy lifting, so make it boring on purpose: Face the camera straight on, in soft daylight near a window. Keep the whole face in frame — no hats, sunglasses or heavy shadows. No beauty filters, no smoothing apps, no heavy makeup. Filters change the features the model learns from. One person, one face, neutral expression. Take three or four shots and pick the sharpest one. This single photo becomes the anchor for every portrait after it. Step 2: Write an identity block — and reuse it word for word An identity block is a short paragraph of the features that never change. Write it once, then paste it into every prompt exactly as-is: [Age range], [face shape] face, [eye shape and colour], [eyebrow shape], [nose shape], [lip shape], [skin tone], [hair: length, colour, style], [one distinguishing feature — for example, a small mole or a scar] A filled-in example: A woman in her early 30s, oval face, almond-shaped dark brown eyes, straight brows, a straight nose, full lips, light warm skin tone, shoulder-length straight black hair parted in the middle, a small mole above the left eyebrow. The rule is simple: never reword this block. The moment you paraphrase it, the face starts to drift. If you want to change the person, you write a new identity block — otherwise, this one stays frozen. Step 3: Change only the scene variables With the identity block locked, everything else becomes a variable: scene, outfit, lighting, mood. Swap those freely and your portraits stay the same person in different settings. Here is a full example prompt for a cafe scene: A woman in her early 30s, oval face, almond-shaped dark brown eyes, straight brows, a straight nose, full lips, light warm skin tone, shoulder-length straight black hair parted in the middle, a small mole above the left eyebrow, sitting at a small wooden table in a sunlit cafe, holding a ceramic cup of coffee with both hands, soft window light on her face, cream knit sweater, blurred cafe interior in the background, shallow depth of field, photorealistic portrait, 85mm lens look Nothing in the first half ever changes. Only the second half — cafe, sweater, light — is yours to play with. Step 4: Settings that matter in Leonardo and ChatGPT Leonardo: Model: Lucid Realism, with the Portrait preset. Turn Prompt Enhance off — it rewrites your prompt, which is exactly how identity wording gets lost. Start at 1024px (1024 x 1024, or 1024 on the long side) so facial detail survives. Upload your reference selfie as an image reference and keep its strength moderate — strong enough to anchor the face, not so strong that it copies the original photo's pose and background. ChatGPT image generation: Start the conversation by uploading your reference selfie and your identity block, and tell it to keep this exact face for every image in the chat. Paste the same identity block with each new scene instead of describing the face again in new words. If a result drifts, don't rewrite the whole prompt — tell it what changed ("keep the face identical, only change the setting to a cafe") and generate again with the same reference attached. Common failures (and how to fix them) Face drift: the face slowly morphs from one image to the next. Usually the identity block was reworded or shortened. Fix: paste the full block verbatim, and remove any extra face adjectives from the scene part of the prompt. The age changed: the person looks five years younger or older. Fix: put an explicit age range in the identity block, and avoid loose words like "young", "mature" or "youthful" anywhere else in the prompt. Style drift: a realistic portrait comes back looking illustrated or cinematic. Fix: keep style words in the scene section only, and keep the identity block written in plain photorealistic terms. One stray "cinematic" in the wrong place can restyle the whole face. If you want a head start, I've packed 30 ready-to-use face-lock templates into a bundle on Whop — AI Portrait Prompt Library: 30 Face-Lock Templates for Leonardo & ChatGPT , built around the same identity-block method in this post. The same shop also has a TikTok script pack and an Etsy seller pack if you're building content or a store around your portraits: https://whop.com/zhuai-studio/ — pick what fits your workflow and keep the face locked.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/zhuai_studio/how-i-keep-the-same-face-across-ai-portraits-my-face-lock-workflow-for-leonardo-and-chatgpt-55dm

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
