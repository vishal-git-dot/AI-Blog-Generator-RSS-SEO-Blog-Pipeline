---
title: "I Ran One Codex Task for 31 Hours. It Survived Restarts and Built an Auditable Textbook Pipeline"
slug: "i-ran-one-codex-task-for-31-hours-it-survived-restarts-and-built-an-auditable-textbook-pipeline"
author: "kfinds"
source: "devto_ai"
published: "Wed, 23 Sep 2026 04:07:03 +0000"
description: "A 31-hour AI run sounds like a stunt. The useful result was not the clock. It was continuity . I used one parent Codex task on Windows (GPT-5.6 Sol) to turn ..."
keywords: "not, one, task, recorded, artifact, what, long, codex"
generated: "2026-09-23T04:13:47.928102"
---

# I Ran One Codex Task for 31 Hours. It Survived Restarts and Built an Auditable Textbook Pipeline

## Overview

A 31-hour AI run sounds like a stunt. The useful result was not the clock. It was continuity . I used one parent Codex task on Windows (GPT-5.6 Sol) to turn an original mathematical framework into a versioned teaching package. During the recorded work cycle, I did not steer the content step by step. My interventions were mainly continuation or restart instructions, plus one read-only recovery request. The application and computer were restarted. The task resumed from verified artifact state instead of reconstructing prior work from a plausible-sounding narrative. What the task produced The final package was not one generated document. It was a coupled artifact graph: source/master, student, and teacher chapter variants; conventional hand-work exercises and a separate AI-assisted exercise track; worked answers with graded difficulty; five deterministic exercise and data generators; reproducibility scripts, manifests, hashes, audit reports, and restart checkpoints. The AI-assisted exercises are part of the curriculum, not an appendix about prompting. Students must use an AI system to generate, inspect, test, or audit mathematical objects under explicit rules. Recorded snapshot Item Recorded value Parent-task duration More than 31 hours Recovered local session log Approximately 338.55 MiB Context-compression events 47 Associated records 21,991 One recorded UI checkpoint 512 changed files (+84,401 / -720 lines) Deterministic generators 5 Audit milestones 67/67 experiment checks; 36/36 student-teacher cross-checks Deterministic reruns 100,000 events; 250,000 events; separate 5,000,000-row validation These figures come from recovered local execution records and artifact audits. The 512-file figure is one recorded checkpoint, not a claimed final total. What appeared to make it work Seven decisions mattered more than clever prompting: Project state lived in versioned artifacts , not only in chat memory. Definitions and authority boundaries were frozen before execution. Acceptance criteria and invariants were explicit. Deterministic generators turned qualitative requirements into executable checks. Student and teacher outputs were checked independently. Negative results and rejected paths were preserved. Resumption began from verified artifacts , not from a guess about earlier progress. The unexpected result was that Codex's most valuable contribution was not prose generation. It converted a research and teaching design into an inspectable production system: textbook material, executable generators, solutions, audits, and provenance working together. The human/AI boundary I retained authority over: definitions; admissible transformations; research direction; acceptance criteria. Codex handled long-horizon construction, implementation, verification, auditing, and documentation. That separation mattered. A long-running agent is not reliable merely because it keeps going. It becomes useful when the project can tell the agent what it is allowed to change, what must remain invariant, and how completion will be checked. What failed The weakest product-level component was observability . Very long histories were difficult to navigate and export as one official report. After a restart, much of the client-visible history disappeared even though local session data and produced artifacts remained recoverable. Native export of checkpoints, token composition, file manifests, and audit events would make cases like this much easier to validate. What I am not claiming This is a sanitized, auditable case study—not a benchmark and not a claim that Codex is universally error-free. I do not claim "zero errors." The evidence package preserves the first disclosed draft and identifies known limitations instead of silently replacing it with a polished retrospective version. The foundational corpus and full internal research protocol are intentionally withheld. The public deposit contains client-visible execution evidence and produced artifacts, not private chain-of-thought. Public evidence Full technical discussion on GitHub Sanitized, timestamped evidence and Chapter 1 artifacts — Zenodo DOI 10.5281/zenodo.22900578 Questions for builders Has anyone documented a comparable personally operated, single-parent-task workflow with restart/resume continuity and artifact-level auditing? Which artifact schemas or checkpoint conventions have worked best for reliable long-horizon resumption? Which native telemetry or export features would make cases like this easier to validate? If you are building long-horizon agent workflows, the central question may not be how long the model can keep talking. It may be whether the work can survive memory loss without losing its identity. AI disclosure: This post was adapted with AI assistance from an artifact-backed case report. The recorded facts were checked against the linked public evidence package.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/kfinds/i-ran-one-codex-task-for-31-hours-it-survived-restarts-and-built-an-auditable-textbook-pipeline-4l3o

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
