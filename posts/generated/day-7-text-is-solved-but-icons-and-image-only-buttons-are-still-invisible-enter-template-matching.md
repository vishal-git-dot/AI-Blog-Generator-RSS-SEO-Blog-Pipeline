---
title: "Day 7. Text is solved. But icons and image-only buttons are still invisible. Enter template matching."
slug: "day-7-text-is-solved-but-icons-and-image-only-buttons-are-still-invisible-enter-template-matching"
author: "Okeke Chukwudubem"
source: "devto_webdev"
published: "Wed, 17 Jun 2026 15:45:23 +0000"
description: "Two days ago, I fixed the OCR bottleneck. The agent can now read text on a screen in under 2 seconds. It handles interruptions. It verifies each step. But th..."
keywords: "agent, matching, template, button, icon, send, icons, image"
generated: "2026-06-17T15:50:36.572003"
---

# Day 7. Text is solved. But icons and image-only buttons are still invisible. Enter template matching.

## Overview

Two days ago, I fixed the OCR bottleneck. The agent can now read text on a screen in under 2 seconds. It handles interruptions. It verifies each step. But there's a problem I've been dodging since Day 1, and it's time to face it. What the Agent Still Can't See Every app has buttons without text. The send button in WhatsApp is a paper plane icon. The attach button is a paperclip. The back button is an arrow. The camera button is a camera. ML Kit sees text. It doesn't see icons. Tesseract doesn't see icons either. So when the agent needs to tap the send button after typing a message, it has no idea where that button is. Right now, my workaround is hardcoded coordinates. I know the send button is roughly at a specific position on my phone. But that breaks on a different device. It breaks if the app updates. It breaks if the screen orientation changes. It's a hack, not a solution. Template Matching: The Plan Template matching is an old-school computer vision technique. You give it a reference image (like a small crop of the send icon) and it scans a larger image (the screenshot) looking for a match. It returns the coordinates of the best match. It's not AI. It's not deep learning. It's pixel math. But it works surprisingly well for static UI elements like icons that don't change appearance. Here's the approach: Build an icon library. For each app the agent supports (WhatsApp for now), I manually crop reference images of the key icons: send, attach, back, camera, search. Before each tap action , if the target isn't found via OCR, the agent runs template matching against its icon library. If a match is found above a confidence threshold (80%), the agent taps the center of the matched region. If no match is found , the agent reports the failure and stops, rather than guessing. Today's Progress Task Status Researched template matching libraries for Python ✅ Done Selected OpenCV as primary engine, NumPy/PIL as fallback ✅ Done Wrote match_template() and _simple_template_match() in vision.py ✅ Done Created first icon reference image (WhatsApp send button) ✅ Done Uploaded send_button.png to repo ✅ Done Integrated into agent.py ⏳ Next The Code The new vision.py now has two template matching functions: match_template() — Uses OpenCV for accurate, fast matching. If OpenCV isn't installed, it falls back to the simple version. _simple_template_match() — A lightweight pure-Python implementation using NumPy and PIL. Zero dependencies beyond what the agent already uses. The function takes a screenshot and a reference icon image, and returns the center coordinates of the best match above the confidence threshold. Why Two Versions? OpenCV is heavy. Installing it in Termux requires compiling from source or finding a pre-built arm64 wheel. The simple fallback means the agent can still do template matching even without OpenCV—just slower and slightly less accurate. Progressive enhancement. No hard dependency. What's Next (Day 8) Wire template matching into agent.py so the agent actually uses it when OCR fails Test the full pipeline: type message → detect send icon via template matching → tap → verify Start building out the icon reference library for WhatsApp The Repo 👉 github.com/Dexter2344/phone-agent vision.py is now at v3 with ML Kit, Tesseract, fuzzy matching, interruption handling, and template matching. send_button.png is in the repo. Agent integration coming next. This is Day 7. The agent is getting eyes for the things that don't have names.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/okeke_chukwudubem_5f3bf49/day-7-text-is-solved-but-icons-and-image-only-buttons-are-still-invisible-enter-template-h87

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
