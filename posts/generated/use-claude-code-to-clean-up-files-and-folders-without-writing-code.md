---
title: "Use Claude Code to clean up files and folders without writing code"
slug: "use-claude-code-to-clean-up-files-and-folders-without-writing-code"
author: "Konstantin Konovalov"
source: "devto_ai"
published: "Thu, 23 Jul 2026 14:10:00 +0000"
description: "Claude Code isn't only for code Most people install Claude Code to work on a repo. But under the hood it's a terminal agent with permission to read files, ru..."
keywords: "you, files, can, folder, run, read, claude, code"
generated: "2026-07-23T14:15:19.716539"
---

# Use Claude Code to clean up files and folders without writing code

## Overview

Claude Code isn't only for code Most people install Claude Code to work on a repo. But under the hood it's a terminal agent with permission to read files, run shell commands, and edit text. Point that at a folder full of PDFs, screenshots, invoices, or CSV exports and it becomes a general file assistant. You describe the outcome in plain language, and it figures out the mv , find , and mkdir calls. You never have to see the script unless you ask for it. But it does run those commands for real, so the whole skill here is describing the job precisely and keeping the agent on a short leash. Four jobs it handles well, plus how to fence it in. 1. Rename Downloads folders rot into IMG_4821.jpg , Scan (3).pdf , final_v2_FINAL.docx . Describe the naming scheme you want and let it read the files to fill in the blanks. Rename every PDF in this folder to YYYY-MM-DD_vendor_amount.pdf . Read each file to get the date and vendor. Show me the full rename list before touching anything. Because it can open the PDFs, it pulls the date and vendor from the content, not just the filename. For photos it can read EXIF dates. Ask for the mapping first ( old -> new ) so you catch a wrong guess before 200 files move. 2. Sort "Put things where they belong" is tedious for a human and trivial for an agent. Sort this directory into subfolders by file type: images, docs, spreadsheets, archives, other. Create the folders if missing. Don't touch existing subfolders. You can sort by anything it can infer: file extension, creation month, a project name inside the filename, or even topic after reading the contents. Sorting a research dump by subject matter is something a plain shell script can't do, and that's where an agent actually beats one. 3. Gather Collecting scattered files is the inverse of sorting. Find every .csv under this folder and its subfolders, copy them into ./collected-csv/ , and if two files share a name, add a numeric suffix instead of overwriting. Say copy, not move, on the first pass. Same idea for pulling all invoices from twelve project folders into one place for accounting, or every .env.example in a monorepo into a single checklist. 4. Report Once it can read a tree, it can summarize it. Walk this folder and write INVENTORY.md : a table of each file with size, modified date, and a one-line description of what it contains. Sort by size, largest first. This is the highest-value job because the output is new information: a manifest for a client handoff, a list of the ten biggest files eating your disk, or a quick answer to "what even is this archive I downloaded in 2019." It reads and writes, but changes none of your originals, so it's also the safest place to start. Writing the task so it actually works A few habits separate a clean run from a mess. State the input and the output. "Rename the PDFs in this folder" beats "clean up my files." Name the scope explicitly. Ask for a plan before execution. Add "show me what you'll do first" or "dry run only." You review the list, then say go. Give it the edge cases. Duplicate names, missing dates, files that don't match the pattern. Tell it what to do with each, or it will guess. Prefer copy over move until you trust the result on that specific folder. Safety: the part people skip This agent runs real commands on real files. Treat it like handing someone your terminal. Scope the directory. Start Claude Code inside the folder you want changed, not your home directory. If it can only see ~/Downloads/sorting-test , it can't wander. Make it undoable. Run git init in the folder, or copy it once, before a destructive run. If a rename goes sideways, you reset instead of grieving. Read before you approve. When it proposes a find ... -delete or a bulk mv , actually read it. Denying one command costs a second; recovering deleted files can cost your afternoon. One folder at a time. Verify on a small copy, then point it at the real thing. None of this is Claude-specific paranoia. It's the same caution you'd want before running any script you didn't write line by line. Where this is weaker For a job you run every day on a fixed pattern, a five-line shell script or a Hazel/Automator rule is faster and free after you write it once; the agent re-reasons the whole thing every time and spends tokens doing it. It's also probabilistic: across a thousand files it can misclassify a handful, so the report step or dry run isn't optional at scale. And reading file contents to decide names or categories is powerful but slower and pricier than matching on extensions. Use it where the judgment is fuzzy and the volume is human-sized. Reach for a real script where the rule is crisp and runs forever. The sweet spot is the one-off messy job: the folder you'd never bother scripting for, but really don't want to click through by hand. I write about turning AI from a chat toy into a working tool. I help build AGINE Academy , a game-based academy for learning Claude by real practice. It is an independent product and is not affiliated with Anthropic.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/academy_agineai/use-claude-code-to-clean-up-files-and-folders-without-writing-code-4el8

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
