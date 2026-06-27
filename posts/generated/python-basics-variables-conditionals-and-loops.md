---
title: "Python Basics: Variables, Conditionals, and Loops"
slug: "python-basics-variables-conditionals-and-loops"
author: "yuna song"
source: "devto_python"
published: "Sat, 27 Jun 2026 08:13:27 +0000"
description: "1. Variables A variable stores a value that can be referenced and reused throughout a program. Syntax name = " Python " age = 20 pi = 3.14 is_active = True N..."
keywords: "use, loop, python, while, condition, print, true, when"
generated: "2026-06-27T08:43:42.523950"
---

# Python Basics: Variables, Conditionals, and Loops

## Overview

1. Variables A variable stores a value that can be referenced and reused throughout a program. Syntax name = " Python " age = 20 pi = 3.14 is_active = True Naming Rules Use letters, numbers, and underscores ( _ ). Variable names cannot start with a number. Do not use spaces (use snake_case instead). Do not use Python keywords (e.g. if , for , while , class ). Common Data Types age = 20 # int pi = 3.14 # float name = " Python " # str is_active = True # bool Notes Variables can be reassigned at any time. Python automatically determines the data type. 2. Conditional Statements Conditional statements execute different code depending on whether a condition is True or False . Syntax score = 85 if score >= 90 : print ( " Grade A " ) elif score >= 80 : print ( " Grade B " ) else : print ( " Grade C " ) Keywords if : Checks the first condition. elif : Checks additional conditions if previous ones are False . else : Executes when none of the above conditions are met. Comparison Operators > < >= <= == != Logical Operators and or not Notes A colon ( : ) is required after each condition. Proper indentation defines the code block. 3. Loops Loops execute a block of code repeatedly. for Loop Used when iterating over a sequence or a fixed range. for i in range ( 5 ): print ( i ) Output: 0 1 2 3 4 while Loop Repeats as long as a condition remains True . count = 0 while count < 3 : print ( count ) count += 1 Output: 0 1 2 Loop Control break # Exit the loop immediately continue # Skip the current iteration pass # Placeholder; does nothing Notes Use for when the number of iterations is known. Use while when repetition depends on a condition. Ensure a while loop eventually becomes False to avoid an infinite loop.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/yunasong/python-basics-variables-conditionals-and-loops-k79

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
