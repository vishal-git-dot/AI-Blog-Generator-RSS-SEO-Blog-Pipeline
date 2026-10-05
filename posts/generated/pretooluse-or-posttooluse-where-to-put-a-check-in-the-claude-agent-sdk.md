---
title: "PreToolUse or PostToolUse? Where to Put a Check in the Claude Agent SDK"
slug: "pretooluse-or-posttooluse-where-to-put-a-check-in-the-claude-agent-sdk"
author: "Poorna Reddy"
source: "devto_python"
published: "Mon, 05 Oct 2026 22:55:18 +0000"
description: "If an agent can trigger a business action, the most important design question is where each check runs. In the Claude Agent SDK, hooks give you two points ar..."
keywords: "agent, tool, hooks, claude, sdk, not, hook, can"
generated: "2026-10-05T23:55:08.862398"
---

# PreToolUse or PostToolUse? Where to Put a Check in the Claude Agent SDK

## Overview

If an agent can trigger a business action, the most important design question is where each check runs. In the Claude Agent SDK, hooks give you two points around every tool call. Only one of them can stop the action. The rule that decides most designs A check that must prevent a side effect belongs in PreToolUse . It runs before the tool executes and returns a decision. PostToolUse runs after execution. It can add context, replace the result the agent sees, or record an event, but it cannot undo what the tool already did. The three PreToolUse decisions Decision Use it when What happens deny Required data is missing or a business rule fails The tool does not run. Return a reason the agent and the operator can act on ask The request is valid but needs a person's approval Your approval handler ( canUseTool in TypeScript, can_use_tool in Python) gets the decision. Returning ask alone does not create an approval screen allow The request meets the hook's policy The call continues to the tool service A PreToolUse hook can also return changed input. Use that sparingly and log it, because the tool then runs something the agent did not ask for. Two traps Async hooks cannot gate. A callback that returns async: true ( async_: True in Python) cannot block the tool or change its input. A hook that gates an action must return its decision before execution. The hook is not the last line. The hook does not own the business record. The tool service must repeat authorization and business validation, and use an idempotency key so a retry cannot create a duplicate. Passing the hook shows the request looked acceptable, not that the action is correct. Agent SDK hooks are not Claude Code hooks The event names overlap, but the owners differ. Agent SDK hooks are registered by the application running the agent, through ClaudeAgentOptions in Python or the SDK options in TypeScript. Claude Code hooks are configured in the Claude Code environment. Exam questions and real incidents both turn on this difference. A test plan before any real side effect Send a valid, below-limit request. Confirm the tool receives unchanged input. Remove a required field, change the supplier, exceed the limit. Confirm the expected deny or ask. Simulate a lookup timeout, a tool error and a duplicate request. Confirm each one produces a visible event and no unintended action. Check that the log records the session ID, tool-use ID, decision and reason, without unnecessary personal data. Review the blocked paths as carefully as the successful one. Go further The full article walks through an invoice approval flow: Claude Agent SDK hooks on Timo Labs . The architect exam covers this as task statement 1.5: Agent SDK hooks . Practise these placement decisions with the free Claude Certified Architect practice exam .

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/poorna_reddy/pretooluse-or-posttooluse-where-to-put-a-check-in-the-claude-agent-sdk-36fh

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
