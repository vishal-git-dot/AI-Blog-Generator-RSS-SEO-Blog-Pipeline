---
title: "My CI hadn't run a single one of those tests in two months and stayed green the whole time"
slug: "my-ci-hadnt-run-a-single-one-of-those-tests-in-two-months-and-stayed-green-the-whole-time"
author: "Juan Camilo Auriti"
source: "devto_python"
published: "Wed, 23 Sep 2026 11:00:00 +0000"
description: "I added a dependency to a test helper and forgot to declare it in the dev extra. Locally it was already installed, so everything passed. In CI it wasn't, and..."
keywords: "tests, you, pytest, test, skipped, green, not, suite"
generated: "2026-09-23T11:11:45.084219"
---

# My CI hadn't run a single one of those tests in two months and stayed green the whole time

## Overview

I added a dependency to a test helper and forgot to declare it in the dev extra. Locally it was already installed, so everything passed. In CI it wasn't, and the tests that needed it did not fail. They skipped. Skips exit 0. The checkmark stayed green for two months. Why it skips instead of failing The pattern is one line, it's in every codebase, and it's usually correct: aiosqlite = pytest . importorskip ( " aiosqlite " ) That line means: this test needs something optional, and if it isn't here, move on . Which is right when the dependency is genuinely optional — a test for the Postgres backend on a machine with no Postgres shouldn't fail the build. The problem is what it looks like from outside. importorskip is a decision that the test is optional, taken at import time, and the only place it surfaces is a number in a summary line nobody reads: 1284 passed, 168 skipped in 42.11s 168 skipped. Two months earlier it was 6. Nothing in that output tells you which number is the anomaly, and the exit code is 0 either way. After declaring the dependency, the same suite reported 1452 passed . The 168 hadn't been slowly rotting. They'd stopped running all at once, on a specific commit, and the build had been green through every one of them. The part that stung I had a suite I trusted. I merged on green. The whole point of the suite was to tell me when I broke something, and for two months it had quietly stopped being able to. Nothing was misconfigured. No warning. No deprecation. CI did exactly what it was asked. The failure mode was that the number of tests it ran was never something anyone asserted on. The guard There is no --min-tests flag. There is a hook, and it's eight lines: # conftest.py MIN_TESTS = 1400 def pytest_sessionfinish ( session , exitstatus ): collected = session . testscollected if collected < MIN_TESTS and not session . config . option . collectonly : session . exitstatus = 1 print ( f " \n FAIL: { collected } tests collected, floor is { MIN_TESTS } . " f " Did a dependency stop resolving? " ) Three notes on that, all learned by getting it wrong. testscollected , not passed. You want to catch tests that vanished, and a skipped test still counts as collected — so this alone would not have caught my bug. Which brings me to the second guard, below. Use the floor to catch tests that disappear from collection entirely (a broken import in a conftest, a renamed directory, a bad -k ), because that's the failure that turns a 1452-test suite into 3 without a word. Guard collectonly . Without it, pytest --collect-only in a subset trips your own floor and you'll waste twenty minutes. Set the floor slightly below current, and raise it. Not at current — every new branch that hasn't added a test yet will fail. Below, and bump it when it drifts far. For the skip case specifically, the guard is different and simpler: # pytest.ini [pytest] addopts = -rs -rs prints the reason for every skip. It doesn't fail anything — it just puts SKIPPED [168] tests/conftest.py:14: could not import 'aiosqlite' in the log where a human can see it. Two months of my logs had that line. I never read them, because they were green. If you want it to actually fail, the strict version: def pytest_sessionfinish ( session , exitstatus ): skipped = len ( session . config . pluginmanager . get_plugin ( " terminalreporter " ). stats . get ( " skipped " , [])) if skipped > MAX_SKIPS : session . exitstatus = 1 I don't use that one. It fights with legitimately environment-dependent tests and I got tired of tuning MAX_SKIPS . The floor plus -rs was enough. The real fix was upstream of all of it The guards catch the symptom. The cause was that a dependency my tests could not run without was declared as though they could. # before — aiosqlite nowhere, importorskip papers over it [project.optional-dependencies] dev = [ "pytest" , "pytest-cov" , "ruff" ] # after dev = [ "pytest" , "pytest-cov" , "ruff" , "aiosqlite" ] And then delete the importorskip for it. If the suite requires it, importorskip is a lie that makes the requirement look like a preference. That's the rule I took away: importorskip is for dependencies you have decided the test can run without. If you haven't made that decision deliberately, you've made it accidentally. Check yours in one command If you have a CI suite you trust, this tells you the number you've never looked at: pytest --collect-only -q 2>&1 | tail -1 Compare it to what you'd have guessed. Then run the real suite with -rs and read the skip reasons — all of them, once. Mine had a two-month-old import error sitting in plain text under a green checkmark. The uncomfortable general version: every green build asserts that the tests that ran, passed. None of them assert that the tests ran.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/juanauriti/my-ci-hadnt-run-a-single-one-of-those-tests-in-two-months-and-stayed-green-the-whole-time-n15

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
