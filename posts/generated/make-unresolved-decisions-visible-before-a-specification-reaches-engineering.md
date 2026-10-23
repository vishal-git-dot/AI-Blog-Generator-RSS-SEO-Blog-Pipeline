---
title: "Make Unresolved Decisions Visible Before a Specification Reaches Engineering"
slug: "make-unresolved-decisions-visible-before-a-specification-reaches-engineering"
author: "Anuj Sadani"
source: "devto_python"
published: "Fri, 23 Oct 2026 16:18:36 +0000"
description: "A specification can look complete while containing two limits for the same field and an unanswered question about who may approve an action. A reviewer might..."
keywords: "findings, not, decision, specification, review, spec, check, decisions"
generated: "2026-10-23T16:48:37.613132"
---

# Make Unresolved Decisions Visible Before a Specification Reaches Engineering

## Overview

A specification can look complete while containing two limits for the same field and an unanswered question about who may approve an action. A reviewer might notice both, but the next revision can make it hard to tell which findings were discussed and which still apply. Spec Sentry explores a narrow approach: annotate the facts that need mechanical checks, then keep review decisions in a separate ledger. This is most useful when a team is willing to make important uncertainty explicit. The checker does not promise to find every contradiction in ordinary prose. Declare the parts that must agree The fixture contains these declarations: @quantity preview.max_size = 10 MB @quantity preview.max_size = 10 GB @decision sharing-policy | pending | Who may invite guests? Both quantities use the same key but declare conflicting values or units. The pending decision makes an unanswered product question visible instead of leaving an engineer to invent a default. Term references can also be explicit: The initial preview uses [[term:external collaborator]]. @define workspace: A named product collaboration area. The undefined external collaborator reference becomes a finding. A definition for a different term does not resolve it. These directives use a small documented grammar. They are easy to inspect because they declare the thing being checked instead of asking the checker to infer the meaning of every sentence. Check the fixture Use Python 3.11 or newer. The runtime needs no third-party dependencies: git clone https://github.com/asadani/spec-sentry.git cd spec-sentry out_dir = " $( mktemp -d ) " python -m spec_sentry check sharing-spec.md \ --root fixtures --out " $out_dir /findings.json" The command exits with status 1 because the example intentionally contains findings. Status 0 means no configured findings were observed; status 2 indicates invalid input or an operational error. The output locates the conflicting declarations, undefined marked term, and pending decision. It gives the reviewer source evidence to inspect rather than editing the document. A reviewer decision belongs to a version A reviewer can accept, dismiss, or defer a finding with a note. The decision ledger is separate from the specification and records the fingerprint associated with the review. That separation matters after an edit. A dismissal against an older version should not automatically hide a finding in new text. When the relevant evidence changes, the prior disposition becomes stale and needs another look. The report excludes only fresh dismissed findings from its unresolved result. Accepting a finding records a review decision; it does not erase the underlying issue. This keeps discussion history distinct from a claim that the specification is now correct. The full walkthrough demonstrates the check, decision, and report lifecycle with a temporary copy of the fixture. Pay attention to the cost of annotations Explicit syntax trades broad coverage for reproducible checks. If a limit appears only in prose without a declared quantity, the tool cannot assume that it belongs to a matching key. Markdown headings do not create implicit scopes, and units are compared as written rather than converted. Those limits affect how a team should use the tool. Annotate the few quantities, terms, and decisions that repeatedly create ambiguity. Do not require a new notation for every sentence unless it produces enough useful findings to justify the authoring burden. The same principle applies to review ledgers. A ledger that requires more effort than it saves will become another stale artifact. Try it before a planning handoff Take one small feature spec with a few consequential limits and unresolved questions. Add the explicit declarations, run the check, and review the findings with the engineer who will implement the feature. Measure whether the check surfaces something actionable and whether the recorded decisions survive the next revision without concealing new uncertainty. That is a more useful test than counting annotations or declaring the document approved because the report is clean. The MIT-licensed repository includes the grammar, ledger format, fixtures, and checks. It offers a bounded way to keep selected questions visible through review. AI disclosure: This article was drafted with AI assistance using the project's implementation and synthetic specification. It does not report a measured reduction in specification defects.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/anuj-sadani/make-unresolved-decisions-visible-before-a-specification-reaches-engineering-3io8

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
