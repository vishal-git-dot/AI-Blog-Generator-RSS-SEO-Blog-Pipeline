---
title: "Making Two TTS Voices Sound Like an Actual Conversation"
slug: "making-two-tts-voices-sound-like-an-actual-conversation"
author: "ivyjsu"
source: "devto_python"
published: "Fri, 24 Jul 2026 19:20:55 +0000"
description: "Rendering a document as a two-host podcast is not just alternating two TTS voices line by line. Do that and you get something that sounds like two people rea..."
keywords: "not, two, turn, conversation, tts, voices, mid, you"
generated: "2026-07-24T19:37:11.864550"
---

# Making Two TTS Voices Sound Like an Actual Conversation

## Overview

Rendering a document as a two-host podcast is not just alternating two TTS voices line by line. Do that and you get something that sounds like two people reading unrelated scripts in the same room. The problem is prosody, not voices Human conversation carries information in timing. A reply that arrives instantly reads as agreement. A short gap reads as consideration. Speakers overlap slightly at turn boundaries. Pitch tends to fall at the end of a statement and rise before a handoff. Concatenated TTS has none of this. Each utterance is synthesised in isolation with neutral prosody and identical gaps, and the result sits in an uncanny valley — clearly speech, clearly not conversation. Things that measurably help Vary inter-turn gaps by turn type. Not one fixed pause: Agreement or continuation: short, 150-250ms Topic shift: longer, 400-600ms Answer to a question: short, the responder was already primed After a complex explanation: longer, it reads as processing time A lookup keyed on turn type gets you most of the way, and it is cheap to implement. Write handoffs into the script. The transition matters more than the voice. "Right — so what happens when the file is large?" carries turn-taking structure that "The file size limit is 10MB" does not. This is a scripting problem before it is an audio problem. Do not centre both voices. A few degrees of stereo separation makes two speakers legible to the ear. Hard-panning is disorienting on headphones; subtle offset is not consciously noticed but does the work. Chunking is where quality actually dies Most TTS APIs have input length limits, so long documents get split. Naive splitting at the limit cuts mid-sentence, and the resulting prosody discontinuity is jarring — the pitch contour restarts mid-thought. Split on semantic boundaries — paragraph, then sentence — and never mid-clause. If a single sentence exceeds the limit, split at a comma and accept a small artefact rather than a mid-word cut. Multilingual complicates the pause table Turn-taking norms are not universal. Japanese conversation tolerates longer pauses than English; treating a 600ms gap as "awkward" is an English-specific assumption. If you support multiple languages, the pause table needs to be per-language, not global. I build this into DuoCast — paste text, a PDF, or a URL, get a two-host podcast with the conversational layer handled. Caveat None of this makes synthetic conversation indistinguishable from a real recording. It moves it from "obviously robotic" to "pleasant enough to listen to on a commute," which is a lower but more achievable bar.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/ivyjsu/making-two-tts-voices-sound-like-an-actual-conversation-3hn7

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
