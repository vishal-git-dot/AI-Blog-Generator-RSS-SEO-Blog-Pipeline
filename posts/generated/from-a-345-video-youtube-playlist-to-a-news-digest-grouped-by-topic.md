---
title: "From a 345-video YouTube playlist to a news digest grouped by topic"
slug: "from-a-345-video-youtube-playlist-to-a-news-digest-grouped-by-topic"
author: "enrico gep"
source: "devto_python"
published: "Thu, 08 Oct 2026 22:48:12 +0000"
description: "I follow a lot of YouTube channels about AI, tech and current affairs, and I make daily news podcasts in Italian. Watching everything is impossible, so I bui..."
keywords: "videos, playlist, supadata, transcript, get, video, youtube, topic"
generated: "2026-10-08T23:09:13.581082"
---

# From a 345-video YouTube playlist to a news digest grouped by topic

## Overview

I follow a lot of YouTube channels about AI, tech and current affairs, and I make daily news podcasts in Italian. Watching everything is impossible, so I built a small pipeline that does the first pass for me: it takes a whole playlist, summarizes every video and groups the summaries by topic into one HTML page I can read in ten minutes. This is what the output looks like (a sample: 8 of the 43 topics from yesterday's run, only the AI and tech ones): Each topic has a short synthesis written by the LLM and the list of videos that talk about it, linked to YouTube. How it works 1. Transcripts with Supadata. The playlist IDs and the native captions come from the Supadata API through its Python SDK ( client.youtube.playlist.videos() and client.transcript(..., mode="native", lang=...) ). At this stage no video or audio is downloaded. The language is inferred from the title and checked against the lang field of the response, because some videos have dubbed tracks in other languages. Requests go through a small rate limiter (the free plan allows 1 request per second) and every transcript is cached on disk, so a restart only fetches what is missing. On this playlist, fetching a transcript took about 4 seconds per video (median). I wrote a separate tutorial with the full, working code for this step: PASTE_TUTORIAL_LINK_HERE 2. Fallback for videos without captions. Only those get their audio downloaded with yt-dlp and transcribed locally with faster-whisper ( large-v3-turbo , batched, on a 6 GB RTX 3060: about 13 seconds for 12 minutes of audio). 3. Summaries. Each transcript is summarized in Italian by an LLM (GLM 5.3 Flash in my setup), four videos at a time. Long transcripts are split into 6,500-word chunks. The videos I care most about get an extra pass that checks the summary against the transcript for missing points. 4. Grouping by topic. The summaries are grouped in batches of 20, then the batch topics are merged into the final list. This merge was the weak spot: with 345 videos the single merge call got too big and timed out twice, so for this run I did the final merge with Claude instead. Next version: save each batch result to disk and merge in two levels. 5. HTML page. A tiny script turns the Markdown digest into one self-contained HTML page with light and dark themes. Numbers from yesterday's run 345 videos in the playlist, 343 summarized (2 had no usable text); 43 topics, from Claude Code "mods" and new models to science and history; transcripts were the fast part; the LLM summaries are now the bottleneck, and that's the next thing I'm optimizing. What I'd tell anyone building something similar Get the text from captions first and keep speech-to-text as a fallback: it's faster, cheaper and avoids downloading hundreds of files. Always check the language of what you get back. And cache every intermediate result, because a long batch can always get interrupted. Disclosure: both Supadata links in this post (above and below) are referral links. If you sign up through either one, I receive free credits. Supadata: https://supadata.ai/r/SD768VWX

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/enrico_gep_b145b3149b358a/from-a-345-video-youtube-playlist-to-a-news-digest-grouped-by-topic-84o

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
