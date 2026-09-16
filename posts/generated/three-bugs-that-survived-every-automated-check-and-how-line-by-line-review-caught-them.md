---
title: "Three Bugs That Survived Every Automated Check (And How Line-by-Line Review Caught Them)"
slug: "three-bugs-that-survived-every-automated-check-and-how-line-by-line-review-caught-them"
author: "ethantao14"
source: "devto_webdev"
published: "Wed, 16 Sep 2026 20:45:30 +0000"
description: "Game Mode Sandbox is a new project our team is building alongside our stock market game: an app-store-style site where each app is a front-end-only version o..."
keywords: "every, game, round, code, can, which, fix, board"
generated: "2026-09-16T21:07:02.237811"
---

# Three Bugs That Survived Every Automated Check (And How Line-by-Line Review Caught Them)

## Overview

Game Mode Sandbox is a new project our team is building alongside our stock market game: an app-store-style site where each app is a front-end-only version of the stock draft game running on fake data, one per rule variant, so we can playtest which rules feel best before locking anything into the real product. Kenny owns the store pages and data, Jane owns the gameplay screens, and I own the engine, the pure logic layer that decides what a player can do and what happens when they do it. Design principles for the engine Pure functions, no UI : every rule can be tested directly, no clicking through screens required Seeded randomness : every random draw, like which stocks appear each round, comes from the game's seed, so the same seed replays the same game and bugs are reproducible Invalid actions are no-ops : they leave the game state unchanged instead of crashing Money is always rounded to whole cents Market data is passed in, never hardcoded , so tests can supply their own What shipped Four pull requests merged this week, +1,703/-25 lines total: Config validation (+792/-10): checks whether a rule setup is actually playable and explains any problem in plain English, pointing at the setting to fix Board drawing (+456/-5): picks which stocks appear each round across all three board types, greys out unpickable stocks with a reason, and guarantees at least one pickable stock every round An off-by-one fix (+30/-5), covered below Spend validation (+425/-5): works out how much a player can spend per pick under four different money rules, holding back enough cash to cover remaining picks 140 tests pass on main, 122 of them for the engine, roughly two lines of test code for every line of engine code. Three bugs, all caught after everything was green Lint, typecheck, the full test suite, and the build all passed on every pull request. An automated code reviewer ran on two of them and reported no actionable defects. It also could not run the tests in its own sandbox. All three bugs below were found by reading the code line by line against the written spec, not by any of the automated tooling. Bug 1: the shrinking board Classic Draft is supposed to show 5 stocks every round. Instead it went 5, 5, 5, 5, 4, 3, 2, 1. // Before const unownedIndustries = industriesWithStock . filter ( ( industry ) => ! ownsIndustry ( state , industry ) ); The one-per-industry board type was filtering out sectors the player already owned before drawing, a rule meant only for the same-industry board type. One committed test even asserted the shrinking 1-card board as correct behavior, since it was written from the buggy code instead of the spec. The fix draws from every industry with an available stock and greys out owned ones instead of removing them. Verified against 5,000 randomly generated game states across five rule sets: 0 violations. Bug 2: the hold that never ends // Before holdYears > rounds // After holdYears >= rounds A stock bought in round 1 of a 5-round game with a 5-year hold needs a 6th round to auto-sell, which never comes. The check only warned when the hold was strictly longer than the game, not equal to it, so this exact setup passed with no warning. The original tests asserted that this case should not warn, which is how it slipped through. Bug 3: the lost cent // Before Math . floor (( cash / picks ) * 100 ) / 100 // After Math . floor ( Math . round ( cash * 100 ) / picks ) / 100 Floating point decimals like $0.57 are stored as something closer to 0.5699999, and flooring that drops a cent. Tested across every dollar amount from $1.00 to $10,000.00, split 2, 3, 5, and 8 ways: the old formula was wrong in 98,440 cases. The fix does the arithmetic in whole cents, which are exact integers. After the fix: 0 errors across 714,215 checked combinations. Takeaway A green checkmark tells you the code matches the tests. It does not tell you the code matches the spec, and a test written from the code instead of the spec can lock in a bug with just as much confidence as it confirms a fix. Repo: https://github.com/AryamanGandhi/app-store

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/ethantao14/three-bugs-that-survived-every-automated-check-and-how-line-by-line-review-caught-them-401h

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
