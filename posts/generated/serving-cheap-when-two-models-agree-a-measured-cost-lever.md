---
title: "Serving cheap when two models agree: a measured cost lever"
slug: "serving-cheap-when-two-models-agree-a-measured-cost-lever"
author: "Tom Jones"
source: "devto_ai"
published: "Mon, 29 Jun 2026 04:18:02 +0000"
description: "The problem A cost efficient AI system sends easy work to a cheap model and only escalates hard work to an expensive frontier model. The trouble is knowing w..."
keywords: "cheap, test, frontier, answer, two, models, agree, wrong"
generated: "2026-06-29T04:27:36.040642"
---

# Serving cheap when two models agree: a measured cost lever

## Overview

The problem A cost efficient AI system sends easy work to a cheap model and only escalates hard work to an expensive frontier model. The trouble is knowing which is which. When a task has a test, like code with unit tests, you just run the test: if the cheap answer passes, serve it; if not, escalate. But most real prompts have no test. A question like "what time is the maintenance window" cannot be checked by running code. With no test, a careful system escalates almost everything, and you pay frontier prices for work a cheap model could have done. We measured our own gateway and found exactly that. On no-test prompts in automatic mode, the system escalated to the frontier 100 percent of the time, at every context length. The cheap tier was capable, but the system did not trust it without a test, so it never served those answers. The idea: agreement as a stand-in for a test Instead of a test, ask a second, independent cheap model the same question. If the two cheap models agree, the answer is very likely correct, so serve it cheap. If they disagree, that is the genuinely hard case, so escalate to the frontier. Disagreement never serves a worse answer than before, because the disagreement path is the same escalation that used to happen anyway. Agreement only adds a chance to skip an unnecessary frontier call. The gate is conservative by construction, so its only failure mode is paying for an avoidable escalation, never serving a wrong answer, unless the two cheap models happen to agree on the same wrong answer. That single risk is the whole ballgame, so we measured it directly. The one number that can break it The only way this gate ever serves a wrong answer is if two cheap models agree on the same wrong answer. We call that P(wrong given agree). If it is zero, agreement is a safe stand-in for a test. So we stress tested it. We ran two architecturally different cheap models across four task families, including a set of brand new hard traps we wrote ourselves so they could not be memorized from training data (a reverse-percentage trap, a rise-then-fall price trap, a buy-two-get-one trap, a clock-chime interval trap, a snail-in-a-well trap, and more). The result, at n=160: P(wrong given agree) was 0.00 in every one of the four families (retrieval, reasoning, multi-fact, and the new adversarial traps), with zero agree-and-wrong cases out of 160 total. When the two cheap models agreed, they were correct 100 percent of the time, across every category, including the traps designed to fool them. They agreed about 76 percent of the time, and each cheap check took about 0.9 seconds at the median. One honest note on rigor: an early run showed a few apparent failures that turned out to be a formatting bug in our scoring, not real errors. We caught it, fixed it, and re-ran clean. The boring re-check is the work. What it does to cost We shipped the gate to production and re-measured escalation on no-test prompts: context length frontier escalation before frontier escalation after accuracy after 1,000 tokens 100% 40% 100% 4,000 tokens 100% 20% 100% 16,000 tokens 100% 0% 100% 32,000 tokens 100% 0% 100% At long context, where frontier calls cost the most, escalation went from total to zero with no loss of accuracy. Across live traffic the system now serves about 91 percent of requests on the cheap tier. Our blended measured cost is about 0.002 dollars per request, and a repeated question is served from cache at close to zero. * Why it matters * The savings on verifiable work, like code with tests, were already real. This extends the same economics to the large class of work that has no test, which is most real questions, without guessing and without giving up accuracy. The hard cases still get the frontier, and those are exactly the cases worth caching a high quality answer for, so the next identical question is served cheap too. Honesty and limits Every case we proved is a single final answer. We have not yet proven the gate on multi-step reasoning where a final answer can be right by luck on a broken chain, or where two models could agree on the same wrong chain. That is the next frontier and we are not claiming it here. The result above is for two specific cheap models; a different pair could behave differently, and widening model diversity is a known lever we hold in reserve. We are publishing the result and the honesty, not the gating engineering.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/tom_jones_230c4659491adcd/serving-cheap-when-two-models-agree-a-measured-cost-lever-3if6

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
