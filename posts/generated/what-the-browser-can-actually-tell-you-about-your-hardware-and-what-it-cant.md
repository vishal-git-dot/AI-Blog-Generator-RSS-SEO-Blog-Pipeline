---
title: "What the browser can actually tell you about your hardware (and what it can't)"
slug: "what-the-browser-can-actually-tell-you-about-your-hardware-and-what-it-cant"
author: "member_2ef2ebd8"
source: "devto_webdev"
published: "Sun, 16 Aug 2026 06:24:10 +0000"
description: "I spent a while building browser-based hardware diagnostics and came away with a much clearer sense of where the web platform is genuinely capable and where ..."
keywords: "you, demo, hardware, screen, api, only, all, events"
generated: "2026-08-16T06:48:23.406440"
---

# What the browser can actually tell you about your hardware (and what it can't)

## Overview

I spent a while building browser-based hardware diagnostics and came away with a much clearer sense of where the web platform is genuinely capable and where it quietly lies to you. Notes below, with live demos for each API so you can poke at them yourself. Refresh rate: requestAnimationFrame is the only signal you get There's no screen.refreshRate . The only approach is timing requestAnimationFrame callbacks and inferring the rate from the median frame delta: const deltas = []; let last = performance . now (); function tick ( now ) { deltas . push ( now - last ); last = now ; if ( deltas . length < 180 ) requestAnimationFrame ( tick ); else { const sorted = deltas . slice (). sort (( a , b ) => a - b ); console . log ( Math . round ( 1000 / sorted [ sorted . length >> 1 ])); } } requestAnimationFrame ( tick ); Two gotchas that cost me time. Use the median , not the mean — a single dropped frame wrecks an average. And browsers throttle rAF in background tabs, so the measurement is meaningless unless the tab is visible; gate it on document.visibilityState . ( live version ) Screen dimensions: four different answers, all "correct" screen.width , window.innerWidth , window.devicePixelRatio and screen.availWidth measure genuinely different things, and the one people usually want — actual native panel resolution — is screen.width * devicePixelRatio . Except that's still CSS-pixel derived, so on a scaled display it can disagree with what the panel physically is. The browser simply does not expose true hardware resolution. ( demo ) Keyboard: event.code vs event.key , and the keys you never receive event.key is layout-dependent, event.code is physical position — for a hardware tester you want code . The real limitation is that some keys never reach JS at all: PrintScreen often doesn't fire keydown , Meta combinations get swallowed by the OS, and Fn isn't a browser-visible key on most laptops. N-key rollover testing works surprisingly well though, since you just track the size of the currently-held Set . Cheap keyboards drop inputs at 3-4 simultaneous keys and it's very visible. ( demo ) Pointer events beat mouse events, with one catch pointerdown / pointerup unify mouse, touch and pen, and pointerId lets you track multi-touch properly. For detecting the classic worn-switch double-click fault, you just measure the gap between consecutive pointerdown events on the same button — under ~80ms with no intervening movement is almost certainly a hardware fault rather than a human. ( mouse demo , touch demo ) The catch: preventDefault() on pointerdown kills the subsequent compatibility mouse events, which will silently break anything expecting them. Gamepad API: polling only, and it starts asleep No events for axis movement — you have to poll navigator.getGamepads() inside your rAF loop. Worse, controllers don't appear at all until the user presses a button, for fingerprinting reasons. That confused me for an hour: the array is full of null until first input. Stick drift shows up as a resting axis value that isn't 0. Anything past about 0.08 at rest is a worn potentiometer. ( demo ) Media devices: labels are gated behind permission navigator.mediaDevices.enumerateDevices() will happily list devices before you request permission — but every label is an empty string. You only get human-readable device names after getUserMedia() succeeds. So a device picker UI has to either request permission first or show useless blank entries. For mic level metering, AnalyserNode with getByteTimeDomainData and computing RMS is more stable than frequency data. ( mic demo , webcam demo , speaker demo ) Dead pixels: nothing programmatic, and that's fine There is no API. The only viable approach is filling the viewport with solid colours via the Fullscreen API and letting the human look. Worth remembering that not every problem needs a programmatic answer — sometimes rendering #ff0000 across the whole screen is the tool. ( demo ) The pattern underneath all of this Every hardware-adjacent API on the web has been deliberately blunted for fingerprinting resistance. You get relative measurements, permission-gated labels, and input-gated device lists. That's the right trade, but it means "detect the user's hardware" is mostly not a solvable problem — and the honest tools are the ones that measure behaviour rather than claim to read specs. All ten of these run client-side with nothing uploaded if you want to compare notes: the full set is here . Happy to hear if anyone has found better approaches, particularly on refresh rate — the rAF median approach still feels like a hack.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/member_2ef2ebd8/what-the-browser-can-actually-tell-you-about-your-hardware-and-what-it-cant-2d2j

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
