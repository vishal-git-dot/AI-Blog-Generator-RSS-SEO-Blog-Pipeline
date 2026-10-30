---
title: "Canada's open baby-food data: a 1000x unit label, a 10x table slip, and lead vs the FDA's action levels"
slug: "canadas-open-baby-food-data-a-1000x-unit-label-a-10x-table-slip-and-lead-vs-the-fdas-action-levels"
author: "munimv2"
source: "devto_python"
published: "Fri, 30 Oct 2026 04:40:04 +0000"
description: "The Canadian Food Inspection Agency (CFIA) tests food for infants and children every year in its Children's Food Project, and it publishes one per-sample CSV..."
keywords: "lead, ppm, ppb, every, not, food, printed, open"
generated: "2026-10-30T05:13:18.341948"
---

# Canada's open baby-food data: a 1000x unit label, a 10x table slip, and lead vs the FDA's action levels

## Overview

The Canadian Food Inspection Agency (CFIA) tests food for infants and children every year in its Children's Food Project, and it publishes one per-sample CSV per year on open.canada.ca, next to a report page with printed tables. That is rare and valuable: anyone can check the printed numbers against the raw data. So we did, for aflatoxin M1 (a mould toxin that reaches milk) in six years of files, and for lead in six more. Every check was pre-registered: the predictions and the grading code were public on GitHub before any result value was read. A sealed compute job then graded them on SHA-256-pinned copies of the files, and a second sealed job later re-ran an independent test against the published results. Most of it reproduces The good news first. For aflatoxin M1 (2012-13 to 2022, 468 samples), the files reproduce every figure CFIA printed. For lead (2017 to 2022, 979 samples), they reproduce every row of every printed table: samples tested, negative, positive and the maximum. Across the two studies, 11 of the 12 consistency checks we registered held. The one miss is a single text figure: the 2021 report says detected lead ranged from 0.015 ppm, and the file's smallest value is 0.016. A unit label that is 1000 times off The 2014-15 file labels its aflatoxin M1 results in µg/g. Every other year uses ng/g. Its four positive infant formula results are stored as 0.011, 0.022, 0.052 and 0.061, which is exactly the report's "0.011 ppb to 0.061 ppb". So the numbers are already in ppb (ng/g) and only the label is wrong. Anyone who pools the open files by their unit column would read 2014-15 as 1000 times higher: the top value would become 61 ppb, about 120 times the Codex reference level of 0.5 ppb for milk. A decimal point that moved The 2021 report's lead table gives a maximum of 0.18 ppm for infant and toddler meals. The same report's text says detected lead ranged up to 0.047 ppm, in pasta, and the table's own meal mean (0.001 ppm over 53 samples) cannot hold a 0.18. The file settles it: the three puree and meal positives are 0.016, 0.018 and 0.022 ppm. Reading the maximum as 0.018 makes every 2021 figure fit. The difference matters for anyone comparing with the U.S. FDA's 2025 action levels: as printed, the table puts a meal at 18 times the FDA's 10 ppb level for such foods; the file puts it at 1.8 times. Two kinds of average under one heading The printed lead means are not one statistic. In 2017, 2019, 2020 and 2021 they average over all samples (non-detects count as zero). In 2018-19 and 2022 they average over the positive samples only. We predicted which convention each year used, and all 12 printed means matched. The 2017 table even carries the note "Average of positive results only", but its two positives (0.007 and 0.009 ppm) average 0.008, while the printed mean is 0.000; only an all-sample mean prints that way. "Not detected" is not "below 10 ppb" From 2018 to 2021 the smallest lead value ever reported was 0.015 ppm (15 ppb). In 2022 it was 0.0050 ppm, and lead was suddenly found in 59% of samples instead of 2-8%. That jump is a change in reporting, not more lead in food. It also means that a 2018-2021 "not detected" result cannot tell you whether a puree, yogurt or pudding was under the FDA's 10 ppb action level. Against the FDA's 20 ppb level for dry infant cereals, 6 of 48 Canadian infant cereals sampled in 2019 were above it (0.026 to 0.093 ppm), and 1 of 39 in 2022 (0.0211 ppm). At a common 0.015 ppm cut, the share fell from 22.9% to 7.7% (one-sided Fisher p = 0.049). One caution, found after grading and so only a hypothesis: the whole fall is among imported or unknown-origin cereals. The 2022 sample has no U.S.-declared cereal at all, and the Canadian-declared cereals did not fall (4 of 12, then 3 of 8). The files cannot tell a change in the market from a change in what was sampled. What this is and is not This is a reproducibility check of open government data. It is not a compliance finding and not about any brand. Health Canada reviewed every result in these surveys and found none a safety concern; the FDA levels are non-binding U.S. guidance, used here only as a reference scale. Nothing here is dietary or medical advice. What it does show is that open per-sample data lets anyone catch the small errors every large report carries, and that two such errors here (a unit label and a decimal point) each change a number by a factor of ten or more. Reproduce it Everything is in github.com/munimtechnologies/spice-lead-recalls (Apache-2.0 code, CC BY 4.0 text and derived data). Start at the Children's Food Project page: https://github.com/munimtechnologies/spice-lead-recalls/blob/main/docs/childrens-food-project.md . It links the pre-registrations, the graded results, the per-sample tables and the tests. The source files are CFIA's Children's Food Project datasets on open.canada.ca (Open Government Licence – Canada). This post and the analysis were made with AI agents working in my name. — MV2, Munim, Inc., mv2@munimtech.com

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/munimv2/canadas-open-baby-food-data-a-1000x-unit-label-a-10x-table-slip-and-lead-vs-the-fdas-action-1492

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
