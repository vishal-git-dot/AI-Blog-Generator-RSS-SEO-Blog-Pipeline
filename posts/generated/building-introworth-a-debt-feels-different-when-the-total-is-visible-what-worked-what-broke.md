---
title: "Building Introworth: A Debt Feels Different When the Total Is Visible. What Worked, What Broke"
slug: "building-introworth-a-debt-feels-different-when-the-total-is-visible-what-worked-what-broke"
author: "OneLifeVibe"
source: "devto_webdev"
published: "Thu, 12 Nov 2026 00:15:18 +0000"
description: "A monthly payment is a terrible progress report. It stays the same while the balance moves, so a person paying a debt down can do everything right for months..."
keywords: "total, what, monthly, can, number, one, when, balance"
generated: "2026-11-12T00:20:19.771834"
---

# Building Introworth: A Debt Feels Different When the Total Is Visible. What Worked, What Broke

## Overview

A monthly payment is a terrible progress report. It stays the same while the balance moves, so a person paying a debt down can do everything right for months and still see no change in the number they look at most. A single monthly payment, repeated for a year, can feel like walking in place, even when hundreds of dollars of principal have already been paid. The problem is not a lack of discipline. It is a lack of a visible total. A debt feels endless when it is only ever seen one payment at a time. It becomes a project with an end date when it is seen alongside every other balance: assets on one side, debts on the other, and the difference between them as the number that matters. Designing around one total Introworth was built around that difference. Instead of opening to a list of accounts, it opens to a single net worth figure, with the assets and debts that make it up underneath. The order is deliberate. A list of accounts invites a person to check each balance in isolation. A single total invites a different question: is this number moving in the right direction, and how fast? The design choice has a second effect. When the total is the main view, the individual accounts stop competing for attention. A savings account, a card balance, and a loan do not each need their own verdict. They need to be weighed together, because the total is the only figure that captures whether the overall position improved. Most of the work was in making the total trustworthy. Balances are entered by hand, so the tool has to make a monthly update quick enough to repeat and hard to get wrong. If updating takes too long, the data goes stale. If it is too easy to mistype, the total lies. A net worth figure is only useful while a person still believes it, and belief depends on how easily the number can be checked. What worked Keeping the home screen to one number worked better than expected. People who had tried spreadsheets said the difference was not the arithmetic, which a spreadsheet does well, but the absence of clutter. There was nothing to maintain, no columns to fix, and no formulas to break. The total was there every time the page opened, and it either moved or it did not. A fixed monthly review also worked. The same set of balances, updated on the same day each month, turned a chore into a routine. The review stayed short because the questions stayed the same: what is owed, what is owned, and has the gap moved the right way? Over several months, that routine produced something a spreadsheet rarely did: a continuous record of the total, month by month, in one place. Showing debts and assets together, rather than in separate sections, worked as well. A debt paid down by $200 while savings fell by $200 is not progress, and the combined total makes that obvious. Separate views can hide the trade. A single total cannot, because it falls when money moves from savings to a card without reducing what is owed overall. What broke, or nearly did The first version tried to do too much with each account. It offered categories, notes, and per account targets, on the assumption that more detail would lead to better decisions. In practice, the extra fields slowed the monthly update and gave people reasons to put it off. Most of the detail was removed. What remained was the balance, the name, and whether it was an asset or a debt. The second problem was the temptation to add charts. A graph of net worth over time sounds useful, and it is, but an early chart made small monthly changes look dramatic by scaling the axis to the range of the data. A $50 improvement looked like a steep climb. The axis was fixed to start at zero for the main view, so that a small gain looks small and a large gain looks large. The third problem was subtler: the tool made it too easy to update balances without thinking. A quick update can become a habit of typing numbers without looking at them, and a mistyped balance can sit unnoticed for a month. A simple confirmation screen was added, showing the new total next to the previous total, so that an unexpected jump has to be acknowledged before it is saved. Lessons for builders Lead with the outcome number, not the activity numbers. Payments, logins, and updates are activity. The total moving in the right direction is the outcome, and it deserves the top of the screen. Show competing items side by side before offering any recommendation. Most ordering advice becomes unnecessary once rates, balances, and minimums share one view. Design the update ritual before designing the dashboard. A monthly, ten minute, never changing routine is what keeps the data fresh enough for the dashboard to mean anything at all. The project behind these lessons is Introworth , which tracks assets and debts together so net worth can be followed as one number over time, rather than reconstructed from separate statements each month.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/onelifevibe/building-introworth-a-debt-feels-different-when-the-total-is-visible-what-worked-what-broke-2n4g

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
