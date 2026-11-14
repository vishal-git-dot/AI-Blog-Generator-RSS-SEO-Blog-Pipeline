---
title: "Designing shareable collections without making users create an account"
slug: "designing-shareable-collections-without-making-users-create-an-account"
author: "同思远"
source: "devto_webdev"
published: "Sat, 14 Nov 2026 05:26:46 +0000"
description: "A collection tracker has two different kinds of state: the list someone is editing and the list they want another person to see. Keeping those separate was a..."
keywords: "collection, link, list, lootprism, saved, shared, snapshot, progress"
generated: "2026-11-14T05:48:05.831649"
---

# Designing shareable collections without making users create an account

## Overview

A collection tracker has two different kinds of state: the list someone is editing and the list they want another person to see. Keeping those separate was an important design decision for LootPrism, a Fortnite tool I work on. The editable collection is saved in the current browser. A shared link captures the selected collection at the time of sharing. Opening that link shows the snapshot instead of silently overwriting the receiving device’s saved progress. To continue on another device, the user explicitly imports it; when progress already exists there, the interface offers a merge. This makes a shared link stable. A friend can open yesterday’s link and see what was shared yesterday. It also gives the interface an obligation: explain that editing a collection does not update an old link. After making changes, the user creates a new snapshot. The same distinction matters for image exports. An image can be a full collection, a missing list or the current filtered view. A QR code should lead to the represented snapshot, while the destination should also offer a clear way to create a separate personal checklist. This approach removes account setup from a small tracking task, but it does not provide automatic synchronization. Clearing browser data still removes locally saved progress. The product needs a visible sharing and import flow rather than calling the feature cloud sync. You can try these interactions at https://lootprism.com/sprites/ . I am interested in feedback on when an explicit import is clearer than automatic synchronization. Disclosure: I work on LootPrism. This draft was prepared with AI writing assistance and reviewed against the product’s actual behavior.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/_6113e847c27e588598b50/designing-shareable-collections-without-making-users-create-an-account-4nk0

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
