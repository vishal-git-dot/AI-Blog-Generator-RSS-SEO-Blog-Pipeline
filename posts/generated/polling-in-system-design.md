---
title: "Polling in System Design"
slug: "polling-in-system-design"
author: "Cibani Joe"
source: "devto_webdev"
published: "Mon, 22 Jun 2026 04:48:14 +0000"
description: "Polling in System Design... Polling is about repeatedly checking a resource eg. Server for new data or change in status of the device at a regular interval o..."
keywords: "polling, client, connection, ready, waiter, request, response, server"
generated: "2026-06-22T05:02:45.250343"
---

# Polling in System Design

## Overview

Polling in System Design... Polling is about repeatedly checking a resource eg. Server for new data or change in status of the device at a regular interval of time. Think of it like checking with the waiter, if our food is ready. The waiter can act in three different ways, which can explain the three different polling method. Short Polling Say the waiter, gets your request "Is my order ready?" and takes it to the chef. If the order isn't ready, the waiter would come back with no response. Again, you ask him at a constant interval of time, and this happens until you get your order. In the same way, in short polling, the client sends http request at a constant interval to the client, and the client responds to each of the request with the data if its ready or sends an empty string if the data is not ready. Long Polling Let's say the waiter, instead of returning with a null response when the chef says the food is not ready, stays next to the chef for a longer period to check on the food status. This is a depiction of long polling. In long polling the client sends for a request and waits and holds until the data is returned. Once the client receives the response, the client immediately sends the next request, thus creating a near real-time connection. It reduces unnecessary empty responses. Event Stream In this method, a constant connection is made between the client and the server. Which means a separate channel is forever active between the client and the server, and whenever an event occurs, the response is sent to the client through this port. This connection is established only once and doesn't close unless the client or server closes the established connection, or due to some network issue. Hence the response is triggered by events, and thus this form of polling is real-time. The major drawback of this form of connection is that a separate port is set aside for the connection and cannot be reused until the connection is closed. Choosing which form of polling technique to implement for your system, depends on the need and tradeoff you're willing to accept.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/cibani_joe/polling-in-system-design-ph6

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
