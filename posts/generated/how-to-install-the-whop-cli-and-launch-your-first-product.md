---
title: "How to Install the Whop CLI and Launch Your First Product"
slug: "how-to-install-the-whop-cli-and-launch-your-first-product"
author: "Karina Egle"
source: "devto_webdev"
published: "Tue, 28 Jul 2026 14:19:17 +0000"
description: "If you sell anything through Whop , there's now a faster way to run it than clicking around a dashboard. Whop's new command-line tool lets you manage your st..."
keywords: "you, whop, command, your, one, install, terminal, what"
generated: "2026-07-28T14:22:20.798661"
---

# How to Install the Whop CLI and Launch Your First Product

## Overview

If you sell anything through Whop , there's now a faster way to run it than clicking around a dashboard. Whop's new command-line tool lets you manage your store by typing short commands in a terminal. Never used a terminal? It's just a plain text window that's already on your computer, called Terminal on a Mac or Command Prompt on Windows. The setup takes a few minutes, and you'll do something useful by the end of it. Here's the whole thing, start to finish. What you'll need A Mac or Linux machine handles this with one command. On Windows, or anywhere you like, you can install through npm, which needs Node.js 22 or newer. That's the only prerequisite. No Node? Installing it first is a quick detour. Step 1: Install it Open your terminal, paste this, and hit enter: curl -fsSL https://whop.com/install.sh | sh On Homebrew, brew install whopio/tap/whop does the same job. On npm, it's npm install -g @whop/cli . Any of the three gets you the same tool. Check that it worked: whop --version See a version number? You're set. If the terminal says it can't find the command, close the window, reopen it, and try again. Step 2: Sign in Type the command on its own: whop Your browser opens and asks you to log into Whop. Approve it, and it asks which business you want to manage. Pick one and you're connected. You won't repeat this every time; the tool remembers you. Running more than one business? whop quickstart switches between them later. Step 3: Look around Before you make anything, see what's already there: whop products list Handy thing to know: almost every command follows the same pattern. It's whop, then what you're working with, then what you want to do, like list, get, create, or update. Forget the options? Add --help to any command and it explains itself: whop plans create --help Step 4: Make a checkout link This is where the setup pays off. Once you've got a plan, one command gives you a ready-to-share checkout link: whop checkout-configurations create --plan_id plan_xxx Swap plan_xxx for your real plan ID (the list commands show you those). What comes back is a checkout URL you can paste into an email, a post, or a message to a customer. No dashboard, no hunting for a share button. Step 5: Check your numbers When you want a quick read on how things are going: whop stats time_series That pulls your figures right into the terminal. One tip, one caution The tip: add --format json to any command and you get raw data instead of a formatted table, handy if you want to drop it into a spreadsheet later. The caution: these commands run instantly. There's no "are you sure?" before something happens. That's fine for listing products or making checkout links. Slow down before anything that moves money or changes a live price, and read what a command does before you run it, especially early on. That's the setup Install is one command, sign-in is one more, and after that you're running your store in short lines of text. Want to practice safely first? Make a test product and delete it before you touch anything real. The Whop CLI docs have the full list of commands, with every option explained.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/egledigital/how-to-install-the-whop-cli-and-launch-your-first-product-212f

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
