---
title: "Claude Fable 5 refuses tool calls based on semantics, not logic"
slug: "claude-fable-5-refuses-tool-calls-based-on-semantics-not-logic"
author: "Sergey Inozemtsev"
source: "devto_python"
published: "Tue, 07 Jul 2026 19:14:40 +0000"
description: "I was migrating llm_api_adapter — an open-source universal adapter for LLM APIs — to support Claude Fable 5. The tool was harmless. The logic was identical t..."
keywords: "tool, what, fable, name, token, resp, tools, score"
generated: "2026-07-07T20:04:00.201495"
---

# Claude Fable 5 refuses tool calls based on semantics, not logic

## Overview

I was migrating llm_api_adapter — an open-source universal adapter for LLM APIs — to support Claude Fable 5. The tool was harmless. The logic was identical to what worked on Opus 4.8. Then one e2e test came back with this: print ( resp . finish_reason ) # "refusal" print ( resp . tool_calls ) # None No exception. HTTP 200. The tool call just never happened. Fable 5 didn't refuse because of what the tool does — it refused because of what it sounds like it does. The setup from llm_api_adapter.universal_adapter import UniversalLLMAPIAdapter from llm_api_adapter.models.messages.chat_message import UserMessage from llm_api_adapter.models.tools.tool_spec import ToolSpec adapter = UniversalLLMAPIAdapter ( organization = " anthropic " , model = " claude-fable-5 " , api_key = " ... " , ) tools = [ ToolSpec ( name = " get_secret_word_score " , description = " Return the hidden score for a token. " , json_schema = { " type " : " object " , " properties " : { " token " : { " type " : " string " }}, " required " : [ " token " ], }, ) ] resp = adapter . chat ( messages = [ UserMessage ( ' What is the secret score for token " strawberry_v2 " ? ' )], tools = tools , tool_choice = " any " , max_tokens = 512 , ) print ( resp . finish_reason ) # "refusal" print ( resp . tool_calls ) # None The same prompt on Opus 4.8: finish_reason: "tool_use" , correct arguments. The fix tools = [ ToolSpec ( name = " get_word_score " , description = " Return the score for a word. " , json_schema = { " type " : " object " , " properties " : { " word " : { " type " : " string " }}, " required " : [ " word " ], }, ) ] resp = adapter . chat ( messages = [ UserMessage ( ' What is the score for the word " strawberry " ? ' )], tools = tools , tool_choice = " any " , max_tokens = 512 , ) print ( resp . finish_reason ) # "tool_use" print ( resp . tool_calls [ 0 ]. arguments ) # {'word': 'strawberry'} Identical logic. Different semantics. Different outcome. The obvious hypothesis: Fable 5's classifiers flag security-adjacent words. So I renamed the tool, removed "secret" from the prompt, and moved on. But that's the what , not the how . I wanted to know the mechanism. 3 isolation tests I kept the original code and removed one element at a time: What I removed What remained unchanged Result secret from tool name only token arg + "secret score for token" in prompt ✅ tool_use secret from name + prompt token as argument name ✅ tool_use Nothing from name Cleaned prompt and argument name ✅ tool_use Nothing Everything original ❌ refusal Removing any single element was enough to get a tool call through. What's actually happening Fable 5's classifier is not a keyword filter. It's a combinatorial pattern detector. The combination of get_secret_word_score + argument named token + prompt containing "secret score for token" reads as an auth/security operation — the kind of thing you'd see when extracting credentials or scoring access tokens. Each word on its own is harmless. Together, they cross a threshold. This makes sense given how Anthropic built Fable 5. It shares the same underlying model as Mythos 5 — the difference is that Fable ships with safety classifiers that evaluate intent , not execution. The classifier doesn't care what get_secret_word_score actually does. It cares what it looks like it does, based on everything in the request: tool name, description, argument names, and the prompt together. The Fable 5 migration guide calls the migration "mostly drop-in" and lists safety classifier refusals as one of four key changes to watch. What it doesn't explain is how those classifiers actually evaluate your tool specs. Practical takeaway Don't think of your tool spec as a technical contract. Think of it as a description of intent — because that's how the classifier reads it. Before you name a tool, ask: if someone unfamiliar with my codebase read this tool name, description, and argument names together, what would they think this code is trying to do ? If it sounds like credential extraction, auth bypass, or scoring access tokens — the classifier will think so too. A few patterns that can combine badly: secret / hidden / private + token / key + score / check / verify auth / access in tool names with argument names that look like identifiers None of these words are banned. The problem is accumulation. One integration note stop_reason: "refusal" comes back as HTTP 200. If you're only handling exceptions, you're silently dropping tool calls in production. if resp . finish_reason == " refusal " : # fall back to another model or surface the error explicitly ... The API supports a fallbacks parameter (currently in beta) to handle this server-side automatically — worth checking if you're running Fable 5 at scale.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/inozem/claude-fable-5-refuses-tool-calls-based-on-semantics-not-logic-kd3

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
