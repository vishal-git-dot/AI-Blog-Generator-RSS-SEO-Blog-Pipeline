---
title: "Rendering a Blender animation in drafts from Cursor or Claude Code: 48 frames first, then the full shot without paying for them twice"
slug: "rendering-a-blender-animation-in-drafts-from-cursor-or-claude-code-48-frames-first-then-the-full-shot-without-paying-for-them-twice"
author: "JANCTION Render"
source: "devto_ai"
published: "Wed, 04 Nov 2026 05:39:02 +0000"
description: "When an AI agent in my editor builds a Blender animation, the expensive part is not the first render. It is the second and third ones: the camera is a little..."
keywords: "frames, gpu, seconds, render, jpy, agent, janction, draft"
generated: "2026-11-04T05:43:20.848430"
---

# Rendering a Blender animation in drafts from Cursor or Claude Code: 48 frames first, then the full shot without paying for them twice

## Overview

When an AI agent in my editor builds a Blender animation, the expensive part is not the first render. It is the second and third ones: the camera is a little off, the color is wrong, the client wants it longer. I wanted to see what that loop actually costs when the agent renders on a cloud GPU over MCP, so I ran one shot end to end and wrote down every number. The scene is a 5-second product reveal (120 frames at 24 fps): a bottle on a turntable, the camera dollying in. Everything below was driven through the JANCTION Render MCP server, the same way it runs from Cursor, Claude Code or OpenCode. Disclosure: I work on JANCTION Render. Connecting the agent Cursor ( .cursor/mcp.json ): { "mcpServers" : { "janction-render" : { "url" : "https://render.janction.jp/mcp" } } } Claude Code: claude mcp add --transport http janction-render https://render.janction.jp/mcp OpenCode ( opencode.json ): { "$schema" : "https://opencode.ai/config.json" , "mcp" : { "janction-render" : { "type" : "remote" , "url" : "https://render.janction.jp/mcp" } } } No local Blender and no GPU are needed. The agent writes a bpy script (or sends a .blend) and gets images or an MP4 back. 1. Preview: four frames in one image, free The agent's first call was a preview of frames 1, 40, 80 and 120 tiled in one image. It came back in 6 seconds (4.65 GPU-seconds) and cost nothing: previews are free up to 2 GPU-minutes a day. The built-in critic said "ok" (exposure, framing, lighting). But at frame 120 the camera had pushed in so far that the bottle's cap was cut off. The critic checks each frame for obvious problems; it does not know that the cap matters to me. So the agent moved the end of the camera move back and previewed again: 5 seconds, 4.73 GPU-seconds, free, cap in frame. This is the cheapest place to iterate. Two previews, zero yen, and the shot was fixed before any final frame existed. 2. A 48-frame draft on the final settings Before committing to 120 frames at 1920x1080 and 128 samples (Cycles), the agent asked for an estimate of frames 1-48. The estimate was 454 GPU-seconds, about 46 JPY, and it said so itself: confidence low, because this scene had never been rendered at final quality, so it was going by my earlier renders. The draft came back in 65 seconds: 179 GPU-seconds, 18 JPY. The estimate was about 2.5 times too high, which is the safe direction (only the GPU time actually used is charged; the rest of the hold comes back). After this draft, the service had a measured per-frame time for this exact scene, and the next estimate was marked confidence high. 3. The full 120 frames, without re-rendering the draft Then the agent asked for frames 1-120 with the same scene and the same settings. The service noticed that frames 1-48 had already been rendered by this key, for this scene, with identical picture settings, and copied them instead of rendering them again. 4 of the 12 chunks were copies; only frames 49-120 went to a GPU. Result: 103 seconds, 272 GPU-seconds, 28 JPY. Rendering all 120 frames from scratch would have been about 440 GPU-seconds at the draft's 3.7 seconds per frame, so the draft was not wasted money. The rule is strict on purpose. Copies are only used when the key, the uploaded scene and the picture settings (size, samples, engine, lighting preset) all match. Change any of them and the frames are rendered again. 4. A real revision: new color, full re-render Next revision: green instead of blue. That is a new script, so it is a new scene, and nothing can be reused. The full 120 frames took 139 seconds, 418 GPU-seconds, 42 JPY. The numbers Step Wall time GPU-seconds Cost Preview, 4 frames (v1) 6 s 4.65 free Preview, 4 frames (v2, camera fixed) 5 s 4.73 free Draft, frames 1-48, 1080p 65 s 179 18 JPY Full, frames 1-120 (1-48 copied) 103 s 272 28 JPY Revision, new color, frames 1-120 139 s 418 42 JPY Total: 88 JPY (about 0.56 USD) for two previews, a draft, the full shot and one full revision. That fits inside the free credit a new key starts with: 100 JPY of GPU time with no card, 400 JPY more after saving a card that is not charged; after that, previews stay free up to 2 GPU-minutes a day and finals cost 0.1 JPY per GPU-second. Current prices are always on https://render.janction.jp/pricing . What I would tell an agent to do Iterate on previews. Four tiled frames cost one 720p frame of GPU time and are free within the daily allowance. Draft a short contiguous range on the final settings before the full animation. It catches problems that previews do not show and calibrates the estimate for the rest. Extend the range with the same scene_id and the same settings. Frames already rendered are copied, not billed again. Treat any change to the scene or the settings as a new render, and say the price before starting it. A max_yen cap on the call refuses anything above it, and an idempotency_key keeps a retried call from rendering twice. The scripts for all three versions are short enough to paste into a chat; ask your agent to "build a 5-second product reveal of a bottle on a turntable with a camera dolly, preview frames 1, 40, 80 and 120" and it will write something close.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/_903a3934b362f0afe2a8/rendering-a-blender-animation-in-drafts-from-cursor-or-claude-code-48-frames-first-then-the-full-4ci9

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
