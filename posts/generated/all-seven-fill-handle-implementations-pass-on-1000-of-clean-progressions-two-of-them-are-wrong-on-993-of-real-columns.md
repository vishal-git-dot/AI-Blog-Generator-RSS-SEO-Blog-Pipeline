---
title: "All Seven Fill-Handle Implementations Pass on 100.0% of Clean Progressions; Two of Them Are Wrong on 99.3% of Real Columns"
slug: "all-seven-fill-handle-implementations-pass-on-1000-of-clean-progressions-two-of-them-are-wrong-on-993-of-real-columns"
author: "Devanshu Biswas"
source: "devto_webdev"
published: "Sun, 23 Aug 2026 12:38:20 +0000"
description: "A fill handle looks like repetition, so the natural implementation is a step: work out how much the value goes up by, then keep adding it. That is not what t..."
keywords: "fill, one, slope, two, not, cells, last, all"
generated: "2026-08-23T12:50:17.233156"
---

# All Seven Fill-Handle Implementations Pass on 100.0% of Clean Progressions; Two of Them Are Wrong on 99.3% of Real Columns

## Overview

A fill handle looks like repetition, so the natural implementation is a step: work out how much the value goes up by, then keep adding it. That is not what the selection means. Selecting n cells and dragging says continue this , and the cells are n observations of a value against a position. Continuing them is fitting a line through all n and reading it one position further along — which is why 1, 2 becomes 3, 4, 5, and why 1, 2, 4 becomes 5.33 and not 6. function fitLine ( v ){ const n = v . length , mi = ( n - 1 ) / 2 ; let sv = 0 ; for ( let i = 0 ; i < n ; i ++ ) sv += v [ i ]; const mv = sv / n ; let sxy = 0 , sxx = 0 ; for ( let i = 0 ; i < n ; i ++ ){ const dx = i - mi ; sxy += dx * ( v [ i ] - mv ); sxx += dx * dx ; } const slope = sxx > 0 ? sxy / sxx : 0 ; // n === 1 lands here: no slope exists return { slope : slope , intercept : mv - slope * mi }; } Seven implementations, live, on cells you can edit: https://dev48.infy.uk/design/day69-fill-handle.html The property everybody tests expect ( fill ([ ' 1 ' , ' 2 ' ], 4 )). toEqual ([ ' 3 ' , ' 4 ' , ' 5 ' , ' 6 ' ]); expect ( fill ([ ' 5 ' , ' 10 ' , ' 15 ' ], 2 )). toEqual ([ ' 20 ' , ' 25 ' ]); A real property — an exact progression continues exactly — and it is satisfied by 7 of 7 implementations on 100.0% of 12,000 generated progressions. It has to be. On data lying exactly on a line, last-two-cells, first-and-last, mean-of-gaps and least-squares all recover the same slope, because the residuals are zero and there is nothing left for the estimators to disagree about. What separates them Nothing changes but the corpus: 12,000 columns of trend plus jitter, the shape of every real column anyone has ever dragged a handle down. implementation disagrees, clean disagrees, noisy trend points the wrong way mean error least squares 0.0% 0.0% 0.0% 0.000 step from the last two cells 0.0% 99.3% 33.4% 13.133 step from first to last 0.0% 99.3% 12.0% 2.662 Five months of sales — 120, 138, 131, 149, 144 — fits +5.9 and predicts 154.1. Last-two-cells fits −5.0 and predicts 139.0: two numbers dipped at the end of a rising column, and the fill inverted the direction of the whole series. Not imprecise, inverted, on a third of real columns, with no error and a perfectly plausible value. And 80.5% of correct fills over integer data come out fractional, which is the single most reported "bug" here and is not one. What the measurement contradicted I wrote the self-consistency test — fill 3, append, fill 1 must equal the 4th cell of a 4-cell fill — expecting it to be the property that separates the implementations. It separates none of them. Worse, my claim that it passes everywhere was wrong: 100.0% on all 6,570 fitted series and 61.4% on the copy path, because when the selection is not extendable a fill is a cyclic repeat and the cycle length is the selection. Averaging the two into one plausible-looking 96% would have hidden a structural difference. That useless property then found the only defect on the page nobody put there. May is the one month that is its own abbreviation, so as an anchor it silently switched a run of full month names into abbreviations — and the oracle agreed throughout, because the oracle implements the same ambiguous rule. Re-filling did not. The register now belongs to the selection rather than the cell. It also killed a planned seventh variant: mean-of-gaps is algebraically identical to first-to-last, because the gaps telescope. One line of algebra, then 200,000 random vectors to confirm nothing floating-point sneaks in — largest slope difference 1.7e-13, zero predictions apart. 3,642,926 assertions on load across 42,000 selections, 137 more in the verifier against three independent oracles, and 4,000 fits checked against exact BigInt rationals — worst deviation 9.5e-10. Part of a from-scratch series — one component a day, vanilla JS, one file, dependency-free engine: https://dev48.infy.uk/designfromzero.php

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/dev48v/all-seven-fill-handle-implementations-pass-on-1000-of-clean-progressions-two-of-them-are-wrong-4e68

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
