---
title: "The AI reviewer found a real bug. Its suggested fix would have broken my app."
slug: "the-ai-reviewer-found-a-real-bug-its-suggested-fix-would-have-broken-my-app"
author: "健太 橘"
source: "devto_webdev"
published: "Sat, 05 Sep 2026 03:23:50 +0000"
description: "TL;DR — I put an AI code reviewer on a pull request written by an AI coding agent. On the default setting it found nothing. On the strict setting it found a ..."
keywords: "text, not, what, code, nothing, reviewer, would, have"
generated: "2026-09-05T03:53:09.693396"
---

# The AI reviewer found a real bug. Its suggested fix would have broken my app.

## Overview

TL;DR — I put an AI code reviewer on a pull request written by an AI coding agent. On the default setting it found nothing. On the strict setting it found a real vulnerability. And the patch it offered would have quietly broken every negative number in the exported file. I ship small browser tools written by Claude Code, and I am not a good enough reviewer to catch a security bug in code I did not write. That is the awkward kind of gap: the code looks fine, the page works, the tests pass. So I installed CodeRabbit on the repository and gave it something real to read: a CSV export for a pricing calculator. One row per material line, then other costs, total cost, selling price, profit, margin. About sixty lines of vanilla JS. My own checks passed first — a static site audit, plus a headless browser run of the tool, 14 of 14. Round 1: silence No actionable comments were generated in the recent review. That is the default. CodeRabbit ships a review profile called CHILL , tuned not to nag. For a team drowning in review comments that is probably right. For someone who cannot fully audit their own code, silence is the least useful answer available. So I committed a config file: # .coderabbit.yaml reviews : profile : assertive Same commit. Same diff. Same reviewer. Only the setting changed. Round 2: a real bug, checked the hard way The strict pass flagged CSV formula injection (CWE-1236) , and it was right. A spreadsheet treats a cell that begins with = , + , - or @ as a formula. Name a product =1+1 , export it, and the number two appears in the file the other person opens. Pick a nastier formula and it stops being a curiosity. My csvCell() escaped quotes and commas correctly and did nothing at all about this. What surprised me was how it checked. Folded into the comment was a shell command it had actually run against the repo — a ripgrep over every place a product name or unit flows into the exporter — to see whether something upstream already sanitised the value. It did not pattern-match on the words "CSV" and "user input" and fire. It went and looked. The part where you cannot just click Accept It also offered a committable patch: if ( typeof value === " string " && /^ [ =+ \- @ ] / . test ( text )){ text = " ' " + text ; } Reasonable on its face: numbers do not need protection. Except in this exporter every number has already been through toFixed() by the time it arrives, so a loss of -1.50 shows up as a string starting with a minus sign. That patch would have quoted it into text, and the profit column in the exported sheet would have silently stopped adding up. It knew the vulnerability class. It did not know what the values in this particular function actually are when they get there. Round 3: it caught the hole in my fix My replacement skipped anything that looked like a number, using a hand-written pattern: optional minus, digits, optional dot, more digits. The next review pointed straight at it — -1e-7 starts with a minus, fails that test, gets exported as text. Reachable here, because raw material amounts never go through toFixed() , so a small enough amount really does stringify into exponent notation. Right again. So I threw my regex away instead of patching it: if ( /^ [ =+ \- @ \t\r] / . test ( text ) && isNaN ( Number ( text ))){ text = " ' " + text ; } Let the language decide what a number is: input output =1+1 '=1+1 @sum '@sum +5x '+5x -1.50 -1.50 -1e-7 -1e-7 That version went back through the same strict review and came back with nothing to add. What I actually take from this The default setting hides the product. Had I tried it once, seen the cheerful nothing and moved on, my conclusion would have been "it finds nothing, so it does nothing." The finding was there the whole time, behind one line of config. It is good at known bug classes in unfamiliar code. CSV injection is well documented, easy to skip while writing, and invisible to a passing test suite. It is weaker on the consequences of its own advice. Twice the finding was right and the patch needed a second pass — once because of what the values already were, once because of a case the pattern missed. Two AIs disagreeing beat either alone. What shipped is not what the coding agent wrote and not what the reviewer suggested. It is the third thing that came out of the argument. On cost, so nobody has to guess: public repositories are reviewed free with no time limit. Signing up put me on a 14-day trial of a paid plan without a card; when it ends, a public repo keeps being reviewed. I have paid nothing. There is no affiliate link in this post. The whole thread is public if you want to read the findings yourself: PR #1 . The question I am left with Auto-apply is the obvious next step for tools like this — the suggestions arrive as committable patches, and merging one is a single click. But both patches I was handed here were correct about the problem and wrong about this codebase. So: do you let an AI reviewer's suggestions go in without reading them? And if you do read them all, how much of the promised time saving is actually left? I would rather hear from people running this on real code than guess.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/ko-hi/the-ai-reviewer-found-a-real-bug-its-suggested-fix-would-have-broken-my-app-1ach

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
