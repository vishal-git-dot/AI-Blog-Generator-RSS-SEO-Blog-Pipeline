---
title: "Counting filler words when speech-to-text deletes them"
slug: "counting-filler-words-when-speech-to-text-deletes-them"
author: "WizMantra Academy"
source: "devto_ai"
published: "Sat, 07 Nov 2026 12:34:02 +0000"
description: "We wanted a one-minute speaking test that gives a learner three numbers: words a minute, filler words and long pauses. The browser's speech recognizer would ..."
keywords: "like, you, words, transcript, speech, text, minute, can"
generated: "2026-11-07T12:45:01.223100"
---

# Counting filler words when speech-to-text deletes them

## Overview

We wanted a one-minute speaking test that gives a learner three numbers: words a minute, filler words and long pauses. The browser's speech recognizer would do the hard part. We'd count. It turns out the transcript fights you on all three. Lie 1: the model cleans up "um" Speech recognizers are trained to produce readable text, so "um" and "uh" mostly vanish. Count fillers from the transcript and a nervous speaker looks fluent. There's no fix for that from the page. What you can do is count the fillers that survive transcription because they're real words: /* Fillers that survive speech-to-text. Recognisers usually drop "um" and "uh". */ var FILL = [ " um " , " umm " , " uh " , " uhh " , " er " , " erm " , " hmm " , " ah " , " basically " , " actually " , " literally " , " matlab " , " you know " , " i mean " , " kind of " , " sort of " , " like " ]; "Matlab" is the Hindi "I mean", and it turns up in Indian English speech often enough to earn a slot. Lie 2: "like" is a filler, except when it isn't "I like Python" isn't a filler. "It was, like, a huge refactor" is. We check the word before it: var LIKE_OK = /^ ( i|you|we|they|would|i'd|feel|feels|look|looks|sound|sounds|just|really|don't|didn't|also|not|is|was|it's|that's|seems ) $/ ; if ( w [ i ] === " like " ) { if ( i > 0 && LIKE_OK . test ( w [ i - 1 ])) continue ; } It's crude and it works well enough for a self-check. "Looks like", "feel like" and "I like" pass. A bare "like" in the middle of a clause gets counted. Lie 3: there's no silence in a transcript A transcript has no timestamps per word in this API, so you can't see a pause directly. But you can see when results arrive. If two onresult events are more than two seconds apart, the speaker stopped: rec . onresult = function ( e ) { var now = Date . now (); if ( last && now - last >= 2000 ) gaps . push ( now - last ); last = now ; // ... }; It's a proxy, and a noisy one on slow networks, since Chrome's recognizer runs on Google's servers. For a learner who stalls for four seconds looking for a word, it's accurate enough. Lie 4: Android repeats itself With continuous = true , desktop Chrome sends each final result once. Android Chrome sends each new final result with the earlier text still inside it. Join them naively and every sentence appears two or three times, and your words-a-minute doubles. if ( r . isFinal ) { var prev = finals [ finals . length - 1 ]; /* Android Chrome repeats earlier text inside each new final result */ if ( prev && tx . toLowerCase (). indexOf ( prev . toLowerCase ()) === 0 ) finals [ finals . length - 1 ] = tx ; else if ( tx ) finals . push ( tx ); } Two smaller ones while we're here. The browser ends a "continuous" session early when it feels like it, so onend restarts it if the timer is still running. And after stop() , the last final result can take over a second to arrive, so we wait up to 1,800 ms before scoring. The scoring is the boring part Once the transcript is honest, the score is plain thresholds: under 70 words a minute: slow 120 to 160: natural over 165: fast, fine if people follow you Fillers per minute and long pauses add to the band. That's about 40 lines. The model does the hearing; the judgement is ours, in plain if statements anyone can read and argue with. Try it 60-second English fluency test . Chrome, Edge or Safari. Firefox gets a typed fallback because it has no SpeechRecognition. Has anyone found a browser-side way to keep "um" in the transcript? I'd like to know. Drafted with help from an AI assistant. Code is from the live tool.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/wizmantraacademy/counting-filler-words-when-speech-to-text-deletes-them-4ifd

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
