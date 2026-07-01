---
title: "Self-Hosted Audio Transcription API with Whisper — Free, No Limits, No Black Box"
slug: "self-hosted-audio-transcription-api-with-whisper-free-no-limits-no-black-box"
author: "Alexey D"
source: "devto_python"
published: "Wed, 01 Jul 2026 08:38:00 +0000"
description: "Most transcription services are a black box. You send audio, you get text, you pay per minute, and you have no idea what's happening on the other side. When ..."
keywords: "language, result, audio, text, you, file, transcribe, whisper"
generated: "2026-07-01T09:59:55.958595"
---

# Self-Hosted Audio Transcription API with Whisper — Free, No Limits, No Black Box

## Overview

Most transcription services are a black box. You send audio, you get text, you pay per minute, and you have no idea what's happening on the other side. When the language is wrong, the timestamps are off, or the accent throws it off — you file a support ticket and wait. There's a better way. OpenAI's Whisper model is open-source, runs on CPU, and produces results that match or beat commercial services for most use cases. The catch is that setting it up in production — with a proper API, format handling, error management, and language detection — takes time that most projects don't have. I've already done that. Here's how to use it. What the API does Single endpoint, straightforward contract: curl -X POST https://sofa-rarely-mailing-buzz.trycloudflare.com/transcribe \ -F "audio=@meeting_recording.mp3" \ -F "language=en" Response: { "text" : "Alright, let's get started. First item on the agenda is the Q3 budget review." , "language" : "en" , "language_name" : "English" , "duration" : 47.3 , "segments" : [ { "id" : 0 , "start" : 0.0 , "end" : 3.2 , "text" : "Alright, let's get started." }, { "id" : 1 , "start" : 3.2 , "end" : 7.8 , "text" : "First item on the agenda is the Q3 budget review." } ], "model" : "whisper-tiny" , "processing_time" : 8.4 } The segments array with timestamps is what makes this useful for real applications — subtitle generation, searchable transcripts, meeting summarization by section. Supported formats MP3, WAV, OGG, M4A, WEBM, FLAC, MP4. Up to 25MB per file. If your file is larger, split it first — ffmpeg -i input.mp3 -f segment -segment_time 300 -c copy part%03d.mp3 . Python — transcribe and search import requests def transcribe ( file_path : str , language : str = None ) -> dict : with open ( file_path , ' rb ' ) as f : data = { " audio " : f } if language : data [ " language " ] = ( None , language ) r = requests . post ( " https://sofa-rarely-mailing-buzz.trycloudflare.com/transcribe " , files = { " audio " : f }, data = { " language " : language } if language else {}, timeout = 120 ) r . raise_for_status () return r . json () result = transcribe ( " interview.mp3 " ) # Full transcript print ( result [ " text " ]) # Find specific moments keyword = " budget " matches = [ seg for seg in result [ " segments " ] if keyword . lower () in seg [ " text " ]. lower () ] for m in matches : print ( f " [ { m [ ' start ' ] : . 1 f } s] { m [ ' text ' ] } " ) Auto-translate to English The task parameter accepts "translate" — it transcribes AND translates to English in one call. No separate translation step needed. r = requests . post ( " https://sofa-rarely-mailing-buzz.trycloudflare.com/transcribe " , files = { " audio " : open ( " german_podcast.mp3 " , " rb " )}, data = { " task " : " translate " } ) result = r . json () print ( result [ " language " ]) # "de" print ( result [ " text " ]) # English translation This works across all 39 supported languages. The model detects the source language automatically when you don't specify one. Language auto-detection Skip the language parameter and Whisper figures it out: result = transcribe ( " unknown_language_audio.ogg " ) print ( result [ " language " ]) # "fr" print ( result [ " language_name " ]) # "French" Detection accuracy drops on very short clips (under 10 seconds) and heavily accented speech. For production, if you know the language, pass it explicitly — it's faster and more accurate. JavaScript — browser upload async function transcribeFile ( file ) { const formData = new FormData (); formData . append ( ' audio ' , file ); // optionally: formData.append('language', 'en'); const res = await fetch ( ' https://sofa-rarely-mailing-buzz.trycloudflare.com/transcribe ' , { method : ' POST ' , body : formData }); if ( ! res . ok ) throw new Error ( `Transcription failed: ${ res . status } ` ); return res . json (); } // In your file input handler: fileInput . addEventListener ( ' change ' , async ( e ) => { const file = e . target . files [ 0 ]; if ( ! file ) return ; statusEl . textContent = ' Transcribing... ' ; const result = await transcribeFile ( file ); transcriptEl . textContent = result . text ; statusEl . textContent = `Done ( ${ result . duration . toFixed ( 1 )} s audio, ${ result . processing_time . toFixed ( 1 )} s processing)` ; }); Processing time expectations The API runs Whisper tiny on CPU. Rough benchmarks: Audio length Processing time 30 seconds 3–6 seconds 2 minutes 12–20 seconds 5 minutes 30–50 seconds 10 minutes 60–90 seconds For a meeting transcription workflow this is fine. For real-time voice-to-text it's not — that needs a streaming setup with a larger server. What it doesn't handle well Heavy accents + background noise is the hardest case for the tiny model. If you're transcribing call center recordings with noisy environments, accuracy will be lower than a commercial service using a larger model. Speaker diarization (who said what) is not included. The output is continuous text with timestamps, not labeled by speaker. Adding diarization requires an additional processing step with something like pyannote.audio . Timestamps are approximate on short segments. The segmentation algorithm sometimes splits sentences in odd places for fast speakers. Available on RapidAPI The stable version with rate limits and API keys is listed on RapidAPI — search "Audio Transcription Whisper." Free tier included. GET /languages returns the full list of 39 supported languages with ISO codes if you need to build a language selector.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/__fdcef087b6/self-hosted-audio-transcription-api-with-whisper-free-no-limits-no-black-box-3f7n

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
