---
title: "We scanned 671 MCP servers to see what happens when an agent retries"
slug: "we-scanned-671-mcp-servers-to-see-what-happens-when-an-agent-retries"
author: "aurumflux20"
source: "devto_webdev"
published: "Tue, 11 Aug 2026 18:58:38 +0000"
description: "Every timeout is a question nobody can answer: did it happen? An agent calls a tool. The call times out. The agent doesn't know whether the email sent, the i..."
keywords: "servers, what, guard, have, scanner, read, than, one"
generated: "2026-08-11T19:08:47.090722"
---

# We scanned 671 MCP servers to see what happens when an agent retries

## Overview

Every timeout is a question nobody can answer: did it happen? An agent calls a tool. The call times out. The agent doesn't know whether the email sent, the invoice was created, the charge went through. So it retries — because that's what agents do. If nothing on either side of that call can tell the second attempt from the first, the effect happens twice. We wanted to know how common that is in practice, so we scanned the ecosystem: 671 MCP servers, 27,153 declared tools. What we found Servers scanned successfully 671 (of 755 attempted) Tools declared across them 27,153 Servers performing real writes 539 (80%) Of those, with zero visible idempotency guards 175 (32%) Servers with retry logic and zero guards 40 Servers with money-adjacent tools and no visible guard 35 Servers with no guard of any kind, anywhere 288 (42%) The sharpest cut — servers that write, retry, and have no guard the scanner could see — is 32 servers with 28,653 combined monthly downloads. Those are the places where a timeout is most likely to become a duplicate. Among the 23 largest servers we scanned (10,000+ downloads/month), 6 perform writes with no visible guard. What this scan cannot see — read this before quoting the numbers This is the most important section, so it goes before the analysis rather than after. A scanner reading a repository from the outside usually cannot prove a double-fire. Three reasons, each of which we hit repeatedly: The guard often lives somewhere else. Many servers call a backend that deduplicates on its own — a payment API keyed by a nonce, a database with a unique constraint. From the client repo, that protection is invisible. "No guard found" means the scanner found none in this code , not "this software is unsafe." A tool that looks like a write may not be one. We found tools that appear to send payments but only return a link for a human to sign. Names lie in both directions. Our own scanner has been wrong. An early version accused a repo of having zero idempotency guards while it shipped an entire module of them — a regex with no word boundary couldn't match deriveIdempotencyKey . It hand-verified at 3 of 7 on its first real targets. Every pattern in the current version exists because an earlier one got something wrong. So these numbers describe what is visible in public code , not a safety verdict on any project. We're publishing aggregates and no names. If you want to know about a specific server, the honest answer is: read it, and ask the maintainer what the backend does. We also excluded failures rather than counting them as zeros: 66 repositories failed to clone, 17 returned unparseable output, 1 crashed the scanner. A failed lookup is not a finding. Including them would have made every percentage look worse and been wrong. Why the pattern shows up so consistently Idempotency isn't hard because the code is hard. A lease, a key, a stored result — that's an afternoon. It's hard because it asks a question most systems never make explicit: What makes two operations the same operation? Get that answer too narrow and you get false duplicates: annoying, safe, loud. Get it too wide and you get silent data loss — two legitimately different actions collapsing into one, where the second silently returns the first one's receipt. That failure looks like success. Nobody investigates a transaction that appears to have worked. We learned this the expensive way. We proposed an idempotency key to a payments project derived from URL, amount, and wallet. A stranger pointed out it omitted payee, network, and asset — meaning two genuinely different purchases would have collapsed into one. Our fix would have been worse than the bug. MCP makes this sharper than ordinary API design, for a structural reason: the caller is a language model. It doesn't know your retry semantics, it can't read your backend, and when a call fails ambiguously its instinct is to try again. In the servers we read, the tool schema is where that knowledge would have to live — and it's usually silent. What actually helps Three things, in order of effort: Say it in the schema. If a tool is unsafe to retry blindly, the description is the only place the model will read it. One sentence: "if this times out, the operation may have completed — check before retrying." Costs nothing, and it's the single highest-leverage change we've seen. Accept a caller-supplied key. Let the caller mark two attempts as the same attempt. Don't derive it from the payload alone. Make the choke point atomic. Whatever admits the effect should also be what checks whether it already happened. Check your own server npx fencescan Zero dependencies, no install, no account. It reports candidates and evidence, never verdicts, for the reasons above. If it flags something you know is guarded, that's a bug worth reporting to us — a false positive costs more than a miss. Methodology, the full pattern list, and the four failure modes we've fixed: https://github.com/aurumflux20/fencescan If you want to see the failure mode rather than read about it, here are 1,000 concurrent agents trying to charge the same card, with and without a guard: https://aurumflux20.github.io/once-kernel-ts/ We build open-source retry-safety tooling ( once-kernel , effectfence ), which is why we had a scanner pointed at this in the first place. The numbers are the numbers either way — and the caveats above are what keep them worth reading.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/aurumflux20/we-scanned-671-mcp-servers-to-see-what-happens-when-an-agent-retries-3pnc

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
