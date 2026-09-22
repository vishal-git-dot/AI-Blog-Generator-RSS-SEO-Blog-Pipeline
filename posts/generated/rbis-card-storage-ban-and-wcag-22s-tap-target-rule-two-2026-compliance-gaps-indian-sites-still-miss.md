---
title: "RBI's card-storage ban and WCAG 2.2's tap-target rule: two 2026 compliance gaps Indian sites still miss"
slug: "rbis-card-storage-ban-and-wcag-22s-tap-target-rule-two-2026-compliance-gaps-indian-sites-still-miss"
author: "ZoopCoder"
source: "devto_webdev"
published: "Tue, 22 Sep 2026 16:33:26 +0000"
description: "Two rules quietly changed what "correct" looks like for two very different parts of an Indian website — payment checkout and accessibility — and most sites w..."
keywords: "card, wcag, indian, target, sites, your, because, against"
generated: "2026-09-22T16:40:24.509196"
---

# RBI's card-storage ban and WCAG 2.2's tap-target rule: two 2026 compliance gaps Indian sites still miss

## Overview

Two rules quietly changed what "correct" looks like for two very different parts of an Indian website — payment checkout and accessibility — and most sites we look at still haven't caught up with either. 1. You are not allowed to store your customer's card number anymore Since 1 October 2022 , RBI's Card-on-File Tokenisation (CoFT) rules mean no entity in the card payment chain — other than the card issuer and card network — is allowed to store a customer's card number, CVV or expiry date for later use. Any card data a merchant or website had already saved before that date was required to be purged. This is easy to miss because nothing breaks visibly if you ignore it — until someone audits you, or until a "remember my card" form built the naive way turns out to be silently illegal. The correct pattern: The card number, CVV and expiry never touch your own server or database. They go straight from the customer's browser to the gateway's hosted form or SDK. Your server only ever sees a token issued by the gateway (Razorpay/PayU/Cashfree/PhonePe), unique to the card + your merchant account, and that token is what "remembers" the card for next time. Order status still has to be verified server-side via signature verification and webhooks — a success page in the browser is not proof of payment, tokenisation or not. We do fixed-price gateway integrations (Razorpay, PayU, Cashfree, PhonePe) and this is exactly the checklist we build against — full writeup with the RBI source: https://zoopcoder.com/services/payment-gateway-integration.php (₹3,999, 2-4 working days). 2. WCAG 2.2 added a tap-target-size rule that most "WCAG 2.1 compliant" sites have never been checked against WCAG 2.2 (published Oct 2023) added Success Criterion 2.5.8 Target Size (Minimum) : pointer targets — buttons, icon links, nav items — must be at least 24 by 24 CSS pixels , with a handful of narrow exceptions (inline text links, targets with enough spacing around them, targets whose size is controlled by the user agent). This did not exist in WCAG 2.1. So a site that was audited and "passed" against 2.1 can genuinely fail 2.2 on exactly this criterion — and in our experience auditing Indian sites, it's one of the most common real failures, because mobile-first Indian layouts lean on icon-only nav buttons and tightly packed link lists that were never measured against a 24px floor. It matters more here than in a lot of markets simply because of how much Indian traffic is mobile-only: a target that's "fine" with a mouse cursor is a genuine miss-tap problem on a phone. Full audit service, checks 2.1 AA plus the WCAG 2.2 target-size criterion specifically: https://zoopcoder.com/services/website-accessibility-audit.php (₹4,999, up to 15 pages, 5-7 working days — automated scan plus real manual keyboard and screen-reader testing, because automated scanners only catch an estimated 30-40% of real issues). Neither of these is a guess — RBI's tokenisation circulars and the W3C's WCAG 2.2 spec are both public. Worth a five-minute check against your own site either way. Disclosure: I work on ZoopCoder, an Indian web/app dev shop — both service links above are ours. Posting because these two specific rules trip up sites that would otherwise call themselves compliant.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/zoopcoder/rbis-card-storage-ban-and-wcag-22s-tap-target-rule-two-2026-compliance-gaps-indian-sites-still-2ch8

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
