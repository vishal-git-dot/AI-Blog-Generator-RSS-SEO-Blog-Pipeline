---
title: "PYTHON - LOOPS7"
slug: "python-loops7"
author: "Keerti Sadana S"
source: "devto_python"
published: "Fri, 21 Aug 2026 18:41:59 +0000"
description: "* 1) Count of Digits, Sum of Digits, Reverse Digit and Palindrome * no = int ( input ( " Enter any Number: " )) copy = no sum = 0 count = 0 reverse = 0 while..."
keywords: "total, print, sum, reverse, number, count, digits, input"
generated: "2026-08-21T18:43:06.893161"
---

# PYTHON - LOOPS7

## Overview

* 1) Count of Digits, Sum of Digits, Reverse Digit and Palindrome * no = int ( input ( " Enter any Number: " )) copy = no sum = 0 count = 0 reverse = 0 while no > 0 : rem = no % 10 reverse = ( reverse * 10 ) + rem sum = sum + rem no = no // 10 count += 1 print ( f ' Count of Digits is { count } ' ) print ( f ' Sum of Digits is { sum } ' ) print ( f ' Reverse Digit is { reverse } ' ) if ( copy == reverse ): print ( ' Palindrome ' ) else : print ( ' Not a Palindrome ' ) OUTPUT: Enter any Number: 1221 Count of Digits is 4 Sum of Digits is 6 Reverse Digit is 1221 Palindrome 2) user input number: 123456 -> 2 + 4 + 6 no = 123456 total = 0 while no > 0 : print (( no % 100 ) % 10 ) total = total + ( no % 100 ) % 10 no //= 100 print ( total ) OUTPUT: 6 4 2 12 * 3) user input number: 123456 -> 56 34 12 and its sum * no = 123456 total = 0 while no > 0 : total = total + ( no % 100 ) print ( no % 100 ) no //= 100 print ( total ) OUTPUT: 56 34 12 102 * 4) user input number: 123456 -> 456 123 * no = 123456 total = 0 while no > 0 : total = total + ( no % 1000 ) print ( no % 1000 ) no //= 1000 print ( total ) OUTPUT: 456 123 579 5) user input number: 123456 -> 56 45 34 23 12 no = 123456 total = 0 while no > 1 : total = total + ( no % 100 ) print ( no % 100 ) no //= 10 print ( total ) OUTPUT: 56 45 34 23 12 170 6) user input number: 123456 -> 1+3+5 [tbd]

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/keerti_sadanas_d3bbb8924/python-loops6-159

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
