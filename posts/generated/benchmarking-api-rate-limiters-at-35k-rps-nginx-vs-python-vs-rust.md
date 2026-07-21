---
title: "Benchmarking API Rate Limiters at 35k+ RPS: Nginx vs. Python vs. Rust"
slug: "benchmarking-api-rate-limiters-at-35k-rps-nginx-vs-python-vs-rust"
author: "__mr__"
source: "devto_python"
published: "Tue, 21 Jul 2026 18:35:52 +0000"
description: "Rate limiters are supposed to shield downstream services from traffic spikes. But what happens to the gateway itself when hit with tens of thousands of unaut..."
keywords: "rate, python, nginx, rust, limit, traffic, scenario, rps"
generated: "2026-07-21T19:39:11.836665"
---

# Benchmarking API Rate Limiters at 35k+ RPS: Nginx vs. Python vs. Rust

## Overview

Rate limiters are supposed to shield downstream services from traffic spikes. But what happens to the gateway itself when hit with tens of thousands of unauthorized requests per second? In this benchmark study, I evaluate an API Rate Limiter Gateway implemented across three distinct proxy engines: Nginx , Python (aiohttp) , and Rust (Axum/Tokio) . All three proxies enforce a Leaky Bucket algorithm variant to shield downstream Flask applications served by Gunicorn. The complete code, benchmark scripts, and Docker configurations are available on the GitHub repo . 1. System Architecture Overview The testing setup simulates a production cloud deployment using Docker Compose: Traffic Generator: wrk load-testing tool executing multi-threaded concurrent connections. Proxy Gateway Layer: Alternates between Nginx, Python, and Rust implementations. Downstream Services: Multi-worker Python Flask applications managed by Gunicorn. 2. Performance Comparison Load generation was running for 30 seconds using wrk with 2 threads and 100 persistent concurrent connections ( wrk -t2 -c100 -d30s --latency ). Resource utilization was sampled directly via the Docker API ( docker stats ). The benchmarks evaluate performance across three traffic profiles: Scenario 1 (Baseline / No Limit): All incoming requests are allowed through to the downstream Flask apps. Scenario 2 (High Rate-Limit): A moderate rate-limit threshold where the gateway rejects the majority of incoming traffic. Scenario 3 (Strict Rate-Limit): A highly restrictive rate-limit threshold triggering immediate rejection for nearly ~100% of incoming flood traffic. Scenario / Engine Avg Latency p99 Latency Throughput (RPS) Peak CPU % Peak RAM Non-2xx Ratio S1: Baseline (No Limit) Nginx 108.49ms 126.28ms 918.69 322.27% 20.25MiB 0.26% Python 128.88ms 170.39ms 773.15 105.58% 38.34MiB 0.00% Rust 64.29ms 85.24ms 1,547.96 882.31% 15.14MiB 0.00% S2: High Rate-Limit Nginx 1.77ms 4.50ms 1,220.85 35.17% 12.17MiB 97.85% Python 13.92ms 21.29ms 7,300.03 108.50% 28.40MiB 99.92% Rust 2.72ms 3.05ms 37,187.73 226.38% 10.60MiB 99.99% S3: Strict Rate-Limit Nginx 3.30ms 9.48ms 1,267.92 26.96% 10.86MiB 99.89% Python 13.21ms 20.01ms 7,568.54 103.06% 25.98MiB 100.00% Rust 2.75ms 3.18ms 36,538.96 228.07% 9.82MiB 100.00% 3. Architectural Insights & Bottlenecks Multi-Core Efficiency vs. The Thread Barrier Rust leverages a multi-threaded, work-stealing execution framework ( tokio ), allowing it to dynamically distribute network polling across all allocated host CPU threads (spiking to 882.31% CPU in Scenario 1 and 228.07% in Scenario 3). Conversely, Python relies on a single-threaded asynchronous loop constrained by the Global Interpreter Lock (GIL), capping compute scaling to roughly 105% CPU (one physical core) regardless of incoming pressure. Rate-Limit Short-Circuiting When active enforcement triggers in Scenarios 2 and 3, average processing latencies across all engines drop to low single digits. This occurs because the proxies reject unauthorized traffic in-memory via an immediate HTTP 429 response. This gateway short-circuiting bypasses downstream payload processing, Gunicorn socket allocation, and Flask app execution entirely, preventing resource saturation on the underlying services. Throttled Throughput Analysis The throughput variance in Scenarios 2 and 3 (~36,500+ RPS for Rust, ~7,500 RPS for Python, and ~1,200 RPS for Nginx) is determined by specific runtime boundaries under load. Python's throughput is capped by single-core execution due to the GIL. Nginx's performance drop stems from connection slot exhaustion ( worker_connections saturation) or socket allocation overhead under intense traffic spikes. Rust circumvents these limitations by utilizing a native, multi-threaded async runtime to evaluate in-memory limits and drop rejected sockets instantly across multiple CPU cores without garbage collection or worker slot starvation. 4. Final Thoughts This benchmark isn't a verdict on which proxy engine is "best". It highlights how different runtimes behave under active rate enforcement. Nginx remains one of the most reliable, deterministic reverse proxies in the industry for static assets, routing, and standard load balancing. However, when serving as an in-memory rate-limiting shield during extreme connection floods , its out-of-the-box worker pool limits can become a bottleneck unless fine-tuned for high-concurrency socket dropping.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/__mr__/benchmarking-api-rate-limiters-at-35k-rps-nginx-vs-python-vs-rust-3i5a

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
