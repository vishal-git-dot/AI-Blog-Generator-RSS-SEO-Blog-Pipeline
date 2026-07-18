---
title: "🚀 DSA Journey | Solved 3 LeetCode Problems in Python"
slug: "dsa-journey-solved-3-leetcode-problems-in-python"
author: "hassam bin shahid"
source: "devto_python"
published: "Sat, 18 Jul 2026 18:21:24 +0000"
description: "Today's practice focused on three different algorithmic patterns, each reinforcing an important concept in problem solving and writing efficient code. ✅ 1. T..."
keywords: "nums, leetcode, prefix, suffix, concept, self, ans, problems"
generated: "2026-07-18T19:11:40.225366"
---

# 🚀 DSA Journey | Solved 3 LeetCode Problems in Python

## Overview

Today's practice focused on three different algorithmic patterns, each reinforcing an important concept in problem solving and writing efficient code. ✅ 1. To Lower Case (LeetCode 709) Concept: String Manipulation class Solution : def toLowerCase ( self , s : str ) -> str : return s . lower () Key Takeaway: Reviewed string operations and learned how character conversion can also be implemented using ASCII values. ✅ 2. Product of Array Except Self (LeetCode 238) Concept: Prefix & Suffix Products class Solution : def productExceptSelf ( self , nums ): n = len ( nums ) ans = [ 1 ] * n prefix = 1 for i in range ( n ): ans [ i ] = prefix prefix *= nums [ i ] suffix = 1 for i in range ( n - 1 , - 1 , - 1 ): ans [ i ] *= suffix suffix *= nums [ i ] return ans Key Takeaway: Practiced solving array problems in O(n) time without using division by leveraging prefix and suffix products. ✅ 3. Maximum Average Subarray I (LeetCode 643) Concept: Sliding Window class Solution : def findMaxAverage ( self , nums , k ): window_sum = sum ( nums [: k ]) max_sum = window_sum for i in range ( k , len ( nums )): window_sum += nums [ i ] - nums [ i - k ] max_sum = max ( max_sum , window_sum ) return max_sum / k Key Takeaway: Applied the Sliding Window technique to optimize repeated calculations and reduce the time complexity to O(n) . Every LeetCode problem teaches more than just syntax—it strengthens analytical thinking, algorithm selection, and code optimization. Consistency in practice is helping me build a stronger foundation in Data Structures and Algorithms, one problem at a time. I'm looking forward to tackling more challenging problems and continuing to grow as a software engineer. 💻 Language: Python 📚 Topics Covered: String Manipulation, Prefix & Suffix Products, Sliding Window LeetCode #Python #DSA #Algorithms #ProblemSolving #SoftwareEngineering #CodingJourney #100DaysOfCode #Developer #Programming

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/hassam645/dsa-journey-solved-3-leetcode-problems-in-python-47bm

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
