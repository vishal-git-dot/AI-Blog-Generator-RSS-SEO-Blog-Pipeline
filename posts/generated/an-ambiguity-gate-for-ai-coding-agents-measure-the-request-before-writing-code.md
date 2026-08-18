---
title: "An ambiguity gate for AI coding agents: measure the request before writing code"
slug: "an-ambiguity-gate-for-ai-coding-agents-measure-the-request-before-writing-code"
author: "Q00"
source: "devto_webdev"
published: "Tue, 18 Aug 2026 01:27:41 +0000"
description: "Every AI coding agent I have used will happily start writing code from a one-line request. "Build a task management CLI" leaves the data model, storage, prio..."
keywords: "gate, you, request, spec, not, ambiguity, agent, one"
generated: "2026-08-18T01:34:47.477505"
---

# An ambiguity gate for AI coding agents: measure the request before writing code

## Overview

Every AI coding agent I have used will happily start writing code from a one-line request. "Build a task management CLI" leaves the data model, storage, priority rules, and ID scheme for the model to guess, and each guess is defensible and wrong. You find out three files into review, and the fix costs a rewrite instead of an answer. An ambiguity gate is the opposite default: the system measures how vague your request still is, and refuses to freeze a spec until the number clears a threshold. This post describes the concrete gate we ship in Ouroboros (MIT, open source), with the actual constants, because when I went looking for prior art the search results were all academic papers and general advice. If other products implement this, I would genuinely like to compare notes. The score The interview loop asks questions and scores three axes of clarity, each in [0, 1]: goal clarity, weight 0.40 constraint clarity, weight 0.30 success-criteria clarity, weight 0.30 Ambiguity is one minus the weighted sum. A request is gate-ready when ambiguity drops below 0.2. Each axis also has its own floor (0.75 goal, 0.65 constraints, 0.70 success criteria), so you cannot buy your way past a vague goal with very crisp constraints. The constants live in bigbang/ambiguity.py in the repo, not in a config file, on purpose: the gate is a product claim, and product claims should be greppable. What the gate actually blocks, and what it does not The gate is a default, not a wall. The UI shows a force option that generates the spec anyway. So the guarantee is narrower than "no vague spec exists". It is "no vague spec exists without someone explicitly choosing it". We think that is the right shape: the gate's job is to make vagueness a decision instead of an accident. What changes in practice is where the iteration happens. Without a gate, iteration happens after code exists: you review, discover the wrong assumption, and re-prompt. With the gate, the same iteration happens in the interview, where a wrong assumption costs one answered question instead of one discarded implementation. Why a number instead of judgment An agent can always say "this seems clear enough". A threshold it must clear removes that discretion. To be precise about what the number controls: in the interactive interview there is no round limit and you decide when to stop asking; the 0.2 threshold gates the next step, generating the spec. In the unattended auto mode, a separate readiness constant (also 0.20, defined independently in the auto driver) decides when the interview is ready to hand off. Either way, a fixed number gates the step, not the model's own sense of "clear enough". The number is not a quality guarantee. A request can score 0.1 and still describe a bad idea clearly. The gate only promises that you decided what goes into the spec. Trying it curl -fsSL https://raw.githubusercontent.com/Q00/ouroboros/main/scripts/install.sh | OUROBOROS_INSTALL_REF = devto-seo1 bash Then, inside your coding agent, run these in order ( ooo setup is a one-time step): > ooo setup > ooo interview "whatever you were about to prompt an agent with" Try it with a request you were about to hand an agent. Reply with the starting score and the first question that exposed an assumption you had not decided yet. Repo: github.com/Q00/ouroboros

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/q00/an-ambiguity-gate-for-ai-coding-agents-measure-the-request-before-writing-code-4n75

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
