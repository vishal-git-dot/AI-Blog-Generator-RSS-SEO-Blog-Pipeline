---
title: "Building an AI project estimator with prices the model cannot invent"
slug: "building-an-ai-project-estimator-with-prices-the-model-cannot-invent"
author: "Edward Amirain"
source: "devto_webdev"
published: "Thu, 01 Oct 2026 04:58:03 +0000"
description: "When I built Project Blueprint at Vaynerov Technologies, I kept pricing outside the language model. Blueprint starts with a product description and proposes ..."
keywords: "model, what, blueprint, pricing, product, when, useful, calculation"
generated: "2026-10-01T05:13:42.621834"
---

# Building an AI project estimator with prices the model cannot invent

## Overview

When I built Project Blueprint at Vaynerov Technologies, I kept pricing outside the language model. Blueprint starts with a product description and proposes an architecture, a delivery plan and a team. Those are useful inputs to a project conversation. The price range comes from a separate calculation engine, using the same rules as our pricing page. That separation shapes the whole feature: what the model may return, how its output is checked, what the browser can submit and what the server will store. This is an adaptation of my original build story , focused on that boundary. Give the model a bounded vocabulary The model proposes selections from the pricing catalog: platforms, features and other scope choices. Before pricing runs, a sanitizer checks those selections. Unknown identifiers are removed, and required single-choice fields receive defaults if they are missing. The catalog in the prompt, the schema’s allowed values and the sanitizer’s allowlist all come from the same rules object. That avoids three independently maintained definitions of what the product supports. The flow is straightforward: Product description → Proposed architecture and scope → Validated, sanitized selections → Calculation engine → Estimate The model influences the proposed scope, so this does not make the estimate independent of model output. It makes that influence explicit and inspectable. Reviewing the selected features remains part of reviewing the estimate. That distinction is useful in any AI feature that feeds a business process. A constrained selection can still be a poor recommendation. Validation tells you whether an input is permitted; it does not settle whether the recommendation suits the user. Check more than the JSON shape Blueprint uses structured output, then validates and sanitizes the parsed result. The graph sanitizer removes duplicate identifiers, self-loops and edges that point to missing nodes. It also repairs phase references so the diagram remains coherent. A response can be valid JSON and still describe an unusable graph. The application needs checks that reflect what its renderer and downstream functions actually require. For a different product, those checks might cover valid references between records, supported combinations of options or bounds on a generated plan. The useful question is: what assumptions will the next function make about this data? Recalculate when the result becomes a record When a visitor requests a quote, the server validates the request, sanitizes the selections and calculates the estimate again. Numbers supplied by the browser are ignored. This gives the stored quote an authoritative calculation point. Browser state is convenient for an interactive preview, but it should not define the value that becomes a business record. The same review question applies to discounts, entitlements and usage charges: where does a displayed suggestion become an authoritative value, and which component is allowed to make that decision? Keep the fallback consistent Blueprint also has hand-authored reference blueprints for use when generation is unavailable. Their estimates still run through the calculation engine. That makes the fallback useful for exploring the product’s planning and pricing behavior. It also keeps an example from establishing a different set of expectations than the full flow. You can explore Blueprint and its reference plans , or read the full implementation story for the surrounding transport, validation and rendering decisions. Where do you draw the boundary between a model’s recommendation and your application’s authority to act on it?

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/edwardamirain/building-an-ai-project-estimator-with-prices-the-model-cannot-invent-53o9

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
