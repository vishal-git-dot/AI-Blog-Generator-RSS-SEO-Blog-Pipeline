---
title: "How I Fixed TTS Hallucinations Without Regenerating Everything"
slug: "how-i-fixed-tts-hallucinations-without-regenerating-everything"
author: "Julian Brown"
source: "devto_python"
published: "Wed, 28 Oct 2026 12:10:58 +0000"
description: "The audit had done its job. I knew where the generated audiobook didn’t match the manuscript. Now I had another problem. Most of the audio around those error..."
keywords: "audio, chapter, performance, replacement, good, model, not, repair"
generated: "2026-10-28T12:28:53.742933"
---

# How I Fixed TTS Hallucinations Without Regenerating Everything

## Overview

The audit had done its job. I knew where the generated audiobook didn’t match the manuscript. Now I had another problem. Most of the audio around those errors was already good. The pacing worked. The voices worked. The performances worked. Regenerating an entire chapter to fix one localized problem meant asking the TTS model to recreate all of that again. And generative audio isn’t deterministic in the ways that matter here. A new generation could change the pacing, emphasis, pauses, emotional delivery, or interaction between voices. I might fix one sentence and lose a performance I already liked. So I stopped thinking about the chapter as something that needed to be regenerated. I started treating it like recorded audio that needed a punch-in. Borrowing From the Recording Studio A punch-in is a familiar idea in audio production. If a musician makes a mistake in one section of an otherwise good recording, you don’t necessarily record the entire performance again. You replace the bad section. The same idea works surprisingly well with generated narration. Instead of: Bad section ↓ Regenerate entire chapter ↓ Hope the new performance is as good I wanted: Good audio ↓ Identify corrupted region ↓ Generate replacement ↓ Match replacement to existing audio ↓ Splice it in ↓ Keep everything else The idea was simple. Making the replacement disappear into the existing performance required three things. Patch Contextual Units, Not Isolated Errors If one word is wrong, generating only that word sounds like the obvious solution. But speech doesn’t work as isolated tokens. Delivery depends on what surrounds a word: pacing, sentence rhythm, emphasis, pauses, and emotional context. So the unit of repair shouldn’t necessarily be the unit of error. If one word is wrong, I may regenerate the sentence. If a sentence is corrupted, I may regenerate the surrounding exchange. The goal is to give the model enough context for a natural performance without replacing more good audio than necessary. Keep the Repair Verbatim The Chapter 9 failure had already demonstrated what could happen when a generative TTS model wandered beyond the manuscript. A repair pass isn’t the place to invite more creativity. The model’s job isn’t to improve or continue the passage. It’s to perform the supplied text verbatim. Conceptually: Speak the supplied text exactly as written. Do not add dialogue. Do not omit dialogue. Do not paraphrase. Do not continue beyond the supplied text. The creative freedom I wanted was in the performance, not the words. Match the Existing Master Even a good replacement can sound like a patch if it doesn’t match the audio around it. So before inserting the replacement, I ran it through the same mastering process as the original chapter. The goal was simple: when the replacement enters, it shouldn’t announce itself as replacement audio. With those three constraints in place, I could repair the actual failure. Repairing the 73-Second Hallucination Chapter 9 was the obvious test. The TTS model had invented roughly 73 seconds of dialogue that wasn’t in the manuscript before eventually finding its way back to the real script. I didn’t want to regenerate the chapter. I wanted to remove the corrupted region and replace it with the exchange that should have been there. The repair region ran from approximately 03:46 to 05:06.75 . That range is wider than the 73-second hallucination itself because the edit needs usable boundaries around the corrupted material rather than cutting at the exact instant the model begins and ends its tangent. The repair became three pieces: Original audio before corruption + Newly generated replacement + Original audio after corruption Using FFmpeg, the operation looked conceptually like this: ffmpeg \ -i chapter_09_master.wav \ -i chapter_09_patch.wav \ -filter_complex " [0:a]atrim=start=0:end=226,asetpts=PTS-STARTPTS[before]; [1:a]asetpts=PTS-STARTPTS[patch]; [0:a]atrim=start=306.75,asetpts=PTS-STARTPTS[after]; [before][patch][after]concat=n=3:v=0:a=1[out] " \ -map "[out]" \ chapter_09_repaired.wav The original chapter stays intact before the edit. The hallucinated region disappears. The newly generated exchange takes its place. Then the original performance resumes. The Result The repaired Chapter 9 dropped from roughly 11 minutes to about 9:51 . The difference wasn’t compression. It was more than a minute of generated material that never belonged there. The intended exchange was restored, and the rest of the performance stayed intact. That was the important part. I didn’t need the model to recreate a chapter that was mostly good. I only needed it to recreate the part that failed. Fix what failed. Keep what worked.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/julianbrown/how-i-fixed-tts-hallucinations-without-regenerating-everything-1c46

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
