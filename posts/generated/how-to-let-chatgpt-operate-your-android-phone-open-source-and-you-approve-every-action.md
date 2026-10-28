---
title: "How to let ChatGPT operate your Android phone (open source, and you approve every action)"
slug: "how-to-let-chatgpt-operate-your-android-phone-open-source-and-you-approve-every-action"
author: "RYO ITABASHI"
source: "devto_ai"
published: "Wed, 28 Oct 2026 04:54:09 +0000"
description: "The ChatGPT app can't touch your phone. But its Codex mode can drive a machine you pair with it, and that machine can be the phone itself. This post shows ho..."
keywords: "phone, chatgpt, shelly, codex, app, approve, your, can"
generated: "2026-10-28T05:00:43.286269"
---

# How to let ChatGPT operate your Android phone (open source, and you approve every action)

## Overview

The ChatGPT app can't touch your phone. But its Codex mode can drive a machine you pair with it, and that machine can be the phone itself. This post shows how to set that up with Shelly , an open-source Android terminal, so ChatGPT can run commands and phone-app tasks on your device. Every phone action waits for your approval on the phone. Everything here runs on the phone. No PC, no Termux, no root. What you need An arm64 Android phone . I develop on a Galaxy Z Fold6; other devices aren't verified yet. A ChatGPT account with access to Codex in the ChatGPT app. Shelly (GPL-3.0): APK from GitHub Releases . For tasks inside other apps (Spotify, Maps…): the ClosePaw Shelly build from its releases page , plus Shizuku . Terminal-only tasks don't need these. Step 1: Install Shelly and sign in to Codex Install the APK and allow "All files access" on first launch. Then, in Shelly's terminal: codex If you're not signed in yet, Shelly starts ChatGPT's device-code login in its built-in browser pane. It uses your ChatGPT subscription, not an API key. Step 2: Pair the phone with the ChatGPT app shelly codex pair This runs the official codex remote-control on the phone and prints a pairing code. In the ChatGPT app, open Codex, add a remote machine, and enter the code. The phone now shows up as a machine in ChatGPT. To keep the connection alive across app restarts and network changes, turn on Settings → Codex Login → Keep ChatGPT connected . Step 3: Ask for something Plain terminal tasks work right away: On this phone, show me how much free storage is left. Reply in English. For a task inside another app, name the tool so Codex knows how to reach the phone's UI: On this phone, open the Spotify app and save the playlist "Grunge Forever" to my library. Use shelly closepaw --wait . Reply in English. Codex runs shelly closepaw --wait "<goal>" in the phone's terminal. Shelly then posts a notification asking you to approve. Approve it (the notification needs the device unlocked), and ClosePaw operates Spotify on a background virtual display while your screen stays yours. When it finishes, the result goes back to ChatGPT, which tells you what happened. Why approval lives on the phone If ChatGPT could approve its own actions, a web page it read could quietly add "…and also do this", and nobody would see it happen. So: Only the phone owner can approve: the notification button (with the device unlocked), or approve <hash> typed in Shelly's own chat. ChatGPT can't approve. Writing an "approved" file from the shell doesn't work either, because the one-time nonce exists only in Shelly's process memory. The result coming back has to come from the signature-pinned ClosePaw build and carry the request's nonce. It's passed to ChatGPT as data, not as instructions. Prompt rules like "never approve yourself" aren't a security boundary. The approval has to live somewhere the model can't reach. Things that tripped me up Codex gives up on quiet commands. If a command prints nothing for about 10 seconds, Codex tends to end its turn. shelly closepaw --wait prints progress lines and an explicit "keep waiting" so the result makes it back into the same chat turn. Say "on this phone" and name the tool. Without that, Codex looked for a Spotify plugin, or tried am start , which Samsung's Knox blocks for apps. Ask for English explicitly if your account usually answers in another language. Limits, honestly Verified end-to-end on one device (N=1). Phone-app tasks depend on ClosePaw reading the screen. Long multi-step tasks (like adding 10 songs one by one) were unreliable in my tests. Short, concrete goals work best. The APK is big because it bundles bash, git, Python, Node and the Codex CLI. Beyond ChatGPT Shelly is also a full terminal (bash, git, Python 3, Node.js, ssh, tmux, vim bundled), with multi-pane AI chat, local LLMs, and scheduled agents that wake on the phone's alarm and save sourced notes to Markdown or Obsidian. Source and releases: github.com/RYOITABASHI/Shelly . Bug reports and results from other phones are very welcome.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/ryoitabashi/how-to-let-chatgpt-operate-your-android-phone-open-source-and-you-approve-every-action-1mi6

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
