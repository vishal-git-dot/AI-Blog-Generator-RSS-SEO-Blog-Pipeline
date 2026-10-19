---
title: "A Practice Planner Should Advance on a Verdict, Not a Stopwatch"
slug: "a-practice-planner-should-advance-on-a-verdict-not-a-stopwatch"
author: "Giang Pham Truong"
source: "devto_webdev"
published: "Mon, 19 Oct 2026 03:41:59 +0000"
description: "Disclosure: I’m Giang Pham, Pianory’s maker. AI helped draft this article and review its claims against the repository. It describes source behavior and exis..."
keywords: "tempo, not, steady, hand, planner, task, session, hands"
generated: "2026-10-19T04:06:19.788872"
---

# A Practice Planner Should Advance on a Verdict, Not a Stopwatch

## Overview

Disclosure: I’m Giang Pham, Pianory’s maker. AI helped draft this article and review its claims against the repository. It describes source behavior and existing unit-test cases, not a runtime study or evidence of better learning outcomes. A practice app can measure how long a screen stayed open. That does not tell it whether a pianist can play the passage. If a planner treats time or a fast playback setting as proof of progress, it can make a difficult task harder for the wrong reason. Pianory’s goal planner uses a smaller, visible signal: the learner’s own verdict after a task. Its session form offers “Still stuck,” “Playable slowly,” and “Fairly steady.” The session record separately stores the player tempo, and the type comment explicitly says that percentage is “not a measure of skill.” The planner does not listen to the piano or verify the learner’s assessment. Make the next step a rule someone can inspect The planner filters to sessions for one goal and ignores review sessions, then reads the newest ordinary session. Its basic ladder is straightforward: “Still stuck” lowers the same hand setup by 10 percentage points. “Playable slowly,” or no rating, repeats the same hand setup and tempo. “Fairly steady” moves a two-hand goal from one hand to the other, then to both hands once the other hand was also steady at that tempo. After both hands are steady, the tempo rises in 10-point steps up to the goal’s target. That target is at least the written tempo and can be higher if the learner chose a higher goal tempo. At the target, the planner suggests completion and a whole-passage task. Here is the core boundary in the implementation: const tempo = last . playbackTempoPercent ; if ( last . rating === ' stuck ' ) { tasks . push ( task ( ' slower ' , passage , last . hands , tempo - TEMPO_STEP )); } else if ( last . rating !== ' steady ' ) { tasks . push ( task ( ' repeat ' , passage , last . hands , tempo )); } TEMPO_STEP is 10. The separate steady branch chooses the next hand, both hands, or the next tempo step. The planner returns advice; it does not turn every elapsed minute into a promotion. Check the boundary with awkward inputs Suppose a goal covers bars 9–16 for both hands at 60% of the written tempo. The first plan asks for the right and left hands separately at 60%. After a steady right-hand session, it asks for the left hand. Once each hand has been steady at 60%, it asks for both hands at 60%. After a steady both-hands session, it can ask for 70%. If the learner instead reports being stuck at 90%, the next task is the same hand setup at 80%. The repository’s unit-test examples also probe misleading signals. One gives a session 86,400 practiced seconds and a 140% playback tempo but rates it “Playable slowly”; the expected task is still a repeat at 140%, not a harder step. Another checks that a steady session at 95% advances to 100%, rather than skipping past the target. These are source tests I inspected; I did not run them for this draft. That suggests a useful test pattern for any adaptive workflow: hold the learner’s explicit verdict constant while making the tempting proxy extreme. A long session with a “stuck” verdict should not advance. A short session rated steady should follow the rule’s next step. The assertion should check the returned task, not just that a planner function ran. Keep the limits visible A self-rating is still a self-rating. Pianory’s code can use it to suggest a smaller next task, but it cannot establish accuracy, comfortable fingering, or whether a learner played the passage correctly. That is a deliberate product boundary in this implementation, and it keeps the planner’s promise modest: help choose what to work on next from information the learner actually supplied. The useful engineering idea is not that every practice app needs this exact ladder. It is that a recommendation should name the signal that moves it forward, keep unrelated telemetry out of that decision, and make the rule easy to test. What input should count as evidence of progress in a learning product?

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/ptrgiang/a-practice-planner-should-advance-on-a-verdict-not-a-stopwatch-5349

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
