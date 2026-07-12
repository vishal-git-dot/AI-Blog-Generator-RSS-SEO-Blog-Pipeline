---
title: "Learn the Agent Loop Without an Agent Framework"
slug: "learn-the-agent-loop-without-an-agent-framework"
author: "Alex Chen"
source: "devto_python"
published: "Sun, 12 Jul 2026 08:07:13 +0000"
description: "The article “An Agent in 100 Lines of Lisp” was one of the most discussed programming items in the Hacker News snapshot I reviewed on 2026-07-12 , with 123 p..."
keywords: "tool, action, not, add, type, name, loop, model"
generated: "2026-07-12T08:25:23.791495"
---

# Learn the Agent Loop Without an Agent Framework

## Overview

The article “An Agent in 100 Lines of Lisp” was one of the most discussed programming items in the Hacker News snapshot I reviewed on 2026-07-12 , with 123 points. The interesting part for a learner is not the line count. It is that a small program can expose the entire control loop. You can study that loop without an API key or model. This Python exercise uses a deterministic “model” so every transition is inspectable. Prerequisites Python 3.10 or newer basic functions, dictionaries, and loops no external packages Save this as tiny_agent.py : TOOLS = { " add " : lambda a , b : a + b , " multiply " : lambda a , b : a * b , } def fake_model ( messages ): observations = [ m for m in messages if m [ " role " ] == " tool " ] if not observations : return { " type " : " tool " , " name " : " add " , " args " : [ 2 , 3 ]} if len ( observations ) == 1 : return { " type " : " tool " , " name " : " multiply " , " args " : [ observations [ 0 ][ " value " ], 4 ]} return { " type " : " final " , " answer " : observations [ - 1 ][ " value " ]} def run ( max_steps = 5 ): messages = [{ " role " : " user " , " content " : " Add 2 and 3, then multiply by 4 " }] for step in range ( max_steps ): action = fake_model ( messages ) print ( step , action ) if action [ " type " ] == " final " : return action [ " answer " ] tool = TOOLS . get ( action [ " name " ]) if tool is None : raise ValueError ( " tool is not allowed " ) value = tool ( * action [ " args " ]) messages . append ({ " role " : " tool " , " name " : action [ " name " ], " value " : value }) raise TimeoutError ( " step budget exhausted " ) assert run () == 20 Expected output: 0 {'type': 'tool', 'name': 'add', 'args': [2, 3]} 1 {'type': 'tool', 'name': 'multiply', 'args': [5, 4]} 2 {'type': 'final', 'answer': 20} What to notice The “agent” is not one magical function. It is four ordinary responsibilities: produce a structured action; validate that action against an allowlist; execute the tool outside the model; return an observation and decide whether to continue. The max_steps budget matters as much as the happy path. Replace fake_model with a function that always asks for add and confirm that the loop stops. Then request a missing tool and observe the allowlist failure. Exercises Validate argument counts before calling a tool. Add a tool_error observation instead of crashing. Give each run a task ID and write the events as JSON Lines. Add a human-approval action for multiplication by values over 100. Replace fake_model with an actual model only after the tests still pass. After this exercise, you should understand that the application—not the language model—owns tools, budgets, state, and termination. Connecting the lesson to MonkeyCode The public MonkeyCode repository describes AI task management and managed development environments for team workflows. It is a useful production-scale project to inspect after learning the small loop: compare how a real platform represents tasks, environments, user input, and validation. The code above is a teaching example and does not describe MonkeyCode internals. Disclosure: I contribute to the MonkeyCode project. I reviewed the linked public documentation; this tutorial does not report a MonkeyCode runtime test. Learners can ask questions in the MonkeyCode Discord . The team can also confirm whether free model credits are currently available and explain eligibility and usage limits. Frameworks become much easier to evaluate once you can point to the loop they are helping you operate.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/magickong/learn-the-agent-loop-without-an-agent-framework-3l5g

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
