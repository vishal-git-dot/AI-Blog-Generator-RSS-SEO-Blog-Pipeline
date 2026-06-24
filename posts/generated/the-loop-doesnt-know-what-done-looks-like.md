---
title: "The loop doesn't know what done looks like."
slug: "the-loop-doesnt-know-what-done-looks-like"
author: "Paul Penling"
source: "devto_ai"
published: "Wed, 24 Jun 2026 09:39:32 +0000"
description: "Loop engineering has been making the rounds. Engineers at Anthropic, Google, OpenAI — people worth listening to — saying they've stopped writing prompts. The..."
keywords: "loop, you, what, spec, not, done, agent, when"
generated: "2026-06-24T09:40:50.192399"
---

# The loop doesn't know what done looks like.

## Overview

Loop engineering has been making the rounds. Engineers at Anthropic, Google, OpenAI — people worth listening to — saying they've stopped writing prompts. They write loops now. The idea is straightforward: instead of manually prompting an agent for each task, you design a system that prompts, runs, evaluates, and iterates until a goal is reached or a stopping condition fires. Act, observe, refine, repeat — without you in between every step. It's a real shift. Loops produce genuinely different results from one-shot prompts, in the same way a program with error handling and retry logic produces different results from a program that crashes on first failure. The pattern is worth taking seriously. But I've noticed something in how it's being described that I think is worth examining. A lot of the framing is: tell the agent what you want, set it loose, let it keep going until it's done. And that particular instruction — "keep going until it's done" — is where I think loop engineering can go wrong in exactly the same way vibe coding does. Vibe coding's failure mode is well-understood by now. You describe roughly what you want, the model builds something, you look at it and say "more like that but better," and you iterate until it feels right. It works for prototypes. It breaks down when you need something specific, when multiple people need to agree on what was built, or when the thing you're building has to keep being right six months from now when nobody remembers the conversation. The failure isn't the model. The failure is the absence of a fixed definition of what success looks like. The model has nothing to converge toward except your next prompt. A loop without a clear target has the same problem, just running autonomously. The agent makes progress, hits an evaluation signal — tests pass, lint is clean, CI goes green — and declares itself done. But "tests pass" is not the same as "we built the right thing." If the original goal was ambiguous, the loop will find a way to satisfy its stopping condition that may or may not match what was actually wanted. It can do this quickly, confidently, and at considerable cost in tokens. This is the part that doesn't get enough attention in the loop engineering conversation: the evaluation layer is only as good as what you're evaluating against. Tests tell you the code does what the tests expect. CI tells you the build is clean. Neither tells you whether the behaviour that shipped is the behaviour that was specified. If you haven't written down what the feature is supposed to do — concretely, with expected results and explicit constraints — the loop is optimising toward a signal that doesn't fully represent the goal. The result tends to be expensive drift. The agent iterates, token costs accumulate, and what emerges is something that passes the available checks without actually satisfying the original intent. Not because the model failed, but because the model was never given a precise enough target to hit. A spec fixes this. Not a prompt — a spec. A written, agreed statement of what done actually looks like: the expected behaviour, the constraints that apply, the things explicitly out of scope. An artifact the loop can validate against, not a description it interprets differently on each pass. When a loop has a spec as its anchor, several things change. The evaluation layer has something real to measure against, not just the proxy signals of passing tests and green builds. The stopping condition becomes meaningful — the loop terminates when the output matches the spec, not when the agent runs out of ideas or token budget. And when something drifts between iterations, the spec is there to catch it: not "the previous output was better" but "this no longer satisfies condition four." It also contains costs in a way that "keep going until done" cannot. A loop without a target will explore. A loop with a spec will converge. The more interesting framing for loop engineering, I think, isn't "how do we keep the agent running longer" — it's "how do we give the agent a precise enough mission that the loop terminates correctly." That's a spec problem, not a loop problem. The mechanism for running autonomously is the easy part. Knowing what done looks like, with enough precision that a model can verify it without ambiguity, is the hard part. It was always the hard part. Penling is built around writing that spec before the loop starts — a shared workspace where product, engineering, and design align on what done looks like, producing a spec that lives in the repository and gets handed directly to the agent or loop as its input. The loop still runs. It just knows where it's going. This is part of a series on spec-driven development. Earlier pieces cover why briefs and specs are different things and where specs tend to get written — and why that placement matters .

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/penling_paul/the-loop-doesnt-know-what-done-looks-like-2864

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
