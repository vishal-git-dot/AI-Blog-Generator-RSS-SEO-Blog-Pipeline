---
title: "When AI-Generated Articles Fail, Keep the Body and Repair Only What Broke"
slug: "when-ai-generated-articles-fail-keep-the-body-and-repair-only-what-broke"
author: "yocho — Hikaru Sato"
source: "devto_ai"
published: "Mon, 14 Sep 2026 12:18:22 +0000"
description: "The dangerous failure in AI publishing is not that a model gets one request wrong. It is losing track of what already succeeded, what was charged, and what i..."
keywords: "title, not, body, source, what, failure, summary, can"
generated: "2026-09-14T12:21:57.414992"
---

# When AI-Generated Articles Fail, Keep the Body and Repair Only What Broke

## Overview

The dangerous failure in AI publishing is not that a model gets one request wrong. It is losing track of what already succeeded, what was charged, and what is safe to run again. While building YOCHO, an AI-industry intelligence service, we changed the editorial pipeline around that problem. The body, summary, and title are separate phases. A failed summary does not throw away a valid body. A bad title does not trigger a full rewrite. You can see the current product at https://yocho.ai . What I built The pipeline is intentionally boring: source snapshot -> body generation -> body checkpoint -> summary generation -> title validation or title-only repair -> final publication transaction Before a generated result is considered publishable, we store a private draft receipt tied to the call ID. It contains the source digest, response digest, phase, cost receipt, validation result, and any title correction. It does not contain API keys, HTTP headers, or an unbounded provider response. The checkpoint lets a later phase reuse the exact body instead of asking the model to recreate it. Why failure states need different treatment A known failure and an unknown failure are not the same thing. A known failure means that the provider response and its billing outcome are settled. If a summary fails validation in that state, we can retry only the summary once under the shared rate and cost controls. An unknown failure is a timeout, connection loss, or an unsettled billing result. We keep it on hold and do not automatically send the request again. The missing response might still exist on the provider side. Retrying blindly can create duplicate work and duplicate charges. This is less about being conservative for its own sake than about preserving a truthful state machine. A concrete example: the title is wrong, the body is fine Corporate disclosure pages are a useful stress case. A generated title may contain a number that is not in the source, an ambiguous company name, metadata such as a URL or JSON fragment, or an English source headline where a Japanese title is required. The safe response is not to regenerate the article. First, construct a source-grounded title from the retrieved issuer name and listing title, then run the same title validator again. If a Japanese title still needs model assistance, run a title-only phase against the stored body and source identity. In the September 14, 2026 bounded rescue, the fixed target was 95 tasks. Stored bodies were reused, and 43 earlier title substitutions were corrected while preserving the body and summary. That number is deliberately not presented as completion of the entire 3,356-task manifest. What I learned Checkpoints are more valuable than optimistic retries Without a checkpoint, every failure becomes a full regeneration. With one, the system can ask a smaller question: “Is the summary the only thing that needs work?” The final database transaction is part of the quality gate Provider-side validation is not enough. The publication transaction can still expose a stale source, a malformed title, or a mismatched identifier. The same contract must be applied again immediately before the status changes to published . Completion is not the same as an empty pending queue A queue with no pending items may still contain holds or in-flight work. We distinguish queue_empty from queue_drained , and we keep the oldest wait time and remaining budget visible. What is next The next question is not whether we can generate more articles. It is whether we can measure the complete path honestly: source freshness, time to publication, checkpoint reuse, known and unknown holds, confirmed cost, and the reasons final validation stopped a draft. That is the direction behind YOCHO: let AI extract, classify, and propose, while keeping the boundary where evidence becomes interpretation visible. The live project is at https://yocho.ai . This is an implementation and operations note as of September 14, 2026. It does not claim perfect factuality, search ranking, readership, or AI-answer inclusion.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/hikaru_sato_ce8ce2cff7c01/when-ai-generated-articles-fail-keep-the-body-and-repair-only-what-broke-1f51

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
