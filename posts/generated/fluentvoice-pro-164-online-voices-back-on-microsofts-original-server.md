---
title: "FluentVoice Pro 1.6.4: online voices back on Microsoft's original server"
slug: "fluentvoice-pro-164-online-voices-back-on-microsofts-original-server"
author: "Nick Otmazgin"
source: "devto_python"
published: "Thu, 15 Oct 2026 20:14:50 +0000"
description: "FluentVoice Pro 1.6.4 is out: the Microsoft online voices are back on their original server. In October 2026 Microsoft's classic voice server started refusin..."
keywords: "microsoft, fluentvoice, pro, server, edge, tts, https, online"
generated: "2026-10-15T21:09:19.876535"
---

# FluentVoice Pro 1.6.4: online voices back on Microsoft's original server

## Overview

FluentVoice Pro 1.6.4 is out: the Microsoft online voices are back on their original server. In October 2026 Microsoft's classic voice server started refusing connections (HTTP 403) for every app built on edge-tts ( edge-tts #490 ). FluentVoice 1.6.3 worked around that by switching to Microsoft's newer server. Upstream edge-tts 7.3.0 / 7.3.1 fixed the outage, so 1.6.4 requires edge-tts 7.3.1 and reads from the classic server again. The 1.6.3 failover stays as a safety net. Also new: if Microsoft briefly limits requests after many readings (HTTP 429), Test providers now says so in plain words and suggests waiting a minute or using an offline voice. GitHub release: https://github.com/nickotmazgin/fluentvoice-pro/releases/tag/v1.6.4 Discussion: https://github.com/nickotmazgin/fluentvoice-pro/discussions/72 Microsoft Store: https://apps.microsoft.com/detail/9N293MJ0MD9F (1.6.4 is in certification) Scoop: scoop update fluentvoicepro Earlier write-up for the 1.6.3 health check and failover: https://dev.to/nickotmazgin/fluentvoice-pro-163-the-microsoft-online-voices-work-again-plus-a-health-check-that-says-what-2bfh Some AI assistance was used while preparing this post.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/nickotmazgin/fluentvoice-pro-164-online-voices-back-on-microsofts-original-server-2nld

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
