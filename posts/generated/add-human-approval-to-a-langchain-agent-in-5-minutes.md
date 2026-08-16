---
title: "Add human approval to a LangChain agent in 5 minutes"
slug: "add-human-approval-to-a-langchain-agent-in-5-minutes"
author: "Shakir Riyaz"
source: "devto_python"
published: "Sun, 16 Aug 2026 01:10:04 +0000"
description: "Add human approval to a LangChain agent in 5 minutes Your agent can send the email. That's the whole problem. A month ago it could only draft one. Now it has..."
keywords: "agent, email, you, tool, str, agentgate, gate, same"
generated: "2026-08-16T01:41:13.466931"
---

# Add human approval to a LangChain agent in 5 minutes

## Overview

Add human approval to a LangChain agent in 5 minutes Your agent can send the email. That's the whole problem. A month ago it could only draft one. Now it has a tool that actually calls the API, and somewhere between "draft" and "send" there used to be a person reading it first. If you've given an agent a tool that does something real — sends an email, deploys code, deletes records, moves money — you've probably already felt the gap between "the agent can do this" and "I actually want it to do this unsupervised." LangGraph gets you halfway there. Its interrupt() primitive is the right idea: pause execution, wait for a human, resume. But interrupt() gives you a pause — not a Slack message with the context in it, not a reject button with a reason field, not a record of who approved what and when. You still have to build all of that yourself, and it's the kind of infrastructure that's tedious to build right and easy to build wrong. This post is the other half: wrapping an existing LangChain tool so it requires a real human decision — in Slack or Microsoft Teams — before it runs, in about five minutes and four lines of new code. The tool you already have Say you've got a tool like this — nothing special, just a BaseTool that sends an email: from typing import Type from pydantic import BaseModel , Field from langchain_core.tools import BaseTool class SendEmailInput ( BaseModel ): recipient : str = Field ( description = " Email recipient address " ) subject : str = Field ( description = " Email subject line " ) body : str = Field ( description = " Email body content " ) class SendEmailTool ( BaseTool ): name : str = " send_email " description : str = " Send an email to a prospect or customer. " args_schema : Type [ BaseModel ] = SendEmailInput def _run ( self , recipient : str , subject : str , body : str ) -> str : # your actual email-sending logic return f " Email sent to { recipient } " Your agent calls this whenever it decides an email needs sending. Today, that's the whole decision — the agent decides, and it happens. Wrapping it pip install useagentgate langchain-agentgate from agentgate import AgentGate from langchain_agentgate import ApprovalRequiredTool gate = AgentGate ( api_key = " ag_your_key " , base_url = " https://your-agentgate-instance " ) gated_email_tool = ApprovalRequiredTool ( wrapped_tool = SendEmailTool (), gate = gate , risk_tier = " high " , timeout_minutes = 15 , ) That's it. gated_email_tool has the same name, the same input schema, the same output type as SendEmailTool — swap it in anywhere the original tool was going. Your agent's code doesn't change. The prompt doesn't change. The only difference shows up at runtime. What actually happens now When the agent decides to call send_email , instead of running immediately, it: Posts a card to Slack (or Teams) with the action, the arguments, and the risk tier Blocks, polling every few seconds A human clicks Approve or Reject — reject requires a reason If approved, SendEmailTool._run() executes exactly as before and its return value comes back to the agent, unchanged If rejected, the agent gets back "Action 'send_email' was rejected by @sarah: wrong recipient list" instead of raising — so it can react in the conversation ("looks like that got rejected because...") instead of crashing If nobody responds in time, it fails closed — no response is treated as no, never as yes result = await agent_executor . ainvoke ({ " input " : " email the Q4 proposal to john@acme.com " }) Everything up to the tool call runs exactly as it did before. The pause — and the record of who decided what — is the only thing that's new. Why wrap instead of rewrite The alternative is building this yourself: a place to post the message, a way to identify which agent run is waiting on which click, a poller or a webhook, a rejection-reason modal, somewhere to log the decision so "why did the agent do that" has an answer three weeks later. All of that already exists behind ApprovalRequiredTool — you're not building an approval system, you're passing one existing tool through a wrapper. It also composes. Gate the tools that matter — send_email , deploy , delete_customer_data , transfer_funds — and leave the read-only ones ( search , fetch , summarize ) alone. Different tools can even get different risk tiers and timeouts: gated_delete = ApprovalRequiredTool ( wrapped_tool = DeleteRecordsTool (), gate = gate , risk_tier = " critical " , timeout_minutes = 10 , ) The other half of the picture interrupt() is still the right call for pausing a graph mid-execution when you need to resume exact state later — that's not what this replaces. This is for the narrower, more common case: a specific tool call that shouldn't happen without a specific person saying yes, with the Slack UI, the audit trail, and the timeout handling already built. Building with CrewAI instead? crewai-agentgate is the same wrapper for CrewAI's BaseTool — same four lines, same behavior. Full docs and setup: useagentgate.com/docs . Free to start, no credit card.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/shakirriyaz/add-human-approval-to-a-langchain-agent-in-5-minutes-281d

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
