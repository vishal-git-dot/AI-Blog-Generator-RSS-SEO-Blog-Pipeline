---
title: "Which Claude Code session is waiting on you? A queue for agents that stopped to ask"
slug: "which-claude-code-session-is-waiting-on-you-a-queue-for-agents-that-stopped-to-ask"
author: "Bargan Constantin"
source: "devto_ai"
published: "Fri, 09 Oct 2026 05:27:18 +0000"
description: "I build ccdeck . The step-by-step version of this post, with every setting, is at ccdeck.dev/guides/waiting-on-you . One silent prompt among many tabs You st..."
keywords: "you, claude, code, waiting, session, one, ccdeck, prompt"
generated: "2026-10-09T05:33:37.108797"
---

# Which Claude Code session is waiting on you? A queue for agents that stopped to ask

## Overview

I build ccdeck . The step-by-step version of this post, with every setting, is at ccdeck.dev/guides/waiting-on-you . One silent prompt among many tabs You start four Claude Code sessions in four repositories, switch to something else, and come back twenty minutes later. Three of them are done. The fourth stopped two minutes after you left, on a permission prompt for a Bash command, and has been sitting there since. Nothing told you. From the outside every terminal tab looks the same — the one that is working and the one that is waiting. You find the stuck one by clicking through them, and it is usually the one that was closest to finished. The scarce resource is not tokens. It is your attention , and the cost is the time an agent spends waiting for you without you knowing. Claude Code already knows — it tells nobody Claude Code has a hook event for exactly this: Notification . It fires when: Claude Code wants to use a tool and is waiting for your permission; the agent stopped to ask you a question; a turn finished and the session has been idle, waiting for your next instruction (Claude Code reports that about a minute after the turn ends). A hook can listen for it. The problem is that a hook in each terminal still talks to only that terminal. What you want is one place that collects them all . npx ccdeck npx ccdeck On its first run, ccdeck adds a hook to ~/.claude/settings.json for the Notification event and nine others. Each event is POSTed to the deck on 127.0.0.1 , and the deck opens at http://127.0.0.1:4317 . The hook cannot steer your agent . Claude Code's hook protocol gives a hook two channels to allow, deny or rewrite a tool call — the exit code and stdout — and this one always exits 0 and prints nothing. It forwards; it never answers. (Install details, the desktop app, and every option are in the first-run guide .) The queue Press L to open the session list. A session stopped on you moves to the top, and its run time is replaced by how long it has been waiting : Demo data. The order is deliberate: Permission prompts and questions first — the agent cannot go on at all. Then finished turns waiting for your next instruction. Within each group, the longest wait first. So a turn that finished 12 minutes ago sits below a prompt from 2 minutes ago, because the prompt is the one actually blocking work. Jump straight to the oldest The topbar shows an amber count of sessions blocked on a prompt or a question: Demo data. Click it, or press W : the deck selects the session that has waited longest, brings its card on screen and opens its detail panel. Each further W goes to the next one. While the count is above zero, the browser tab title reads (2) ccdeck and its icon turns into an amber disc, so you can see it from any other tab. On the card itself, an amber row holds the start of Claude Code's own sentence and a clock: Demo data. For a finished turn the row reads Your turn instead. Either way, you answer in the terminal where Claude Code is running, and the row goes away as soon as the session moves again. When you are not looking at the page Sounds. V opens the Sound menu: one tone when a turn finishes, another when Claude is asking. M mutes from anywhere. Notifications. Switch on Notifications while closed in the same menu. With the deck's tab hidden, each new prompt or question raises a browser notification; with no deck tab open at all, you get a system notification instead. Click it to land on that session. The desktop app puts the count in the menu bar on macOS (in the tray tooltip and menu on Windows and Linux), so you do not need a tab open at all. Demo data. What it does not do I would rather you know the limits before you install it: It cannot answer for you. The hook only forwards, so the deck cannot allow, deny or reply. You still switch to the terminal. Claude Code only. Codex CLI is drawn on the same canvas, but the deck reads Codex from its rollout log, and that log records no approval request, so a Codex session is never marked waiting. (Codex's app-server does report a waiting status; reading it is open work.) The tool name is a guess. "waiting 6m · Bash" names the newest call still running when the prompt arrived, if it started within 30 seconds of it. Claude Code does not report it. Hover the time for Claude Code's own sentence. Ninety minutes. A session that sends nothing for 90 minutes stops showing as waiting. Try it npx ccdeck Then start a Claude Code session, ask it to run something that needs permission, and switch away. When the prompt appears, the session moves to the top of the list with a clock beside it. Guide: https://ccdeck.dev/guides/waiting-on-you/ Repo: https://github.com/BarganConstantin/ccdeck (AGPL-3.0)

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/bargan/which-claude-code-session-is-waiting-on-you-a-queue-for-agents-that-stopped-to-ask-1ok9

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
