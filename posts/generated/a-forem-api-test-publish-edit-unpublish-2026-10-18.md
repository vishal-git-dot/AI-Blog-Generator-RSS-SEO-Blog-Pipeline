---
title: "A Forem API test: publish, edit, unpublish (2026-10-18)"
slug: "a-forem-api-test-publish-edit-unpublish-2026-10-18"
author: "StarPresence"
source: "devto_webdev"
published: "Sun, 18 Oct 2026 15:36:33 +0000"
description: "This is a short test note about the Forem API v1. It was drafted with AI assistance and checked by a person before it was published. What this post checks An..."
keywords: "api, forem, test, published, post, draft, edit, article"
generated: "2026-10-18T15:40:21.692225"
---

# A Forem API test: publish, edit, unpublish (2026-10-18)

## Overview

This is a short test note about the Forem API v1. It was drafted with AI assistance and checked by a person before it was published. What this post checks An article can be created as a draft, edited, published and set back to draft through the API with the author's own key. A minimal request curl -X POST https://dev.to/api/articles \ -H "api-key: $DEV_API_KEY " \ -H "accept: application/vnd.forem.api-v1+json" \ -H "content-type: application/json" \ -d '{"article":{"title":"Hello","body_markdown":"Hello","published":false}}' The post is set back to draft after the test. This paragraph was added by an edit made through the API.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/starpresence/a-forem-api-test-publish-edit-unpublish-2026-10-18-3p0

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
