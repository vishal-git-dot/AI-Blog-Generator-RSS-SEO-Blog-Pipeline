---
title: "I stopped reading subtitles in video. I built a video voice translator, keep the tone, keep the emotion."
slug: "i-stopped-reading-subtitles-in-video-i-built-a-video-voice-translator-keep-the-tone-keep-the-emotion"
author: "Qiushui"
source: "devto_ai"
published: "Sun, 25 Oct 2026 03:58:23 +0000"
description: "One evening last year, I was watching an insightful tech video on my computer. It was in English with Chinese subtitles. As I watched, a thought struck me: I..."
keywords: "video, you, but, can, voice, one, something, your"
generated: "2026-10-25T04:06:12.675397"
---

# I stopped reading subtitles in video. I built a video voice translator, keep the tone, keep the emotion.

## Overview

One evening last year, I was watching an insightful tech video on my computer. It was in English with Chinese subtitles. As I watched, a thought struck me: I wish I could just listen to the Chinese version. No need to stare at subtitles all the time. I could listen during my commute, before bed, wherever. Eventually, I actually built it. But from the moment the idea struck me to creating a product everyone could use, it took far longer than I expected. After the idea came, I tried a few video translation tools. Chinese translation was there, but something always felt off when I listened. The person in the video was still there, but it was no longer their voice. The emotion in how they spoke each sentence, also gone. Imagine a face you know well, suddenly speaking in a different tone, a different voice. You can follow the meaning, but that connection breaks. It's like watching a familiar person while hearing a stranger speak for them. What I really wanted was simple. Translate to Chinese, but keep the original voice intact. Keep the emotion, the nuance in how they say each word. These small details in a voice matter. The same sentence said softly versus forcefully hits you completely differently. I searched around and found a model approach. At the time, options were limited, but this approach's voice preservation quality gave me hope. Having a model is one thing. Getting a finished video is another. The inference was painfully slow, and I couldn't just throw an entire video at it and wait for perfectly translated output with audio synced with the video, all while preserving background music. I had to wire everything together myself. After I shared some samples, quite a few people asked if I could turn it into a tool everyone could use. I thought so too. Honestly, with AI-assisted coding, I figured it would be fast, right? The core translation pipeline was working. Everything else? Just building a website for video uploads. Turns out, it took a year. Turns out building something you can demo and building something people can reliably use are very different things. Using it myself, all I needed was proper video processing. But for others, I needed registration, login, data persistence. One user's data can't leak to another's. Multiple concurrent uploads can't crash the system. What if the system goes down? What if users multiply and I need to scale? Would users instinctively know how to use it? Databases, servers, object storage, domains, DNS, one by one, you have to get them right. Each piece seems fine alone, but how do you wire them together so people can smoothly use your service? There's always something else, and something else after that. AI can help. But whether it's right, what to do when something breaks, that's still on you. So why keep going? Because I promised. I promised the people who wanted this, promised myself. That thought kept me going. Now, finally, I can deliver. It's called SoulDub , dubbing with soul. It supports 30+ languages and some dialects. Using it is straightforward: Web way: Go to souldub.ai, upload a video, pick a language, hit start. That's it. Agent way: Search for github-souldub-skills in your browser and install it via your preferred Agent (ChatGPT, Claude, Gemini, etc.) and have it install the skill. After that, your Agent can translate your local videos. The translated video and subtitles automatically download to the original video's folder. Videos from both methods show up in your SoulDub account. One more critical piece: manual review and editing. If a subtitle isn't quite right, if a dubbed voice needs adjustment, you edit it directly on the site. The AI does the first pass, then you refine the parts that matter to you. Quality keeps going up. Give it a try. Any feedback, questions, ideas, I'm here listening. How to translate a person's voice in a video in three steps

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/zainingqiushui/i-stopped-reading-subtitles-in-video-i-built-a-video-voice-translator-keep-the-tone-keep-the-35ce

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
