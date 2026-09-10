---
title: "Test the Scope of Your Concurrency Limit"
slug: "test-the-scope-of-your-concurrency-limit"
author: "joinwell52"
source: "devto_python"
published: "Thu, 10 Sep 2026 03:30:08 +0000"
description: "Test the Scope of Your Concurrency Limit Two event loops can each respect a concurrency limit of one while running two tasks in total. Our controlled AG2 exp..."
keywords: "loop, two, one, not, peak, limit, its, tasks"
generated: "2026-09-10T04:04:27.714253"
---

# Test the Scope of Your Concurrency Limit

## Overview

Test the Scope of Your Concurrency Limit Two event loops can each respect a concurrency limit of one while running two tasks in total. Our controlled AG2 experiment separates that valid local behavior from a real cache-replacement defect that let one loop admit too many tasks. The distinction changes the assertion a resource-budget test needs. Adapted from the complete English research article . Reproducing the actual defect AG2 is an open-source framework for building and coordinating Agents. PR #3243 changes the semaphore cache used when admitting subtasks. A semaphore supplies a limited number of slots: later coroutines wait when all slots are occupied, and a completed task releases its slot. The earlier method stored one semaphore and its owning event loop on the Agent. When another loop arrived, it replaced the cached semaphore. Threads alternating between loops could keep replacing that reference while earlier tasks still occupied older semaphores. We pinned the base and head source and executed the original _spawn_subtask method. The subtask body was a waiting counter, not a model call. Rather than relying on random scheduling, we arranged an explicit interleaving: A1 enters on loop A and holds a slot. B1 enters on loop B in another real OS thread. While both remain active, A requests A2. We record local and aggregate peaks, then release the tasks. On the old method, A2 obtained a newly created slot. Loop A now had two active subtasks and the experiment had three overall. This violates even the narrower per-loop interpretation of a limit of one. Which peak becomes one after the fix? The proposed implementation keeps a semaphore for each running event loop and protects lookup and creation with a thread lock. B no longer replaces A's entry. Under the same interleaving, A2 waits for A1 to release its slot. Revision and execution shape Loop A peak Loop B peak Aggregate peak Base, one loop 1 0 1 Base, two loops 2 1 3 Proposed head, one loop 1 0 1 Proposed head, two loops 1 1 2 We ran each configuration five times per round, across two rounds: forty controlled trials with identical outcomes and no exceptions. Recording both local and aggregate peaks makes the result precise. The proposed method repaired the per-loop limit; two loops still ran two subtasks in aggregate. These are in-flight synthetic waiting subtasks, not measurements of model requests, throughput or cost. The upstream regression test explicitly targets the per-loop contract. An aggregate peak of two should therefore not be called a failed fix. It identifies a different guarantee that this patch does not provide. Turn the number into an acceptance contract A limit intended to protect a real resource needs at least four definitions. The first is its scope : loop, Agent, process, host or tenant. The second is its admission authority : which object or service can issue slots, and whether all relevant executors share it. The third is its lifetime : what task completion, process exit, lease expiry or manual cleanup means for an occupied slot. The fourth is its uncertainty policy : losing sight of an old task does not establish that the resource it held is free. A user may select one to prevent two expensive tasks from using the same account simultaneously. A correct semaphore in each loop could still fail to satisfy that product requirement. Conversely, a product deliberately promising one task per loop should not silently impose cross-domain serialization in the name of safety and remove intended parallelism. The design starts with the contract, followed by the appropriate lock, shared counter or lease. A lock around creation protects that operation. It does not automatically turn separate counters into a shared resource budget. What this experiment establishes We did not run a complete AG2 Agent, toolchain or model service, and did not test multiple processes, hosts or tenants. Initialization was a version-matched fixture; the admission method itself came from pinned upstream source. The PR remained open at the time of our inspection. The useful acceptance question is therefore not only “did the peak exceed the cap?” It is also “within which domain did we count that peak?” Without that domain, the limit is difficult both to implement and to review fairly. A review you can apply Add separate assertions for each loop's peak and the aggregate peak. Choose which one represents the product contract before deciding whether two concurrent tasks are a defect. Full English edition · 中文版本 · Methods and saved observations Research repository

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/joinwell52/test-the-scope-of-your-concurrency-limit-52bi

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
