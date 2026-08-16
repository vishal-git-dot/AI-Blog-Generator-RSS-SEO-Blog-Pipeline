---
title: "Is Friday the 13th really more common? I counted 400 years to find out"
slug: "is-friday-the-13th-really-more-common-i-counted-400-years-to-find-out"
author: "Lucian (LKB)"
source: "devto_webdev"
published: "Sun, 16 Aug 2026 18:20:40 +0000"
description: "The superstition claims Friday the 13th is unlucky. It turns out it's also, very slightly, the most likely — the 13th lands on a Friday more often than on an..."
keywords: "year, friday, years, weekday, one, every, more, than"
generated: "2026-08-16T18:35:30.116180"
---

# Is Friday the 13th really more common? I counted 400 years to find out

## Overview

The superstition claims Friday the 13th is unlucky. It turns out it's also, very slightly, the most likely — the 13th lands on a Friday more often than on any other weekday. I counted every month in a full 400-year Gregorian cycle (plain Date UTC math) to see how big that edge really is. The edge, in one line: over 400 years the 13th falls on a Friday 688 times — more than any other weekday — but the rarest weekday still gets 684. The superstition has a real statistical edge; it's just a minuscule one. Which weekday the 13th prefers Counts across all 4,800 months of one cycle. The mean, if it were perfectly even, would be 685.7: Weekday Times the 13th lands here Friday 688 Sunday 687 Wednesday 687 Monday 685 Tuesday 685 Thursday 684 Saturday 684 Friday wins — by about two months in 4,800. On a true zero-based axis the seven bars are almost identical, and that is the story: the bias is real but tiny, an artefact of how the Gregorian leap rule favours some starting weekdays over others. You can't dodge it: every year has one However the weekdays fall, no year escapes a Friday the 13th — and no year has more than three. Across the cycle, 171 years have exactly one, 170 have two, and 59 have three . (For the record: the next Friday the 13ths are Nov 13 2026, Aug 13 2027, and Oct 13 2028.) The calendar is a 400-year loop Here's the fact that makes every count above exact rather than an estimate. A 400-year block holds 97 leap years and 146,097 days — and 146,097 divides by seven with nothing left over, giving exactly 20,871 weeks . Because days and weeks line up perfectly at the 400-year mark, the entire calendar resets and repeats. Your birthday in 2426 falls on the same weekday it does in 2026. And some years get 53 weeks Most years span 52 ISO weeks, but 71 of every 400 (about 17.8%) carry 53 — a year does when it starts on a Thursday, or on a Wednesday in a leap year. The next 53-week years are 2026, 2032, 2037 and 2043 . That extra week is why payroll and planning calendars occasionally gain a period. Reproduce it Every number is printed by one dependency-free Node script over one 400-year cycle (the calendar repeats, so the counts are exact, not sampled): → Run it yourself (public gist) Originally published at lkforge.com , where the weekday distribution is an interactive deviation chart. Built alongside the free LK Forge Calendar tools .

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/lucian_lkb_1f009d/is-friday-the-13th-really-more-common-i-counted-400-years-to-find-out-4ph6

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
