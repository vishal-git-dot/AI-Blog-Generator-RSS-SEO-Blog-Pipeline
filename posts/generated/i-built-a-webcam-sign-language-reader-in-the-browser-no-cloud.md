---
title: "I Built a Webcam Sign-Language Reader in the Browser (No Cloud)"
slug: "i-built-a-webcam-sign-language-reader-in-the-browser-no-cloud"
author: "Devanshu Biswas"
source: "devto_webdev"
published: "Mon, 15 Jun 2026 21:00:57 +0000"
description: ""AI that reads sign language" sounds like a research lab and a GPU cluster. But a genuinely useful starting version runs entirely in your browser, with no mo..."
keywords: "hand, sign, thumb, tip, you, its, browser, your"
generated: "2026-06-15T21:11:31.715509"
---

# I Built a Webcam Sign-Language Reader in the Browser (No Cloud)

## Overview

"AI that reads sign language" sounds like a research lab and a GPU cluster. But a genuinely useful starting version runs entirely in your browser, with no model upload and no cloud — the camera feed never leaves your machine. Here's how I built a webcam sign reader from scratch. This is Day 7 of SolveFromZero, where I solve a real, useful problem each day. The browser can track a hand You don't need a server or a camera SDK. Google's MediaPipe ships a tiny hand-tracking model that runs on WebAssembly right in the tab. Hand it a video frame, get back the hand's skeleton — all on-device. import { HandLandmarker , FilesetResolver } from " https://cdn.jsdelivr.net/npm/@mediapipe/tasks-vision/vision_bundle.mjs " ; const hand = await HandLandmarker . createFromOptions ( files , { runningMode : " VIDEO " }); 21 points per hand For every frame the model returns 21 landmarks — the wrist plus four points per finger (knuckle, two joints, tip) — each as an (x, y, z) coordinate from 0 to 1. That skeleton is all you need; you never touch raw pixels again. const lm = hand . detectForVideo ( video , performance . now ()). landmarks [ 0 ]; // 21 points A finger is "up" if its tip beats its knuckle Geometry does the recognition. For a roughly upright hand, a finger is extended when its tip is higher on screen (smaller y) than its middle joint. Check that for the four fingers and you instantly know how many are raised. const up = [ 8 , 12 , 16 , 20 ]. map (( tip , i ) => lm [ tip ]. y < lm [[ 6 , 10 , 14 , 18 ][ i ]]. y ); The thumb is the awkward one The thumb bends sideways, not up, so the tip-above-knuckle trick fails on it. Instead, measure how far the thumb tip sticks out from the hand. Far out = extended. Handling the thumb separately is the classic gotcha in gesture code. const thumb = dist ( lm [ 4 ], lm [ 5 ]) > 0.13 ; Map the finger pattern to a sign Now turn the pattern of raised fingers into meaning — no fingers = 0, index only = 1, index+middle = 2, all five = an open-palm "hi", thumb alone = 👍: if ( ! thumb && count === 0 ) return " 0 " ; if ( ! thumb && count === 2 ) return " 2 " ; if ( thumb && count === 4 ) return " hi " ; It's a hand-coded lookup — simple, transparent, and enough for counts and a few gestures. Hold to commit A hand wobbles, so only "type" a sign once it's been steady for ~12 frames. That debounce stops the transcript from filling with noise as your hand moves between signs. if ( sign === lastSign ) stable ++ ; else stable = 0 ; if ( stable === 12 ) type ( sign ); Scaling to real ASL This demo recognises counts 0–5 plus a couple of gestures with pure geometry. Full ASL — dozens of letters, motion, two hands, facial cues — needs a small trained classifier sitting on top of these same 21 landmarks. But that's the beautiful part: the hard perception (finding the hand) is done for you, and the pipeline you'd build for the real thing is exactly the one here. Landmarks in, sign out, fully on-device. It's also a reminder that a lot of "AI" products are 20% model and 80% turning its output into something useful. 👉 Try it with your webcam (Chrome/Edge, grant camera): https://dev48v.infy.uk/solve/day7-sign-language.html 🌐 All solutions: https://dev48v.infy.uk/solvefromzero.php Tomorrow: live captions for any video, in the browser.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/dev48v/i-built-a-webcam-sign-language-reader-in-the-browser-no-cloud-11hg

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
