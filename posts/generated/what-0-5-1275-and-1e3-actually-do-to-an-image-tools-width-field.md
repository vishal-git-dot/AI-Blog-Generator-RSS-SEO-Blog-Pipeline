---
title: "What 0, -5, 12.75 and 1e3 actually do to an image tool's width field"
slug: "what-0-5-1275-and-1e3-actually-do-to-an-image-tools-width-field"
author: "sharefun2023"
source: "devto_webdev"
published: "Sat, 07 Nov 2026 12:40:08 +0000"
description: "What 0 , -5 , 12.75 and 1e3 actually do to an image tool's width field I maintain a handful of free, client-side image tools. Last month I ran an audit acros..."
keywords: "width, box, you, value, image, number, canvas, one"
generated: "2026-11-07T12:45:01.218405"
---

# What 0, -5, 12.75 and 1e3 actually do to an image tool's width field

## Overview

What 0 , -5 , 12.75 and 1e3 actually do to an image tool's width field I maintain a handful of free, client-side image tools. Last month I ran an audit across all of them and found that the numeric size fields — the "width / height" boxes almost every canvas-based tool has — fail in four different ways depending on what you type into them. Not one of those failures shows up if you only test the happy path, because the happy path is "leave the box empty". Every number below was measured in Chromium 149 on Linux, against my own pages. I'll show the exact mechanics, then the six-line fix. The four kinds of damage Take a resizer that reads the box like this — which is what most tutorials show: const w = box . value ? parseInt ( box . value ) : naturalWidth ; canvas . width = w ; Now type into that box: You type box.validity.valid What the canvas gets What the user sees 0 false ( rangeUnderflow ) width 0 → toBlob returns null → createObjectURL(null) throws "Your file seems to be corrupted" -5 false ( rangeUnderflow ) 4294967291 per WebIDL, then Chrome resets the bitmap to 300 px A 300px-wide image, no error at all 12.75 false ( stepMismatch ) 12 Silently 12px 1e3 true 1 (because parseInt("1e3") === 1 ) 1px-wide image, 1000× off The last row is my favourite, and it's the one nobody believes until they run it: parseInt ( " 1e3 " , 10 ) // 1 Number ( " 1e3 " ) // 1000 parseInt ( " 12.75 " , 10 ) // 12 1e3 is a valid HTML number — validity.valid === true , because the browser parses it as 1000 and 1000 is inside min="1" max="8000" . So any validation that defers to the browser says "fine", and then parseInt throws away two orders of magnitude. Why 0 produces an error message about your file The chain is short and completely silent: const c = document . createElement ( ' canvas ' ); c . width = 0 ; c . height = 120 ; const blob = await new Promise ( res => c . toBlob ( res , ' image/png ' )); // null URL . createObjectURL ( blob ); // TypeError: Failed to execute 'createObjectURL' on 'URL': Overload resolution failed. A zero-width canvas has nothing to encode, so toBlob calls back with null , and createObjectURL refuses it. If that line sits inside the same try block that wraps decoding — and it almost always does — then the catch that was written for "could not decode the image" catches it instead. The user dropped in a perfectly good JPEG, typed 0 , and got told their file is broken. And -5 doesn't even throw. Assigning a negative value to canvas.width goes through WebIDL's unsigned long conversion ( -5 → 4294967291 ), which exceeds the maximum canvas dimension, so Chrome resets the bitmap to its default 300×150 rather than failing: const c = document . createElement ( ' canvas ' ); c . width = - 5 ; c . width // 300 The fix: stop inventing your own validation The mistake I kept making was writing a second set of thresholds in JavaScript ("if w < 1 || w > 8000…") next to the min / max / step already declared in the HTML. Two sources of truth, and the JS one is always the one that goes stale. The browser already computed all of it. validity.valid is a single boolean covering rangeUnderflow , rangeOverflow , stepMismatch and badInput : function outputSize ( box , fallback ) { if ( box . value && ! box . validity . valid ) return { error : box . value }; return { value : box . value ? Number ( box . value ) : fallback }; // Number, never parseInt } Three rules that matter more than the code: Return before you enter the try . If the validity check lives inside the block whose catch says "could not decode the image", a bad width will still be reported as a bad file. Check first, then encode. Number() , not parseInt() . parseInt truncates at the first non-digit: it turns 12.75 into 12 , 1e3 into 1 , and 0x10 into 0 . Number() is the same conversion the HTML parser used when it decided the value was valid, so validation and use finally agree. Say which field, with the value. "Output size must be a whole number from 1 to 8000 px — you entered width "-5". Leave a box empty to keep the original dimension." Inline, not alert() : a modal blocks the page, can't be re-read, and hides whatever the user was about to compare against. Here's what that looks like now on the resizer , measured just before writing this: w = "0" → ⚠️ ... you entered width "0". (no conversion performed) w = "-5" → ⚠️ ... you entered width "-5". (no conversion performed) w = "12.75" → ⚠️ ... you entered width "12.75". (stepMismatch, no conversion) w = "1e3" → 1000×120, 2.9 KB (was 1×120) One more edge: the warning that outlives its own mistake If you show the warning by writing into the same status line that shows the filename, you get a stale-state bug: the user fixes the number, hits convert, a new image is produced — and the line still reads you entered width "0" next to a successful result. Reset the status line when a conversion actually starts (back to 📄 filename (W×H) ), not when it finishes. Then the only message on screen always describes the current state. The test matrix If you take one thing from this post, make it a checklist rather than a fix: for every numeric input, try 0 , -1 , a value above max , a decimal, 1e3 , and the empty string. The empty string is the one every manual test uses and the only one that never touches this code path. The tools I audited — resize , SVG → PNG , crop — all run entirely in the browser; nothing is uploaded. That's also why the bug class is so common in this space: no server means no second line of defence, so the input field is the contract.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/sharefun2023/what-0-5-1275-and-1e3-actually-do-to-an-image-tools-width-field-3fn1

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
