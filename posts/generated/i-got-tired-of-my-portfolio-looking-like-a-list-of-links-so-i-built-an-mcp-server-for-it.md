---
title: "I Got Tired of My Portfolio Looking Like a List of Links. So I Built an MCP Server for It."
slug: "i-got-tired-of-my-portfolio-looking-like-a-list-of-links-so-i-built-an-mcp-server-for-it"
author: "Ayush Singh Tomar"
source: "devto_python"
published: "Mon, 06 Jul 2026 03:30:13 +0000"
description: "The obvious fix for "my projects all look similar" is a better README — more screenshots, clearer descriptions, maybe a comparison table. I considered that f..."
keywords: "what, claude, tool, mcp, server, project, built, you"
generated: "2026-07-06T04:05:09.365175"
---

# I Got Tired of My Portfolio Looking Like a List of Links. So I Built an MCP Server for It.

## Overview

The obvious fix for "my projects all look similar" is a better README — more screenshots, clearer descriptions, maybe a comparison table. I considered that for about five minutes and decided it was still just a nicer list of links. What actually made a portfolio project feel different was making it something you could talk to instead of read. That's what MCP (Model Context Protocol) is built for — it's the standard that lets AI clients like Claude Desktop call external tools directly, not just process text. So I built a server that exposes my 9 projects as queryable tools instead of static entries. What is MCP, and why does it matter here Almost every AI-developer portfolio I've seen is a list of links. Mine now includes something you can actually talk to . Open Claude Desktop, connect my server, and ask "what has Ayush built with FastAPI?" — it doesn't guess from a cached README, it calls a real tool and answers from structured, live data. What I built A Python MCP server ( FastMCP , stdio transport) exposing five tools: list_projects — short summary of all 9 projects get_project_details(project_name) — full stack, GitHub link, demo URL for one project, fuzzy-matched by name search_projects_by_stack(technology) — "show me everything using Groq" or "LangGraph" or "React" get_flagship_project — the single best project to look at first get_resume_summary — background, target role, core stack The data itself lives in plain Python dictionaries right now — no database needed for something this size. Each tool is a thin function around that data, decorated with @mcp.tool() . @mcp.tool () def search_projects_by_stack ( technology : str ) -> list [ dict ]: """ Find all projects that use a given technology or tool. """ query = technology . lower (). strip () matches = [ { " name " : p [ " name " ], " stack " : p [ " stack " ], " github " : p [ " github " ]} for p in PROJECTS if any ( query in tech . lower () for tech in p [ " stack " ]) ] return matches or [{ " message " : f " No projects found using ' { technology } '" }] What actually broke The concept is simple. The setup had four separate rabbit holes: 1. MCP Inspector defaults to uv , not plain Python. Running mcp dev server.py opens a UI that assumes your project uses the uv package manager by default. If you're on a plain venv + pip setup, the command field needs to be manually changed to python with server.py as the argument, or it never connects. 2. Claude Desktop as a Windows Store app uses a different config path entirely. I'd installed it via the Microsoft Store first. The standard setup instructions all point to %APPDATA%\Claude\claude_desktop_config.json — which doesn't exist for the Store version, which stores its config somewhere under AppData\Local\Packages\... instead. Uninstalling and reinstalling the direct .exe from claude.ai/download fixed it. 3. Two nearly-identical config files. Once the real app was installed, there's a config snippet file in your own project folder (for reference) and the actual app config file (found via Settings → Developer → Edit Config). They can look identical at a glance. I edited the wrong one twice before I noticed the tab breadcrumb showing which was real. 4. The model doesn't always call your tool just because it's connected. My first test — "what projects has Ayush built with FastAPI?" — got answered from Claude's own internal guesswork instead of actually calling my server, and got a detail wrong as a result (called ResumeIQ a FastAPI project; it's Flask). Naming the tool or server explicitly in the prompt ("use the portfolio tool to search for...") forced an actual tool call, which then returned correct data every time. Seeing it work Once connected, this is what a real session looks like: Me: What's Ayush's flagship project and why? (Claude Desktop shows: "Claude wants to use Get flagship project from portfolio" — Always Allow / Deny) Claude: Your flagship is SalesAgent — an autonomous B2B sales agent that takes a LinkedIn URL, researches the lead, scores them with an ML model (84/100 accuracy), and drafts a hyper-personalized cold email, all in under 45 seconds. Why it's the flagship: full-stack complexity (LangGraph + FastAPI + React + scikit-learn scoring), not a thin API wrapper around an LLM call... That permission dialog matters — it's proof this is a real, sandboxed tool call happening live, not a scripted response. Try it yourself Repo: https://github.com/ayush-s-tomar/portfolio-mcp-server Connect it to your own Claude Desktop in under 10 minutes — full setup instructions in the README. If you're building an AI-developer portfolio and every project you have looks the same shape as the last one, this is a cheap way to add something structurally different: not another agent, but the plumbing that lets other agents actually use what you've built. What would you expose if you built one of these for yourself?

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/ayushsinghtomar/i-got-tired-of-my-portfolio-looking-like-a-list-of-links-so-i-built-an-mcp-server-for-it-440o

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
