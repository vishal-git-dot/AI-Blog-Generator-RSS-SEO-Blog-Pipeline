---
title: "Add email verification to your LangChain agent"
slug: "add-email-verification-to-your-langchain-agent"
author: "james-sib"
source: "devto_python"
published: "Sun, 28 Jun 2026 08:44:34 +0000"
description: "If your LangChain agent sends email, books demos, or accepts signups, sooner or later it will act on an address that does not exist. A typo like gmial.com , ..."
keywords: "agent, com, email, tool, langchain, address, false, verifly"
generated: "2026-06-28T09:19:21.765619"
---

# Add email verification to your LangChain agent

## Overview

If your LangChain agent sends email, books demos, or accepts signups, sooner or later it will act on an address that does not exist. A typo like gmial.com , a disposable mailinator.com throwaway, a dead domain. The agent has no way to know, so it sends anyway. The message bounces, your sending reputation drops, and the agent happily moves on to the next bad row. The fix is to give the agent a tool that checks an address before it acts on it. This walkthrough wires Verifly into a LangChain agent so the model can verify deliverability mid-loop, the same way it would call any other tool. The use case You hand an agent a list of leads scraped from a CSV and ask it to draft outreach. Some of those addresses are garbage. You want the agent to skip the bad ones and flag the fixable ones, on its own, without you writing bounce-handling glue. That decision needs a real deliverability signal, and that is exactly what a verification tool provides. Install pip install langchain-verifly langchain langchain-openai The langchain-verifly package ships a ready-made BaseTool called VeriflyEmailVerifier . You do not have to write a wrapper. Get a key Verifly is agent-native, so a key is one HTTP call away. No dashboard click-through required: curl -s -X POST https://verifly.email/api/v1/autonomous/register \ -H "Content-Type: application/json" \ -d '{"email":"you@example.com","password":"a-strong-password"}' The response contains an api_key.key (it starts with vf_ ) and 100 free credits. Export it: export VERIFLY_API_KEY = "vf_..." The tool, by itself Before handing it to an agent, run the tool directly so you can see the shape of what it returns. The class reads VERIFLY_API_KEY from the environment automatically: from langchain_verifly import VeriflyEmailVerifier verifier = VeriflyEmailVerifier () # picks up VERIFLY_API_KEY print ( verifier . run ( " jane.doe@gmial.com " )) That call against the live API returns: { ' email ' : ' jane.doe@gmial.com ' , ' result ' : ' undeliverable ' , ' reason ' : ' Invalid email: bad_domain ' , ' confidence ' : 90 , ' is_valid ' : False , ' recommendation ' : ' do_not_send ' , ' did_you_mean ' : ' jane.doe@gmail.com ' , ' details ' : { ' syntax_valid ' : True , ' domain_exists ' : True , ' mx_records ' : True , ' smtp_valid ' : False , ' is_disposable ' : False , ' is_role_account ' : False , ' is_catch_all ' : False , ' is_free_provider ' : False , ' provider ' : ' gmial.com ' } } Two things matter for an agent here. recommendation is a flat instruction ( do_not_send ), and did_you_mean proposes the correction jane.doe@gmail.com . The model can act on both without parsing anything fancy. A real address looks different: print ( verifier . run ( " james@sibscientific.com " )) { ' email ' : ' james@sibscientific.com ' , ' result ' : ' deliverable ' , ' reason ' : ' Email exists and accepts mail ' , ' confidence ' : 95 , ' is_valid ' : True , ' recommendation ' : ' safe_to_send ' , ' did_you_mean ' : None , ' details ' : { ' smtp_valid ' : True , ' is_disposable ' : False , ' is_catch_all ' : False , ...} } Wire it into an agent Now give the tool to an agent and let the model decide when to call it. The tool's own description ("Use before emailing a lead or accepting a signup to avoid bounces") is enough for the model to reach for it. from langchain_openai import ChatOpenAI from langchain.agents import create_tool_calling_agent , AgentExecutor from langchain_core.prompts import ChatPromptTemplate from langchain_verifly import VeriflyEmailVerifier tools = [ VeriflyEmailVerifier ()] prompt = ChatPromptTemplate . from_messages ([ ( " system " , " You clean lead lists. For each address, verify it. " " Drop anything with recommendation ' do_not_send ' . " " If did_you_mean is set, suggest the corrected address instead. " ), ( " human " , " {input} " ), ( " placeholder " , " {agent_scratchpad} " ), ]) llm = ChatOpenAI ( model = " gpt-4o-mini " , temperature = 0 ) agent = create_tool_calling_agent ( llm , tools , prompt ) executor = AgentExecutor ( agent = agent , tools = tools , verbose = True ) executor . invoke ({ " input " : " Clean these: jane.doe@gmial.com, james@sibscientific.com, test@mailinator.com " }) The agent verifies each address and reasons over the structured verdict. The typo gets the gmail.com correction surfaced, the real address passes, and the throwaway is dropped because Verifly flags it: verifier . run ( " test@mailinator.com " ) # {'result': 'undeliverable', 'reason': 'Disposable/temporary email address', # 'recommendation': 'do_not_send', 'details': {'is_disposable': True, ...}} Why a tool, not a regex Syntax checks catch bad@@example . They do not catch gmial.com , dead domains, disposable providers, or full mailboxes, because those require DNS, MX, and SMTP probing at request time. That is the work the tool does, and it returns one field, recommendation , that the model can branch on directly. Notes Verdicts are deliverable , undeliverable , risky , or unknown . Treat risky (catch-all domains, confidence around 40) as "send with caution," not "drop." Catch-all domains cannot be confirmed at the individual-mailbox level by anyone, so a risky verdict there is honest, not a failure. The free tier is 100 verifications. For list cleaning at volume there is a batch endpoint and an async bulk job API. That is the whole integration: one pip install , one tool in the tools list, and your agent stops sending into the void. Docs and the rest of the API live at verifly.email .

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/jamessib/add-email-verification-to-your-langchain-agent-3e59

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
