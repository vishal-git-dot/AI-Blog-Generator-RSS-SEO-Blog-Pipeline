---
title: "Catch Broken Markdown Links and #Anchors Offline Before They Hit Production with DeadLinkFinder"
slug: "catch-broken-markdown-links-and-anchors-offline-before-they-hit-production-with-deadlinkfinder"
author: "Umut Güngör"
source: "devto_python"
published: "Fri, 16 Oct 2026 10:57:38 +0000"
description: "Documentation rots quietly. You rename a file, refactor a section heading in your README.md , or move a diagram into a new folder—and suddenly your documenta..."
keywords: "deadlinkfinder, github, heading, anchors, file, your, anchor, install"
generated: "2026-10-16T11:05:26.345207"
---

# Catch Broken Markdown Links and #Anchors Offline Before They Hit Production with DeadLinkFinder

## Overview

Documentation rots quietly. You rename a file, refactor a section heading in your README.md , or move a diagram into a new folder—and suddenly your documentation is full of dead relative links and broken #heading-anchors . Code review rarely catches these because nobody manually clicks every link and table-of-contents anchor in every pull request. That is why I built DeadLinkFinder —a fast, zero-dependency Python CLI that verifies local Markdown links, image assets, GitHub-flavored heading anchors, and optional external URLs before they reach production. Why Existing Link Checkers Frustrated Me When I looked for a link linter for my repositories, I kept running into three problems: Heavy runtime dependencies: Installing a full Node.js or headless browser stack just to check if ../docs/architecture.md exists in a Python repo felt unnecessary. False positives on GitHub #anchors : GitHub's heading slug algorithm has specific rules around punctuation, Unicode characters, emojis, and duplicate headings ( #install , #install-1 ). Naive regex checkers constantly fail on valid anchors. Detection without diagnosis: Telling me "Target not found" is only half the job. If I made a typo in a 40-heading document, the tool should tell me what I probably meant. Quick Start DeadLinkFinder uses only the Python standard library ( re , pathlib , difflib , urllib ), meaning zero external dependencies to audit or maintain. Install it directly from PyPI : pip install deadlinkfinder Run it against any directory or Markdown file: deadlinkfinder docs/ README.md Example terminal output: $ deadlinkfinder docs/ 🔍 DeadLinkFinder - Verifying documentation integrity... [!] DLF-001 ERROR docs/getting-started.md:28 Target not found: '../guides/setup.md' Suggestion: Did you mean '../guides/install-setup.md'? [!] DLF-002 ERROR README.md:64 Anchor not found: '#configuration-option' Suggestion: Did you mean '#configuration-options'? Key Features Built for CI/CD 1. Offline-First with Fuzzy Suggestions ( difflib ) By default, DeadLinkFinder runs 100% offline in milliseconds. It checks local file paths, image references ( ![alt](./assets/demo.png) ), and cross-file anchors ( ./guide.md#installation ). Whenever a target or anchor is missing, it uses difflib to suggest the closest existing file or heading slug. 2. GitHub-Compatible Heading Anchor Engine Whether your headings contain Turkish characters, emojis, inline code backticks, or repeated section titles across a document, the anchor resolver mirrors GitHub's exact slug generation rules. 3. Native SARIF v2.1.0 & JSON Output Want inline annotations directly on your GitHub Pull Requests or GitHub Code Scanning dashboard? Generate a SARIF report with deterministic line fingerprints: deadlinkfinder . --format sarif --output results.sarif Or use --format json for custom CI pipelines and pre-commit hooks. Part of a Zero-Dependency CLI Suite DeadLinkFinder is part of my open-source suite of zero-dependency developer tools, alongside EnvDoctor (for .env contract auditing) and TokenGuard (for pre-commit secret scanning). Case Study & Architecture Notes: umutgungorr.com/projects/deadlinkfinder Source Code (GitHub): github.com/umutgungorr/deadlinkfinder PyPI Package: pypi.org/project/deadlinkfinder More Engineering Articles & Projects: Umut Güngör — umutgungorr.com If you maintain open-source documentation or internal engineering wikis, give deadlinkfinder a spin in your CI pipeline—feedback and issues are always welcome!

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/umutgungor/catch-broken-markdown-links-and-anchors-offline-before-they-hit-production-with-deadlinkfinder-2g42

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
