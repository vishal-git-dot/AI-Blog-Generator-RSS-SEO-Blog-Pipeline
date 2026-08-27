---
title: "TSS, ICS2, GVMS and NCTS: A Technical Overview"
slug: "tss-ics2-gvms-and-ncts-a-technical-overview"
author: "Kristi Hampson"
source: "devto_ai"
published: "Thu, 27 Aug 2026 08:30:55 +0000"
description: "TSS, CDS, ICS2, GVMS and NCTS are best understood as a small distributed system with a shared input layer and four specialised backends. The pipeline The tra..."
keywords: "tss, gvms, receives, ncts, cds, system, shared, pipeline"
generated: "2026-08-27T08:36:24.650559"
---

# TSS, ICS2, GVMS and NCTS: A Technical Overview

## Overview

TSS, CDS, ICS2, GVMS and NCTS are best understood as a small distributed system with a shared input layer and four specialised backends. The pipeline The trader submits movement information once. TSS validates and enriches it, then routes structured messages to the correct downstream system. CDS receives the customs declaration payload. ICS2 receives the safety and security payload. GVMS receives declaration references bundled into a Goods Movement Reference. NCTS receives the transit declaration when the movement runs under the Common Transit Convention. ## Shared identifiers All four backends describe the same consignment. They share EORI numbers, commodity codes and transport identifiers. That shared vocabulary is what lets TSS route once and reconcile later. Where the pipeline breaks Historical development created inconsistencies in formatting expectations. A commodity code entered one way in CDS may be accepted differently by another system, and a vehicle registration mismatch will fail GVMS check-in. Most production incidents are data quality issues at the entry point. The TSS routing to HMRC systems walkthrough covers the flow in more detail. Practical takeaway Treat the entry layer as the schema-of-record. Normalise once, validate at the boundary, and rely on TSS to route. Want to see this pipeline running end to end? Watch a demo to see iCustoms.ai orchestrate the flow.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/kristi-hampson/tss-ics2-gvms-and-ncts-a-technical-overview-5b5e

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
