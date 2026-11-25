---
title: "Wan 2.2 S2V in ComfyUI: text, image and pose conditioning with audio"
slug: "wan-22-s2v-in-comfyui-text-image-and-pose-conditioning-with-audio"
author: "AI-KSK"
source: "devto_ai"
published: "Wed, 25 Nov 2026 21:18:40 +0000"
description: "Wan 2.2 S2V is an audio-driven video model with several conditioning paths: text plus audio, text plus image plus audio, and pose/video control plus text and..."
keywords: "audio, text, image, video, plus, pose, control, reference"
generated: "2026-11-25T21:26:57.090205"
---

# Wan 2.2 S2V in ComfyUI: text, image and pose conditioning with audio

## Overview

Wan 2.2 S2V is an audio-driven video model with several conditioning paths: text plus audio, text plus image plus audio, and pose/video control plus text and audio. The episode builds these in ComfyUI and tests a cloud image. Watch the episode: https://youtu.be/pE56YlWiZFc Chinese original: https://www.bilibili.com/video/BV1hwhmzLEQ5 Image entry: https://www.compshare.cn/images/PBDSdOcBm3T3?referral_code=A7fTQUYY9lCDFJwA6MMvoq Input combinations Text + audio: a speaking person generated from a description and voice track. Text + image + audio: character-specific lip sync, for real or anime images. Control video + text + audio: pose-guided speaking video. Image reference + control video + audio: possible, but less strong in the test. Tested settings The official flow is accelerated at six steps and CFG 1. Audio uses the MultiTalk-derived preprocessing path: optional trimming and voice separation. The official audio encoder is English-only at this point; Chinese support is expected later. A 48GB 4090 is recommended for higher resolution. The cloud image includes the workflows and a one-click startup path; trial hours are point-in-time terms. Observed results The text-plus-audio result is natural. Pose control follows the source video closely, and image plus pose plus audio produces matching lip sync and body motion. The model also invents body parts beyond the head reference. Combining image reference with motion reference works but is weaker. The episode keeps text short because too much instruction can pull the result away from the intended motion. Known limits English audio encoding only in the tested release. Combining every conditioning path does not guarantee a better result. Short prompts preserve motion better. No workflow JSON or weights are bundled with this article.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/ai-ksk/wan-22-s2v-in-comfyui-text-image-and-pose-conditioning-with-audio-ndo

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
