---
title: "SM-2 Is Not Enough: Where Classic Spaced Repetition Breaks Down"
slug: "sm-2-is-not-enough-where-classic-spaced-repetition-breaks-down"
author: "Alex Chen"
source: "devto_python"
published: "Fri, 24 Jul 2026 19:21:26 +0000"
description: "SM-2 — the algorithm behind Anki and most spaced repetition tools — was published in 1987 and is remarkably durable. It is also wrong in specific, predictabl..."
keywords: "ease, not, failure, you, card, interval, reps, cards"
generated: "2026-07-24T19:37:11.864268"
---

# SM-2 Is Not Enough: Where Classic Spaced Repetition Breaks Down

## Overview

SM-2 — the algorithm behind Anki and most spaced repetition tools — was published in 1987 and is remarkably durable. It is also wrong in specific, predictable ways that matter once your deck grows. What SM-2 does Each card carries an ease factor, starting at 2.5. Grade a review 0-5; on success the interval multiplies by ease, on failure it resets: if quality >= 3 : interval = 1 if reps == 0 else 6 if reps == 1 else round ( interval * ease ) reps += 1 else : reps , interval = 0 , 1 ease = max ( 1.3 , ease + ( 0.1 - ( 5 - quality ) * ( 0.08 + ( 5 - quality ) * 0.02 ))) Simple, no training data, works offline. Genuinely good engineering for 1987. Failure 1: ease hell Every lapse decrements ease and it recovers slowly. A card you failed a few times early gets pinned near the 1.3 floor — permanently reviewed at short intervals even after you have learned it perfectly. The algorithm has no way to say "this card was hard then , it is easy now ." Ease is a one-way ratchet in practice. Failure 2: binary-ish grading carries too much weight The 0-5 scale collapses in practice to "got it / did not." But how you recalled it matters — instant recall and dredging it up after eight seconds are very different memory states that produce identical grades. Response latency is a strong signal and SM-2 ignores it entirely. Failure 3: cards are treated as independent They are not. Learning "kanji A" helps with "compound containing A." Confusable pairs interfere with each other. SM-2 schedules every card in isolation, so interference-prone cards get scheduled adjacently by chance, which is the worst possible arrangement. Failure 4: no forgetting curve per user SM-2 assumes one exponential decay shape. Real retention varies by person, by material type, and by time of day. A fixed curve over-schedules some users and under-schedules others, and neither group can tell. What modern approaches change FSRS models memory with three variables — difficulty, stability, retrievability — and fits parameters to your review history. Concretely that means: Difficulty is not a one-way ratchet You can target an explicit retention rate (say 0.9) rather than accepting whatever falls out Latency and grade both inform the update The cost is that it needs review history to fit, so cold-start is worse. Reasonable compromise: SM-2 defaults until you have a few hundred reviews, then refit. I work on this at SmartRecall — AI-generated cards with scheduling that does not pin everything to the ease floor. Caveat For small decks with few lapses, SM-2 is fine and the added complexity buys nothing. These failures compound with deck size and time — they are invisible at 200 cards and painful at 5000.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/alexrchen/sm-2-is-not-enough-where-classic-spaced-repetition-breaks-down-4hdd

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
