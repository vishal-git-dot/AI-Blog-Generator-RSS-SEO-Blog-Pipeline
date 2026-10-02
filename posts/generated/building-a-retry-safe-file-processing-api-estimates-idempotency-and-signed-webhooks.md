---
title: "Building a retry-safe file processing API: estimates, idempotency and signed webhooks"
slug: "building-a-retry-safe-file-processing-api-estimates-idempotency-and-signed-webhooks"
author: "Skavio"
source: "devto_python"
published: "Fri, 02 Oct 2026 11:14:18 +0000"
description: "The hard part of a processing API is usually not the first successful request. It is everything that happens after retries, timeouts, duplicate submissions, ..."
keywords: "skavio, api, https, processing, www, job, before, jobs"
generated: "2026-10-02T12:13:45.782411"
---

# Building a retry-safe file processing API: estimates, idempotency and signed webhooks

## Overview

The hard part of a processing API is usually not the first successful request. It is everything that happens after retries, timeouts, duplicate submissions, long-running jobs and cost surprises enter the picture. Skavio Processing API v1 uses one company-scoped job model for document extraction, PDF and image tools, media processing, transcription and meeting workflows. This post shows the integration pattern we use publicly: upload → estimate → cap cost → submit idempotently → poll or receive a signed webhook → download results . The endpoints The production base is: https://www.skavio.eu/v1 The public developer surface is available as: Developer docs: https://www.skavio.eu/api/docs/ OpenAPI 3.1: https://www.skavio.eu/api/openapi.json GitHub developer kit: https://github.com/skavio-eu/skavio-processing-api Postman docs: https://documenter.getpostman.com/view/58677341/2sBYHNWi4n A new company starts with 1,000 trial credits so the flow can be tested before topping up. 1. Upload once, then work with IDs Files are uploaded first with POST /v1/uploads . The returned upload ID is then referenced by estimates and jobs. That separation matters because the expensive operation can be retried without uploading the same source again. 2. Estimate before starting work Before submitting a job, send the intended payload to POST /v1/estimate . For example, document extraction can look like this in Python: payload = { " operation " : " flow-extract " , " upload_ids " : [ upload_id ], " fields " : [ " supplier " , " invoice_number " , " total " ], } quote = requests . post ( " https://www.skavio.eu/v1/estimate " , headers = headers , json = payload , timeout = 30 , ) quote . raise_for_status () payload [ " max_credits " ] = quote . json ()[ " estimated_credits " ] The important part is max_credits . It lets the client turn the quote into a hard ceiling. If the submission no longer fits that limit, the server can reject it instead of silently doing more expensive work. 3. Make submission retry-safe Network failures are normal. A client may submit a request, lose the response, and have no idea whether the server accepted it. Use a stable Idempotency-Key for the same business request: job_headers = { ** headers , " Idempotency-Key " : persisted_key , } job = requests . post ( " https://www.skavio.eu/v1/jobs " , headers = job_headers , json = payload , timeout = 30 , ) job . raise_for_status () job_id = job . json ()[ " id " ] Persist the idempotency key before submitting. Reuse it only for the same request. If the payload changes intentionally, generate a new key. This prevents a timeout retry from creating a second job or a second charge. 4. Treat processing as asynchronous Jobs move through a small lifecycle: queued → processing → completed ↘ failed For simple integrations, polling GET /v1/jobs/{job_id} every few seconds is enough. For production workflows, signed webhooks avoid keeping workers blocked. Verify the signature against the raw request body , reject stale timestamps, and durably deduplicate the event ID before doing side effects. The public Python verifier uses: expected = " v1= " + hmac . new ( secret . encode (), timestamp . encode () + b " . " + raw_body , hashlib . sha256 , ). hexdigest () valid = hmac . compare_digest ( expected , signature ) Webhook delivery is at-least-once, so signature verification and event deduplication solve different problems. You need both. 5. Download only through authenticated result paths Completed jobs return result metadata with authenticated download paths. Do not construct arbitrary storage URLs in client code. The public quickstart validates that the returned path starts with the expected job route before downloading it with the same bearer authentication. Sources and results currently have a seven-day retention window, so durable business records should be copied to your own storage after successful processing. What the same API can process The current v1 surface includes: document extraction with selected fields and review signals PDF merge, split, page operations, compression, watermarking, protection and OCR image resize, crop, rotation, compression, conversion and OCR audio/video conversion, trimming and compression transcription meeting transcription with speaker-aware processing Exact operation names, live limits and current credit rates are exposed by GET /v1/capabilities . Try it without guessing the contract The repository contains runnable Python and Node.js examples, a webhook verifier, a synthetic sample document and a Postman collection. The hosted OpenAPI document is the source of truth for the current HTTP contract. Useful starting points: GitHub: https://github.com/skavio-eu/skavio-processing-api Postman: https://documenter.getpostman.com/view/58677341/2sBYHNWi4n Developer docs: https://www.skavio.eu/api/docs/ OpenAPI: https://www.skavio.eu/api/openapi.json Product/API page: https://www.skavio.eu/api/ The developer kit is public. The processing service itself is hosted and uses company-scoped authentication and a prepaid credit wallet. If you build against it, the safest default is simple: estimate first, cap the cost, persist the idempotency key, and verify webhooks before acting on them.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/skavioeu/building-a-retry-safe-file-processing-api-estimates-idempotency-and-signed-webhooks-32p6

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
