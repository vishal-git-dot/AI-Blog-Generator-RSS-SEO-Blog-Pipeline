---
title: "Why 0.1 + 0.2 Is Not 0.3 (and the Money Bug It Causes)"
slug: "why-01-02-is-not-03-and-the-money-bug-it-causes"
author: "Muiduzzaman Lipu"
source: "devto_python"
published: "Sat, 21 Nov 2026 18:35:18 +0000"
description: "Ask almost any programming language for 0.1 + 0.2 and you get this: >>> 0.1 + 0.2 0.30000000000000004 >>> 0.1 + 0.2 == 0.3 False $ node -e "console.log(0.1 +..."
keywords: "decimal, math, you, same, number, money, python, total"
generated: "2026-11-21T18:56:47.821352"
---

# Why 0.1 + 0.2 Is Not 0.3 (and the Money Bug It Causes)

## Overview

Ask almost any programming language for 0.1 + 0.2 and you get this: >>> 0.1 + 0.2 0.30000000000000004 >>> 0.1 + 0.2 == 0.3 False $ node -e "console.log(0.1 + 0.2 === 0.3)" false It's not a bug in Python or JavaScript. Java, C, Go and others give the same answer, because they all use the same number format: IEEE 754 binary floating point. Below is why it happens, the real money bug it causes, and how to fix it. Everything here was run on Python 3.15 and Node.js 22. Video version: Why: 0.1 can't be stored exactly in binary In decimal, 1/3 is 0.3333… forever, so any finite number of digits is slightly wrong. In binary , 1/10 has the same problem: it repeats forever. So the computer stores the closest value it can, and you can see it if you ask for more digits: >>> f "{0.1:.20f}" '0.10000000000000000555' >>> from decimal import Decimal >>> Decimal ( 0.1 ) Decimal ( '0.1000000000000000055511151231257827021181583404541015625' ) The stored 0.1 is slightly more than one tenth. 0.2 is off the same way, and when you add them, the error lands just above 0.3 . Numbers built from halves, quarters, eighths (powers of two) are exact: >>> 0.5 + 0.25 == 0.75 True Most "nice" decimals aren't: >>> 1.1 * 3 3.3000000000000003 The errors add up >>> total = 0.0 >>> for _ in range ( 10 ) : total += 0.1 >>> total 0.9999999999999999 Ten tiny errors don't cancel out. They accumulate. The money bug >>> 4.35 * 100 434.99999999999994 >>> int ( 4.35 * 100 ) 434 int() truncates, so $4.35 just became 434 cents . JavaScript does the same thing with Math.floor(4.35 * 100) , which also gives 434 . Rounding is affected too, because the stored value is slightly below the "half": >>> round ( 2.675 , 2 ) 2.67 $ node -e "console.log((1.005).toFixed(2))" 1.00 Fix 1: never compare floats with == import math math . isclose ( 0.1 + 0.2 , 0.3 ) # True math.isclose() uses a relative tolerance ( rel_tol=1e-09 by default), so it works for big and small numbers. In JavaScript, the common check is: Math . abs ( a - b ) < Number . EPSILON // 2.220446049250313e-16 Number.EPSILON is the gap between 1 and the next representable number, so this check only makes sense for values around 1. For larger values, scale the tolerance: Math.abs(a - b) < Number.EPSILON * Math.max(Math.abs(a), Math.abs(b)) . Fix 2: store money as integer cents price_cents = 435 # store cents total = price_cents * 3 # 1305, exact f "${total / 100:.2f}" # '$13.05' only for display Integer math is exact. Add, multiply and compare cents, and only convert to dollars when you display the value. Payment APIs such as Stripe take amounts in the smallest currency unit for exactly this reason. Fix 3: Decimal , but create it from strings from decimal import Decimal Decimal ( "0.1" ) + Decimal ( "0.2" ) # Decimal('0.3') Decimal ( "0.1" ) + Decimal ( "0.2" ) == Decimal ( "0.3" ) # True The trap: if you pass a float , the error is already baked in, and Decimal copies it perfectly: >>> Decimal ( 0.1 ) + Decimal ( 0.2 ) Decimal ( '0.3000000000000000166533453694' ) Always build Decimal values from strings (or integers). Bonus: Python 3.12+ sum() is smarter than your loop >>> sum ( [ 0.1 ] * 10 ) 1.0 >>> import math >>> math . fsum ( [ 0.1 ] * 10 ) 1.0 Since Python 3.12, the built-in sum() of floats uses compensated summation: it tracks the rounding error as it goes. math.fsum() does the same (on every Python version). The manual += loop above still gives 0.9999999999999999 . Recap 0.1 is stored as 0.1000000000000000055… . Binary can't represent most decimals exactly. Never compare floats with == . Use math.isclose() or a tolerance. Store money as integer cents and format only for display. Use Decimal("0.1") from strings, never Decimal(0.1) . Let sum() (3.12+) or math.fsum() add your floats. Has floating point ever bitten you in production? 👇 I post one tested coding tip every day on YouTube at Refactorly . The 30-second version of this one is here .

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/refactorly/why-01-02-is-not-03-and-the-money-bug-it-causes-872

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
