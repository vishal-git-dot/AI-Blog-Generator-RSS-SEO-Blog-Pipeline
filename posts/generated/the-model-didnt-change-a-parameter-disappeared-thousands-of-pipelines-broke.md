---
title: "The Model Didn't Change. A Parameter Disappeared. Thousands of Pipelines Broke."
slug: "the-model-didnt-change-a-parameter-disappeared-thousands-of-pipelines-broke"
author: "Vinicius Fagundes"
source: "devto_python"
published: "Wed, 22 Jul 2026 03:00:00 +0000"
description: "An LLM vendor dropped two sampling parameters this month. Every hard-coded call that passed them started throwing errors. The model was fine. The weights wer..."
keywords: "one, model, vendor, you, your, call, not, llm"
generated: "2026-07-22T03:17:44.188842"
---

# The Model Didn't Change. A Parameter Disappeared. Thousands of Pipelines Broke.

## Overview

An LLM vendor dropped two sampling parameters this month. Every hard-coded call that passed them started throwing errors. The model was fine. The weights were fine. The contract changed — and thousands of pipelines discovered they never had one. Here's the uncomfortable symmetry. You pin your packages. You contract-test your APIs. You'd never let a payment provider change a request schema under you without a canary catching it. But the LLM call — the one sitting in the middle of your most visible feature — is a raw dict of kwargs assembled by hand, validated by nothing, tested against production only. Your LLM is a dependency too. Treat it like one. Three habits, all boring: 1. One choke point, not forty call sites # llm_client.py — the ONLY file in the repo that talks to the vendor. PINNED_MODEL = " vendor-model-2026-06-01 " # dated snapshot, never "latest" def build_request ( prompt : str , max_tokens : int = 1024 ) -> dict : return { " model " : PINNED_MODEL , " max_tokens " : max_tokens , " messages " : [{ " role " : " user " , " content " : prompt }], # sampling params live HERE and nowhere else — # when the vendor drops one, you change one line, not forty call sites " temperature " : 0.2 , } When the parameter vanished, teams with a choke point shipped a one-line fix. Teams with kwargs scattered across forty files spent the day grepping. 2. A contract test that fails in CI, not in production # test_llm_contract.py — runs on every deploy and on a nightly schedule import jsonschema from llm_client import build_request REQUEST_SCHEMA = { " type " : " object " , " required " : [ " model " , " max_tokens " , " messages " ], " properties " : { " model " : { " const " : " vendor-model-2026-06-01 " }, " temperature " : { " type " : " number " , " minimum " : 0 , " maximum " : 1 }, }, " additionalProperties " : True , } def test_request_matches_contract (): jsonschema . validate ( build_request ( " ping " ), REQUEST_SCHEMA ) def test_canary_call_against_live_api ( client ): """ The nightly canary: one real call. If the vendor drops a param, THIS fails at 3am in CI — not at 9am in your product. """ resp = client . messages . create ( ** build_request ( " Reply with the word: ok " )) assert resp . content [ 0 ]. text . strip (). lower (). startswith ( " ok " ) $ pytest test_llm_contract.py -q .. [100%] 2 passed in 1.84s 3. Pin the snapshot, schedule the upgrade "latest" in a model string is the same lie as >= in a requirements file: it means "surprise me in production." Pin the dated snapshot, and make upgrading a deliberate event — run the golden evals against the new snapshot, diff the outputs, then move the pin. On your calendar, not the vendor's. None of this is new engineering. It's the same discipline you already apply to every other dependency — the only novelty is admitting the LLM is one. I'm Vinicius Fagundes — principal data engineer, independent consultant, and MBA lecturer in São Paulo. I write about data pipelines and the practices that keep them boring, through vf-insights.com .

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/fagundesv/the-model-didnt-change-a-parameter-disappeared-thousands-of-pipelines-broke-4k4o

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
