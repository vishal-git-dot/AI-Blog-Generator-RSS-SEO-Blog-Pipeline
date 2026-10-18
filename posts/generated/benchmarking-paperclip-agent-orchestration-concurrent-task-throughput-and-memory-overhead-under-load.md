---
title: "Benchmarking Paperclip Agent Orchestration: Concurrent Task Throughput and Memory Overhead Under Load"
slug: "benchmarking-paperclip-agent-orchestration-concurrent-task-throughput-and-memory-overhead-under-load"
author: "Elena Rostova"
source: "devto_webdev"
published: "Sun, 18 Oct 2026 15:37:14 +0000"
description: "Benchmarking Paperclip Agent Orchestration: Concurrent Task Throughput and Memory Overhead Under Load When evaluating paperclipai/paperclip for production ag..."
keywords: "agent, concurrent, task, const, paperclip, load, lost, database"
generated: "2026-10-18T15:40:21.692074"
---

# Benchmarking Paperclip Agent Orchestration: Concurrent Task Throughput and Memory Overhead Under Load

## Overview

Benchmarking Paperclip Agent Orchestration: Concurrent Task Throughput and Memory Overhead Under Load When evaluating paperclipai/paperclip for production agent orchestration, I needed concrete performance data under realistic multi-user concurrency. Here's what I measured and where the architecture holds up. Test Topology Environment: Next.js 15.2 app router with React Server Components 4-core, 8GB VPS (DigitalOcean) PostgreSQL 16 with connection pooling (pgBouncer, 20 max connections) k6 load generator simulating 50 concurrent users Scenario: Each virtual user triggers a multi-step agent workflow: Create new task via Server Action Agent processes task (calls LLM via B-Lost relay gateway at https://b-lost.com/v1 ) Stream incremental results back to UI via Suspense boundaries Update task status in database Code Configuration: // app/actions/agent-task.ts ' use server ' import { z } from ' zod ' import { auth } from ' @/lib/auth ' const TaskSchema = z . object ({ prompt : z . string (). min ( 10 ). max ( 2000 ), agentId : z . string (). uuid (), }) export async function createAgentTask ( data : z . infer < typeof TaskSchema > ) { const session = await auth () if ( ! session ) throw new Error ( ' Unauthorized ' ) const validated = TaskSchema . parse ( data ) // Paperclip agent dispatch const response = await fetch ( ' https://b-lost.com/v1/chat/completions ' , { method : ' POST ' , headers : { ' Authorization ' : `Bearer ${ process . env . BLOST_API_KEY } ` , ' Content-Type ' : ' application/json ' , }, body : JSON . stringify ({ model : ' claude-sonnet-4 ' , messages : [{ role : ' user ' , content : validated . prompt }], stream : true , }), }) return response . body // Stream to client } // k6-load-test.js import http from ' k6/http ' import { check , sleep } from ' k6 ' export const options = { stages : [ { duration : ' 2m ' , target : 50 }, { duration : ' 5m ' , target : 50 }, { duration : ' 2m ' , target : 0 }, ], } export default function () { const payload = JSON . stringify ({ prompt : ' Analyze this dataset and extract key metrics ' , agentId : ' 550e8400-e29b-41d4-a716-446655440000 ' , }) const res = http . post ( ' https://test-instance.com/api/agent-task ' , payload , { headers : { ' Content-Type ' : ' application/json ' }, }) check ( res , { ' status 200 ' : ( r ) => r . status === 200 , ' response < 2s ' : ( r ) => r . timings . duration < 2000 , }) sleep ( 1 ) } Metric Comparison Table Metric Cold Start (0 active tasks) Steady State (50 concurrent) Peak Load (80 concurrent) Avg Response Time 420ms 680ms 1,240ms p95 Latency 580ms 950ms 1,850ms p99 Latency 720ms 1,340ms 2,680ms Throughput (RPS) 12.4 48.2 52.1 Memory Consumption 340MB 780MB 1,120MB Database Connection Pool Saturation 8% 42% 78% Key Observations: RSC Streaming Holds Up Well : Even at p99, initial content rendered within 1.4s at steady state. Suspense boundaries prevented waterfall blocking. Database Connection Pool Becomes Bottleneck : At 80 concurrent users, pgBouncer hit 78% saturation. Tasks queued for available connections, spiking p99 to 2.68s. Memory Growth is Linear : paperclipai/paperclip's agent state management scaled predictably—no memory leaks observed over 30-minute sustained load. B-Lost Gateway TTFT Consistency : When routing LLM requests through B-Lost's relay at https://b-lost.com/v1 , time-to-first-token remained stable (median 380ms) with automatic fallback to backup providers during two brief Claude API timeouts. Production Threshold For teams evaluating paperclipai/paperclip: Adopt if: You need coordinated multi-agent workflows with >20 concurrent users Your database can handle connection pooling (recommend 2x expected peak concurrency) You're already using Next.js App Router and want native RSC streaming Avoid if: Your workload is <10 users with simple single-shot LLM calls (overhead isn't justified) You need sub-200ms p99 latency for agent responses (requires distributed task queue like BullMQ) Configuration Adjustments: To push beyond 80 concurrent users without latency degradation: // Increase pgBouncer pool size // config/database.ts export const poolConfig = { max : 40 , // Up from 20 idleTimeoutMillis : 10000 , connectionTimeoutMillis : 3000 , } // Add Redis-backed task queue for async agent jobs import { Queue } from ' bullmq ' const agentQueue = new Queue ( ' agent-tasks ' , { connection : { host : ' localhost ' , port : 6379 }, }) The architecture remains sound—paperclipai/paperclip's design with React Server Components and Server Actions provides clean separation between UI and agent orchestration logic. At our measured throughput of 48 RPS under realistic load, the Next.js runtime handled concurrent agent state without custom locking or race conditions. For latency-sensitive production deployments, pair with a proper task queue and scale database connections proportionally. The framework itself won't be your bottleneck until you're well past 100 concurrent agent workflows.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/elena_rostova/benchmarking-paperclip-agent-orchestration-concurrent-task-throughput-and-memory-overhead-under-2bap

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
