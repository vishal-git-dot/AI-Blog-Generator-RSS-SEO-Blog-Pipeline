---
title: "Soul in Motion — 5:28 PM | 2026-09-21"
slug: "soul-in-motion-528-pm-2026-09-21"
author: "Dev Rajput"
source: "devto_webdev"
published: "Mon, 21 Sep 2026 12:21:27 +0000"
description: "TL;DR Refactored the Soul in Motion site’s color scheme and added subtle text motion inspired by a peer’s design. Tackled a personal celestial distance visua..."
keywords: "motion, text, design, visualizer, debounce, soul, site, subtle"
generated: "2026-09-21T12:28:55.243297"
---

# Soul in Motion — 5:28 PM | 2026-09-21

## Overview

TL;DR Refactored the Soul in Motion site’s color scheme and added subtle text motion inspired by a peer’s design. Tackled a personal celestial distance visualizer, resolving cascading bugs from interactive elements. Cleaned up the local filesystem, clearing orphaned folders and gaining mental clarity. Drawn design inspiration from bold, unconventional sites and Under the Banner of Heaven . Ended the day with progress on both the company site and the side project, feeling satisfied with incremental wins. Morning: Ripping Apart the Soul in Motion Palette I started the day staring at the black‑and‑red combo that had been stuck on the Soul in Motion homepage for months. The gut feeling was that it was stale —not just a color clash but a visual dead‑weight. Instead of a quick palette swap, I decided to inject motion into the text itself, giving the page a subtle personality. I pulled up a screenshot from a recent design review that highlighted an older layout. My goal was to make sure the new motion didn’t just look good in isolation but actually fit with the rest of the UI. The tension between “this looks striking” and “this is usable” is a constant in front‑end work, and I kept circling back to that balance. Implementation Snapshot /* Simple keyframes for subtle horizontal text motion */ @keyframes slide { 0 %, 100 % { transform : translateX ( 0 ); } 50 % { transform : translateX ( 5px ); } } .text-move { animation : slide 4s ease-in-out infinite ; } I wrapped the headline text in a div.text-move and tweaked the timing until it felt natural. The result is a gentle, almost imperceptible glide that adds life without distracting from the content. Afternoon: Debugging the Celestial Distance Visualizer The side project was a visualization of distances between celestial bodies. The goal was to make the data intuitive , not a wall of numbers. Unfortunately, adding a tiny interactive element broke three others. A ghost of a removed element lingered, and a quiet button caused chaos downstream. I spent the afternoon chasing these cascading bugs: Ghost Element – A hidden div still existed in the DOM, causing layout shifts. Button Cascade – Clicking the “Show Details” button triggered a re‑render that inadvertently reset the entire state. Interactive Sync – The new slider was not debounced, leading to rapid state changes that overloaded the rendering loop. After a series of refactors, I introduced a debounced handler and cleaned up the component hierarchy: // debounce.js export const debounce = ( func , wait ) => { let timeout ; return (... args ) => { clearTimeout ( timeout ); timeout = setTimeout (() => func . apply ( null , args ), wait ); }; }; // distance-visualizer.js import { debounce } from ' ./debounce ' ; const handleSliderChange = debounce (( value ) => { updateDistances ( value ); }, 200 ); The visualizer finally behaved as expected, and the interactive elements no longer interfered with each other. Inspiration Hunt While the code was running, I opened a few sites known for bold, unconventional design—think Awwwards winners and experimental UI showcases. I took mental notes on layout tricks and motion details that could be adapted for the company site later. I also let Under the Banner of Heaven play in the background. The vivid scenes made me pause and question the intentionality of my own work. It’s a reminder that design is as much about narrative as it is about pixels. File System Clean‑Up A small but surprisingly satisfying task: I hunted through my hard drive for folders that had stopped showing up where they should, cleared out the junk, and felt a wave of relief. Not every win needs to be complicated, but a tidy workspace can boost productivity and reduce cognitive load. Wrap‑Up By the end of the day, I had: A redesigned homepage with subtle text motion. A stubborn side project finally behaving. A cleaner hard drive. A head full of borrowed inspiration. Both the company site and the distance visualizer are closer to completion than they were this morning. That, for me, is enough. Stay tuned for the next update.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/dev_rajput_2d46f92f8a3418/soul-in-motion-528-pm-2026-09-21-1pjk

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
