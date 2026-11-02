---
title: "How I Rendered 159 Narrated Lesson Videos With Free, Open-Source Tools"
slug: "how-i-rendered-159-narrated-lesson-videos-with-free-open-source-tools"
author: "Sean Ofodile"
source: "devto_python"
published: "Mon, 02 Nov 2026 15:12:05 +0000"
description: "For CoreQ Academy , my free cybersecurity training platform, I wanted a video for every lesson: 125 certification-level objectives, 19 track lessons, 7 Linux..."
keywords: "lesson, free, each, videos, video, lessons, narration, rendered"
generated: "2026-11-02T15:18:23.747382"
---

# How I Rendered 159 Narrated Lesson Videos With Free, Open-Source Tools

## Overview

For CoreQ Academy , my free cybersecurity training platform, I wanted a video for every lesson: 125 certification-level objectives, 19 track lessons, 7 Linux modules and 8 lab briefings. Recording 159 videos by hand wasn't realistic, so I built a pipeline that turns lesson content into narrated 1080p videos on an ordinary CPU, with no paid services. The pipeline lesson data (TypeScript) -> video spec (JSON) -> narration (Kokoro TTS) -> slides (HTML rendered in Chromium) -> MP4 + captions + chapters (ffmpeg) 1. Specs generated from the lessons Each lesson already exists as structured data: an intro, groups of terms with definitions, a scenario and a quiz. A script converts that into a scene list. Each scene has a slide layout and "steps": one sentence of narration plus which element to reveal. Because specs are generated from the same source as the website, videos never drift out of sync with the lessons. 2. Narration with an open neural voice I used Kokoro via ONNX Runtime. On an 8-core CPU it renders speech about three times faster than real time. A small pronunciation layer handles security vocabulary: def speakable ( t ): # read file paths aloud, spell out most acronyms, keep pronounceable ones t = re . sub ( r ' (?<![\w])(~?/[\w./-]*) ' , path_to_words , t ) # /etc/ssh -> "slash etc slash ssh" t = re . sub ( r ' \b([A-Z]{2,6})\b ' , spell_unless_word , t ) # IAM -> "I A M", NIST stays "NIST" return t 3. Slides as HTML Slides are plain HTML and CSS in the site's brand, rendered at 1920x1080 with Playwright. Each newly revealed element gets about nine animation frames for an ease-in, then holds while the narration plays. HTML means real fonts, perfect text and layouts I can test like a web page. 4. Assembly with ffmpeg An ffmpeg concat list gives each frame its exact duration, the narration is loudness-normalised ( loudnorm=I=-16 ), and the output is H.264 tuned for still images. A five-minute lesson comes out around 10 to 14 MB at 1080p. Captions (WebVTT) and chapter timestamps come free, because the pipeline knows exactly when each sentence starts. Lessons learned the hard way Clean up temp files. My first batch wrote hundreds of PNG frames per video to /tmp and never deleted them. Around video 120, the system disk hit 100%. Now each video renders in a work directory that's removed in a finally block. Make batches resumable. Skip videos whose output is newer than their spec. Restarts become free. Don't run two batches at once. Two processes writing the same output file will corrupt each other. Results 159 videos and about 5.6 hours of narrated lessons, rendered for free, with captions and chapters, organised for YouTube upload. The Security+ level series is live on YouTube , and every video links back to its free lesson, quiz and lab. I'm Sean Ofodile, a cybersecurity leader, founder of Quantum Core Services and CIO of Seenu.io , an early-stage social discovery startup. I teach free cybersecurity classes at CoreQ Academy and on YouTube as Professor Sean Ofodile, and was featured on 11Alive in Atlanta with the Seenu team.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/seanofodile/how-i-rendered-159-narrated-lesson-videos-with-free-open-source-tools-213a

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
