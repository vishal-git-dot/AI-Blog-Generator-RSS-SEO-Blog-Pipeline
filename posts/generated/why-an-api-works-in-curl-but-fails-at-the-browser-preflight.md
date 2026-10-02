---
title: "Why an API works in curl but fails at the browser preflight"
slug: "why-an-api-works-in-curl-but-fails-at-the-browser-preflight"
author: "Arthur031221"
source: "devto_ai"
published: "Fri, 02 Oct 2026 12:07:01 +0000"
description: "I have seen a request work in curl and fail before the browser sends the same POST. The difference can be an OPTIONS preflight. The browser asks whether the ..."
keywords: "request, browser, origin, preflight, options, headers, post, names"
generated: "2026-10-02T12:13:45.784528"
---

# Why an API works in curl but fails at the browser preflight

## Overview

I have seen a request work in curl and fail before the browser sends the same POST. The difference can be an OPTIONS preflight. The browser asks whether the origin, method, and request headers are allowed. If the server responds with 401 or omits one of the required headers, the application request never goes out. I built corswhy to inspect that exchange from a terminal. It takes the URL of the API, the page origin, the intended method, and names from the browser's Access-Control-Request-Headers field. It sends OPTIONS with those details and prints one row for each check. The command does not send the POST, request body, or credentials. Here is the command used in the local fixture: node bin/corswhy.js http://127.0.0.1:18765/auth \ --origin http://localhost:5173 \ --method POST \ --header authorization,content-type The failing endpoint returns 401 to OPTIONS. The report names the status failure first and suggests letting OPTIONS reach the CORS handler without authentication. The second endpoint answers with a 204 response and the required allowed origin and header names, so its report passes. The repository tests also assert that the server sees OPTIONS and never sees POST. There are a few details that matter when reading the output. A GET, HEAD, or POST with no unsafe request headers usually does not require a preflight. In that case corswhy sends nothing and says so. The header names passed with --header should be the names a browser includes in Access-Control-Request-Headers. If cookies will accompany the real cross origin request, use --credentials include ; the allowed origin must then match the page origin and the preflight must allow credentials. A green report is limited to the OPTIONS exchange. It does not test the actual response or browser cookie policy. It also does not model private network access, service workers, or extensions. This scope is useful when the observed failure is specifically the preflight, but it should not be read as a full browser verdict. The source, local fixture, and test suite are at https://github.com/Arthur031221/corswhy . I would like reports of preflight responses that the command explains incorrectly, with any private headers removed first.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/arthur031221/why-an-api-works-in-curl-but-fails-at-the-browser-preflight-3lb1

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
