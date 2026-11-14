---
title: "A Simple Puzzle to learn Python Loops"
slug: "a-simple-puzzle-to-learn-python-loops"
author: "Sowntharya"
source: "devto_python"
published: "Sat, 14 Nov 2026 05:43:21 +0000"
description: "problem : 1 Tenali Raman and the Palace Guards Tenali Raman wishes to meet the King. Before reaching the royal court, he has to pass through many palace gate..."
keywords: "guard, gets, tenali, raman, number, guards, king, gate"
generated: "2026-11-14T05:48:05.829138"
---

# A Simple Puzzle to learn Python Loops

## Overview

problem : 1 Tenali Raman and the Palace Guards Tenali Raman wishes to meet the King. Before reaching the royal court, he has to pass through many palace gates. A guard is posted at each gate. Every guard demands a share of whatever reward Tenali Raman receives from the King. Tenali Raman agrees and promises: "I will give you half of whatever reward I receive from the King." All the guards allow him to enter. After meeting the King, Tenali Raman receives a reward of 1024 lashes. Keeping his promise, Tenali Raman shares his reward with the guards. At each gate, he gives half of the lashes he still has to receive to the guard at that gate and proceeds to the next gate. Write a program to determine: How many lashes each guard receives. How many Guards are there if Tenali Raman gets only one lash. code : number = 1024 guard = 1 while number >= 1 : number = number // 2 // floor division print ( "Guard" , guard , "gets" , number ) guard += 1 output : Guard 1 gets 512 Guard 2 gets 256 Guard 3 gets 128 Guard 4 gets 64 Guard 5 gets 32 Guard 6 gets 16 Guard 7 gets 8 Guard 8 gets 4 Guard 9 gets 2 Guard 10 gets 1

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/sowntharya/a-simple-puzzle-to-learn-python-loops-3ao4

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
