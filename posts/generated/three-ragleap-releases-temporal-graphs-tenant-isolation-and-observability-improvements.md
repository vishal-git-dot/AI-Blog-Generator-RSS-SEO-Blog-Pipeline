---
title: "Three RagLeap Releases: Temporal Graphs, Tenant Isolation, and Observability Improvements"
slug: "three-ragleap-releases-temporal-graphs-tenant-isolation-and-observability-improvements"
author: "RagLeap"
source: "devto_python"
published: "Sat, 14 Nov 2026 05:26:46 +0000"
description: "AI infrastructure has to get the fundamentals right. A system can generate excellent responses and still have problems with historical knowledge, tenant isol..."
keywords: "ragleap, tenant, graph, temporal, relationship, new, filter, observability"
generated: "2026-11-14T05:48:05.830057"
---

# Three RagLeap Releases: Temporal Graphs, Tenant Isolation, and Observability Improvements

## Overview

AI infrastructure has to get the fundamentals right. A system can generate excellent responses and still have problems with historical knowledge, tenant isolation, unsupported search filters, or its own monitoring stack. We recently released updates across three RagLeap libraries: ragleap-graph v0.11.0 ragleap-observability v0.8.5 ragleap-vectorstores v0.7.0 Here is a technical look at the changes. 1. Temporal relationships in ragleap-graph v0.11.0 Knowledge graph relationships can change as documents are added, updated, or removed. Previously, applications could query the current graph, but preserving relationship validity over time required additional work. The new release introduces opt-in temporal relationship tracking: GraphIndex ( temporal = True ) Temporal relationship edges can contain: valid_from valid_to When the last supporting document for a relationship is removed, the edge is closed by setting valid_to instead of deleting it. If supporting evidence returns, the edge can reopen with a new valid_from . Historical queries The release adds an as_of parameter: find_relations ( . . . , as_of =< timezone - aware datetime > ) This allows historical queries against the graph's recorded relationship validity. With temporal mode enabled, regular relationship and community relation queries use open edges. Important: The timestamps represent indexing time, not real-world event time. Temporal mode is opt-in, and reads and writes must use the same setting. Tenant isolation We also improved namespace and user filtering in graph query paths, including: document_entities Community member-name lookup search_related_entities New offline and live tests cover tenant-isolation behavior. 2. Grafana and Kubernetes improvements in ragleap-observability v0.8.5 The observability stack needs security maintenance and actual deployment testing. Grafana image update We upgraded the Grafana image: 12.4.12 → 12.4.15 The previous image had a fixable critical vulnerability in its Alpine base layer. The updated image passed the critical-vulnerability gate, with no fixable critical finding reported in the new scan. Kubernetes validation We tested chart install, upgrade, and uninstall on: Kubernetes v1.34.11 Kubernetes v1.36.4 Kubernetes v1.37.0 The checks included Grafana health, database connectivity, admin login, Prometheus and Loki datasource health, and application logs. Availability alert testing A throwaway Kubernetes environment was used to validate alert behavior with a stand-in notification receiver. The tests covered: Healthy-system behavior with no alerts. Exporter failure triggering availability alerts. Target removal triggering a target-absent alert. Notification delivery to the test receiver. Resolved notification delivery. This verifies specific alert scenarios, not every production monitoring scenario. Slow-burn alert behavior, real Slack/email delivery, and multi-node long-running environments still need validation. 3. Tenant-aware filtering in ragleap-vectorstores v0.7.0 Tenant filtering must be enforced, not merely accepted as an argument. This release improves tenant_id filtering across three backends. Backend Change Redis tenant_id is now a filterable TAG field OpenSearch tenant_id is mapped as a keyword field, including on existing indexes LanceDB tenant_id is a nullable column, including existing tables Chunks without a tenant identifier never match a tenant filter. Unsupported filters now fail explicitly Previously, Redis could silently ignore unsupported filter keys. That meant a caller might believe a filter was applied when it was not. The new behavior is explicit: RedisBackend raises ValueError for unsupported filter keys. OpenSearchBackend raises ValueError for unsupported filter keys. LanceDBBackend and UpstashBackend also validate filter keys. This follows a simple principle: if a requested restriction cannot be enforced, fail instead of silently continuing. Redis migration note: Existing Redis indexes without the tenant_id field cannot use the new tenant filter. Use a new index created with the updated schema. Chroma metadata protection ChromaBackend.insert_chunk now prevents caller-provided metadata from overwriting reserved fields: document_id document_name chunk_index token_count This protects metadata used for document and chunk identification. Why these changes matter These three releases address different layers of a dependable AI infrastructure stack: Graph layer: Track relationship changes and query historical graph state. Vector layer: Enforce tenant-aware retrieval and protect metadata. Observability layer: Maintain the monitoring stack and validate real deployment and alert scenarios. For self-hosted AI systems, these foundations matter just as much as model selection. Release links and project RagLeap is an open-source, self-hosted AI employee platform. Explore the source code, libraries, and documentation: GitHub: https://github.com/ragleap/ragleap-core Website: https://ragleap.com Documentation: https://docs.ragleap.com Package directory: https://packages.ragleap.com We welcome contributors interested in AI infrastructure, knowledge graphs, vector retrieval, observability, and security.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/ragleap/three-ragleap-releases-temporal-graphs-tenant-isolation-and-observability-improvements-977

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
