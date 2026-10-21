---
title: "You can answer Claude Code's AskUserQuestion from a hook (and from your phone)"
slug: "you-can-answer-claude-codes-askuserquestion-from-a-hook-and-from-your-phone"
author: "Dawon Lee"
source: "devto_ai"
published: "Wed, 21 Oct 2026 11:26:55 +0000"
description: "Claude Code sometimes stops and asks you a multiple-choice question with the AskUserQuestion tool ("Which framework?", "Keep the old API or replace it?"). If..."
keywords: "hook, claude, you, askuserquestion, question, permissionrequest, allow, answer"
generated: "2026-10-21T11:30:28.806796"
---

# You can answer Claude Code's AskUserQuestion from a hook (and from your phone)

## Overview

Claude Code sometimes stops and asks you a multiple-choice question with the AskUserQuestion tool ("Which framework?", "Keep the old API or replace it?"). If you're away from the terminal, the run just sits there. The hooks docs describe answering it in -p mode: a PreToolUse hook returns allow plus an updatedInput that carries the answers. I wanted to know if the same works in a normal interactive session through a PermissionRequest hook, so I tested it on Claude Code 2.1.283. It does. What the hook receives When Claude calls AskUserQuestion in an interactive session, a PermissionRequest hook gets this on stdin (trimmed): { "hook_event_name" : "PermissionRequest" , "tool_name" : "AskUserQuestion" , "tool_input" : { "questions" : [ { "question" : "Which color do you want?" , "header" : "Color" , "options" : [ { "label" : "Red" , "description" : "red" }, { "label" : "Blue" , "description" : "blue" } ], "multiSelect" : false } ] } } What the hook returns Copy tool_input , add an answers object that maps each question's text to the chosen label (comma-separated for multi-select), and return it as updatedInput with behavior: "allow" : { "hookSpecificOutput" : { "hookEventName" : "PermissionRequest" , "decision" : { "behavior" : "allow" , "updatedInput" : { "questions" : [ ...same as input... ], "answers" : { "Which color do you want?" : "Blue" } } } } } Claude Code then shows: ⏺ User answered Claude's questions: ⎿ · Which color do you want? → Blue ⎿ Allowed by PermissionRequest hook and Claude continues with "Blue". No terminal prompt appears. A minimal test hook #!/bin/sh # Answers every AskUserQuestion with the last option. For testing only. python3 -c ' import json, sys d = json.load(sys.stdin) if d.get("tool_name") != "AskUserQuestion": sys.exit(0) # no decision: the normal permission prompt shows ti = d["tool_input"] ti["answers"] = {q["question"]: q["options"][-1]["label"] for q in ti.get("questions", [])} print(json.dumps({"hookSpecificOutput": {"hookEventName": "PermissionRequest", "decision": {"behavior": "allow", "updatedInput": ti}}})) ' Register it under hooks.PermissionRequest in a settings file and try claude --settings test-settings.json . Two things to watch allow alone doesn't answer the question. If your approval hook (or an approval app) just returns allow for AskUserQuestion , the question stays open and the session still waits. I hit exactly this: my phone approval said "allowed", but Claude was still waiting. The hook blocks until it returns. To answer from somewhere else, the hook has to wait for that answer (and give up before the hook timeout so the terminal prompt still works). Using it from a phone I build Lidnight , a menu bar app that keeps a Mac awake while Claude Code and Codex work. Version 1.7.79 uses this: when Claude asks a question, the options show up on the phone status page (end-to-end encrypted) and in the Mac menu bar, and the one you tap goes back to Claude through the hook. You can still answer in the terminal; whichever comes first wins.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/dawonlee/you-can-answer-claude-codes-askuserquestion-from-a-hook-and-from-your-phone-1ddn

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
