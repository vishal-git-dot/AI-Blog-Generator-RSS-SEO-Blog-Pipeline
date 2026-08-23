---
title: "How GitFlow Three-Tree Architecture Works"
slug: "how-gitflow-three-tree-architecture-works"
author: "weskibet"
source: "devto_webdev"
published: "Sun, 23 Aug 2026 12:39:50 +0000"
description: "Introduction In your journey into tech, no matter which path you take, you will always come across Git and GitHub, and on your first encounter, you'll wonder..."
keywords: "you, your, git, how, github, repository, staging, area"
generated: "2026-08-23T12:50:17.232512"
---

# How GitFlow Three-Tree Architecture Works

## Overview

Introduction In your journey into tech, no matter which path you take, you will always come across Git and GitHub, and on your first encounter, you'll wonder: what is this thing people keep talking about? Why do I need it? Why do devs talk about it like it's a fire Spotify playlist? Worry not, I am here to debunk it and make you understand why it's like Spotify Wrapped to devs. Git and GitHub are basically the same; the only difference is that Git is local, i.e., it sits on your machine and acts as a bridge for you to connect and push your code to the cloud repository, i.e GitHub. For many devs, GitHub acts as their Spotify Wrapped, as it showcases how active they were during a month based on how many projects they pushed throughout the year, so if you are a dev trying to sharpen your skill, don't worry about people judging your Spotify Wrapped, worry about how many projects you pushed to GitHub throughout the year _(not an easy thing to achieve but with dedication, your GitHub "heat map" can be that of pros if you do small projects every day) _ How It Works and Its Three-Tree Architecture Enough of the introduction, let's commit and get right into it. Git organizes projects into three distinct trees; Working Directory : This is where you actively edit your files on your local machine. Staging Area (Index) : This is where you prepare your files to ensure you don't push files that include your keys. Repository (HEAD) : This is where all your files are saved and committed permanently until you decide to go anonymous with zero trails. For each part of the tree, below are the commands that you will use: git add. (From Working Directory to Staging Area) It stages current changes (Stages means to put something in line for the next course of action) git add. git commit -m "message (From Staging Area to Repository) It saves the staged changes permanently and allows you to write the message about the changes included in the file. git commit -m "This is my first article" git checkout -- (From Repository to Working Directory) It discards all local modifications git checkout -- <file> git reset HEAD (From Repository to Staging Area) It helps to remove a file from the staging area without losing edits. git reset HEAD <file> In Conclusion... There are a myriad of other Git commands; watch this space for more of them. I will walk through each, step by step, and help you understand what each means and how they can help you in your tech journey of becoming the best in your domain of choice.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/weskibet/how-gitflow-three-tree-architecture-works-1kcn

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
