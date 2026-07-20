---
title: "Make Multipart Upload Abort Idempotent Before Orphaned Parts Start Billing You"
slug: "make-multipart-upload-abort-idempotent-before-orphaned-parts-start-billing-you"
author: "kongkong"
source: "devto_webdev"
published: "Mon, 20 Jul 2026 03:18:37 +0000"
description: "Multipart finalization is not the only retry boundary. Abort can succeed in object storage while the HTTP response is lost, leaving your database convinced t..."
keywords: "abort, upload, not, storage, state, aborted, await, multipart"
generated: "2026-07-20T03:39:19.784067"
---

# Make Multipart Upload Abort Idempotent Before Orphaned Parts Start Billing You

## Overview

Multipart finalization is not the only retry boundary. Abort can succeed in object storage while the HTTP response is lost, leaving your database convinced the upload is active. Model abort as a state transition, not a button wired directly to an SDK call: active → aborting → aborted └──→ cleanup_pending The endpoint should own an idempotency key and durable intent: await db . transaction ( async tx => { const upload = await tx . lockUpload ( uploadId ); if ( upload . state === " aborted " ) return ; await tx . markAborting ( uploadId , idempotencyKey ); await outbox . enqueue ( " abort-multipart " , { uploadId , storageKey }); }); A worker calls storage. If a retry receives NoSuchUpload , do not blindly fail: reconcile whether the upload was already completed, already aborted, or expired. Only the “already absent because abort succeeded” path may converge to aborted ; completion requires a separate terminal state. Test this sequence: Step Fault Required invariant persist abort intent process dies outbox resumes work storage abort succeeds response is lost retry does not reactivate upload duplicate message delivered twice one terminal state client retries same key same operation result cleanup scan stale active row reconcile before deleting Amazon S3’s AbortMultipartUpload API notes that in-progress part uploads may still succeed around an abort and recommends verifying that parts are gone. That makes a post-abort verification pass part of correctness, not optional housekeeping. Expose abort_requested_at , attempt count, last storage result, and remaining-part count. Alert on age in aborting , then run a lifecycle cleanup policy as a backstop—not as a substitute for application reconciliation.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/kongkong1/make-multipart-upload-abort-idempotent-before-orphaned-parts-start-billing-you-4gd7

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
