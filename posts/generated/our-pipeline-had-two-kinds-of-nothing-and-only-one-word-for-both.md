---
title: "Our pipeline had two kinds of nothing and only one word for both"
slug: "our-pipeline-had-two-kinds-of-nothing-and-only-one-word-for-both"
author: "Unmanned Ops"
source: "devto_ai"
published: "Sat, 26 Sep 2026 20:40:57 +0000"
description: "The quietest line our unattended agent writes is the one that says the work queue is empty. It shows up on mornings when everything is fine, and it shows up ..."
keywords: "not, one, nothing, what, does, producer, because, empty"
generated: "2026-09-26T20:53:25.486789"
---

# Our pipeline had two kinds of nothing and only one word for both

## Overview

The quietest line our unattended agent writes is the one that says the work queue is empty. It shows up on mornings when everything is fine, and it shows up on mornings when everything is broken. Same seven words. Same log level. Same position in the run summary. For a long stretch we read that line the way you read a weather report for a city you do not live in: acknowledged, ignored, moved on. Then we started asking what the line actually asserts, and the answer was uncomfortable. It asserts that a consumer looked at a container and found zero items in it. That is all. It does not assert that the producer ran. It does not assert that the producer ran and honestly concluded there was nothing to produce. It does not assert that the producer ran, threw something it swallowed, and returned an empty list on its way out the door. Three very different states in the world collapse into one identical string on disk, and once they are on disk, no amount of downstream cleverness can pull them back apart. This is the specific shape of the problem with unattended operation. When a human is in the loop, ambiguity gets resolved by a person who happens to remember what yesterday looked like. Someone glances at the summary, thinks huh, that's the third empty morning in a row , and goes digging. Remove the person and you remove the only component in the system that was doing the comparison. The log keeps being technically accurate and completely uninformative, indefinitely, at no cost, which is the worst possible combination of properties for a signal. What makes it worse is that emptiness is the default failure mode of almost every producer we have. A step that crashes loudly gets a stack trace and a nonzero exit code and a red mark in the summary. A step that returns [] because a filter matched nothing, because an upstream fetch returned stale data, because a condition silently evaluated false, because an exception got caught two frames up and logged at debug level — that step exits clean. It passes. The run passes. Every gate we built to catch failure was watching for noise, and this failure is made of silence. So we changed what the consumer is allowed to accept. An empty queue is no longer a valid input on its own. It has to arrive with a statement from whoever produced it: this step ran, it examined some number of candidates, it applied some set of criteria, and it is asserting on the record that zero of them qualified. The count of things considered is the part that matters most. Zero candidates examined and zero candidates passing are different sentences, and until we wrote both numbers down we had been reading only the second one. The other half is that the consumer now refuses to interpret an unsigned nothing. If there is no producer statement attached, the run does not proceed quietly to a clean finish. It stops and says it cannot distinguish between having no work and having no information, because that is the literal truth of its situation. It took a surprising amount of arguing with ourselves to accept that this is not over-engineering. The alternative was a pipeline that reports success on the days it does nothing at all, which is not a pipeline, it is a very expensive way to write a timestamp. None of this makes the agent smarter. It just makes one specific lie impossible to tell. Our logs used to describe what the system observed; now, in this one narrow place, they describe who observed it

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/unmannedops/our-pipeline-had-two-kinds-of-nothing-and-only-one-word-for-both-50li

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
