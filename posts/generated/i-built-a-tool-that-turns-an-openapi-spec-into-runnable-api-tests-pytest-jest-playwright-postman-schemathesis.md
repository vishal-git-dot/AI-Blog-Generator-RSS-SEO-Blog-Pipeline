---
title: "I built a tool that turns an OpenAPI spec into runnable API tests (pytest, Jest, Playwright, Postman, Schemathesis)"
slug: "i-built-a-tool-that-turns-an-openapi-spec-into-runnable-api-tests-pytest-jest-playwright-postman-schemathesis"
author: "ITFabers"
source: "devto_python"
published: "Mon, 03 Aug 2026 09:38:01 +0000"
description: "If you keep an OpenAPI spec around, you already have most of what you need to test the API — the spec says what every endpoint takes and returns. But turning..."
keywords: "spec, what, api, tests, postman, you, actually, openapi"
generated: "2026-08-03T09:55:50.591632"
---

# I built a tool that turns an OpenAPI spec into runnable API tests (pytest, Jest, Playwright, Postman, Schemathesis)

## Overview

If you keep an OpenAPI spec around, you already have most of what you need to test the API — the spec says what every endpoint takes and returns. But turning that into an actual test suite is the boring part nobody wants to hand-write, so it usually doesn't get written. I built apitestgen to close that gap: paste an OpenAPI spec (or a Postman collection, or point it at a spec URL), and it generates runnable API tests. What it actually generates pytest (+ conftest.py ) — Python Jest — JS/TS Playwright — API tests, not just browser Postman collection — runnable with newman Schemathesis — property-based fuzzing off the same spec The tests don't just assert 200 . They validate the response body against the schema in the spec — via jsonschema (pytest), ajv (Jest), and Postman's jsonSchema — with $ref resolution so nested/reused schemas actually get checked (and a guard against circular refs). A couple of things I cared about Multi-environment CI. The generated GitHub Actions workflow runs the suite as a matrix across environments, each with its own API_BASE_URL_<ENV> secret — so staging vs prod isn't a copy-paste job. Fetch-by-URL is SSRF-guarded. Importing a spec by URL blocks private / loopback / link-local / metadata IPs and refuses redirects, so it can't be pointed at internal infra. Honest status This is new and I'm running it solo — no "trusted by 10,000 teams" line here, because that wouldn't be true. The free tier gives 5 generations/day (log in with GitHub), which is enough to see whether the output is actually usable for your API. Paid unlocks unlimited + the CI workflow export. What I'd genuinely like: point it at a spec you actually use and tell me where the generated tests are wrong or too shallow. Schema-validation edge cases and auth flows are where I most expect gaps, and that feedback is what decides what I build next. → apitestgen.dev

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/itfabers/i-built-a-tool-that-turns-an-openapi-spec-into-runnable-api-tests-pytest-jest-playwright-4p2

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
