---
title: "Why approval in an automated pipeline should expire"
slug: "why-approval-in-an-automated-pipeline-should-expire"
author: "Cadence by NoxyTree"
source: "devto_python"
published: "Sat, 18 Jul 2026 07:29:23 +0000"
description: "A file can be approved and still become unsafe five seconds later. The failure mode is simple: A human reviews a file. The workflow stores approved = true . ..."
keywords: "approval, fingerprint, content, approved, path, str, file, not"
generated: "2026-07-18T08:00:40.324146"
---

# Why approval in an automated pipeline should expire

## Overview

A file can be approved and still become unsafe five seconds later. The failure mode is simple: A human reviews a file. The workflow stores approved = true . Someone edits one sentence. The filename is unchanged. Downstream automation continues from content nobody approved. The approval belongs to a version of the content, not to the filename. A tiny dependency-free approach Use a SHA-256 fingerprint of the reviewed bytes: from hashlib import sha256 from pathlib import Path def fingerprint ( path : str ) -> str : return sha256 ( Path ( path ). read_bytes ()). hexdigest () When the reviewer approves the file, store that fingerprint. Before dependent work runs, compare the current fingerprint with the approved one: def approval_state ( path : str , approved_hash : str | None ) -> str : if approved_hash is None : return " waiting_for_approval " if fingerprint ( path ) != approved_hash : return " stale " return " approved " That gives the pipeline an honest rule: no recorded fingerprint → waiting for approval fingerprint matches → approved fingerprint changed → stale, block downstream work Why modification time is not enough Modification times help find potentially stale outputs, but they are not proof of reviewed content. Files can be copied, restored, or touched without a meaningful content change. A content fingerprint binds the approval to the exact bytes a human reviewed. The wider workflow rule The same principle applies to source notes, claims, scene plans, asset manifests, and release checklists. Each approval should name: the file or manifest the content fingerprint who or what recorded the approval the timestamp the downstream stages that depend on it When content changes, reopen the gate. Do not silently carry approval forward. Try it in 3 KB I extracted the core idea into a dependency-free Python sample: https://noxytree.github.io/cadence-starter/downloads/cadence-approval-sample.zip Try: python cadence_sample.py approve script.md # edit script.md python cadence_sample.py status script.md The second command reports the approval as stale. A larger local implementation I also packaged the local engine I use around this idea—dependency state, next-safe-action resolution, dry-run-first execution, tests, schemas, and templates—as Cadence Starter . The complete source download is a paid product, currently $29. For launch day, this link applies 30% off until midnight: https://ko-fi.com/noxytree/link/FIRSTSALE The free sample above is enough to inspect and reuse the core fingerprinting pattern. It carries an MIT license. The full package is a separate paid source download. Neither one requires Claude, an OpenAI account, a hosted service, or a subscription. How do you bind human approval to changing local files: hashes, signed manifests, commit SHAs, or something else?

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/cadencestarter/why-approval-in-an-automated-pipeline-should-expire-19ef

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
