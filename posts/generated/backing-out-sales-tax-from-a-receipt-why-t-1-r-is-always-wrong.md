---
title: "Backing Out Sales Tax From a Receipt: Why T * (1 - r) Is Always Wrong"
slug: "backing-out-sales-tax-from-a-receipt-why-t-1-r-is-always-wrong"
author: "Ashley Chen"
source: "devto_webdev"
published: "Sun, 15 Nov 2026 22:36:37 +0000"
description: "When an accounting script or expense parser tries to recover the pre-tax price from a tax-inclusive receipt total, the most common bug is multiplying the tot..."
keywords: "tax, sales, total, pre, reverse, rate, invoice, integer"
generated: "2026-11-15T22:39:51.909507"
---

# Backing Out Sales Tax From a Receipt: Why T * (1 - r) Is Always Wrong

## Overview

When an accounting script or expense parser tries to recover the pre-tax price from a tax-inclusive receipt total, the most common bug is multiplying the total by (1 - r) instead of dividing by (1 + r) . Forward vs. Reverse Arithmetic If the pre-tax price is P = 100.00 and the combined tax rate is r = 0.0825 (8.25%): Total = P * (1 + r) = 100.00 * 1.0825 = 108.25 Going backward from Total = 108.25 : Wrong: 108.25 * (1 - 0.0825) = 99.319375 -> $99.32 (off by $0.68) Right: 108.25 / (1 + 0.0825) = 100.00 Because (1 + r)(1 - r) = 1 - r^2 , subtracting r introduces a systematic downward bias of r^2 * P . At an 8.25% tax rate that is 0.68% of every invoice; at 10% it is 1% of gross spend. Two Edge Cases in U.S. Sales Tax Code Integer-cent rounding per line vs. per invoice. Point-of-sale terminals round round_half_up(subtotal * r) to integer cents. When an invoice contains multiple taxable lines, summing rounded line-level taxes can differ by $0.01 from applying r to the combined subtotal. Jurisdiction stacking. State, county, city, and transit-district rates combine into one effective rate r , though certain states cap local tax above a threshold per single item. If you want to inspect forward tax and reverse pre-tax extraction across U.S. state rates in integer cents, the Miryori Sales Tax Calculator shows the exact breakdown step by step. Related reading a shorter math note on why reverse sales tax diverges quadratically YMYL note: examples above are illustrative arithmetic only; verify jurisdiction-specific exemptions, thresholds, and filing rules with local tax authorities.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/miri-calc/backing-out-sales-tax-from-a-receipt-why-t-1-r-is-always-wrong-4bkb

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
