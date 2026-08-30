---
title: "The Hidden Cost Of A Line of Code"
slug: "the-hidden-cost-of-a-line-of-code"
author: "Mona Moxie"
source: "devto_python"
published: "Sun, 30 Aug 2026 20:24:15 +0000"
description: ""Given an integer array nums , return true if any value appears at least twice in the array, and return false if every element is distinct." My first approac..."
keywords: "list, container, nums, elem, set, return, solution, item"
generated: "2026-08-30T20:50:18.008666"
---

# The Hidden Cost Of A Line of Code

## Overview

"Given an integer array nums , return true if any value appears at least twice in the array, and return false if every element is distinct." My first approach was to use a list class Solution : def containsDuplicate ( self , nums : List [ int ]) -> bool : container = [] for elem in nums : if elem in container : return True container . append ( elem ) return False I was hoping to optimise for time and trade space. For a list with a sample size of 5 items and where the duplicate item sits on the tail end of the list, this would require me to traverse the list 5 times. For a 100 item list, then 100 times. For a billion, then a billion times. So O(n). But my assumption was wrong. The above solution won't get me an O(n). Second Idea: Use a Set class Solution : def containsDuplicate ( self , nums : List [ int ]) -> bool : container = set () for elem in nums : if elem in container : return True container . add ( elem ) return False Same structure as the first but now I'm using a set and not a list. This is the true O(n), better than the earlier solution because of a very simple line I overlooked. It's been sitting there there all this while but I didn't notice. MY ASSUMPTION, A WRONG ONE: The first solution required me to loop through every item in the list container = [] for elem in nums : ... I was willing to grow my space-cost as long as my time-cost is efficient. My space-cost kept a track of each unique item I've seen. I called it container . What a silly name! But before that, I ran a lookup to know if this item was already in the container. for elem in nums : if elem in container : # <---------- THE HIDDEN COST That lookup was the HIDDEN COST. Looping over a list is not usually efficient, since it needs to blindly go over each item in the list. To do this, Python has to loop through each item in the container variable, each and every time. If the container had 100 items in it, Python would need 100 lookups to know if the item was in the list or not. If there are 10B times in the original list, then on the 10th billion item, Python would also require 10B - 1 lookups in the local variable. Therefore in general, (n-1) for each (n), which in itself is a terrible solution and a miscalculation. I wanted to trade space for time but ended up spending both and optimising for none. WHY MY SET WAS BETTER THAN A LIST/ARRAY Compare both solutions again: A: USING A LIST class Solution : def containsDuplicate ( self , nums : List [ int ]) -> bool : container = [] for elem in nums : if elem in container : return True container . append ( elem ) return False B: USING A SET class Solution : def containsDuplicate ( self , nums : List [ int ]) -> bool : container = set () for elem in nums : if elem in container : return True container . add ( elem ) return False By switching from a list to a set, I immediately drew closer to an optimal solution. From $O(n^2)$ to O(n). But I can do better. Not in terms of performance, but possibly in terms of clarity and simplification. OPTION C class Solution : def containsDuplicate ( self , nums : List [ int ]) -> bool : return len ( set ( nums )) != len ( nums ) One line. But so powerful, while maintaining the use of a Set. THE SYNOPSIS: A set can only hold unique items. This is what it was made for. And if I need the duplicates out the door, I only need to call this guy to help me out. What I get in turn is an output that contains only unique items. It takes python 0(n) time to get me the Set, neatly and perfectly done. Everything after that happens in constant time, 0(1). At this point, I can simply count everything in the original list and everything in the set. If they are the same, it means the list never had any duplicates. But if they differ, it means the Set did a good job removing the duplicates. The difference in the number of items tells us in a nutshell if the original list was full of duplicates or not. class Solution : def containsDuplicate ( self , nums : List [ int ]) -> bool : return len ( set ( nums )) != len ( nums )

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/monamoxie/the-hidden-cost-of-a-line-of-code-3c5b

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
