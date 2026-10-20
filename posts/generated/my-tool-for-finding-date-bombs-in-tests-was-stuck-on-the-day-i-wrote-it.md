---
title: "My Tool for Finding Date Bombs in Tests Was Stuck on the Day I Wrote It"
slug: "my-tool-for-finding-date-bombs-in-tests-was-stuck-on-the-day-i-wrote-it"
author: "Sungsoo Youn"
source: "devto_ai"
published: "Tue, 20 Oct 2026 04:10:04 +0000"
description: "A field note from the autonomous Claude Code agent I run every day on one Windows PC. The numbers come from its own ledgers, not from memory. Free to read fi..."
keywords: "date, tool, run, code, day, test, today, tests"
generated: "2026-10-20T04:19:10.501781"
---

# My Tool for Finding Date Bombs in Tests Was Stuck on the Day I Wrote It

## Overview

A field note from the autonomous Claude Code agent I run every day on one Windows PC. The numbers come from its own ledgers, not from memory. Free to read first: a PDF sample of the book behind this setup — its first 3 chapters: https://dbsoul.gumroad.com/l/autonomous-ai-agents-claude-code-free-sample A date bomb is a test that passes today and fails on a later date: an expiry check, a weekly cycle, a cutoff someone wrote as a fixed day. My project has a small tool for finding them. It moves today forward by 1, 2, 3, 4, 5, 9, 30 and 100 days and runs the whole test suite at each date. Its first run, on August 20, found a test that would have turned red four days later. October 8 I opened the tool while looking for material for a post. The base date was hard-coded to August 20, the day the tool was written. The comment next to it said the tool should not depend on today. So on October 8 the eight dates it tried were August 21 to 25, August 29, September 19 and November 28. Seven of the eight were already in the past. A tool built to catch tests that only work today only worked on the day it was written. Four more problems in the same file One clock out of two. It replaced date.today() and left datetime.now() alone. Before fixing anything, I ran a quick copy of the same approach on six future dates of my own choosing. Every date showed the same two failures, in two tests whose shared helper read date.today() while the code under test read datetime.now() . Those failures came from the time travel, not from the project. It wrote the fake date into the project. It put a conftest.py at the top of the repository and removed it at the end. While it ran, any other pytest started in that folder saw the fake date too, and my agent's scheduled runs and its CI hook both start pytest there. If the run was interrupted, the file stayed. Importing it ran it. The loop sat at module level, with no main guard. A fixed path. The repository path was hard-coded as an absolute path to my own folder. The mutation-testing tool next to it had the same string. Number 3 went off while I was writing a test for it. I already knew about it. To watch the new test fail first, I loaded the old file inside a test. Loading it started the full eight-date loop and wrote a conftest.py that set today to August 21. I stopped it within two minutes and deleted the file. Any other test run in that folder during those minutes would have seen August 21. The fix The base date is the day you run it. --base 2026-08-20 repeats an old run. Both clocks move by the same number of days. The time of day stays. The fake date lives in a pytest plugin in a temporary folder, loaded with -p for that one run. Nothing is written into the project, and nothing is left behind if you stop it. A main() function behind a main guard. Both tools find the repository from their own file location. Two surprises after the fix pandas crashed. When I ran the fixed tool, pandas was first imported after the datetime classes had been swapped, and its C extension crashed while loading with a stack overflow: exit code 127, and no pytest summary. Every date came back red with an empty result column. The plugin now imports pandas before swapping, and a run that ends without a summary prints its exit code and last line. A shift inside a shift. One of my new tests runs the tool on a tiny fake project. On the next full run, after the pandas fix, that test failed inside the outer time travel: the inner run's date came out one day off. The plugin now receives the target date instead of a number of days, and measures the shift against the real clock. Result On October 8 the fixed tool ran the suite at October 9, 10, 11, 12, 13 and 17, November 7, and January 16, 2027. All eight dates passed, each with 2,915 or 2,916 tests. No date bombs this time. The tool now has tests of its own: importing it runs nothing, with no base date every date is in the future, and a fake project passes only if both clocks return the shifted day and nothing is written into it. I then broke the tool on purpose in four ways: fixed base date, datetime.now() left alone, fake date written into the repository, pandas not loaded first. The tests caught all four. The rules A checker is code too. Give it the same tests as the code it checks. Take today from the run, not from the source. If you need a fixed date to repeat a result, pass it in. Move every clock the code reads. date.today() and datetime.now() are two clocks. A check should not write into the folder it checks. Other jobs share that folder. Where this comes from. Every post here comes from one setup I run daily: a CLAUDE.md, memory files the agent reads before it touches anything, and a separate auditor agent that returns PASS or FAIL. The first 3 chapters of the book that walks through it are free as a PDF: https://dbsoul.gumroad.com/l/autonomous-ai-agents-claude-code-free-sample The full edition is 11 chapters plus 4 ready-to-use templates (CLAUDE.md starter, memory files, auditor checklist, measurement guide) and a hands-on section for every chapter, $19 as a PDF: https://dbsoul.gumroad.com/l/autonomous-ai-agents-claude-code Questions about the setup are welcome in the comments — I'll answer with what actually happened, not theory.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/dbsoul/my-tool-for-finding-date-bombs-in-tests-was-stuck-on-the-day-i-wrote-it-5af7

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
