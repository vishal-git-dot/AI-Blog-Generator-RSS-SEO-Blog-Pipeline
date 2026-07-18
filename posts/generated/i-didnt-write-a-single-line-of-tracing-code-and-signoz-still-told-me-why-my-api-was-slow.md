---
title: "I Didn't Write a Single Line of Tracing Code, and SigNoz Still Told Me Why My API Was Slow"
slug: "i-didnt-write-a-single-line-of-tracing-code-and-signoz-still-told-me-why-my-api-was-slow"
author: "Abrar Ahmed"
source: "devto_ai"
published: "Sat, 18 Jul 2026 18:58:56 +0000"
description: "This article is my submission for the Agents of SigNoz Hackathon: Blog Track. I self-hosted SigNoz for the first time last night. I expected to spend the who..."
keywords: "signoz, docker, trace, app, api, what, didn, first"
generated: "2026-07-18T19:11:40.229203"
---

# I Didn't Write a Single Line of Tracing Code, and SigNoz Still Told Me Why My API Was Slow

## Overview

This article is my submission for the Agents of SigNoz Hackathon: Blog Track. I self-hosted SigNoz for the first time last night. I expected to spend the whole session fighting Docker. I did, but not with SigNoz. The actual "aha" moment came about ten minutes after I finally got things running, when I looked at my first trace and realized my API wasn't slow because of my code. It was slow because of TLS handshakes I didn't know were happening on every single request. Why I was doing this: I'm a freelance web developer, and most of what I build talks to third-party APIs — payment providers, data sources, whatever the client needs. I've always monitored these the crude way: console.log timestamps and vibes. I wanted to see what a real observability platform would actually show me, without spending a cent, so I self-hosted SigNoz and pointed a small Node app at it. Getting it running I installed SigNoz using Foundry, their new CLI installer, on Windows via WSL2: curl -fsSL https://get.docker.com | sh curl -fsSL https://signoz.io/foundry.sh | bash Then a minimal casting.yaml: apiVersion : v1alpha1 kind : Installation metadata : name : signoz spec : deployment : flavor : compose mode : docker And one command to deploy the whole stack SigNoz, ClickHouse, the OTel collector, all of it: foundryctl cast -f casting.yaml One real gotcha worth flagging if you're on Windows: don't run this through Docker Desktop's default WSL integration. ClickHouse Keeper segfaults under that virtualization layer. I installed native Docker Engine directly inside my WSL2 Ubuntu distro instead, and everything came up clean on the first try after that. For the demo app, I used SigNoz's own sample-nodejs-app, a small Express app with one route, /data, that hits three unrelated public APIs (a cat fact API, a random dog image API, and a joke API) and returns all three responses together. I picked it specifically because it makes multiple outbound calls per request I wanted to see what a real, slightly-more-than-trivial trace looked like. I pointed it at my local collector instead of SigNoz Cloud: environment : OTEL_TRACES_EXPORTER : " otlp" OTEL_EXPORTER_OTLP_ENDPOINT : " http://host.docker.internal:4318" OTEL_EXPORTER_OTLP_PROTOCOL : " http/protobuf" OTEL_SERVICE_NAME : " promptpulse-blog-demo" NODE_OPTIONS : " --require @opentelemetry/auto-instrumentations-node/register" extra_hosts : - " host.docker.internal:host-gateway" That extra_hosts line matters if you're on native Docker Engine rather than Docker Desktop host.docker.internal isn't resolved automatically outside of Desktop, so without it the app can't reach the collector at all. The important thing here: I added zero lines of tracing code. NODE_OPTIONS pulls in OpenTelemetry's auto-instrumentation package, which patches Node's built-in HTTP client at runtime. My actual route handler doesn't know or care that it's being observed. What the trace actually showed me: I hit /data about twenty times to build up some data, then opened the trace waterfall in SigNoz. Each request to /data produced 11 spans, not 1. The parent span was the incoming request (684ms total), and under it were three GET spans one for each external API each of which had its own tcp.connect and tls.connect child spans broken out automatically. That's when the actual number caught my eye. One of the three external calls took 643.99ms end to end. Its tls.connect child span alone was 366.39ms, 57% of that call's total time was spent just establishing the TLS handshake, before a single byte of the actual API response came back. Another call showed the same pattern: 675.67ms total, 374.98ms of it just tls.connect. I hadn't touched connection pooling or keep-alive anywhere in this demo app, and the trace made the consequence of that visible immediately, every request was opening a brand-new HTTPS connection from scratch. If this were a production endpoint under real load, that's the first thing I'd fix, and I wouldn't have known to look at it without seeing the span breakdown. Log timestamps would have told me "this call took 650ms," full stop. They wouldn't have told me why. What I'd tell my past self Auto-instrumentation is genuinely "no code" I was skeptical going in, since most "zero config" tooling ends up needing some config. This didn't. One NODE_OPTIONS env var and it caught every outbound HTTP call, including the low-level connection setup I didn't even think to look for. The Windows/WSL2 install gotcha (native Docker Engine, not Docker Desktop's integration) cost me more time than anything SigNoz-specific did. If you're on Windows, sort that out first. I went in expecting to evaluate "is this a good dashboard tool." I came out having found an actual, fixable performance issue in a demo app I didn't even write. That's a different (better) thing than a dashboard tool. What I'd do next: The obvious follow-up is adding connection reuse (keepAlive: true on the HTTP agent) and re-running the same trace to see the tls.connect spans shrink or disappear on subsequent requests. I didn't get to that tonight, but the trace already told me exactly what to try — which is the whole point. If you haven't self-hosted SigNoz and thrown a real app at it yet, the setup friction is genuinely lower than I expected, and the first trace waterfall is worth it on its own.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/abrar_ahmed_583e13ae94f75/i-didnt-write-a-single-line-of-tracing-code-and-signoz-still-told-me-why-my-api-was-slow-1bgl

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
