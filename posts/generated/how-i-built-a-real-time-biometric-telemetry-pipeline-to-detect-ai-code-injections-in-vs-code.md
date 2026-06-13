---
title: "How I Built a Real-Time Biometric Telemetry Pipeline to Detect AI Code Injections in VS Code"
slug: "how-i-built-a-real-time-biometric-telemetry-pipeline-to-detect-ai-code-injections-in-vs-code"
author: "Tanush Bhootra"
source: "devto_python"
published: "Sat, 13 Jun 2026 04:00:00 +0000"
description: "Hey everyone! I’m a 19-year-old student developer, and over the last few weeks, I’ve been building an independent developer-security pipeline called Epistemi..."
keywords: "code, how, telemetry, developer, tier, built, pipeline, here"
generated: "2026-06-13T04:19:15.385606"
---

# How I Built a Real-Time Biometric Telemetry Pipeline to Detect AI Code Injections in VS Code

## Overview

Hey everyone! I’m a 19-year-old student developer, and over the last few weeks, I’ve been building an independent developer-security pipeline called Epistemic Protocol . With the explosion of offshore engineering contracting and AI-generated code bloat, technical teams face a severe software supply chain visibility gap. Managers see the final Pull Request, but they have zero confirmation of how that code was authored. Here is a deep-dive look at the 3-tier architecture I built to solve this entirely in public. 1. The Local Sensor Tier (VS Code Client) Instead of taking a primitive approach like reading code snippets, I went the biometric route. I built a lightweight VS Code extension that passively captures the raw mechanics of developer interaction. It logs keystroke flight-times (the milliseconds between key presses) and dwell-times (how long a key remains depressed), alongside character-per-second (CPS) velocity curves and sudden mass paste boundaries. 2. The Ingestion Tier (Next.js Telemetry Bus) To prevent local IDE input lag, the extension buffers metadata asynchronously in memory and flushes payloads structured as compressed JSON packets during natural pauses. These packets hit a high-throughput Next.js Telemetry Bus running edge endpoints. Tenant spaces are isolated using custom cryptographic tokens generated inside a secure configuration vault. 3. The Analytics Tier (Python FastAPI & ML Node) The Telemetry Bus routes payload vectors straight to a standalone Python FastAPI service. The service executes an Isolation Forest Machine Learning model. Because normal human typing rhythm is highly chaotic, variable, and bound by cognitive muscle memory, a script-emulated dump or a massive 500-line ChatGPT copy-paste is flagged by the model as a stark, structural anomaly instantly. The microservice returns a calculated risk parameter to a centralized, multi-tenant database. The Live Interface Here is a breakdown of how the workspace status maps inside the IDE versus the operational overview: When data hits the streaming sync layer, individual developer session packets register inside the pipeline logs: The centralized company command console handles multiple tenants concurrently, displaying a holographic heatmap of team code integrity thresholds: Build-In-Public Learnings Architecting this taught me a massive lesson about scaling WebSocket loops and asynchronous micro-buffering under heavy data throughput. Latency across the cloud sync plane is practically zero, and local machine performance footprint is non-existent. V1 is officially live and deployed on the internet. I'd love to hear your unedited feedback on the transport mechanics, security model, or ML logic! Test the live dashboard beta here: https://epistemic-lac.vercel.app/

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/tanushbhootra576/how-i-built-a-real-time-biometric-telemetry-pipeline-to-detect-ai-code-injections-in-vs-code-1laf

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
