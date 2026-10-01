---
title: "A long-lived stream is not a standing permission grant"
slug: "a-long-lived-stream-is-not-a-standing-permission-grant"
author: "Auth By Example"
source: "devto_webdev"
published: "Thu, 01 Oct 2026 05:07:43 +0000"
description: "SSE and WebSocket handlers often authorize once when the connection opens, then push events for minutes or hours. That first check is not a standing grant. W..."
keywords: "stream, not, when, subject, standing, permission, grant, authorize"
generated: "2026-10-01T05:13:42.619841"
---

# A long-lived stream is not a standing permission grant

## Overview

SSE and WebSocket handlers often authorize once when the connection opens, then push events for minutes or hours. That first check is not a standing grant. While the stream is open, membership can be revoked, a role narrowed, or the resource moved out of the subject's scope. If you only gate the handshake, later events can leak data the subject is no longer allowed to see. Re-authorize before sensitive payloads leave the server—on a short interval, on each privileged event type, or when the subject's session/membership version changes. Close the stream when the check fails. A connection lifetime is not a permission lifetime. Authorization still belongs at the moment of access.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/authbyexample1/a-long-lived-stream-is-not-a-standing-permission-grant-1201

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
