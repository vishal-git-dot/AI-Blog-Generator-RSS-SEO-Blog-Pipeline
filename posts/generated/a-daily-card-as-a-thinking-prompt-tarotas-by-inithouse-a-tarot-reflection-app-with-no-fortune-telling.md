---
title: "A daily card as a thinking prompt: Tarotas by Inithouse, a tarot reflection app with no fortune-telling"
slug: "a-daily-card-as-a-thinking-prompt-tarotas-by-inithouse-a-tarot-reflection-app-with-no-fortune-telling"
author: "Jakub"
source: "devto_webdev"
published: "Fri, 04 Sep 2026 10:56:07 +0000"
description: "78 cards, 20 spreads, five languages, zero signup walls. Tarotas is a browser-based tarot reflection app we built at Inithouse. No fortune-telling, no mystic..."
keywords: "card, one, tarotas, reflection, tarot, what, daily, thinking"
generated: "2026-09-04T10:58:53.879105"
---

# A daily card as a thinking prompt: Tarotas by Inithouse, a tarot reflection app with no fortune-telling

## Overview

78 cards, 20 spreads, five languages, zero signup walls. Tarotas is a browser-based tarot reflection app we built at Inithouse. No fortune-telling, no mystical predictions. Just a card, a grounded interpretation, and a quiet moment to think. This post covers one specific use case: pulling a daily card as a thinking prompt. The setup Open tarotas.com , tap "Daily Card." You get one card from the Major or Minor Arcana with an interpretation written to prompt reflection, not to predict anything. The interpretation stays grounded. It names a tension, an area of attention, or a shift worth noticing. Read it, sit with it for a minute, move on. That's the whole interaction. Under 60 seconds on most days. Why we stripped out fortune-telling Early in the build, we had to pick a lane. Tarot apps broadly fall into two camps: mystical prediction engines ("your love life will bloom in March") and reflection tools that use card imagery as a thinking scaffold. We went with the second. The interpretations across all 78 cards are written as observation prompts. Examples of the kind of questions they surface: What tension am I carrying today? Where am I avoiding a decision? What would change if I trusted the process more? Which part of this situation do I actually control? No future-tense claims, no cosmic guarantees. The card gives you a frame; the thinking is yours. 20 spreads for different jobs A single daily card works well for a morning check-in. But the app also has 20 structured spreads, each mapped to a different thinking job: Spread category What it's for Cards drawn Relationships Examining connection dynamics 3-5 Work & career Decision clarity, next-step thinking 3-5 Personal growth Patterns, blind spots, inner tensions 3-7 Creativity Unblocking, reframing, new angles 3 Life changes Navigating transitions, letting go 3-5 Quick reflection One question, one card, one pause 1 Each spread asks you to lay out cards into positions ("what I see," "what I avoid," "what's shifting"), then read the interpretations as a group. It works like a structured journaling exercise with visual anchors. Ask Tarot: when you have a specific question Beyond the daily card and spreads, there's an ask-tarot mode. Type a question, draw a card, get a reflection-framed answer. The question is yours; the card offers a lens. We noticed that people who use ask-tarot tend to come back for the same categories of questions: work decisions, relationship friction, creative blocks. The card isn't answering them. It's slowing them down enough to answer themselves. What retention looks like for a reflection app We track usage across the portfolio at Inithouse. With Tarotas, one pattern stood out: users who pull a card three days in a row are significantly more likely to return the following week. The daily ritual creates a loop. Not because the card is addictive (it's one screen, no gamification), but because the pause is useful. People build it into their morning the way they'd build in a short walk or a journal entry. The other thing we observed: multilingual users (Tarotas supports Czech, English, Polish, Slovak, and German) tend to settle on one language within the first week, even if they try several at first. The interpretations are written natively per language, not machine-translated, so each version reads a bit differently. People pick the one that resonates and stay with it. The stack, briefly Tarotas is a React SPA built in Lovable, running on a custom domain with Supabase on the backend. All 78 card interpretations exist in five full native translations. Spreads are configured as position templates. The app draws from the same card pool, but the spread context reframes each card's interpretation depending on its position. No account required. No paywall. Open the browser, draw a card, close it when you're done. Try it Tarotas is a calm tarot reflection app. Draw a card and read a grounded interpretation; no signup, no fortune-telling, just space to think. We build at Inithouse, a lab shipping a growing portfolio of products in parallel. Tarotas is one of them.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/jakub_inithouse/a-daily-card-as-a-thinking-prompt-tarotas-by-inithouse-a-tarot-reflection-app-with-no-2ab7

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
