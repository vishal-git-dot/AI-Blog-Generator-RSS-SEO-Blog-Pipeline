---
title: "The LiteLLM incident check you shouldn't run with Python — and the scanner I built for it"
slug: "the-litellm-incident-check-you-shouldnt-run-with-python-and-the-scanner-i-built-for-it"
author: "XM Yang"
source: "devto_python"
published: "Wed, 28 Oct 2026 12:19:27 +0000"
description: "On Oct 21, 2026, LiteLLM disclosed that its v1.107.0 release had been compromised and published to PyPI, Docker Hub, and GHCR before being contained. The par..."
keywords: "litellm, check, deepseek, not, files, you, pip, file"
generated: "2026-10-28T12:28:53.741841"
---

# The LiteLLM incident check you shouldn't run with Python — and the scanner I built for it

## Overview

On Oct 21, 2026, LiteLLM disclosed that its v1.107.0 release had been compromised and published to PyPI, Docker Hub, and GHCR before being contained. The part of the official response steps that stuck with me: in an affected environment, any Python start re-runs the implant . So the vendor tells you not to begin with pip install or pip show on a suspect box. The first-pass checks are file and metadata checks, done from the shell, by hand: - Is litellm pinned to exactly 1.107.0 anywhere — or does the version spec admit 1.107.0 (unpinned, >= , ~= , ^ )? - What did the lockfiles actually resolve to? - Do any Dockerfiles or compose files reference the compromised tags ( v1.107.0 , latest , main-latest ) or the published bad image digest? - Is there a litellm-1.107.0.dist-info in any virtualenv on the box? - Are the implant marker files there — cook.pth , cook.py , remote_code_loader.lock ? Doing that by hand across a few projects and a folder of virtualenvs is exactly the kind of boring, error-prone pass a small tool should do. So I built one. ## litellm-check bash pip install litellm-check litellm-check scan ~/src/my-service Zero third-party dependencies, Python 3.11+. It reads files and package metadata only — it never executes Python (or pip) inside a scanned environment, which is the whole point: the check itself must be safe to run on a suspect machine, ideally with a clean interpreter. A few design choices worth noting: Specs are evaluated, not grepped. A pin of exactly 1.107.0 is critical. A spec that admits it is high — exposure surface, not proof of installation, because whether it actually resolved to 1.107.0 depends on installs inside the announced windows (PyPI 11:39:51–13:23 UTC on Oct 21; Docker Hub until 14:20 UTC; GHCR until 13:51 UTC). A spec that excludes it is reported as info, so a reviewer can see the coverage instead of a silent pass. Every rule traces to the announcement. The 13 rules (LL-001–LL-013) are derived solely from LiteLLM's official incident post — no third-party IOC lists. Each finding in the report carries the file:line evidence, the incident basis, and the remediation (delete the implant files from the shell, kill the daemon holding the lock file, rebuild pinned to litellm==1.106.2 , rotate reachable secrets, check CloudTrail). The limits are printed on every report. A clean scan means "none of the known indicators were found in this tree" — nothing more. Environments rebuilt after exposure, images pulled without any definition file, installs recorded only in CI logs: none of that leaves anything for a file scanner to find. The tool collects evidence; it does not certify anything. The repo ships a deliberately exposed demo project; scanning it produces 16 findings (10 critical, 4 high, 2 info) so you can see the report shape before pointing it at anything real: https://github.com/dylanXM/litellm-check ## The sibling tool: DeepSeek Exposure Scan Same rules-as-data engine shape, different problem. DHS Exclusion and Removal Order #2026-01 (published in the Federal Register on Oct 20) directs federal civilian agencies to remove DeepSeek products — including third-party products built using DeepSeek implementations — and FAR 52.204-30 flows that down to contractors, who now get asked by customers: what model components are inside what you ship? deepseek-scan ( https://github.com/dylanXM/deepseek-scanner ) does the first evidence pass for that question: hosted API endpoints, SDK imports, model ids, dependency manifests and lockfiles, container model pulls, and local weight files — written up as a Markdown or AI-BOM-style JSON report, with the same honesty about what it cannot detect (a renamed, distilled model leaves no textual trace). bash pip install deepseek-scanner Both tools were recently reviewed and merged into the awesome-ai-security-tools list (in its watchlist section — they're new, and the maintainer is right that adoption signals come first). If you try either one, the feedback I value most is false positives and missing rules: both rule sets are single JSON files, so a new detection is a data change, not a code change. Disclosure: I'm the author of both tools. They're Apache-2.0 and not affiliated with BerriAI/LiteLLM or DeepSeek.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/xmyang0223/the-litellm-incident-check-you-shouldnt-run-with-python-and-the-scanner-i-built-for-it-5gc6

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
