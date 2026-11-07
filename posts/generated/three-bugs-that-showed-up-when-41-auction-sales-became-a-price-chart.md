---
title: "Three bugs that showed up when 41 auction sales became a price chart"
slug: "three-bugs-that-showed-up-when-41-auction-sales-became-a-price-chart"
author: "Jason Trogdon"
source: "devto_python"
published: "Sat, 07 Nov 2026 21:15:43 +0000"
description: "I run What The Slab , a site that turns sold auction results for graded trading cards into year-by-year price tables. The site's code is written with an AI c..."
keywords: "card, sale, sales, price, grade, psa, three, page"
generated: "2026-11-07T21:39:06.286322"
---

# Three bugs that showed up when 41 auction sales became a price chart

## Overview

I run What The Slab , a site that turns sold auction results for graded trading cards into year-by-year price tables. The site's code is written with an AI coding assistant; I decide what it builds and check what comes out. Each page is one card: every sale gets matched by its listing title, sorted by grade, screened for outliers, and summed into a median per year. This week we added the 2000 Playoff Contenders Tom Brady rookie, plus its rare parallel, the Championship Ticket (only 100 made). That one card exposed three bugs in a pipeline that had handled 25 other cards fine. 1. The grader assumption Every card on the site was graded by PSA, so "grade" quietly meant "PSA grade." This card mostly trades in Beckett (BGS) slabs: the auction house had 136 BGS sales against 73 PSA, and no PSA grade had enough sales for a yearly table. The fix was making the grader part of the card spec instead of a constant: @dataclass ( frozen = True ) class CardSpec : key : str name : str require : tuple # phrases every counted title must contain optional : tuple = () # extra words a title may contain grader : str = " PSA " grades : tuple = ( " 10 " , " 9 " , " 8 " ) Page titles, table labels and the social post all read spec.grader . The data model was the only place that actually needed to change, which says the rest was built right. 2. Matching titles when the seller numbers the copy A sale counts only if its title is exactly this card at exactly this grade. The matcher strips the required phrases and the one grade, drops boilerplate words ("ROOKIE", "GEM MINT"), and rejects the sale if anything is left over. That's what keeps signed copies, lots and foreign-language versions out. Championship Tickets are numbered out of 100, and sellers write it three ways: ... Tom Brady RC AUTO /100 #144 BGS 9 ... Tom Brady ROOKIE AUTO 35/100 BGS 8.5 ... Tom Brady ROOKIE AUTO 97/100 BGS 8.5 35/100 was a leftover word, so those sales were thrown out. The fix treats a copy number as the print run it belongs to: _SERIAL_RE = re . compile ( r " ^\d{1,4}(/\d{1,5})$ " ) def _serial_run ( token : str ) -> str : m = _SERIAL_RE . match ( token ) return m . group ( 1 ) if m else token # "35/100" -> "/100" left = [ t for t in tokens if t not in allowed and _serial_run ( t ) not in allowed ] 35/50 still gets rejected, because that's a different print run, so a different card. 3. The outlier filter that deleted a real market move The outlier screen sets a sale aside when it's more than 6x away from the median of the three sales before it and the three after it. That catches a $1 typo among $400 sales. Here's the BGS 8 Championship Ticket history: Date Price 2015-2016 $3,800 to $3,876 Jan 2019 $61,100 Jan 2020 $144,100 Sep 2020 $205,300 Aug 2021 $1,020,000 Jan 2022 $1,290,000 The 2020 sales are more than 6x the sales before them and less than a sixth of the sales after them. Far from both sides, so the filter dropped them. But they aren't errors. They're the steps between a $4,000 card and a $1,000,000 card. The fix: an outlier has to be far from both sides in the same direction . def _far_from ( sale , side ) -> int : mid = statistics . median ( s [ " price " ] for s in side ) if sale [ " price " ] > mid * 6 : return 1 if sale [ " price " ] < mid / 6 : return - 1 return 0 out = _far_from ( sale , before ) == _far_from ( sale , after ) != 0 A $9,000,000 sale sitting between those two levels is above both sides, so it still gets set aside. There's a test for exactly that. Bonus: a link that promised too much The site also has a "highest sales on record" page where card names link to their price-history page. The link check matched the card and ignored the grade, so a PSA 9 sale linked to a page that only shows PSA 8 and below. That had been live for a day before this card showed it. The link now requires the grade to be one the page actually displays. What I took from it All three bugs passed every test the site had, because every test card was PSA, unnumbered, and had a smooth price history. The 26th card was the first one that broke the pattern. Now each of these cases is a unit test built from the real listing titles. Working with an AI assistant didn't change that lesson: tests only cover the cases you've already seen, whoever writes the code. The two new pages, if you want to see the output: Contenders Brady price history and the Championship Ticket .

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/whattheslab/three-bugs-that-showed-up-when-41-auction-sales-became-a-price-chart-1k5l

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
