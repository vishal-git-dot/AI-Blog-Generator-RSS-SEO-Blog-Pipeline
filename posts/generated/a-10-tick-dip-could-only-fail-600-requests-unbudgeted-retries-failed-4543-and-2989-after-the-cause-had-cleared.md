---
title: "A 10-Tick Dip Could Only Fail 600 Requests. Unbudgeted Retries Failed 4,543, and 2,989 After the Cause Had Cleared"
slug: "a-10-tick-dip-could-only-fail-600-requests-unbudgeted-retries-failed-4543-and-2989-after-the-cause-had-cleared"
author: "Devanshu Biswas"
source: "devto_ai"
published: "Sun, 23 Aug 2026 12:43:09 +0000"
description: "Level 0 of Arc Ops made a retried tool call safe to repeat. This level is about what happens next, which is that it gets repeated - by every client at once, ..."
keywords: "budget, not, breaker, has, tick, only, every, dependency"
generated: "2026-08-23T12:50:17.234186"
---

# A 10-Tick Dip Could Only Fail 600 Requests. Unbudgeted Retries Failed 4,543, and 2,989 After the Cause Had Cleared

## Overview

Level 0 of Arc Ops made a retried tool call safe to repeat. This level is about what happens next, which is that it gets repeated - by every client at once, at the moment the dependency is least able to answer. A retry is a request that a failure created, and metastable failure needs nothing exotic: finite capacity, a brief trigger, and clients that retry. Repo: https://github.com/dev48v/arc-ops - PUBLIC, MIT, dependencies = [] , 238 pytest (114 of them in the five new L1 files), no network and no model. Level 1 computes in your browser on a page that really is self-contained: no CDN, no font host, not one asset fetched off the page - https://dev48.infy.uk/arcops/level1-retry-budgets.html Steady 100 intents per tick, capacity 120, dipping to 40 for ten ticks. Four fleets, identical traffic, and every panel ships its control ( budget.NoBudget , selectable as use: none ). fleet ceiling failures after the cause cleared recovery intents lost no budget (the control) 400 4,543 2,989 +29 ticks 0 no budget, no jitter 400 2,840 1,800 +20 ticks 0 budget 0.10 110 730 0 +0 594 budget + breaker 110 1,224 201 +2 1,116 The dip could only fail 600 requests. The control failed 7.57x that, hit 2,443 requests that first arrived once the dependency was already healthy , and turned a ten-tick dip into a thirty-nine-tick outage. The difference is not max_retries , which is 3 in all three of the first rows. A per-call limit multiplies by a client count nobody chose; a budget expressed as a fraction of successful traffic caps the fleet at 1.1x normal regardless of how many clients exist. Retries are funded by successes, so in a total outage there are none: the count-only policy still permits 3,000 retries over 1,000 calls, the token bucket permits 10 - its min_tokens floor, and the deliberate hole in the scheme. l1_retry_budgets : use : token_bucket settings : budget_ratio : 0.1 # no default - it has to be chosen out loud jitter : full max_retries : 3 # kept last: the setting every codebase has, # and the least important of the four The trade points the other way from what I set out to claim I expected the budget to make the incident smaller. It does not. The unbudgeted control permanently loses 0 intents - it eventually rescues everything - while the budget drops 594 . It buys that rescue by inflicting roughly 3,800 extra failures on traffic that was never involved. A retry budget does not shrink the incident. It decides who pays for it, and that has to be said in two columns, never one. Two more results that came out sideways. Full jitter is not enough: 200 clients failing at the same instant put a peak of 78 arrivals into 60 spare capacity and 23 of them re-fail. Fixed and exponential backoff have the identical peak of 200 - a deterministic delay applied to a synchronised population produces a synchronised population, and only decorrelated jitter, at peak 33, is absorbed. And the false-trip worry about circuit breakers is largely misplaced. A consecutive-failure breaker trips zero times against a healthy dependency at 2% errors, and a threshold-3 breaker needs a 10% background error rate before it opens at all. Its real cost is partial failure: a breaker has one all-or-nothing lever, so a dependency that is 30% broken has 100% of its traffic shed, and 114 answers that existed are thrown away - counted, not estimated, because the ground-truth outcome is drawn for every request including the ones the breaker refused to send. 173 in-page assertions. Nine levels, one at a time: https://dev48.infy.uk/arcops.php

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/dev48v/a-10-tick-dip-could-only-fail-600-requests-unbudgeted-retries-failed-4543-and-2989-after-the-26b2

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
