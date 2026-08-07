---
title: "Building a Multi-Agent AI for Company LinkedIn Pages - Part 9: Building the Writing Critic Agent"
slug: "building-a-multi-agent-ai-for-company-linkedin-pages-part-9-building-the-writing-critic-agent"
author: "Manav"
source: "devto_python"
published: "Fri, 07 Aug 2026 06:45:34 +0000"
description: "Our system can now understand a topic, gather research, find supporting examples, identify weak assumptions, structure everything into a content brief, gener..."
keywords: "drafts, agent, linkedin, json, writing, hooks, critic, draft"
generated: "2026-08-07T07:23:56.534840"
---

# Building a Multi-Agent AI for Company LinkedIn Pages - Part 9: Building the Writing Critic Agent

## Overview

Our system can now understand a topic, gather research, find supporting examples, identify weak assumptions, structure everything into a content brief, generate multiple hooks, and write two complete LinkedIn post drafts. But generating two drafts creates a new problem. Which one is actually better? That's why we built the Writing Critic Agent. Unlike the earlier Critic Agent, which evaluates the research before any writing begins, the Writing Critic Agent evaluates the finished LinkedIn drafts. It doesn't rewrite or improve them. Instead, it scores each draft so the user can confidently choose the stronger one. 5 Hooks │ ▼ 2 Drafts │ ▼ Writing Critic Agent │ ▼ Scores + Recommendation Before we start writing code, let's define the system prompt. I wanted the Writing Critic Agent to judge the drafts the same way a real LinkedIn reader would. Instead of checking grammar or rewriting sentences, it scores each draft across three dimensions: Originality: Does it sound fresh or like another generic AI-generated LinkedIn post? Promise fulfilment: Does the post actually deliver what the hook promised? Shareability: Would someone realistically save, comment on, or repost it? It also compares both drafts and recommends which one should be used. SYSTEM_PROMPT = """ Evaluate 2 LinkedIn drafts. Score each draft on: - Originality - Promise fulfilment - Shareability Compare both drafts. Return valid JSON. """ The production prompt is much longer, but I've shortened it here to highlight the core rules. Unlike the Draft Agent, this agent doesn't require the Content Brief anymore. At this stage, we only need the generated hooks and the two drafts because those are the outputs being evaluated. user_message = ( f " Hooks: { hooks } \n\n DRAFTS: \n " + " \n --- \n " . join ( drafts ) ) Instead of returning a list, the Writing Critic Agent returns a structured JSON object. Each draft receives individual scores and explanations, followed by a comparison section that recommends the stronger draft. { "draft_0" : { ... }, "draft_1" : { ... }, "comparison" : { ... } } Since downstream code expects a valid JSON object, we parse the response inside a try and except block. If parsing fails, the function returns None instead of crashing the pipeline. try : parsed = json . loads ( refined_response ) except json . JSONDecodeError : print ( " LLM did not return valid JSON: " ) print ( raw_response ) return None Before writing the function, let's break down what happens. The function takes the generated hooks and two LinkedIn drafts as input, builds the user message, calls the LLM, strips markdown fences, parses the JSON response, and finally returns the structured evaluation. def rate_drafts ( hooks : list [ str ], drafts : list [ str ]) -> dict | None : user_message = ( f " Hooks: { hooks } \n\n DRAFTS: \n " + " \n --- \n " . join ( drafts ) ) raw_response = call_llm ( SYSTEM_PROMPT , user_message ) refined_response = strip_json_fences ( raw_response ) try : parsed = json . loads ( refined_response ) except json . JSONDecodeError : print ( " LLM did not return valid JSON: " ) print ( raw_response ) return None return parsed At this point, every individual agent has been built and tested independently. Each one has a single responsibility, from understanding the topic to scoring the final drafts. In the next article, we'll wire all these agents together into a complete multi-agent pipeline that takes a topic as input and automatically generates, evaluates, and returns ready-to-publish LinkedIn posts. Github Repo: https://github.com/Manav-N4/linkedin-agent#linkedin-agent

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/mnv/building-a-multi-agent-ai-for-company-linkedin-pages-part-9-building-the-writing-critic-agent-1hh

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
