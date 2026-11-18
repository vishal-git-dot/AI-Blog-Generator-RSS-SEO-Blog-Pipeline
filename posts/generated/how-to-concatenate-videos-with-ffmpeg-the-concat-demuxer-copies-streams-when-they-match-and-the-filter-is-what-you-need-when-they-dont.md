---
title: "How to Concatenate Videos With FFmpeg: The Concat Demuxer Copies Streams When They Match, and the Filter Is What You Need When They Don't"
slug: "how-to-concatenate-videos-with-ffmpeg-the-concat-demuxer-copies-streams-when-they-match-and-the-filter-is-what-you-need-when-they-dont"
author: "Voor AI"
source: "devto_python"
published: "Wed, 18 Nov 2026 00:48:39 +0000"
description: "Short answer: to join two clips end to end, write a text list and pass it to FFmpeg's concat demuxer with -c copy only when both files already share a codec,..."
keywords: "concat, copy, not, frame, ffmpeg, demuxer, when, you"
generated: "2026-11-18T00:48:50.457547"
---

# How to Concatenate Videos With FFmpeg: The Concat Demuxer Copies Streams When They Match, and the Filter Is What You Need When They Don't

## Overview

Short answer: to join two clips end to end, write a text list and pass it to FFmpeg's concat demuxer with -c copy only when both files already share a codec, frame size, and timebase. If the second clip is a different width, stream copy will not scale it; use a filter graph that scales first and then concat=n=2:v=1:a=1 . The five pytest checks below were run on a real 12.064-second 720×1280 fixture ( grey-hoodie-v2.mp4 , md5 a50e13313b71a76dbd179dcdc2c2b6bf ). This is a reproducible FFmpeg/Python check, not a product walkthrough. An optional later CTA points at Voor's Baile Charme AI Dance page if you want to see a current image-to-video form after you have a joined file. Why -c copy is not a join button FFmpeg has two common "concat" paths, and they do different jobs. The concat demuxer reads a list of files and can stream-copy packets: ffmpeg -f concat -safe 0 -i list.txt -c copy joined.mp4 The list is plain text, one path per line: file '/absolute/path/part-a-6s.mp4' file '/absolute/path/part-b-rest.mp4' -safe 0 is required when those paths are absolute. The demuxer does not resample video. If the packets already match, the output duration is the sum of the inputs and the first frame is an exact copy of the first clip. The concat filter is a filter-graph operation. It re-encodes, and you can scale or pad a mismatched input before the join: ffmpeg -i part-a-6s.mp4 -i part-b-640-wide.mp4 \ -filter_complex "[1:v]scale=720:1280,setsar=1[v1];[0:v][0:a][v1][1:a]concat=n=2:v=1:a=1[v][a]" \ -map "[v]" -map "[a]" -c:v libx264 -c:a aac joined.mp4 concat=n=2:v=1:a=0 is the silent-video form. These clips have AAC audio, so the graph uses v=1:a=1 . The fixture and the two matching parts The source clip is 12.064 seconds, H.264 720×1280 at 24 fps, with a stereo AAC track at 32 kHz. To give the demuxer two legal inputs, the tests re-encode a 6.0-second head and the remainder with the same libx264/AAC settings. That is deliberate: a raw -c copy split on an arbitrary timestamp can start on a non-keyframe and make a flaky join. Five pytest checks All five passed in 1.76 seconds ( uvx --from pytest pytest -q test_concat.py ). Matching parts share codec and size. Both segments are H.264 720×1280 with AAC. The head is 6.0 seconds; the tail is the remainder of the 12.064-second source. Concat demuxer + -c copy sums duration. The joined file is H.264+AAC, 720×1280, and its duration equals the sum of the two parts (12.096 seconds on this run, within 0.12 seconds of the sum). The first frame is an exact copy. The RGB24 md5 of frame 0 in the joined file matches frame 0 of part A. Copy does not fix a resolution mismatch. Part B is scaled to 640×1136 and listed after part A. ffmpeg -f concat -c copy still exits 0 on this pair, but the coded width of the output stays 720 — the second clip is not resized. That is the trap. The concat filter joins after scaling. The same 640-wide clip is scaled back to 720×1280 in a filter graph ( concat=n=2:v=1:a=1 ). The output is 720×1280 with audio, and the duration matches the sum (12.064 seconds on this run). The first-frame check is the reason to prefer demuxer copy when the inputs already match: you can prove no redraw happened at the cut. What I would not trust without a test Joining a 1080p clip to a 720p clip with -c copy and assuming the player will scale the second half. A concat list with unsanitized relative paths and no -safe 0 , or the opposite: -safe 1 with absolute paths. concat=n=2:v=1:a=1 on a silent video (no audio stream) — that graph will fail; use a=0 . Measuring "length" from the container alone when you also care that frame 0 is unchanged. Duration can look right after a re-encode even when the first frame does not. Optional next step If you are joining generated shorts and then want a current image-to-video form, Voor's Baile Charme AI Dance page is a live generator with a visible credit quote. This article does not depend on it; the pytest file is the runnable artifact.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/voorai/how-to-concatenate-videos-with-ffmpeg-the-concat-demuxer-copies-streams-when-they-match-and-the-30fl

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
