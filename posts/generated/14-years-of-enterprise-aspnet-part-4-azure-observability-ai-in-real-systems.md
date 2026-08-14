---
title: "14 Years of Enterprise ASP.NET, Part 4: Azure, Observability & AI in Real Systems"
slug: "14-years-of-enterprise-aspnet-part-4-azure-observability-ai-in-real-systems"
author: "kirandeepjassal-crypto"
source: "devto_ai"
published: "Fri, 14 Aug 2026 18:40:21 +0000"
description: "Originally published at prepstack.co.in Part 4 of 4 — 14 Years of Enterprise ASP.NET (finale). Where the system actually runs: choosing Azure architecture by..."
keywords: "you, net, part, enterprise, azure, system, grounded, context"
generated: "2026-08-14T19:00:48.694534"
---

# 14 Years of Enterprise ASP.NET, Part 4: Azure, Observability & AI in Real Systems

## Overview

Originally published at prepstack.co.in Part 4 of 4 — 14 Years of Enterprise ASP.NET (finale). Where the system actually runs: choosing Azure architecture by cost and scaling profile, making the system observable, and treating AI as a real architectural component — not a demo. Running example: Mattrx — .NET 9 / ASP.NET Core, 110k MAU, Azure SQL, ~3,200 req/sec peak. Lesson 10 — Azure: match the platform to the workload Pick the compute by your scaling and operational profile, then right-size — don't default to the biggest box or the trendiest platform. Most enterprise .NET runs perfectly on Azure App Service; you reach for Container Apps or AKS when you have a specific reason, not because Kubernetes is on your résumé. The decision framework: App Service for standard web/API (default), Container Apps when you want containers + scale-to-zero without running a cluster, AKS only when you genuinely need its control plane and have the ops capacity. A 5-person team has no business running Kubernetes. Over-provisioning is the most common and most invisible cloud waste — it never pages anyone, so nobody fixes it. Right-sizing the web tier (P2v3×6 always-on → P1v3×2 + autoscale), moving to managed Redis, and tuning the SQL tier saved roughly $2,000/month total — with better peak headroom, because autoscale handles the month-end burst the fixed fleet was over-sized for. Lesson 11 — Observability is essential For years I "had logging" and was still blind in production. The shift from logging to observability — answering new questions about a running system without shipping new code — is the difference between a 4-minute incident and a 4-hour one. You can't fix what you can't see, and you can't see what you didn't instrument. Three pillars, tied by a correlation ID: logs (what happened), metrics (how much/how often), traces (where the time went). // structured fields + a correlation scope so every line in the request is linkable using ( logger . BeginScope ( new Dictionary < string , object > { [ "CorrelationId" ] = correlationId })) { logger . LogInformation ( "Fetched {Count} campaigns for {TenantId} in {Ms}ms" , count , tenantId , sw . ElapsedMilliseconds ); } // OpenTelemetry: traces + metrics out of the box, exported to App Insights builder . Services . AddOpenTelemetry () . WithTracing ( t => t . AddAspNetCoreInstrumentation (). AddSqlClientInstrumentation ()) . WithMetrics ( m => m . AddAspNetCoreInstrumentation (). AddRuntimeInstrumentation ()) . UseAzureMonitor (); This took mean-time-to-diagnose a production incident from ~35 minutes to ~4 — you jump straight to the failing span instead of grepping by timestamp and hoping. Lesson 12 — AI is part of enterprise architecture now AI stopped being a side experiment and became a component — with the same rigor as any dependency. Treat an LLM like an untrusted, probabilistic service: wrap it, ground it, validate its output, measure it. Three distinct shapes, NOT interchangeable: RAG (answer from your docs, grounded + cited), agentic (tools + reasoning loop), classical ML (ML.NET for churn/forecast — no LLM needed). // AFTER — retrieve context, ground the prompt, validate the output, measure it public async Task < HelpAnswer > AskAsync ( string question , CancellationToken ct ) { var context = await search . RetrieveAsync ( question , topK : 5 , ct ); // ground in OUR docs if ( context . Count == 0 ) return HelpAnswer . NoAnswer ( "I don't have docs on that." ); // refuse, don't hallucinate var prompt = Prompt . Grounded ( question , context ); var raw = await llm . CompleteAsync ( prompt , ct ); var answer = Guardrails . Validate ( raw , context ); // citations + safety metrics . RecordAiCall ( tokens : raw . Usage , grounded : true ); // cost + quality tracking return answer ; } The grounded RAG help system deflects ~520 support tickets/month — but only because it's grounded and has a refuse-path; the naive ungrounded version hallucinated answers that created tickets. Classical-ML predictions run in-process via ML.NET at ~3 ms with no LLM cost at all. The thread through the whole series Fourteen years, twelve lessons, one theme: enterprise software rewards restraint and fundamentals over novelty. Clean boundaries (Part 1), a data layer that respects the database (Part 2), ceilings removed and architecture split only when warranted (Part 3), and infrastructure sized to reality with eyes-on observability and AI treated as an engineered component (Part 4). None of it is flashy. All of it is what keeps a system alive — and a team shipping — past year five. That's all four parts. Full finale with every before/after, the diagrams, and the numbers — and Parts 1–3 — on PrepStack .

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/kirandeepjassalcrypto/14-years-of-enterprise-aspnet-part-4-azure-observability-ai-in-real-systems-36da

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
