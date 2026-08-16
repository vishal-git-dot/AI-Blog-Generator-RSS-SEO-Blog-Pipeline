---
title: "Code Review From the Terminal and CI, No MCP Client Required"
slug: "code-review-from-the-terminal-and-ci-no-mcp-client-required"
author: "Will"
source: "devto_python"
published: "Sun, 16 Aug 2026 06:17:00 +0000"
description: "A month ago I shipped aicraft-code-review , an MCP server that reviews code locally. This week I added a CLI mode — because not everyone wants to wire up an ..."
keywords: "code, review, mcp, file, diff, high, aicraft, issues"
generated: "2026-08-16T06:48:23.403325"
---

# Code Review From the Terminal and CI, No MCP Client Required

## Overview

A month ago I shipped aicraft-code-review , an MCP server that reviews code locally. This week I added a CLI mode — because not everyone wants to wire up an MCP client just to check a diff. Now the same reviewer runs three ways: MCP tools — review_code / review_diff / review_file inside Claude Code, Cursor, Cline CLI — mcp-code-review review-file path/to/file.py CI — pipe git diff into it and branch on the exit code The CLI pip install aicraft-code-review # a single file (config auto-discovered from the file's directory upward) mcp-code-review review-file src/api.py # the current diff git diff | mcp-code-review review-diff # a snippet mcp-code-review review-code "import os; os.system('ls')" Exit codes are CI-friendly: Code Meaning 0 clean, or only info-level findings 1 high / medium issues found 2 critical issues found What it catches out of the box Security (OWASP patterns), performance (N+1, unbounded growth), quality (bare excepts, TODOs, missing type hints), style (naming, line length). Real output: ### 🟠 High (2) | Line | Issue | Category | Fix | | 4 | Command injection risk | security | subprocess.run with args list | | 9 | N+1 query in loop | performance | batch query / eager loading | ### 🟢 Info (2) — missing return type annotations Verdict: Conditional Pass — address high/medium issues Making it match YOUR rules The config file is the part I'd actually show a teammate: custom_rules : - name : no-console-log pattern : ' console\.log\(' severity : high category : quality issue : Console logging left in production code fix : Use a structured logger instead disabled_checks : - todo_comment severity_overrides : hardcoded_secret : critical .mcp-code-review.yaml is auto-discovered from the reviewed file's directory upward MCP_CODE_REVIEW_CONFIG points a whole team at one shared profile valid severities: critical / high / medium / info regex patterns work best in single quotes (double quotes will error on escapes like \. ) One caveat if you're also shipping Python MCP servers Pin your MCP dependency. mcp 2.0.0 shipped breaking changes and broke fresh installs of servers that had mcp>=1.6 unpinned. Use mcp>=1.6,<2 until you've migrated. The server is MIT-licensed: pip install aicraft-code-review , or claude mcp add code-review -- uvx aicraft-code-review . Issues and feedback welcome on GitHub .

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/goodjobwilliam/code-review-from-the-terminal-and-ci-no-mcp-client-required-33jf

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
