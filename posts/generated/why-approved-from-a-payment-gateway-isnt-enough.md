---
title: "Why "Approved" From a Payment Gateway Isn't Enough"
slug: "why-approved-from-a-payment-gateway-isnt-enough"
author: "Jose Daniel Leon Ruiz"
source: "devto_webdev"
published: "Thu, 22 Oct 2026 16:45:50 +0000"
description: "If your payment gateway responds with approved: true, do you also check that the approved amount matches what you asked it to charge? We didn't, until this w..."
keywords: "approved, payment, you, amount, gateway, check, payphone, order"
generated: "2026-10-22T16:56:20.010034"
---

# Why "Approved" From a Payment Gateway Isn't Enough

## Overview

If your payment gateway responds with approved: true, do you also check that the approved amount matches what you asked it to charge? We didn't, until this week. We're building DymCore, an invoicing platform for small businesses, and one of its payment integrations is PayPhone, a payment gateway used in Ecuador. Like most integrations, our code trusted the boolean the gateway returned: if PayPhone said the transaction was approved, we marked the order as paid. The boolean told us the transaction went through. It never told us it went through for the right amount. This week we added an explicit check before confirming any order: compare the amount PayPhone approved against the amount we expected to charge. If they don't match, the payment isn't silently accepted. It raises a critical alert and the order stays unconfirmed instead of moving forward. We also added dedicated test coverage for the mismatch case specifically, because this is exactly the kind of check you want to be sure never regresses silently. The lesson generalizes past this one gateway: when a third-party system tells you "this succeeded," the amount is usually the part worth re-verifying server-side, not just the success flag. A field saying "approved" is a claim from someone else's system, not a receipt you generated yourself. Have you run into a payment or billing integration that approved a different amount than what was requested? Curious how other teams guard against this. We write about things like this while building DymCore .

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/jdevleon/why-approved-from-a-payment-gateway-isnt-enough-3ch8

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
