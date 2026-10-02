---
title: "Two-photo inputs beat a blank prompt: building Hotel Lobby AI with Next.js"
slug: "two-photo-inputs-beat-a-blank-prompt-building-hotel-lobby-ai-with-nextjs"
author: "zhifen zhu"
source: "devto_ai"
published: "Fri, 02 Oct 2026 12:10:36 +0000"
description: "I built Hotel Lobby AI , a focused tool that turns two separate photos into an orange-booth rap duo video with generated audio. Here are a few implementation..."
keywords: "two, photo, separate, file, preview, use, hotel, lobby"
generated: "2026-10-02T12:13:45.784277"
---

# Two-photo inputs beat a blank prompt: building Hotel Lobby AI with Next.js

## Overview

I built Hotel Lobby AI , a focused tool that turns two separate photos into an orange-booth rap duo video with generated audio. Here are a few implementation and interface decisions from a small Next.js, React, and TypeScript project. Give each upload a meaning Instead of one generic image picker, the interface asks for a left performer and a right performer. The implementation keeps two separate File values and two preview URLs. That makes the intended placement explicit before generation starts. The request also preserves the distinction: the multipart form has separate person1 and person2 fields, and the server validates both images. The useful idea is not the field names themselves; it is making the UI and request contract tell the same story. A preview has a lifecycle The photo previews use URL.createObjectURL . In a React component, replacing a selected file should also retire its old preview URL. Keeping preview state separate from output state helps avoid showing a generated result where the source photo is expected. For anyone building an upload-driven tool, I would check three states early: a new file selection, a replacement selection, and a missing required file. Those small transitions are easy to overlook when most attention goes to the model call. Expose useful choices, keep the scene focused The user can choose duration, 480P or 720P quality, and portrait or landscape format. The prepared performance workflow removes the need to write a prompt or edit a timeline. This is intentionally a narrow creative tool, not an attempt to expose every possible model parameter. The output includes generated audio and can be downloaded. Faces may vary from the source photos, so clear input guidance and realistic expectations matter. People should use photos they have permission to use. Explain the trial before generation Google sign-in is required. New users receive 20 credits, enough for one 4-second 480P trial. Further generations use credits available through one-time purchases. I prefer stating those conditions directly instead of calling the entire service unlimited or completely free. You can try the workflow at https://hotel-lobby-ai.org . I would welcome feedback on the clarity of the two-photo inputs, or how you structure upload state in your own React projects.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/zhifen_zhu_3df68293e0ddb6/two-photo-inputs-beat-a-blank-prompt-building-hotel-lobby-ai-with-nextjs-fo9

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
