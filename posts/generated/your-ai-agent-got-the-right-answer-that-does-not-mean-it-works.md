---
title: "Your AI Agent Got the Right Answer. That Does Not Mean It Works."
slug: "your-ai-agent-got-the-right-answer-that-does-not-mean-it-works"
author: "Paul Crinigan"
source: "devto_ai"
published: "Mon, 28 Sep 2026 22:51:34 +0000"
description: "If you have shipped an agent that passed every test and then broke in production, this one is for you. Here is what changes when the software you are testing..."
keywords: "agent, same, one, model, judge, every, test, different"
generated: "2026-09-28T23:06:03.075934"
---

# Your AI Agent Got the Right Answer. That Does Not Mean It Works.

## Overview

If you have shipped an agent that passed every test and then broke in production, this one is for you. Here is what changes when the software you are testing does not give the same answer twice. Most teams test their first agent the way they test regular software. Write a few inputs, check the outputs, ship when everything is green. Then the agent fails in production on a request that looks almost identical to one that passed, and nobody can say why. The agent is only part of the problem. The testing approach assumes a kind of predictability that agents simply do not have. Why a Passing Test Means Less Than You Think Traditional tests rely on determinism: same input, same output, pass today and pass tomorrow. Agents break that. The same prompt sent to the same model can produce a different reasoning chain, a different sequence of tool calls and a different answer on consecutive runs. Errors also compound. An agent can pick the right tool, write a sensible query, get valid results, then misread one field and carry that mistake through every step after it. That changes what a test result means. One pass is a sample, not a proof. Fifty to one hundred cases per task category is roughly where real performance differences separate from random variance, and the useful assertion becomes "this category passes at least 90 percent of the time" rather than "this case passed." Our complete guide to AI agent evaluation covers the different eval types, from offline and online runs to adversarial and regression suites. Grade the Path, Not Just the Destination Consider a research agent asked for the population of Tokyo. It searches, gets a page about Japanese demographics, pulls the right number and passes. Ask it about Osaka and it may run a sloppy search, get a Tokyo page back and return the wrong city's figure. The first run was correct by luck, and output only testing could never tell the difference. Trace based evaluation looks at every step: the queries the agent wrote, the tools it chose, whether it used what those tools returned, and how it recovered when something failed. An agent that passes 95 percent of output checks but shows flawed reasoning in 30 percent of its traces is fragile, and small changes in input will expose it. The cheapest checks need no model at all: alert when step count goes past twice the median for a task type, and validate every tool call's arguments against its JSON schema. There is a full walkthrough of trace based evaluation if you want the implementation details. Make Your LLM Judge Earn Its Trust Open ended outputs like emails, summaries and plans have no single right answer, so most teams use a language model as a judge. It works, but only after calibration. Pick 50 to 100 real outputs across the full quality range, have two or more people score them with the same rubric, then run the judge on the same set. Aim for at least 80 percent agreement within one point on a five point scale before letting the judge gate anything. Judges bring their own biases too. They tend to favor longer answers, whichever option is shown first, and output from their own model family. Concrete rubrics with separate dimensions, temperature at zero, and a judge from a different model family than the agent all help. Our guide on how to use an LLM as a judge goes through rubric design, prompt structure and bias checks step by step. Put Cost on the Same Scorecard An agent that reaches 95 percent accuracy with twelve model calls per task is a different product from one that reaches 93 percent with three. If evaluation only reports accuracy, every change that adds another retry or a bigger model looks like progress. Report cost per successful task next to accuracy, and the tradeoff becomes a decision instead of a surprise on the invoice. The Takeaway Agent evaluation is less about writing more tests than about asking better questions of each run: how often it passes, how it got there, and what it cost. Start with volume and trace checks, calibrate any judge against real people, and let every production failure become a new test case.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/paulcrinigan/your-ai-agent-got-the-right-answer-that-does-not-mean-it-works-46b5

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
