---
title: "The One Decorator That Makes Your Script Agentic: @mcp.tool() vs. Subprocess"
slug: "the-one-decorator-that-makes-your-script-agentic-mcptool-vs-subprocess"
author: "gentic news"
source: "devto_ai"
published: "Mon, 20 Jul 2026 03:38:18 +0000"
description: "Wrap your Claude Code helper scripts in @mcp .tool() to expose typed, discoverable interfaces agents can reason about—the schema, not the AI call, is what ma..."
keywords: "tool, mcp, your, server, subprocess, claude, you, same"
generated: "2026-07-20T03:39:19.785143"
---

# The One Decorator That Makes Your Script Agentic: @mcp.tool() vs. Subprocess

## Overview

Wrap your Claude Code helper scripts in @mcp .tool() to expose typed, discoverable interfaces agents can reason about—the schema, not the AI call, is what makes it agentic. What Changed — The One Decorator That Makes Your Script Agentic You have a 20-line Python script that generates Conventional Commit messages. It shells out to claude -p , prints a result, and works perfectly when you run python git_commit.py by hand. Then you wrap the same logic in an MCP tool with @mcp.tool() , and suddenly it's "agentic." But why? The author of this Dev.to post diffed the two approaches and found the AI call is identical—same subprocess, same prompt, same OAuth session. The difference is one line: @mcp.tool() . That decorator converts your function's Python signature ( def generate_commit_message(diff: str) -> str ) into a JSON Schema object with a name, description from the docstring, and typed parameters—published over the MCP protocol before any tool is ever called . An agent deciding what to do next reads that schema, not your function body. It knows "this tool takes a string called diff and returns a string." That's the entire interface contract. Your plain script has none of that—it's a black box only a human who already knows to run python git_commit.py can use. What It Means For You — Why Schema Beats Subprocess This distinction bites when you try to let an agent use both interchangeably. The author tried wiring an agent to shell out to git_commit.py directly via a generic bash-execution tool. It failed because the script's failure mode is a print() and a nonzero exit code—fine for a human, useless for an agent parsing stdout/exit-code pairs generically. Is that "expected condition, try something else" or "real error, stop"? The agent has to guess. The MCP tool avoids this because the interface is typed. A -> str return means the agent always gets a message back. Error signaling goes through the protocol's own mechanism, not smuggled through print statements designed for human eyes. Try It Now — Convert Your Scripts to MCP Tools Install the MCP SDK : pip install mcp Create a server file ( server.py ): from mcp.server import Server , Tool server = Server ( " my-tools " ) @server.tool () def generate_commit_message ( diff : str ) -> str : """ Generate a Conventional Commits message from a git diff string. """ # Your existing logic here—same subprocess call as before import subprocess SYSTEM = " You are a commit message generator... " raw = subprocess . check_output ( [ " claude " , " -p " , SYSTEM + " \n\n " + diff ], text = True , ). strip () return raw Wire it into Claude Code : Add to your claude.json or project config: { "mcpServers" : { "my-tools" : { "command" : "python" , "args" : [ "server.py" ] } } } Now Claude Code can discover and call your tool by its schema. The same AI call, but now agentic—because the boundary of what it does is described in a form something other than a human can read. Source: dev.to Originally published on gentic.news

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/gentic_news/the-one-decorator-that-makes-your-script-agentic-mcptool-vs-subprocess-5ddp

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
