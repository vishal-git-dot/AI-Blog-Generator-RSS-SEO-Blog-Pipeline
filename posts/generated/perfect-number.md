---
title: "Perfect Number"
slug: "perfect-number"
author: "Bala Murugan"
source: "devto_python"
published: "Sun, 07 Jun 2026 13:51:18 +0000"
description: "Definition : A Perfect Number is a number that is equal to the sum of its proper divisors (excluding the number itself). Example Number = 6 Proper divisors o..."
keywords: "number, sum, perfect, print, not, input, equal, divisors"
generated: "2026-06-07T14:06:36.534863"
---

# Perfect Number

## Overview

Definition : A Perfect Number is a number that is equal to the sum of its proper divisors (excluding the number itself). Example Number = 6 Proper divisors of 6 are: 1 2 3 Sum = 1 + 2 + 3 = 6 Since the sum of the divisors is equal to the number, 6 is a Perfect Number. Algorithm 1.Start 2.Read the number n 3.Initialize i = 1 and sum = 0 4.Check whether i < n 5.If n % i == 0, add i to sum. 6.Increment i by 1 7.Repeat steps 4 to 6 until i becomes equal to n 8.Check whether sum == n 9.If true, print Perfect Number 10.Otherwise, print Not a Perfect Number Stop. FLOWCHART: ┌───────┐ │ Start │ └───┬───┘ │ ▼ ┌─────────────┐ │ Input n │ └─────┬───────┘ │ ▼ ┌─────────────┐ │ i = 1 │ │ sum = 0 │ └─────┬───────┘ │ ▼ ┌────────┐ │ i < n ?│ └──┬──┬──┘ Yes No │ │ ▼ ▼ ┌──────────┐ │sum == n ?│ └──┬────┬──┘ Yes No │ │ ▼ ▼ ┌────────┐ ┌────────────┐ │ Print │ │ Print │ │Perfect │ │Not Perfect │ │Number │ │ Number │ └────┬───┘ └─────┬──────┘ │ │ ▼ ▼ ┌─────────┐ │ Stop │ └─────────┘ (If i < n) ▼ ┌─────────┐ │n % i=0 ?│ └──┬───┬──┘ Yes No │ │ ▼ │ ┌─────────┐ │sum=sum+i│ └────┬────┘ │ ▼ ┌─────────┐ │ i=i+1 │ └────┬────┘ │ └──────► Back to i < n ? Code : n = int ( input ( " Enter a number: " )) i = 1 sum = 0 while i < n : if n % i == 0 : sum += i i += 1 if sum == n : print ( " Perfect Number " ) else : print ( " Not a Perfect Number " ) Input 1 Enter a number: 6 Output 1 Perfect Number Input 2 Enter a number: 10 Output 2 Not a Perfect Number

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/bala_murugan_/perfect-number-13on

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
