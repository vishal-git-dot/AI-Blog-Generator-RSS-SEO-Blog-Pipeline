---
title: "You copied the list, but the original changed too. Shallow and deep copy in Python"
slug: "you-copied-the-list-but-the-original-changed-too-shallow-and-deep-copy-in-python"
author: "TalentOp Systems LLC"
source: "devto_python"
published: "Sun, 15 Nov 2026 05:41:04 +0000"
description: "Checked against official sources on November 15, 2026 You make a copy of a list. You change the copy. Then you look at the first list, and it changed too. No..."
keywords: "copy, list, print, inner, you, shallow, python, new"
generated: "2026-11-15T05:48:55.489595"
---

# You copied the list, but the original changed too. Shallow and deep copy in Python

## Overview

Checked against official sources on November 15, 2026 You make a copy of a list. You change the copy. Then you look at the first list, and it changed too. Nothing is broken. Python did what it was told. The copy was only one level deep. Everything below was run in Python 3.13.5. The bug in six lines a = [ [ 1 , 2 ] , [ 3 , 4 ] ] b = a . copy ( ) b [ 0 ] . append ( 99 ) print ( a ) It prints: [ [ 1 , 2 , 99 ] , [ 3 , 4 ] ] We changed b , and a shows the new number. Why? What a shallow copy really does a.copy() makes a new outer list. But the inner lists are not copied. The new list just points to the same inner lists. We can check it: print ( a [ 0 ] is b [ 0 ] ) That prints True . Both names point to the same inner list. So an edit through one name shows up in the other. The Python docs call this a shallow copy. The copy module page says a shallow copy makes a new outer object, such as a new list. It then puts the same inner items into it, not fresh copies of those items. Many "copies" are shallow These all share inner objects: list.copy() a[:] dict(d) and d.copy() copy.copy(x) Here is a dictionary that holds a list: d = { "tags" : [ "x" ] } e = dict ( d ) e [ "tags" ] . append ( "y" ) print ( d ) It prints {'tags': ['x', 'y']} . The new dictionary shares the same tags list. Objects can behave the same way. copy.copy() on a simple object with a list field gives a new object, but both objects share that list. We ran it, and the original's list grew from ['x'] to ['x', 'y'] . A class can define its own copy methods and change this. The docs name them __copy__ and __deepcopy__ . We did not do that here. (see the Python copy module docs ) The fix: deepcopy copy.deepcopy() copies the inner objects too. import copy a = [ [ 1 , 2 ] , [ 3 , 4 ] ] # start fresh c = copy . deepcopy ( a ) c [ 1 ] . append ( 77 ) print ( a ) print ( c ) print ( a [ 0 ] is c [ 0 ] ) We reset a first, so the earlier 99 is gone. It prints: [ [ 1 , 2 ] , [ 3 , 4 ] ] [ [ 1 , 2 ] , [ 3 , 4 , 77 ] ] False Only c has the 77. The last line prints False , so the inner lists are separate. Deep copy costs more time and memory, because it copies everything. Use it when you need a fully separate copy. It is not free, so do not call it on huge data in a tight loop. A close cousin: the repeated row This one catches many people: f = [ [ 0 ] * 2 ] * 3 f [ 0 ] [ 0 ] = 1 print ( f ) It prints [[1, 0], [1, 0], [1, 0]] . The * repeats the same inner list three times. It does not build three lists. Build separate rows like this: g = [ [ 0 ] * 2 for _ in range ( 3 ) ] g [ 0 ] [ 0 ] = 1 print ( g ) Now you get [[1, 0], [0, 0], [0, 0]] . Only the first row changed. Quick check you can use Is the data flat? A list of numbers or strings is fine with .copy() . Those values cannot be changed in place. Is there a list, dict or object inside? A shallow copy shares it. Think about deepcopy . Not sure? Compare with is , like a[0] is b[0] . True means shared. Docs we opened Python docs, copy: Shallow and deep copy operations Python docs, Programming FAQ: How do I create a multidimensional list? About TalentOp Systems LLC Our team works out of Omaha, Nebraska, and we have been in business since February 2025. We do IT staffing, software consulting and project development, and we staff software roles for clients in banking, insurance, healthcare and retail. Roles can be W2 or C2C, and many run 12+ months. TalentOp Systems is a direct vendor for Kroger, whose offices are in Blue Ash, Ohio. E-Verify: yes, TalentOp Systems LLC is enrolled and E-Verified. Need H-1B sponsorship? TalentOp Systems LLC provides it for hires who meet the role's requirements and eligibility. We also take H-1B transfers, and OPT or STEM OPT candidates are welcome to reach out. Find us at www.talentopsystems.com or email info@talentopsystems.com .

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/talentopsystems/you-copied-the-list-but-the-original-changed-too-shallow-and-deep-copy-in-python-5hkn

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
