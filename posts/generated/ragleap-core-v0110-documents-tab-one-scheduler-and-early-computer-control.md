---
title: "ragleap-core v0.11.0 – Documents Tab, One Scheduler, and Early Computer Control"
slug: "ragleap-core-v0110-documents-tab-one-scheduler-and-early-computer-control"
author: "RagLeap"
source: "devto_python"
published: "Tue, 20 Oct 2026 16:20:28 +0000"
description: "ragleap-core v0.11.0 is out – first release under ragleap org Repo moved: antonyrag/ragleap-core → ragleap/ragleap-core Tag: v0.11.0 / commit c1fc164 This is..."
keywords: "ragleap, core, now, tab, documents, not, only, files"
generated: "2026-10-20T16:39:11.046498"
---

# ragleap-core v0.11.0 – Documents Tab, One Scheduler, and Early Computer Control

## Overview

ragleap-core v0.11.0 is out – first release under ragleap org Repo moved: antonyrag/ragleap-core → ragleap/ragleap-core Tag: v0.11.0 / commit c1fc164 This is a stability + product release. Here's the breakdown. 1. Documents Tab (the main feature) Before: adding docs was scattered. Now: dedicated Documents tab to list, upload, and delete. Important: deleting also removes the document's entries from the knowledge graph. python # #710, #711 – deletion now cleans graph # Dashboard now accepts: # 28 file types + web pages by address (#720) 2. AI Office Two new tabs: Proactive Connectors PR #740 – foundation for AI employees to act, not just chat. 3. Offline Language Detection LANGUAGE_DETECTION_MODEL=lite Works without internet now (#741). Useful for air-gapped installs. 4. Infra fixes that matter Non-root container: # #742 USER 10001 # pinned dependencies One scheduler: Previously, extra web workers repeated scheduled triggers. Now only one process runs background jobs (#817). 5. Providers DemonRoute added – 20 providers total (#851). # provider count 20 6. Experimental: Computer Control (OFF by default) ⚠️ Not independently reviewed. Do NOT enable for real data. Design: Share via CLI only: ragleap files Sandbox runner = read-only AI can: list, read, ask for access Access request ≠ grant. Always needs owner approval. File contents never enter activity log Grants visible in Files tab ragleap files off = pause everything Issues: #747, #776, #777, #789-#792. Review RFC: #800. Community Testing issues #779-#787 Number words for every language #801 ragleap-phone RFC #814 Thanks @sammist2 @mig-builds @ahmet-izgi @haterfactory Upgrade Container user is now 10001. No migration needed, app writes no files of its own. Packages (ragleap-rag, ragleap-graph, voice, agents) versioned separately. Known Limits Neo4j default password still public in compose (localhost only) – per-install random password planned Tested: Windows laptop + Linux servers. NOT verified: macOS, Linux desktops, Ollama on Windows (#779-#781) No named users/roles, no security audit yet Links: Release: github.com/ragleap/ragleap-core/releases/tag/v0.11.0 Core: github.com/ragleap/ragleap-core If you self-host, try the Documents tab and tell me what breaks. PRs welcome.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/ragleap/ragleap-core-v0110-documents-tab-one-scheduler-and-early-computer-control-mg2

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
