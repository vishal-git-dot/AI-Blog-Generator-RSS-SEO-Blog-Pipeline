---
title: "Building Cabree: Architectural Decisions for Sub-Second Taxi Dispatching"
slug: "building-cabree-architectural-decisions-for-sub-second-taxi-dispatching"
author: "Calvinburns"
source: "devto_webdev"
published: "Fri, 28 Aug 2026 10:46:08 +0000"
description: "Building real-time logistics software requires balancing instant job allocation with low operational latency across high-concurrency mobile clients. We built..."
keywords: "real, time, high, state, cabree, sub, job, allocation"
generated: "2026-08-28T10:48:56.457673"
---

# Building Cabree: Architectural Decisions for Sub-Second Taxi Dispatching

## Overview

Building real-time logistics software requires balancing instant job allocation with low operational latency across high-concurrency mobile clients. We built Cabree , a cloud-native cab dispatch system designed to give taxi operators and private hire fleets a fast alternative to legacy software. Here is a breakdown of our core tech stack, architectural choices, and the technical challenges we solved. Key Tech Stack Backend Engine: Microservices architecture deployed via isolated Docker containers. Geospatial Processing: PostgreSQL with the PostGIS extension for dynamic boundary matching, zone prioritization, and spatial queries. Real-Time Layer: Redis pub/sub and WebSocket streams for low-latency GPS tracking and live dispatch wallboard state sync. Mobile Clients: Cross-platform mobile applications optimized for efficient background location tracking without draining driver device batteries. Core Engineering Challenges 1. Sub-Second Auto-Allocation Engine Job assignment requires evaluating multiple dynamic variables in real time—driver proximity, traffic conditions, zone queues, and priority rules. By using spatial indexing ($R$-Tree / GiST) paired with cached Redis driver states, we reduced allocation calculations to under two seconds. 2. Managing High-Frequency Telemetry Pings Active drivers continuously stream location updates. Writing every raw GPS ping directly to primary persistent storage causes severe database $I/O$ bottlenecks. We routed high-frequency location updates into a fast in-memory Redis layer, writing persistent snapshots to PostgreSQL only during active job state changes or trip completions. 3. Zero-Downtime State Synchronization Operators, drivers, and passengers require real-time visibility without reliance on constant API polling. Implementing persistent bidirectional WebSockets keeps network overhead minimal while delivering immediate UI state sync across all active endpoints. Explore the platform live at cabree.co.uk . How do you handle high-throughput geospatial streams or real-time event distribution in your applications? Let's discuss in the comments below!

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/calvinburns/building-cabree-architectural-decisions-for-sub-second-taxi-dispatching-40fa

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
