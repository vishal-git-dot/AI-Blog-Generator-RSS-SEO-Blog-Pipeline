---
title: "I Built a Face Shape Detector That Shows Its Work — and Keeps Going"
slug: "i-built-a-face-shape-detector-that-shows-its-work-and-keeps-going"
author: "KnowYourFaceShape"
source: "devto_webdev"
published: "Thu, 22 Oct 2026 03:56:01 +0000"
description: "Most face shape tools give you a label and a list of haircuts. I wanted to build the opposite: something that shows the five measurements behind the label, t..."
keywords: "face, shape, your, you, photo, tools, mediapipe, against"
generated: "2026-10-22T04:08:58.350832"
---

# I Built a Face Shape Detector That Shows Its Work — and Keeps Going

## Overview

Most face shape tools give you a label and a list of haircuts. I wanted to build the opposite: something that shows the five measurements behind the label, then keeps going into the questions people actually have afterwards. Try it here: knowyourfaceshape.com — free, no sign-up, and your photo never leaves your browser. What it does You can get your face shape three ways: upload a photo, take a 60-second quiz, or enter four tape-measure readings. The photo path runs MediaPipe Face Landmarker on your device, takes ten landmarks, builds five ratios — face length, forehead, jaw, jaw angle and chin taper — and compares them against a published prototype table for seven shapes: oval, round, square, oblong, heart, diamond and triangle. The part I care about comes next. Each result links to a shape guide, hairstyle breakdowns written against the same measurements, and sizing calculators for glasses frames, hats, earrings and necklaces. There's an AI attractiveness test on the site now too, and more tools are on the way. Tech stack React 19, MediaPipe tasks-vision running inside a Web Worker, deployed on Cloudflare Workers. Inference happens on your device, so there is no photo upload and nothing for me to store. Two things that were harder than expected MediaPipe normalizes x by image width and y by image height, which means the same face measures differently in a landscape photo than a portrait one until you undo it. And resisting the urge to print an accuracy percentage was its own challenge. The site publishes the full rule set and every threshold instead, so you can check the call against your own numbers. Why I built it Because a lot of face shape content online ends in a product recommendation. This site sells nothing and recommends no brand. What's next A shareable result card and a hairstyle matcher are first in line, along with more measuring tools. Would love feedback from anyone who tries it — especially if you land on a borderline result and disagree with the shape. Tell me which measurement looked off and I'll dig in.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/knowyourfaceshape/i-built-a-face-shape-detector-that-shows-its-work-and-keeps-going-khh

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
