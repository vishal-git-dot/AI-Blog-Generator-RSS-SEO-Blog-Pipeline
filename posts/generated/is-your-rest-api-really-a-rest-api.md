---
title: "Is Your REST API really a REST API?"
slug: "is-your-rest-api-really-a-rest-api"
author: "Daniel Possible Kwabi"
source: "devto_webdev"
published: "Thu, 20 Aug 2026 01:13:53 +0000"
description: "Before anything I want us to keep this name at the top of our heads, not forever but for now. LEONARD RICHARDSON . I know your question. Why? That's because ..."
keywords: "rest, server, api, not, but, your, level, client"
generated: "2026-08-20T01:35:46.538808"
---

# Is Your REST API really a REST API?

## Overview

Before anything I want us to keep this name at the top of our heads, not forever but for now. LEONARD RICHARDSON . I know your question. Why? That's because he gave us a practical measure of some sorts to measure how "RESTful" your API actually is, the Richardson Maturity Model (RMM). Essentially, it's like a grading system for APIs. From RPC-over-HTTP (Level 0) to hypermedia (Level 3). So let's not be so sure your API is RESTful, let's walk through some ground rules. The 6 REST Constraints Contrary to what a lot of novices think, it's not about slapping JSON on HTTP. REST is defined by six additional architectural constraints. 1. Client-Server Separation of concerns. The client (frontend) focuses on the UI and experience while the server (backend) handles data and security. And they evolve independently. 2. Uniform Interface The way I look to put this is that a "contract" should be established between client and server, in the sense that they are on the same page. Resources are identified by URLs ( /users/5 ), manipulated via standard HTTP methods (GET, POST, PUT, DELETE), and described with self-contained messages. This uniformity makes APIs predictable and interoperable. 3. Stateless The server should "remember" nothing between requests. All requests must carry all the information needed to process it. This makes scaling and reliability possible. 4. Cacheable Because we want to be stateless, things can get expensive real fast, so we cache. Resources must "say" whether they should be cached or not. So we keep data in some sort of volatile storage as opposed to persistent storage so we prevent the server from repeating identical work. 5. Layered Architecture As the name suggests, we should have different layers, e.g., a web tier, app tier, and DB tier. Clients don't really know if they are talking to the actual server or some form of intermediary — maybe a proxy, load balancer, or a gateway. This allows for scalability behind the scenes. 6. Code on Demand This is the only optional constraint, as in reality not every system would need this. Servers can extend client functionality by sending executable code. Again, this is rarely used but it's part of the family. RMM Good, we have looked at the 6 REST constraints. But how do we measure RESTfulness? Well, remember our name? It comes into play here again. We'll use the Leonard Richardson Maturity Model. Level Name What It Looks Like Problem / Limitation 0 The Swamp One single endpoint ( /api ) doing everything. RPC over HTTP. No real REST. Hard to scale, brittle. 1 Resources Multiple endpoints ( /users , /orders ). But still relies mostly on POST for all actions. Slightly better, but verbs are misused. 2 HTTP Verbs Proper use of GET, POST, PUT, DELETE. Most APIs stop here. Good practice, but still missing hypermedia. 3 Hypermedia (HATEOAS) Server responses include links that tell the client what actions are possible next. True REST. Flexible, evolvable, self-describing. At level 3, your API becomes truly navigable like a website. Instead of hardcoding routes, the client can follow links provided by the server. Which means backend can evolve without breaking the frontend. That's the point of REST in the first place... So, is your API really REST? If it's a level 2, I think you're in good company. Not so bad (most APIs are). But if we want to embrace the full REST vision, we should aim for level 3. Hypermedia is not just some fancy word, it's the key to building truly resilient, adaptable, and RESTful APIs. Peace!!!

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/daniel_possiblekwabi_b57/is-your-rest-api-really-a-rest-api-3bbj

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
