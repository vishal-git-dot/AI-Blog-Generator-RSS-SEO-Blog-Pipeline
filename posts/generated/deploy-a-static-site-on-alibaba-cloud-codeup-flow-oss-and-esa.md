---
title: "Deploy a Static Site on Alibaba Cloud: Codeup, Flow, OSS and ESA"
slug: "deploy-a-static-site-on-alibaba-cloud-codeup-flow-oss-and-esa"
author: "weiyi"
source: "devto_webdev"
published: "Mon, 02 Nov 2026 05:20:41 +0000"
description: "Once an article is written, the release process should deliver it reliably to readers. Build, upload, refresh and verification need distinct steps so you can..."
keywords: "content, refresh, search, static, flow, oss, esa, article"
generated: "2026-11-02T05:25:25.627129"
---

# Deploy a Static Site on Alibaba Cloud: Codeup, Flow, OSS and ESA

## Overview

Once an article is written, the release process should deliver it reliably to readers. Build, upload, refresh and verification need distinct steps so you can see where a failure occurred. A clear release path This project currently builds and publishes through local commands, uploads static output to OSS and serves it through ESA. Codeup and Flow configuration templates are ready, but the actual repository and cloud pipeline are not connected yet. When configuring Flow later, reuse these steps: Install dependencies from the lockfile with npm ci. Run npm run build to check types and generate pages. Upload static assets first, then publish HTML and Sitemap. Refresh ESA caches and verify that public content matches the build. Notify search engines and save successful submission state. Treat different content differently in the cache Content-hashed assets can be cached for a long time. HTML and Sitemap benefit from revalidation and a refresh after publication so readers don't receive stale content. Cache refresh is asynchronous. Verify that public pages return the new content before submitting URLs, reducing the chance that a search service sees an old page or error response. Make failures recoverable A multi-file OSS upload isn't atomic. If it fails midway, rerunning can complete the missing parts. Search notifications save successful batches, leaving only pending content for a later attempt. A platform accepting a request does not mean an article is indexed. Check website publication and search notifications separately. See the project's deployment documentation for configuration and maintenance details. This article was prepared for DEV with AI assistance.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/weiyi/deploy-a-static-site-on-alibaba-cloud-codeup-flow-oss-and-esa-4o53

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
