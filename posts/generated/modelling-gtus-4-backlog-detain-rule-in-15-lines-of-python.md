---
title: "Modelling GTU's 4-backlog detain rule in 15 lines of Python"
slug: "modelling-gtus-4-backlog-detain-rule-in-15-lines-of-python"
author: "Prince"
source: "devto_python"
published: "Sat, 31 Oct 2026 04:40:26 +0000"
description: "I keep seeing GTU (Gujarat Technological University) juniors panic about the "4 backlog" rule, and half of them count it wrong. The rule has one twist that m..."
keywords: "semester, sem, gtu, not, you, counted, backlog, rule"
generated: "2026-10-31T04:57:14.107129"
---

# Modelling GTU's 4-backlog detain rule in 15 lines of Python

## Overview

I keep seeing GTU (Gujarat Technological University) juniors panic about the "4 backlog" rule, and half of them count it wrong. The rule has one twist that makes it a nice little exercise in code. The rule A backlog is a subject with an FF grade (below 35 marks). Missing the exam also counts as not cleared. At any time you can carry at most 4 pending backlogs. More than 4 and you can be detained for one year. Backlogs from the semester just before your current one are not counted. That last line is the bug in most people's mental model. The code def detention_check ( current_sem : int , pending : dict [ int , int ]) -> tuple [ int , bool ]: """ pending maps semester -> number of FF subjects still not cleared. """ just_previous = current_sem - 1 counted = sum ( n for sem , n in pending . items () if sem < just_previous ) return counted , counted > 4 # Sem 4 student: 2 in Sem 1, 1 in Sem 2, 3 in Sem 3 (6 total) print ( detention_check ( 4 , { 1 : 2 , 2 : 1 , 3 : 3 })) # (3, False) -> safe # Same student moves to Sem 5 and clears nothing print ( detention_check ( 5 , { 1 : 2 , 2 : 1 , 3 : 3 })) # (6, True) -> detained Same backlogs, different semester, opposite result. A backlog that is "free" today gets counted the moment you move up, so the real deadline for clearing a paper is one semester later than it looks. What the function does not cover Students admitted from 2018-19 onward follow a stricter table from GTU circular 5440 (19 July 2018), where certain semesters must be fully cleared before you enter the semester two years ahead. Attendance: you need at least 75% to fill the exam form at all. So treat this as a sanity check, not a verdict. Your college exam cell has the final word for your batch. The full write-up, with the 2018 table, fees and a semester-by-semester plan, is on GTU Hero . Disclosure: I build GTU Hero.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/offpage_prince/modelling-gtus-4-backlog-detain-rule-in-15-lines-of-python-32nc

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
