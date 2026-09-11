---
title: "Serverless: When It Helps and When It Hurts"
slug: "serverless-when-it-helps-and-when-it-hurts"
author: "Cloud Frontier"
source: "devto_webdev"
published: "Fri, 11 Sep 2026 16:01:29 +0000"
description: "I have shipped serverless functions that handled millions of requests for pennies, and I have watched a serverless architecture quietly bankrupt a team's vel..."
keywords: "serverless, you, not, when, latency, spiky, event, traffic"
generated: "2026-09-11T16:13:33.442095"
---

# Serverless: When It Helps and When It Hurts

## Overview

I have shipped serverless functions that handled millions of requests for pennies, and I have watched a serverless architecture quietly bankrupt a team's velocity. The technology is not good or bad. It is a fit problem. Here is how I decide. Where serverless wins The model shines when your workload is spiky, event-driven, and stateless . A few patterns I keep coming back to: Webhooks and integrations. A Stripe webhook, a GitHub hook, a Slack slash command. Low volume, unpredictable timing, and you do not want a server idling for it. Scheduled jobs. A cron that runs every 15 minutes to sync data. You pay for the seconds it runs, not the 24 hours it sits idle. Glue code. Resize an image after upload, fan out a message, write to a queue. Small units of work with clear inputs and outputs. Unpredictable traffic. A marketing launch or a viral post. The platform scales to zero and back without you provisioning anything. A minimal handler is genuinely small: export const handler = async ( event ) => { const { orderId } = JSON . parse ( event . body ); await processOrder ( orderId ); return { statusCode : 200 , body : JSON . stringify ({ ok : true }) }; }; No servers, no Dockerfile, no load balancer. For the right job, that is a real win. Where serverless hurts The pain shows up in three places: latency, state, and cost at scale. Cold starts. A function that has not run recently pays an initialization tax. For a user-facing request in a latency-sensitive path, a 500ms cold start is a 500ms tax on a real person. If your traffic is steady, you are paying that tax for no reason. State is awkward. Serverless wants stateless. The moment you need a connection pool, a WebSocket, an in-memory cache, or a long-running process, you fight the platform. Database connections are the classic trap: // Anti-pattern: new connection per invocation const db = new Pool ({ connectionString : process . env . DATABASE_URL }); export const handler = async () => { return db . query ( ' select 1 ' ); }; Under load this exhausts the database's connection limit fast. You end up adding a proxy layer like RDS Proxy or PgBouncer, which is fine, but it is complexity you took on to use serverless. Cost flips. At low volume, per-request pricing is unbeatable. At high, steady volume, a small always-on container is often cheaper and faster. Do the math with your own numbers instead of trusting a blog post (including this one). Local dev and debugging. Replicating the platform locally is doable but never identical. Distributed tracing across a dozen functions is a skill you have to build. A decision checklist I ask these before committing: Is the workload spiky or steady? Spiky favors serverless. Does it need to stay warm or hold state? If yes, lean toward containers. What is the p99 latency budget? Cold starts eat into it. What does it cost at 10x current traffic? Model it. How hard is it to debug when it breaks at 3am? If most answers point to short, stateless, event-driven work, go serverless. If they point to long-lived connections, steady high throughput, or tight latency, a container or a plain VM will make you happier. The honest summary Serverless is a deployment model, not a religion. I reach for it for glue, webhooks, and spiky traffic. I reach for containers when I need warm processes, predictable latency, or persistent connections. The teams that struggle are usually the ones that picked one and forced everything through it. Pick per workload, not per ideology. Measure, then decide.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/cloudfrontier/serverless-when-it-helps-and-when-it-hurts-j1b

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
