---
title: "I built an AI speechwriter for the moments you can't get wrong"
slug: "i-built-an-ai-speechwriter-for-the-moments-you-cant-get-wrong"
author: "KunStudio"
source: "devto_webdev"
published: "Sun, 05 Jul 2026 03:48:11 +0000"
description: "A best man's toast. A eulogy for a parent. An obituary you have three days to write while grieving. These are the moments where the blank page hurts the most..."
keywords: "you, your, speech, not, built, memories, speechwriter, moments"
generated: "2026-07-05T03:58:51.639859"
---

# I built an AI speechwriter for the moments you can't get wrong

## Overview

A best man's toast. A eulogy for a parent. An obituary you have three days to write while grieving. These are the moments where the blank page hurts the most, and where a generic template feels worst. I built AI Speechwriter to help with exactly those moments: wedding toasts, eulogies, tributes, retirement and anniversary speeches. You answer a few questions about the person and the moment, and it writes a real speech from your own memories, not a fill-in-the-blank template. Why I built it Most speech tools give you a template with [NAME] and [MEMORY] placeholders. That is the easy part. The hard part is turning a few scattered memories into something that flows and sounds like you meant it. And the highest-stakes version of this, a eulogy or obituary, usually has to be written on a deadline, by someone who is not in a state to fight with a text editor. So the goal was narrow: take what the person actually knows about their subject, and return a finished draft they would be proud to read out loud. How it works technically The whole thing runs on Cloudflare Pages with Functions for the backend, so there is no server to manage and it stays fast globally. Generation : Claude does the writing. The prompt is built from the user's structured answers (who it is for, the relationship, specific memories, the tone) rather than a freeform box, which keeps the output grounded in their details instead of drifting into cliche. Free preview : The opening paragraph is generated for free, on the spot, from the real inputs. You see your actual opening before deciding to pay. This matters more than a screenshot gallery because the preview is your speech, not a sample. Payment : A one-time PayPal charge unlocks the full speech. No subscription. For a thing you use once at a wedding or a funeral, a monthly plan would be absurd. Price validation : The price is checked server-side at unlock time, not trusted from the client, so the amount can't be tampered with in the browser. Using it in three steps Tell it the moment. Who the speech is for, your relationship, a few memories or qualities, and the tone you want. Preview free. It writes your real opening paragraph from your details. Unlock the full speech. Pay once, get the complete draft, and revise the details if you want. Try it here: ai-speechwriter.pages.dev What I'd tell another builder The lesson that kept proving itself: for emotional, high-stakes writing, the value is not the AI, it is the questions you ask before the AI runs. A good structured intake beats a bigger model with a worse prompt. If you are building anything in this space, spend your time on the interview, not the inference.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/kunstudio/i-built-an-ai-speechwriter-for-the-moments-you-cant-get-wrong-dmc

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
