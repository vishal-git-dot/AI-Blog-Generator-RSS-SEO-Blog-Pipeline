---
title: "How to catch caption timing drift in a 29.97 fps video export with Python"
slug: "how-to-catch-caption-timing-drift-in-a-2997-fps-video-export-with-python"
author: "Anlin"
source: "devto_python"
published: "Sun, 08 Nov 2026 05:13:20 +0000"
description: "A caption that looks fine at the start of a movie recap can land noticeably early or late near the end. Measure the error at several known frames before shif..."
keywords: "frame, subtitle, cue, caption, fps, rate, export, start"
generated: "2026-11-08T05:28:47.822892"
---

# How to catch caption timing drift in a 29.97 fps video export with Python

## Overview

A caption that looks fine at the start of a movie recap can land noticeably early or late near the end. Measure the error at several known frames before shifting individual cues. A constant error suggests a shifted start time. An error that grows with elapsed time suggests a clock or frame-rate conversion problem. Cover: AI-generated schematic showing caption cues moving progressively ahead of the frame clock. The gaps are exaggerated and not to scale. Use the exact frame rate Assume a constant-frame-rate export at 30000/1001 fps. Frame 0 and subtitle time 0 share the same origin. Each expected caption onset is a zero-based frame index on the output timeline. The actual onset comes from the subtitle export in milliseconds. Keep the math exact until reporting the result. At frame 17,982, the expected time is 17982 × 1001 / 30000 , or 599.9994 seconds. Treating the same frame index as 30 fps gives 599.4 seconds. The clocks differ by 599.4 milliseconds after about ten minutes. Check three known onsets This example uses fictional data and runs with Python's standard library. Positive error means the caption starts late. One frame is a simple tolerance for this example. Set your real tolerance based on the cues and delivery requirements of the project. from fractions import Fraction fps = Fraction ( 30_000 , 1_001 ) frame_ms = 1_000 / fps # (name, expected output frame index, actual subtitle start in ms) anchors = [ ( ' opening cue ' , 0 , 0 ), ( ' middle cue ' , 8_991 , 299_700 ), ( ' final cue ' , 17_982 , 599_400 ), ] for name , frame , actual_ms in anchors : expected_ms = frame * frame_ms error_ms = actual_ms - expected_ms result = ' REVIEW ' if abs ( error_ms ) > frame_ms else ' OK ' print ( f ' { name : < 12 } { float ( error_ms ) : + 8.1 f } ms { result } ' ) opening cue +0.0 ms OK middle cue -299.7 ms REVIEW final cue -599.4 ms REVIEW Here the captions start early, and the error grows nearly linearly. The fictional subtitle times were deliberately calculated at 30 fps. In a real export, compare the frame-rate metadata and subtitle timing first. If all three errors instead cluster around the same offset, check whether the video, audio, and subtitle exports started at the same point. Know when to use presentation timestamps The frame formula works for constant frame rate with a shared origin. For variable-frame-rate footage, use each output frame's presentation timestamp and apply the track's time base. B-frames can appear in decode order that differs from presentation order, so compare frames in the order viewers see them. Normalize any nonzero stream start to the subtitle timeline before measuring the difference. After fixing a suspected conversion or offset, export again and check the same anchors. Watch one short excerpt around a story cue to make sure the caption lands when the viewer needs it. AI disclosure: AI generated this article and its example. The Python example was executed to verify the output.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/_a2923b30009c0d41b7dad/how-to-catch-caption-timing-drift-in-a-2997-fps-video-export-with-python-5cd7

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
