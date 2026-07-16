---
title: "I built a CLI to catch broken UTM parameters before they wreck your analytics"
slug: "i-built-a-cli-to-catch-broken-utm-parameters-before-they-wreck-your-analytics"
author: "Assmira Lahcen"
source: "devto_ai"
published: "Thu, 16 Jul 2026 19:12:38 +0000"
description: "One mistyped utm_medium — Email instead of email — splits one marketing channel into two rows in every dashboard downstream. It's a tiny bug that's easy to m..."
keywords: "urldn, utm, validator, https, com, result, console, log"
generated: "2026-07-16T19:20:26.288266"
---

# I built a CLI to catch broken UTM parameters before they wreck your analytics

## Overview

One mistyped utm_medium — Email instead of email — splits one marketing channel into two rows in every dashboard downstream. It's a tiny bug that's easy to miss when you're pasting links by hand into Google Ads, Mailchimp, or a social scheduler. I built urldn-utm-validator to catch it before the link goes out. Install npx urldn-utm-validator "https://yoursite.com?utm_source=fb&utm_medium=cpc&utm_campaign=q3" What it catches Missing required params ( utm_source , utm_medium , utm_campaign ) Duplicate keys in the query string Inconsistent casing ( Facebook vs facebook — these count as two separate channels in most analytics tools) Unencoded spaces Non-standard utm_medium values, as a soft nudge It scores the URL 0-100 and prints plain-English fixes instead of just flagging the problem. Node API import { validateUtm } from " urldn-utm-validator " ; const result = validateUtm ( " https://example.com?utm_source=fb&utm_medium=cpc&utm_campaign=q3 " ); console . log ( result . score ); // 100 console . log ( result . valid ); // true console . log ( result . issues ); // [] Also works with --json for CI pipelines, and --strict if you want warnings to fail the build too, not just hard errors. Repo: https://github.com/urldn/urldn-utm-validator npm: https://www.npmjs.com/package/urldn-utm-validator I maintain this alongside URLdn , a link shortener with an AI layer that reads your click data directly and answers questions about it in plain English — this validator is the free standalone piece of that same problem.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/lahcenassmira/i-built-a-cli-to-catch-broken-utm-parameters-before-they-wreck-your-analytics-3049

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
