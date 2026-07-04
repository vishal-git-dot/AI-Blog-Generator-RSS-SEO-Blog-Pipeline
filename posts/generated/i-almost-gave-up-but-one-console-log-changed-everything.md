---
title: "I Almost Gave Up... But One Console Log Changed Everything"
slug: "i-almost-gave-up-but-one-console-log-changed-everything"
author: "Usama"
source: "devto_webdev"
published: "Sat, 04 Jul 2026 19:05:28 +0000"
description: "Today I spent hours chasing a bug that looked impossible. When I clicked "Add Cabin" , nothing happened. No modal. No error. Nothing. At first, I thought the..."
keywords: "modal, step, console, log, click, changed, cabin, today"
generated: "2026-07-04T19:22:30.078233"
---

# I Almost Gave Up... But One Console Log Changed Everything

## Overview

Today I spent hours chasing a bug that looked impossible. When I clicked "Add Cabin" , nothing happened. No modal. No error. Nothing. At first, I thought the problem was in my React state. Then I thought it was styled-components . Then I suspected PropTypes . I kept changing code, but the bug was still there. Instead of randomly editing files, I decided to debug step by step. Step 1: Check if the button works I added a simple log: console . log ( " Button clicked " ); The console printed: Button clicked Great! That meant the click event was working. Step 2: Check the modal state Next, I logged my modal state. console . log ({ openName , name }); I expected to see: openName : " cabin-form" name : " cabin-form" Instead, I noticed something strange. The value became "cabin-form" for only a moment, then immediately changed back to an empty string. That was the biggest clue. Step 3: Ask the right question Instead of asking, "Why doesn't the modal open?" I started asking, "Who is closing the modal immediately?" That changed everything. Step 4: Find the real culprit The problem wasn't React. It wasn't the modal. It wasn't styled-components . It was my outside click handler. I had this: document . addEventListener ( " click " , handleClickOutside ); The same click that opened the modal was also triggering the outside click listener, so the modal closed instantly. Step 5: The fix I changed it to: document . addEventListener ( " mousedown " , handleClickOutside ); And suddenly... The modal opened perfectly. What I learned Today taught me a lesson I'll remember for a long time. Debugging isn't about guessing. It's about collecting evidence. Every console.log() is a clue. Every observation eliminates another possibility. The goal isn't to write more code. The goal is to understand what the code is actually doing. Today I didn't just fix a modal. I learned how experienced developers think when they debug. And that lesson is worth much more than fixing a single bug.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/usama_dev/i-almost-gave-up-but-one-console-log-changed-everything-2l23

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
