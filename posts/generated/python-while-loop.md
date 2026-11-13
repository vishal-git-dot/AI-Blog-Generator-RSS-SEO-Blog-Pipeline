---
title: "Python While Loop!"
slug: "python-while-loop"
author: "Vinoth"
source: "devto_python"
published: "Fri, 13 Nov 2026 05:40:20 +0000"
description: "** Tenali Raman and the Palace Guards** Tenali Raman wishes to meet the King. Before reaching the royal court, he has to pass through many palace gates. A gu..."
keywords: "guard, guards, while, tenali, raman, loop, king, reward"
generated: "2026-11-13T05:58:50.739466"
---

# Python While Loop!

## Overview

** Tenali Raman and the Palace Guards** Tenali Raman wishes to meet the King. Before reaching the royal court, he has to pass through many palace gates. A guard is posted at each gate. Every guard demands a share of whatever reward Tenali Raman receives from the King. Tenali Raman agrees and promises: "I will give you half of whatever reward I receive from the King." All the guards allow him to enter. After meeting the King, Tenali Raman receives a reward of 1024 lashes . The interesting question is: How many guards can receive half of the remaining reward until the value becomes less than 1? ##Step 1: Manual Calculation First, we can calculate the result manually. python guard = 0 received_lashes = 1024 guard = 1 received_lashes = received_lashes / 2 guard = 2 received_lashes = received_lashes / 2 guard = 3 received_lashes = received_lashes / 2 guard = 4 received_lashes = received_lashes / 2 guard = 5 received_lashes = received_lashes / 2 guard = 6 received_lashes = received_lashes / 2 This approach helps us understand the calculation at a basic level. However, writing the same code repeatedly is not efficient. Also, we do not know how many guards there are. ## Step 2: Identifying the Repeated Pattern We can see that two operations are repeated: 1. Divide `received_lashes` by `2` . 2. Increase the guard count by `1` . For example: #python guard = guard + 1 received_lashes = received_lashes / 2 Since the same operations are repeated, we can use a while loop . Step 3: Using a While Loop guard = 0 received_lashes = 1024 while received_lashes >= 1 : received_lashes = received_lashes / 2 guard = guard + 1 print ( received_lashes ) print ( guard ) ! [ ] ( https : // dev - to - uploads . s3 . us - east - 2 . amazonaws . com / uploads / articles / x3tse2qigyuiqyeo9xpc . png ) Output 0.5 11 Explanation The value is divided by 2 repeatedly: 1024 → 512 → 256 → 128 → 64 → 32 → 16 → 8 → 4 → 2 → 1 → 0.5 The loop runs 11 times . Therefore: Number of guards = 11 Remaining value = 0.5 Step 4: What Happens if We Start with guard = 1 ? guard = 1 received_lashes = 1024 while received_lashes >= 1: received_lashes = received_lashes / 2 guard = guard + 1 print(received_lashes) print(guard) Output 0.5 12 This happens because we started counting the guards from 1 instead of 0 . is the correct and clearer approach. Correct Answer: Guards counted: 11 Final remaining value: 0.5

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/vinothab27/python-while-loop-237o

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
