---
title: "The GB to NI Customs Workflow, System by System"
slug: "the-gb-to-ni-customs-workflow-system-by-system"
author: "iCustoms"
source: "devto_ai"
published: "Thu, 27 Aug 2026 08:32:10 +0000"
description: "Here is a clean trace of a standard GB to NI road movement across the four HMRC systems. Step 1: Trader submits movement information A single entry captures ..."
keywords: "step, movement, goods, customs, data, reference, declaration, workflow"
generated: "2026-08-27T08:36:24.649399"
---

# The GB to NI Customs Workflow, System by System

## Overview

Here is a clean trace of a standard GB to NI road movement across the four HMRC systems. Step 1: Trader submits movement information A single entry captures the goods, value, procedure, transport and route. This is the source of truth for everything downstream. Step 2: TSS validates and routes TSS enriches the entry, checks it against reference data, and sends structured payloads out. Step 3: CDS returns the customs decision The declaration is filed and returns a decision on duty, procedure and clearance status. CDS is the answer to "what did customs decide about these goods". Step 4: ICS2 receives safety and security data Safety and security data goes to ICS2 before the goods arrive. This is a separate obligation from the customs declaration. Step 5: GVMS bundles references into a GMR GVMS packages the declaration references into a single Goods Movement Reference. The driver presents the GMR at check-in. The Goods Movement Reference explained view covers what causes rejection. Step 6: Vehicle embarks When the vessel departs, the movement moves to embarked status. That triggers the automated downstream processes. Practical takeaway Every step depends on clean data at Step 1. That is where engineering effort pays back. Ready to see this workflow in a working product? Watch a demo to walk through iCustoms.ai with a live agent.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/icustoms12/the-gb-to-ni-customs-workflow-system-by-system-2lig

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
