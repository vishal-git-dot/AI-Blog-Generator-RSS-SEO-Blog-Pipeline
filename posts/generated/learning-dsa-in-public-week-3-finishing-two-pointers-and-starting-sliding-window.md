---
title: "Learning DSA in Public, Week 3: Finishing Two Pointers and Starting Sliding Window"
slug: "learning-dsa-in-public-week-3-finishing-two-pointers-and-starting-sliding-window"
author: "Victor Ogbonna"
source: "devto_python"
published: "Fri, 20 Nov 2026 15:04:05 +0000"
description: "Last week I finished Arrays & Hashing and started Two Pointers. This week I completed Two Pointers with Container With Most Water , then moved into Sliding W..."
keywords: "window, week, longest, left, two, sliding, water, heights"
generated: "2026-11-20T15:10:11.459712"
---

# Learning DSA in Public, Week 3: Finishing Two Pointers and Starting Sliding Window

## Overview

Last week I finished Arrays & Hashing and started Two Pointers. This week I completed Two Pointers with Container With Most Water , then moved into Sliding Window with Best Time to Buy and Sell Stock and Longest Substring Without Repeating Characters . Same rule as always: if I can't explain it with an everyday picture, I don't understand it yet. The big idea this week: don't re-check everything from scratch. Keep a moving frame, and only adjust it when a rule forces you to. 1. Container With Most Water: move the shorter wall The problem: Pick two vertical lines that, together with the ground, hold the most water. Picture it: Two fences hold water, but the water can only rise as high as the shorter one. Start with the fences furthest apart. Then move the shorter fence inward, since that's the only move that could find a taller wall to make up for the lost width. def maxArea ( heights ) : res = 0 l , r = 0 , len ( heights ) - 1 while l < r : area = ( r - l ) * min ( heights [ l ] , heights [ r ] ) res = max ( res , area ) if heights [ l ] < heights [ r ] : l += 1 else : r -= 1 return res Slow vs. fast: Trying every pair is O(n²). Two pointers moving inward: O(n) time, O(1) space. What I learnt the hard way: I hit almost every kind of small bug on this one: a wrong variable name ( height vs heights ), a stray comma, comparing the wrong values, and return res indented inside the loop so it returned after the first round. The logic was right; the details weren't. Now I check names and indentation before I run anything. 2. Best Time to Buy and Sell Stock: remember the cheapest day The problem: Given daily prices, buy once and sell later for the biggest profit. If no profit is possible, return 0. Picture it: Walk through the week with a sticky note showing the cheapest price you've seen so far. Each day, ask: "If I sold today, how much would I make?" def maxProfit ( prices ) : min_price = prices [ 0 ] max_profit = 0 for price in prices : min_price = min ( min_price , price ) max_profit = max ( max_profit , price - min_price ) return max_profit Slow vs. fast: Checking every buy/sell pair is O(n²). One pass with a running minimum: O(n) time, O(1) space. 3. Longest Substring Without Repeating Characters: the sliding window The problem: Find the length of the longest stretch of a string with no repeated characters. Picture it: A window sliding across the string. The right edge keeps adding new characters. When a repeat shows up, the left edge moves forward, dropping characters, until the repeat is gone. def lengthOfLongestSubstring ( s ) : seen = set ( ) left = 0 longest = 0 for right in range ( len ( s ) ) : while s [ right ] in seen : seen . remove ( s [ left ] ) left += 1 seen . add ( s [ right ] ) longest = max ( longest , right - left + 1 ) return longest Slow vs. fast: Checking every substring is O(n²) or worse. The window is O(n), because each character enters and leaves at most once. What I learnt the hard way: I started left at 1 instead of 0, which skipped the first character and made every window one short. Python counts from 0, and that matters from the very first line. Week 3 cheat sheet Problem Pattern Question it answers Container With Most Water Two pointers Which wall should I move to have a chance at more water? Best Time to Buy and Sell Stock Running minimum If I sold today, what's the cheapest day I could have bought? Longest Substring Without Repeating Characters Sliding window + set How far must the left edge move to remove the repeat? What's working for me Picture first, code second. A clear image tells me why a pointer moves before I write it. One instruction per line. Writing each step in plain English, including whether it's inside or outside the loop, keeps nested code straight. Reading the exact error line. The traceback almost always points to the problem. Most of my bugs this week were one-character fixes. Next week More Sliding Window. If you're learning DSA too, which part of sliding window trips you up more: moving the left edge, or updating the answer?

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/outstandingvick/learning-dsa-in-public-week-3-finishing-two-pointers-and-starting-sliding-window-2il2

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
