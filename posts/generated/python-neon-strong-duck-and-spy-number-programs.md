---
title: "Python - Neon, Strong, Duck, and Spy Number programs"
slug: "python-neon-strong-duck-and-spy-number-programs"
author: "VINOTH"
source: "devto_python"
published: "Sun, 23 Aug 2026 05:52:26 +0000"
description: "Neon Number 1)Write a Python program to check whether a given number is a Neon Number or not. Example: 9 × 9 = 81 8 + 1 = 9 def sum_of_digits ( no ): sum = 0..."
keywords: "number, sum, factorial, duck, print, python, neon, strong"
generated: "2026-08-23T06:49:22.751454"
---

# Python - Neon, Strong, Duck, and Spy Number programs

## Overview

Neon Number 1)Write a Python program to check whether a given number is a Neon Number or not. Example: 9 × 9 = 81 8 + 1 = 9 def sum_of_digits ( no ): sum = 0 while no > 0 : sum = sum + no % 10 no = no // 10 return sum number = 9 square = number ** 2 #number * number sum = sum_of_digits ( square ) if number == sum : print ( ' Neon Number ' ) o/p: Neon Number Strong Number 2)Write a Python program to check whether a given number is a Strong Number or not. def find_factorial ( no ): factorial = 1 while no > 0 : factorial *= no #factorial = factorial * no no -= 1 # no = no - 1 return factorial def digits ( no ): #145 total = 0 while no > 0 : digit = no % 10 factorial = find_factorial ( digit ) total += factorial #total = total + factorial #print(f'factorial of {digit} is {factorial}') no = no // 10 return total number = int ( input ( " Enter no. " )) result = digits ( number ) if result == number : print ( " Strong Number " ) o/p: Strong Number Duck Number 3) Write a Python program to check whether a given number is a Duck Number or not. no = input ( " Enter no. " ) if no [ 0 ] == ' 0 ' : print ( ' Not a Duck Number ' ) else : if ' 0 ' in no : print ( " Duck Number " ) o/p: Duck Number Spy Number 4) Write a Python program to check whether a given number is a Spy Number or not. def sum_of_digits ( no ): sum = 0 multiply = 1 while no > 0 : sum = sum + no % 10 multiply = multiply * ( no % 10 ) no = no // 10 return sum , multiply no = 1411 result1 , result2 = sum_of_digits ( no ) print ( ' Spy Number: ' , result1 == result2 ) o/p: Spy Number: False

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/vinoth_manickam_d707cb7bb/python-neon-strong-duck-and-spy-number-programs-5c70

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
