---
title: "Python Task -Factorial Problem using Loop"
slug: "python-task-factorial-problem-using-loop"
author: "vidhya murali"
source: "devto_python"
published: "Tue, 11 Aug 2026 06:52:25 +0000"
description: "1,A king announces a unique reward for Hard Workers. On each day, the reward is multiplied by the day's number. The reward starts at 1 gold coin. Given the n..."
keywords: "days, day, frog, flowers, well, totalfeet, his, reward"
generated: "2026-08-11T07:15:40.513673"
---

# Python Task -Factorial Problem using Loop

## Overview

1,A king announces a unique reward for Hard Workers. On each day, the reward is multiplied by the day's number. The reward starts at 1 gold coin. Given the number of days n, write a program to calculate the final reward. days=int(input("Enter no of days : ")) rewards=1; for i in range(1,days+1): rewards*=i print("Total rewards for" , days,"days is : ",rewards) 2,Suppose a password consists of the letters: A, B, C, D. Each letter must be used exactly once. How many different passwords are possible? letters=['A','B','C','D'] passwordCount=1; for i in range(1,len(letters)+1): passwordCount *= i print('passwordCount',passwordCount) 3,Frog in a Well A frog accidentally falls into a 60-foot-deep well. Every day: * During the day, the frog climbs 2 feet. * During the night, it slips down 0.5 feet. This pattern continues every day until the frog reaches the top of the well and escapes. Write a program to determine: 1. How many days it takes for the frog to get out of the well. 2. On which day the frog escapes. Note: Once the frog reaches or crosses the top of the well during the daytime, it escapes immediately and does not slip back that night. totalFeet = 60 days = 1 daytime = 2 while totalFeet > 0: totalFeet -= daytime if totalFeet <= 0: print(days) break totalFeet += 0.5 days += 1 4, A saint goes for a morning walk every day. During his walk, he plucks flowers and keeps them in a basket. On his way back home, he visits 7 temples. At each temple, he offers half of the flowers currently in his basket. After visiting all 7 temples, he reaches home with exactly one flower remaining in his basket. Write a program to determine how many flowers the saint had in his basket before he visited the first temple. Hint: Think carefully about whether it is easier to solve the problem from the beginning or by working backwards from the final flower. temple=7 flowers=1 for i in range(1,temple+1): flowers*=2 print("total Flowers: " , flowers)

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/vidhya_murali_5aabe7784bd/python-task-factorial-problem-using-loop-3051

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
