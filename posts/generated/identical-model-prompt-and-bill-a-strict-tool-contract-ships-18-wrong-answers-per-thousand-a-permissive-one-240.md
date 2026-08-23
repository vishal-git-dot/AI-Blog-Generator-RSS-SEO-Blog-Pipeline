---
title: "Identical Model, Prompt and Bill: a Strict Tool Contract Ships 18 Wrong Answers Per Thousand, a Permissive One 240"
slug: "identical-model-prompt-and-bill-a-strict-tool-contract-ships-18-wrong-answers-per-thousand-a-permissive-one-240"
author: "Devanshu Biswas"
source: "devto_ai"
published: "Sun, 23 Aug 2026 12:41:46 +0000"
description: "A wrong tool call has two completely different fates. It either errors - 404, schema violation, permission denied - in which case the agent sees it and retri..."
keywords: "step, wrong, one, per, call, which, silent, trip"
generated: "2026-08-23T12:50:17.235123"
---

# Identical Model, Prompt and Bill: a Strict Tool Contract Ships 18 Wrong Answers Per Thousand, a Permissive One 240

## Overview

A wrong tool call has two completely different fates. It either errors - 404, schema violation, permission denied - in which case the agent sees it and retries with that tool excluded, or it returns something plausible - an empty list, a default object, the right shape with the wrong contents - in which case the agent proceeds on corrupted state. Call the second share silent . Then every later call that validates its inputs is an accidental verifier: call that per-step probability trip . Nothing here simulates language. A step is a choice among K tools, right with probability p, and the whole page turns on one closed form: success = p ^ H wrong = SUM_i p ^ i * ( 1 - p ) * silent * ( 1 - trip ) ^ ( H - 1 - i ) value of a check at step j , relative to the last = ( 1 - trip ) ^ ( H - 1 - j ) Read the second line: a silent error at step i has H-1-i later calls to be caught by, so its chance of reaching the user decays geometrically in how early it happened. Dependency-free JavaScript, five worlds of 1,000 tasks: https://dev48.infy.uk/ai/days/day69-agent-step-reliability.html At 96.5% per step over twelve steps, compounding gives 65.2% - the familiar half. The half nobody prices is the tool layer. Strict ( silent 0.20, trip 0.35): 91.5% success, 18 confidently wrong answers per thousand tasks. Permissive ( silent 0.85, trip 0.05): 68.6% success, 240 . Same model, same prompt, same retry policy, bills of 12.18 against 11.92 - a 13.6x gap in the thing that reaches a customer, bought entirely by whether a wrong call errors and whether the next call validates its input. Neither appears in any agent config. The recommendation I set out to make is Pareto-dominated Spread the verification budget: check every step, or sample every third one. That was the advice. At an identical check count, placement moves the result more than the budget does. verification cost confidently wrong success none 11.86 7.7% 77.5% 3 checks at the front 13.29 7.6% 81.0% 3 checks sampled across 12.94 2.6% 81.2% 1 check on the last step 12.32 1.7% 78.8% 2 checks at the tail 12.62 0.7% 80.0% all 12 steps 17.05 0.7% 93.9% One check at the end beats three sampled on both axes. Three at the front cost 1.43 per task to move 7.7% to 7.6% - indistinguishable from having bought nothing. The mechanism is the geometric term: over twelve steps at trip 0.22, a check at step 1 is worth 15.4x less than one at step 12, because everything downstream is already checking it for free. And then the follow-up conclusion also lost Having found the tail is where checks belong, the tempting next line is that the middle is waste. It is not - it is waste for one of two objectives , and the page had to be rewritten. Two tail checks and all twelve both reach 0.7% wrong, but success is 80.0% against 93.9%. A verifier converts a silent error into a loud one, which does two separate things: it stops a wrong answer shipping, which only matters near the end, and it repairs the step, which matters everywhere. Only repair wants a uniform budget, and a single accuracy number hides which purchase you made. Two more things died. Escalating retries to the 4x model buys 0.3 points for 1.37 units per task, because what makes a retry work is in the error message. And the 4x model itself - 47.86 per task, 93.0% success, 2.7% wrong - is beaten on all three axes by cheap-plus-verify-all at 36% of the price. 93 verifier assertions, including a from-scratch reference simulator agreeing exactly on 1,200 configurations; 23 run in the page. One AI concept a day, measured in-browser: https://dev48.infy.uk/aifromzero.php

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/dev48v/identical-model-prompt-and-bill-a-strict-tool-contract-ships-18-wrong-answers-per-thousand-a-2pd

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
