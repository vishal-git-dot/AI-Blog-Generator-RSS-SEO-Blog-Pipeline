---
title: "My CI/CD Pipeline Passed for 3 Months — Then I Read the Logs"
slug: "my-cicd-pipeline-passed-for-3-months-then-i-read-the-logs"
author: "kol kol"
source: "devto_webdev"
published: "Fri, 03 Jul 2026 14:07:21 +0000"
description: "My CI/CD Pipeline Passed for 3 Months — Then I Read the Logs The green checkmark was our favorite color. Every PR. Every merge. Every deploy. All green. Then..."
keywords: "tests, test, pipeline, real, had, mock, our, not"
generated: "2026-07-03T14:21:09.821083"
---

# My CI/CD Pipeline Passed for 3 Months — Then I Read the Logs

## Overview

My CI/CD Pipeline Passed for 3 Months — Then I Read the Logs The green checkmark was our favorite color. Every PR. Every merge. Every deploy. All green. Then one Tuesday afternoon, a user reported a feature that had been broken for weeks. Not hours. Weeks. I opened the CI pipeline logs. And that's when I realized — our "passing" builds had been lying to us the entire time. The Setup Our pipeline looked textbook: Lint → 2. Unit tests → 3. Integration tests → 4. Build → 5. Deploy Every step passed. 100% success rate. For months. The Discovery A user filed a bug: "The export button doesn't work." I clicked it myself — nothing happened. No error message, no crash. Just... silence. I traced it back to a PR from 11 weeks ago. The pipeline had passed. The code review had been approved. But the feature had been silently broken since day one. Here's what went wrong — and it's not what you'd expect. The Problem: Tests That Don't Test Our integration test suite had a bug. A real bug, in the test code itself. // What we thought we were testing: describe ( ' Export feature ' , () => { it ( ' should export user data ' , async () => { const result = await exportUserData ( userId ); expect ( result . status ). toBe ( ' success ' ); }); }); // What was actually happening: // The test mocked the ENTIRE export service. // So it tested the mock, not the real code. // The mock always returned { status: 'success' }. The mock was configured at the module level. Every test that imported the export module got the mocked version — including the integration tests that were supposed to catch exactly this kind of bug. The Root Cause: Over-Mocking We had fallen into the classic over-mocking trap: Unit tests: Mocked everything to isolate the unit → fine Integration tests: Also mocked everything "for speed" → not fine E2E tests: Didn't cover this specific flow → gap in coverage Our integration tests were really just expensive unit tests. They verified that our mocks worked correctly. Not that our actual code worked. The Fix Three changes that made a real difference: 1. Mock Boundaries Only mock at unit test level. Integration tests must hit real service boundaries — databases, APIs, file systems. If it's slow, that's a signal, not a problem to hide. 2. Contract Tests Added contract tests between services. If the mock returns something the real service wouldn't, the contract test catches it. // Contract test: verify mock matches real behavior it ( ' export mock matches real service contract ' , async () => { const mockResult = await mockExport ( userId ); const realResult = await realExport ( userId ); expect ( Object . keys ( mockResult )). toEqual ( Object . keys ( realResult )); expect ( typeof mockResult . data ). toEqual ( typeof realResult . data ); }); 3. Pipeline Health Metrics Started tracking not just pass/fail rates, but what the tests actually exercised. Coverage numbers went down initially (from 94% to 67% real coverage) — and that was the most honest metric we'd had in months. The Real Lesson A green pipeline doesn't mean your code works. It means your tests passed. Those are two different things. The most dangerous bugs aren't the ones that break your pipeline. They're the ones your pipeline says are fine. If your CI/CD is all green all the time, ask yourself: are my tests catching bugs, or just confirming that my mocks are consistent? Questions I Ask Myself Now When was the last time a test failed for a real bug? Do my integration tests actually integrate? If I removed all my mocks, how many tests would still pass? Am I measuring test coverage or test confidence? A pipeline that never fails isn't reliable. It's untested.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/kollittle/my-cicd-pipeline-passed-for-3-months-then-i-read-the-logs-4mbj

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
