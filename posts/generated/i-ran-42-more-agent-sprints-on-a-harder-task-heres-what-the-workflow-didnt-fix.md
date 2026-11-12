---
title: "I ran 42 more agent sprints on a harder task. Here's what the workflow didn't fix."
slug: "i-ran-42-more-agent-sprints-on-a-harder-task-heres-what-the-workflow-didnt-fix"
author: "Huzair Saputra"
source: "devto_ai"
published: "Thu, 12 Nov 2026 23:23:17 +0000"
description: "In the first post a Scrum workflow for coding agents looked clean: with the skill, 6 of 6 runs met every item of the Definition of Done, against 3 of 6 witho..."
keywords: "runs, skill, item, one, gpt, model, every, without"
generated: "2026-11-12T23:24:23.225505"
---

# I ran 42 more agent sprints on a harder task. Here's what the workflow didn't fix.

## Overview

In the first post a Scrum workflow for coding agents looked clean: with the skill, 6 of 6 runs met every item of the Definition of Done, against 3 of 6 without it. Several of you pointed out the obvious catch. One small task, one model, three runs per side. That's a hint, not a result. So I ran a bigger one, and I wrote down the rules before I looked at a single run. What changed A harder sprint. A new Go repo with four items that depend on each other across modules. Two of them carry an authorization rule the tickets only imply. One runs a code generator that also writes into a module no role may commit. Hidden acceptance tests. Each item has tests the agents never see. This is the part I care about most, because a tidy process that ships the wrong code is still the wrong code. Seven models, two vendors. Haiku, Sonnet and Opus 5.5 in Claude Code; gpt-6-luna , gpt-6.1-sol , gpt-5.6-sol and gpt-6-astra in Codex CLI. Each with and without the skill. Pre-registered. Hypotheses, measures, the rule for adding runs and the scoring script were frozen before the first data run. Every change after that is logged with a date. Two runs per cell first. The pre-registered rule then flagged every model as inconsistent, so every cell got a third run. 42 runs, 14 hours, all on subscriptions. What the skill still does It makes the process complete. Without it, review verdicts and the sprint reports were missing in 10 of 21 runs. With it, 2 and 1 of 21. Same pattern as last time, now across seven models instead of one. It also made runs cheaper for Sonnet, Opus, gpt-6.1-sol and gpt-6-astra . I expected the opposite. And nobody, in either arm, committed the generator's write into the other module. Strong models respect write regions when you spell them out. What it doesn't do It doesn't reliably make the code more correct. Hidden tests went up for Haiku (+1.3 of 4 items), Sonnet and gpt-5.6-sol . They stayed flat for gpt-6.1-sol and Astra, and dipped slightly for Opus and Luna. The whole hidden suite passed in 3 of 21 runs without the skill and 4 of 21 with it. A workflow can make sure tests exist and get reviewed. It can't make the reviewer spot an authorization rule nobody wrote down. It doesn't help every small model. Haiku gained the most. Luna, the small Codex model, got worse with the skill. One of its runs merged nothing at all. It can get expensive. With gpt-5.6-sol , the skill's portable mode burned through tokens: one attempt alone read 17.9 million input tokens. Cost per passed hidden item went from $0.72 to $2.79. The bug in my own grader This one stung. One Definition-of-Done item checks that implementation and tests were committed separately for each item. My grader found an item's commits through its branch or an item ID in the commit message. Lanewright deletes item branches after merging, and its role commits don't repeat the ID. So the grader saw only the docs commits and failed that item in 17 of 21 runs with the skill. The separation was there. Reading the same commits from each merged pull request, with the same rules, gives 19 of 21 with the skill and 21 of 21 without. I didn't touch the frozen grader. The report shows its numbers as the main result and the re-scored ones next to them. With the fix, the skill raised the Definition-of-Done score in 6 of 7 models. Without it, in 3. You can decide which one you believe; both are in the data. Claude vs Codex, briefly Matched by list price, the Claude model met as many or more items in 7 of 8 comparisons. Codex was cheaper per passed item on the cheap and middle pairs. On the expensive pairs it flipped. Price isn't ability and the model generations differ, so I'd read this as a sketch, not a ranking. What's next Sixteen more runs start this weekend: Lanewright against the free scrum-kit in Claude Code, across four model settings, including a cheap orchestrator driving stronger roles. After that the task, hidden tests and harness go public too. Everything above, with every run's numbers, the pre-registration and the deviations log, is here: bench/hard-2026-11-10 . If you want to try it Lanewright is a paid skill on Agensi: Lanewright on Agensi . Version 1.0.1, the exact build tested here. The planning side is free. Four MIT skills take a loose brief to an SRS, a weekly sprint plan and a backlog a human signs off before any agent starts: Intake , SRS , Sprint Planner , Backlog Check . And scrum-kit stays free and MIT, with prompts in Bahasa Indonesia.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/huzair_saputra/i-ran-42-more-agent-sprints-on-a-harder-task-heres-what-the-workflow-didnt-fix-33hj

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
