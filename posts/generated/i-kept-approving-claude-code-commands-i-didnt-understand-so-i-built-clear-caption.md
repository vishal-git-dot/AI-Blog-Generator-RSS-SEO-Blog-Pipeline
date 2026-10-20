---
title: "I kept approving Claude Code commands I didn't understand, so I built clear-caption"
slug: "i-kept-approving-claude-code-commands-i-didnt-understand-so-i-built-clear-caption"
author: "Kashif Manzer"
source: "devto_ai"
published: "Tue, 20 Oct 2026 21:18:54 +0000"
description: "I approve dozens of commands from Claude Code every day. Most I skim. Some I don't really understand, especially the long, complex ones. I click yes anyway a..."
keywords: "caption, one, claude, clear, you, call, not, captions"
generated: "2026-10-20T21:26:05.883186"
---

# I kept approving Claude Code commands I didn't understand, so I built clear-caption

## Overview

I approve dozens of commands from Claude Code every day. Most I skim. Some I don't really understand, especially the long, complex ones. I click yes anyway and hope nothing breaks. Like everyone else. So I built clear-caption. Now, before anything runs, Claude tells me in plain English what it is about to do. A command, a file edit, doesn't matter. One quiet line above the call, in words I can actually read. The real command stays on screen, unchanged. Nothing gets hidden or rewritten. The caption just sits above it. What it looks like Before, a normal session looked like this: ● Bash ( find . -name "*.tmp" -exec rm {} \; ) ● Bash ( git reset --hard HEAD ) ● Update ( math.js ) Three calls. One deletes files by pattern, one throws away local work, one edits code for a reason you have to guess from the diff. With clear-caption, the same session looks like this: ● clear-caption: Delete all .tmp files ● Bash(find . -name "*.tmp" -exec rm {} \;) ● clear-caption: ⚠ Throw away all local changes ● Bash(git reset --hard HEAD) ● clear-caption: Fix clamp: Math.min should cap at hi, not lo. ● Update(math.js) That is the whole idea. Reviewing a step takes a glance instead of a decode. What gets a caption Every shell command and every subagent call gets one. It is the call's own description, shown right above its row. Every file edit gets one too. Edit and Write have no description of their own, so the mod asks Claude to write one sentence on why the file is changing, and shows it above the diff. Subagents' own calls stay quiet. A busy subagent running twenty commands should not flood your screen with captions, so only the top level gets them. Captions are also their own lines, separate from the tool rows. If you use a skin or another mod that redraws those rows, the captions still show. The warning is the part I wanted most Some commands can wipe out your work in one keystroke. Those get a ⚠ in the caption, even when the description sounds harmless. The warning is based on the real command, not on what Claude says about it. It triggers on things like: Recursive deletes ( rm -r ) outside temp folders Commands that throw away git work, like git reset --hard , git clean -f , git branch -D , or dropping and clearing stashes Force pushes Deletes by search ( find ... -delete ) sudo , piping curl into a shell, or chmod -R Deleting files only under /tmp or a scratchpad folder is not flagged. Cleanup in a temp folder is normal work, not a risk. It is a short list of common spellings, matched as patterns. It is not a guarantee, and I won't pretend otherwise. It catches the stuff people actually type, which is where the accidents live. Turn it up or down /caption all every caption (default) /caption risky only ⚠ captions /caption off no captions /caption show the current setting Your choice is saved, so it carries across sessions. If you only want the safety net and none of the narration, /caption risky is a good place to start. The honest limits The caption is Claude's own words. It can be vague, and it can be wrong. That is exactly why the real command and the real diff always stay on screen. The caption is a reading aid, not a replacement for the call itself. On testing: edit captions landed on 57 of 57 edits across Opus, Sonnet, and Haiku. The average cost on the Opus test tasks was the same with captions on or off, for about 3% more output tokens. It is built on Claude Code's mod hooks, which are early access. Hooks can change between releases, so things may shift. It is tested on Claude Code 2.1.296. How it works, briefly Two hooks do the work. One asks Claude for a one-line description on Edit and Write calls, then strips that description out before the call is checked, so the edit itself runs exactly as it would have. The other holds each call until its arguments arrive, logs the caption, and passes the call on unchanged. Install Paste this at the Claude Code prompt: /plugin install clear-caption --marketplace KashifManzer/clear-caption Answer y to add the marketplace, pick a scope, and you are done. It is free and open source under the MIT license. The repo is here: https://github.com/KashifManzer/clear-caption If it saves you a squint, a star helps other people find it. Bug reports, ideas, and pull requests are all welcome too. One question before you go. Have you ever approved something you didn't fully understand?

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/kashif_manzer/i-kept-approving-claude-code-commands-i-didnt-understand-so-i-built-clear-caption-a64

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
