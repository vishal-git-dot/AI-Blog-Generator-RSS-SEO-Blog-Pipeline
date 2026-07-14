---
title: "I Made My Voice Agent Feel Faster by Streaming Sentences, Not Audio"
slug: "i-made-my-voice-agent-feel-faster-by-streaming-sentences-not-audio"
author: "Todd Sullivan"
source: "devto_python"
published: "Tue, 14 Jul 2026 08:05:39 +0000"
description: "The annoying thing about voice agents is that “the model is fast” does not mean the experience is fast. I had a small voice assistant running on a local devi..."
keywords: "sentence, not, sentences, model, chat, voice, audio, backend"
generated: "2026-07-14T08:17:51.107042"
---

# I Made My Voice Agent Feel Faster by Streaming Sentences, Not Audio

## Overview

The annoying thing about voice agents is that “the model is fast” does not mean the experience is fast. I had a small voice assistant running on a local device, talking to a hosted chat backend. The actual LLM call was only one part of the wait. The full path looked more like this: wake word detection speech recognition authenticated /chat call model response local TTS synthesis audio playback If you wait for step 4 to finish before starting step 5, the user hears nothing until the entire reply is done. That feels dead, even when the backend is technically fine. So I changed the contract. The hardware client now calls the chat endpoint with stream_tts: true : response = self . session . post ( f " { CHAT_API_BASE } /chat " , json = { " message " : message , " stream_tts " : True }, timeout = 30 , stream = True , ) The backend yields text chunks as they arrive from the model. The device keeps a small buffer, splits complete sentences, and starts synthesizing each sentence immediately: _SENTENCE_BOUNDARY_RE = re . compile ( r ' (?<=[.!?])\s+ ' ) def split_complete_sentences ( buffer : str ) -> tuple [ list [ str ], str ]: * sentences , remainder = _SENTENCE_BOUNDARY_RE . split ( buffer ) return [ s . strip () for s in sentences if s . strip ()], remainder That is deliberately boring. Not phoneme streaming. Not a custom audio protocol. Just sentence-level pipelining. The next useful bit was overlapping synthesis and playback. A single background worker waits for synthesized WAV files and plays them in order, while a one-worker ThreadPoolExecutor starts rendering the next sentence as soon as it is complete. for sentence in sentences : future = synth_executor . submit ( self . tts_engine . synthesize , sentence ) playback_queue . put (( sentence , future )) That removed the worst gap: “sentence one finished playing, now start thinking about sentence two’s audio.” The hardware now does the obvious thing a human expects — keep talking. I also cut backend time-to-first-token by doing less. For this conversational path, I turned off extended model thinking: _NO_THINKING = types . ThinkingConfig ( thinking_budget = 0 ) And I stopped advertising Google Search on every request. The search tool is only added when the prompt smells like it needs current/external information. Most turns do not. if self . _needs_search ( built_contents ): all_functions . append ( self . google_search ) The result was about a 5x cut in chat time-to-first-byte for the common path, plus a much better perceived response because speech starts before the full answer exists. The lesson was not “stream everything.” It was smaller than that: stream at the boundary the product can actually use overlap the slow local work with the slow network work do not give the model tools or reasoning budget unless the turn needs them log chunks, sentence counts, gaps, and total time so you can see where the pause moved Voice agents do not need heroic architecture to feel better. Sometimes the fix is a regex, a queue, and deleting the expensive defaults.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/toddsullivan/i-made-my-voice-agent-feel-faster-by-streaming-sentences-not-audio-4jej

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
