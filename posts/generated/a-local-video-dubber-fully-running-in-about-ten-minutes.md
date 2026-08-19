---
title: "A Local Video Dubber, Fully Running, in About Ten Minutes"
slug: "a-local-video-dubber-fully-running-in-about-ten-minutes"
author: "Syed Masood Shah"
source: "devto_python"
published: "Wed, 19 Aug 2026 01:29:13 +0000"
description: "I've sat through a lot of "10-minute setup" tutorials that secretly take an hour. So let me be straight with you up front: this one really took me about ten ..."
keywords: "you, local, two, audio, your, install, livedub, one"
generated: "2026-08-19T01:37:09.903249"
---

# A Local Video Dubber, Fully Running, in About Ten Minutes

## Overview

I've sat through a lot of "10-minute setup" tutorials that secretly take an hour. So let me be straight with you up front: this one really took me about ten minutes, mostly because nothing here fights you. No compiling, no API keys, no juggling cloud credentials. If you're on Windows with Python 3.10 or newer, this should just work. Before we start, here's the two-second version of what you're building. A browser extension grabs the audio from whatever video is playing. A local Whisper model turns that into text. LM Studio's local LLM translates it. A neural TTS model called Kokoro reads the translated words out loud, and it automatically switches between male and female voices based on pitch. The original audio ducks underneath so you actually hear the dub. Every step runs on your machine. Nothing gets uploaded anywhere. Here's the whole walkthrough. Step one: install Python and LM Studio Get Python 3.10 or newer if you don't already have it. Then install LM Studio — it's free. Download one small model into it; a couple of GB is plenty. You do not need a GPU. A decent CPU handles this fine, a GPU just makes it snappier. Step two: install the browser extension Add the LiveDub extension to your browser. It asks permission to capture tab audio, which sounds more alarming than it is — that's just how a browser hands audio to a local app. No audio ever leaves your machine. Step three: start the local server Run the LiveDub app on Windows. It starts a small local helper that connects the extension to your models. Create a virtual environment, install the dependencies, and run it: pip install -r requirements.txt python livedub.py That's the whole setup. Play any video — a foreign film, a YouTube clip, a file on your own disk — and within a sentence or two you'll hear the dub follow along. Two things worth knowing so you're not blindsided. There's a natural delay of a sentence or two. That's not a bug and it can't be avoided: the tool literally cannot translate until the speaker finishes talking. Every dubbing pipeline works this way, cloud-based or local. And yes, you need internet for that first model download; after that it's fully offline. Does listening to a real-time dub feel like cheating at watching movies? A little. But I mostly use it for two things: keeping up with foreign cinema and actually improving at languages. Watching something in a language I'm trying to learn, with a live translation read over the top, has been genuinely useful — I catch words I'd never pick up just reading subtitles, because I'm hearing them spoken instead of scanning text. If you'd rather skip the assembly and have the thing working tonight, LiveDub is a one-time $19 purchase for Windows — https://symshah.gumroad.com/l/livedub — no subscription, no per-token bills, and it keeps running after you yank the internet cable. Either path, ten minutes and you're done.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/syed_masoodshah_1984/a-local-video-dubber-fully-running-in-about-ten-minutes-424j

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
