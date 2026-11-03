---
title: "The health check passed while every job failed"
slug: "the-health-check-passed-while-every-job-failed"
author: "Manh Liem"
source: "devto_webdev"
published: "Tue, 03 Nov 2026 22:59:23 +0000"
description: "I ran a paid red-team endpoint. The buyer page loaded, the form submitted, the job id came back 202 running, and the poll returned status: error every single..."
keywords: "check, every, job, one, endpoint, single, model, roster"
generated: "2026-11-03T23:03:46.606906"
---

# The health check passed while every job failed

## Overview

I ran a paid red-team endpoint. The buyer page loaded, the form submitted, the job id came back 202 running, and the poll returned status: error every single time. The error read model endpoint unreachable at http://127.0.0.1:10100/v1 . The model was not unreachable. The health check was asking the wrong question. What the probe did The worker's first action before running any probe was a liveness check on GET /v1/models. That route belonged to a local model proxy that also serves a hosted provider roster. Building that roster required a refresh token for a third-party account. That token had expired, so the roster endpoint answered 500 Internal Server Error. The liveness check treated any non-200 as model unreachable and returned before running a single probe. The route that actually does the work is a different one: POST /v1/chat/completions. That route is served by a provider router, not by the roster. It answered 200 with a real completion the whole time. I confirmed this by sending one request with max_tokens: 1 and reading the response body. So the system had a working inference path, a broken metadata path, and a gate that checked the metadata path. Every job failed at the gate. Why this is worse than a hard outage A hard outage is visible. A gate that fails on a healthy system is silent and self-consistent. The buyer page returned 200, which is true. The submit endpoint returned 202 running, which is true. The job status said error, which was true. The liveness check said 500, which was false. Every individual response was accurate. The composition was not. Nothing in the logs contradicted the other lines, so the failure produced no anomaly to alert on. The check that would have caught it Run the same call the product runs, at the smallest size that still proves the path: POST /v1/chat/completions with a single token. One token costs almost nothing and exercises the exact route the product depends on. A metadata endpoint can be down, renamed, rate limited, or gated behind an expired token without affecting a single real request. Probing it tells you about the roster, not about your product. The second gate After fixing the probe, I added a monitor that runs one real job end to end every two hours and requires status done plus a non-empty report. That is the only check that covers the whole chain: page serving, submit, queue, worker, model call, and report write. Any single component can be healthy while the chain is broken, and a chain check is the only one that sees it. The cost is one real job per two hours. The alternative cost was a full day of traffic to a page where every submission failed.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/llmrt/the-health-check-passed-while-every-job-failed-mfc

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
