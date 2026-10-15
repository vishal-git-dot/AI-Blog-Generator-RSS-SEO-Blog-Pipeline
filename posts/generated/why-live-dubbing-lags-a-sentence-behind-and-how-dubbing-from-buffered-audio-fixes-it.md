---
title: "Why live dubbing lags a sentence behind, and how dubbing from buffered audio fixes it"
slug: "why-live-dubbing-lags-a-sentence-behind-and-how-dubbing-from-buffered-audio-fixes-it"
author: "Chris Cornell"
source: "devto_webdev"
published: "Thu, 15 Oct 2026 03:46:53 +0000"
description: "Disclosure: I work on EarDub, a browser extension that dubs videos into other languages. This post is about a design problem we hit, not a product pitch, but..."
keywords: "sentence, video, you, can, audio, ahead, buffered, has"
generated: "2026-10-15T04:04:26.698863"
---

# Why live dubbing lags a sentence behind, and how dubbing from buffered audio fixes it

## Overview

Disclosure: I work on EarDub, a browser extension that dubs videos into other languages. This post is about a design problem we hit, not a product pitch, but the product comes up at the end. If you've tried a "real-time" video translator that listens to a video and speaks a translation, you've probably noticed the voice runs about one sentence behind the speaker. The person on screen finishes a thought, there's a pause, then the translation starts, and by then the speaker is already on the next point. On a talk or tutorial, that lag makes the dub feel like a bad simultaneous interpreter. This post explains why that happens and the approach we took to remove most of it for videos that have no captions. Why listen-as-it-plays dubbing trails the picture A tool that captures audio as it comes out of the speakers can only work with what has already been played. To translate a sentence well, you need the whole sentence, because word order changes between languages: a German verb can land at the end, and a Japanese sentence can flip the order of a whole clause. So the pipeline has to: wait for the speaker to finish the sentence, run speech recognition on it, translate it, synthesize speech, play it. Steps 2 to 4 take time, and step 1 alone guarantees the dub starts after the original sentence ends. That's the one-sentence lag. You can shorten it by translating partial sentences, but then the translation gets worse, which is the trade-off live interpreters face. Recorded video is different: the player already has the future For recorded video (not live streams), the browser's media player downloads ahead of the playhead. You can see this yourself in any page with a <video> element: const v = document . querySelector ( ' video ' ); for ( let i = 0 ; i < v . buffered . length ; i ++ ) { console . log ( v . buffered . start ( i ), v . buffered . end ( i )); } console . log ( ' playing at ' , v . currentTime ); The buffered ranges usually extend well past currentTime ( MDN: HTMLMediaElement.buffered ). That audio exists before the viewer hears it. If you recognize speech from the audio the player has already loaded, you're working ahead of the viewer instead of behind them. That changes the pipeline: Recognition runs on audio that's ahead of the playhead. Fragments are joined into complete sentences before translation, so you never have to translate half a thought. The translated sentence is synthesized and queued against the original timing, so it can start when the speaker starts that sentence. The viewer gets a dub that starts with the speaker instead of a sentence later. The details that matter in practice A few things we learned building this: Stay a few sentences ahead, not the whole video. Processing an entire video up front means a long wait before anything plays. Keeping a small window ahead of the playhead lets the first sentence start within seconds, and you pause when the video pauses. Seeking resets the window. When someone jumps to a new point, there's nothing prepared there yet, so the first sentence after a jump takes a few seconds. After that, the window refills ahead of playback. Translated sentences don't always fit. A translation can be longer than the original. Cutting it off sounds broken, so we let the voice speed up gently, capped at 1.45x, and never stop a sentence mid-word. At very high playback rates some sentences can't physically fit, so it's better to skip one than to cut one in half. That's why we recommend staying at 1.5x video speed or below while dubbing. Context beats word-for-word. Translating each sentence with the video's title and surrounding sentences as context keeps names and technical terms consistent across a long tutorial. Know what it can't do. Working ahead requires a recorded video, so live streams are out. Loud music, overlapping speakers and heavy accents still cause recognition errors. One voice reads everyone, because recognized speech doesn't say who is talking. Captions first, audio when there are none When a video already has captions, including auto-generated ones, you don't need speech recognition at all. The caption timing tells you exactly when each sentence starts. Audio recognition is the fallback for videos without captions. Where this ended up This is how EarDub handles videos without captions on YouTube, X, Bilibili and Gumroad (on its paid plans). Captioned videos work on the free plan, including Udemy and Coursera lectures. Audio sent for recognition is processed into text and not stored. If you want to try it, the user-facing details are on the EarDub site, and the extension is on the Chrome Web Store . I'd love to hear from anyone who has worked on similar timing problems, especially sentence segmentation for languages without spaces between words.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/chriscornell/why-live-dubbing-lags-a-sentence-behind-and-how-dubbing-from-buffered-audio-fixes-it-5pe

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
