---
title: "One command, one file: script in, 1080p episode and a vertical short out"
slug: "one-command-one-file-script-in-1080p-episode-and-a-vertical-short-out"
author: "EL E"
source: "devto_python"
published: "Sun, 27 Sep 2026 03:44:40 +0000"
description: "I run a small storytelling channel. Every episode needs the same five things done in the same order: clean the script, generate narration, render a 1080p vid..."
keywords: "one, not, script, same, short, output, have, out"
generated: "2026-09-27T04:44:48.252941"
---

# One command, one file: script in, 1080p episode and a vertical short out

## Overview

I run a small storytelling channel. Every episode needs the same five things done in the same order: clean the script, generate narration, render a 1080p video, cut a vertical short, and verify the output is what I think it is. For a while I did that with a folder of half-remembered ffmpeg incantations. Then I wrote it down as one script. Now an episode is a single command: python make_episode.py ep05_minxiong.md ep05_minxiong Here is the actual output from the last run: [1/5] cleaned script: 2096 chars [2/5] narration: ep05_minxiong_narration.mp3 2,658,384 bytes 443.1s [3/5] long video: ep05_minxiong_long_1080p.mp4 6,871,754 bytes / 443.1s [4/5] short cut: ep05_minxiong_short_vertical.mp4 892,786 bytes / 58.0s [5/5] evidence (ffprobe measured, not filename-inferred) Nothing exotic is happening. The interesting part is what I stopped doing. Step 5 is the whole point The last line of that output says "ffprobe measured, not filename-inferred". That exists because of a bug that cost me several planning cycles. Two files in my working directory were called ep02_..._long_1080p.mp4 and ep03_..._long_1080p.mp4 . For weeks they appeared in my schedule as full episodes. They were 80.7 and 78.9 seconds. Nobody had ever measured them. The word long in the filename had been doing the job that a measurement should have been doing. So the pipeline now ends by running ffprobe on everything it produced and printing the real duration and byte count: def evidence ( path ): out = subprocess . run ( [ " ffprobe " , " -v " , " error " , " -show_entries " , " format=duration " , " -of " , " default=noprint_wrappers=1:nokey=1 " , path ], capture_output = True , text = True , check = True ). stdout . strip () return float ( out ), os . path . getsize ( path ) It is four lines. It is also the only part of the script that has ever caught a real problem. A pipeline that does not measure its own output is not a pipeline, it is a hope. The dependency question The whole thing is standard library plus two external binaries: ffmpeg and a text-to-speech CLI. No framework, no orchestration layer, no config format I have to remember the schema of six months from now. That is a deliberate trade. I give up a plugin system I would never have written plugins for, and in exchange the script still runs on a machine I have not touched since I wrote it. There is no lockfile to resolve, no transitive dependency that went unmaintained, no virtualenv that quietly rotted. For a tool that runs on a schedule and that nobody is watching, "still runs a year later" beats "elegant" by a wide margin. Why a short is generated from the same source The vertical cut is not a separate project. It comes out of the same render, in the same run, from the same narration. If I had made it a second workflow, it would have drifted: different intro, different loudness, different title convention. Two pipelines for the same content is two pipelines to keep in sync, and one of them always loses. One honest limitation, stated plainly: the short is currently the first 58 seconds of the long cut, not a selected highlight. That is a known weakness and it is on the list. I would rather ship a mediocre short automatically than a good one manually, because the manual one does not happen on a week when I am busy. The shape that generalizes The specific thing here is video. The shape is not: A repeated task that has an order to it. One command that does the whole order. A final step that measures the output and prints the number . That third step is the one people skip, and it is the one that turns "the script said it worked" into "the file is 443.1 seconds and 6.8 MB". Those are different claims, and only one of them is evidence. I build these pipelines to order — content production, ops automation, scheduled jobs. Single file, zero third-party Python dependencies, and a final step that proves what it produced. Available for hire on Fiverr .

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/el_e_3dc94dfc336bfb025ef2/one-command-one-file-script-in-1080p-episode-and-a-vertical-short-out-4c9i

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
