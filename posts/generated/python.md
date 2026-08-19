---
title: "Python"
slug: "python"
author: "Kiruthiga S"
source: "devto_python"
published: "Wed, 19 Aug 2026 12:47:45 +0000"
description: "16) Secret VIP Numbers A security system assigns special numbers to the first few VIP lockers. A number is considered a VIP number if it can be divided exact..."
keywords: "number, vip, chocolate, numbers, div, count, wrapper, while"
generated: "2026-08-19T12:56:23.246393"
---

# Python

## Overview

16) Secret VIP Numbers A security system assigns special numbers to the first few VIP lockers. A number is considered a VIP number if it can be divided exactly by only 1 and itself. The security officer wants the numbers of the first 5 VIP lockers. Write a Python program to display those 5 numbers. Expected Result: 2, 3, 5, 7, 11 def find_vip_number(no): div = 2 while div <= no//2: if no % div == 0: return 'not VIP' div+=1 else: return 'VIP' no = 2 count = 0 while count < 5: result = find_vip_number(no) #Function Calling Statement if result == 'VIP': print(no) count+=1 no = no+1 Output:2 3 5 7 11 17) The Special Numbers A teacher is preparing a Number Exhibition for students. She writes the numbers 1 to 20 on 20 cards. She wants to select only the special cards. A card is special if its number can be divided exactly by only two numbers: 1 and the number itself. The teacher asks the students: “Check all the cards from 1 to 20 and display the numbers that are special.” def find_vip_number(no): div = 2 while div <= no//2: if no % div == 0: return 'not VIP' div+=1 else: return 'VIP' no = 2 while no < 20: result = find_vip_number(no) #Function Calling Statement if result == 'VIP': print(no) no = no+1 Output:2 3 5 7 11 13 17 19 18) You have Rs. 100 /- One chocolate costs Rs. 5. Every time you buy a chocolate, you get one wrapper. You can exchange 3 wrappers for 1 additional chocolate. What is the maximum number of chocolates you can have with Rs. 100? chocolate = 20 wrapper = 20 while wrapper >= 3: wrapper = wrapper - 3 chocolate = chocolate + 1 wrapper = wrapper + 1 else: print("chocolate:", chocolate) Output:chocolate: 29 19) There is one person called Viyan. He is a Software Engineer. He employs a maid for cooking. One day, the maid prepared n number of chapathis and kept in a hot box. Viyan ate those chapathis and the count is as follows: * For Morning breakfast, he completed 1/3 number of chapathis in the hot box. * For Lunch, He had 1/3 of what was there in the hot box. * For Dinner, again he took and ate 1/3 number of chapathis present in the box. The next day morning, When the maid checked the number of chapathis remaining, it was 8. What was the number of chapathis, She made - in total? remains=8 count=0 while count<3: eaten=remains//2 remains=remains+eaten count+=1 print("starting:", remains) Output:starting: 27

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/kiruthiga_05/python-j1

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
