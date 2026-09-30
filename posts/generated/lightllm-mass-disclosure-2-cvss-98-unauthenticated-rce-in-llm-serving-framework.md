---
title: "LightLLM Mass Disclosure — 2 CVSS 9.8 Unauthenticated RCE in LLM Serving Framework"
slug: "lightllm-mass-disclosure-2-cvss-98-unauthenticated-rce-in-llm-serving-framework"
author: "threataft"
source: "devto_python"
published: "Wed, 30 Sep 2026 04:20:16 +0000"
description: "Two unauthenticated CVSS 9.8 RCEs in LightLLM — the LLM serving framework used with LLaMA, Mistral, and Qwen deployments. No patch confirmed. All versions th..."
keywords: "cve, rce, pickle, rpyc, service, lightllm, cvss, unauthenticated"
generated: "2026-09-30T04:59:51.110457"
---

# LightLLM Mass Disclosure — 2 CVSS 9.8 Unauthenticated RCE in LLM Serving Framework

## Overview

Two unauthenticated CVSS 9.8 RCEs in LightLLM — the LLM serving framework used with LLaMA, Mistral, and Qwen deployments. No patch confirmed. All versions through 1.2.0 are affected. The CVEs CVE CVSS Type Vector CVE-2026-103040 9.8 Pickle deserialization RCE Router profiler RPyC service CVE-2026-103041 9.8 Pickle deserialization RCE Embed cache RPyC service CVE-2026-103042 7.5 Memory exhaustion DoS NCCL control channel What happened Both RCE flaws share the same root cause: unauthenticated RPyC services passing untrusted input directly to pickle.loads() . Python's pickle module executes arbitrary code on deserialization — no authentication, no validation, full RCE with service privileges. CVE-2026-103040 only fires when --enable_profiling is set. If you don't need profiling, that flag should never be on in production. CVE-2026-103041 affects multimodal deployments. The embed cache RPyC service is exposed on all interfaces by default. CVE-2026-103042 lets unauthenticated attackers call exposed_set_value on the NCCL control channel without size limits, growing the KV-transfer worker's memory until the node crashes. Why this hits hard in production A compromised LightLLM node exposes every user prompt, model weight, and API key the service processes. These aren't dev tools — they're inference servers running in production AI stacks. The pickle deserialization pattern is well-understood and preventable. It shouldn't be appearing in frameworks deployed at this scale. What to do now Don't enable --enable_profiling in production — removes CVE-2026-103040 attack surface entirely Firewall the RPyC ports — profiler and embed cache services should never be internet-exposed Restrict --pd_trans_mode nccl — NCCL control channel to trusted nodes only Apply memory limits — cgroups or container resource quotas to cap exhaustion impact Watch for patches — no fix confirmed yet for 1.2.0 Full technical breakdown with CVSS vectors, CWE classifications, and full mitigation checklist: LightLLM Mass Disclosure — CVE-2026-103040, CVE-2026-103041, CVE-2026-103042 Originally published at ThreatAft

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/threataft_dev/lightllm-mass-disclosure-2-x-cvss-98-unauthenticated-rce-in-llm-serving-framework-4ob0

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
