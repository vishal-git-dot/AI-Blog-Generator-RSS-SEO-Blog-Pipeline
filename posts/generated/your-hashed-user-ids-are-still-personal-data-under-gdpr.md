---
title: "Your Hashed User IDs Are Still Personal Data Under GDPR"
slug: "your-hashed-user-ids-are-still-personal-data-under-gdpr"
author: "Mehwish Malik"
source: "devto_webdev"
published: "Tue, 18 Aug 2026 06:36:44 +0000"
description: "Plenty of engineering teams believe that hashing an email or swapping a real user ID for a random token takes a table out of GDPR scope . It does not, and th..."
keywords: "data, personal, not, your, gdpr, still, table, does"
generated: "2026-08-18T06:52:25.243212"
---

# Your Hashed User IDs Are Still Personal Data Under GDPR

## Overview

Plenty of engineering teams believe that hashing an email or swapping a real user ID for a random token takes a table out of GDPR scope . It does not, and the wording of the law is the reason. Article 4(5) defines pseudonymisation as processing personal data so that it "can no longer be attributed to a specific data subject without the use of additional information". The ICO reads that exactly as written: pseudonymisation is "effectively only a security measure. It does not change the status of the data as personal data". So if a salt, a key vault entry, a lookup table or a join key exists anywhere in your estate, the hashed table is personal data. Retention limits, breach reporting and subject access requests all still apply to it. What actually leaves scope Only irreversible anonymisation. If any reasonable means could relink a row to a person, you are still inside GDPR. Where this bites in real stacks Client-side tags firing before the consent state resolves. Web servers keeping full IP addresses in default log config. Error monitoring attaching session and device IDs to stack traces. Mobile SDKs reading the advertising identifier on app launch. Each of those touches something on the regulator list of what counts as personal data under GDPR , so each one needs a lawful basis before it runs. Why the business cares Article 83 puts the upper tier at 20 million euros or 4% of global annual turnover. A logging default is a cheap fix. An enforcement action is not. Fix it at the edge, not in twelve codebases Chasing consent logic through every SDK is work you will repeat forever. Move collection behind server side tagging and you get one control point instead of twelve. Seers.AI sits there and decides, per visitor, per identifier, what is allowed to leave. The AI learns your tag landscape as it changes, so a new script added by the marketing team does not quietly become your next incident. Give the boring part to a system that never forgets to check.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/mehwish_malik_4f29ff7fb04/your-hashed-user-ids-are-still-personal-data-under-gdpr-46cp

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
