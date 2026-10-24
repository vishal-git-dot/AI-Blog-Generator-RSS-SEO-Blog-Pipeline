---
title: "Sloth AI Folder Tidier: Let Open-Source AI Clean Your Downloads Folder So You Don't Have To"
slug: "sloth-ai-folder-tidier-let-open-source-ai-clean-your-downloads-folder-so-you-dont-have-to"
author: "Viktor"
source: "devto_python"
published: "Sat, 24 Oct 2026 10:02:48 +0000"
description: "This is a submission for the Hacktoberfest Open-Source AI Challenge Week 3: Slow and Steady What I Built Let’s be honest about the Downloads folder. For most..."
keywords: "open, folder, files, sloth, models, you, file, code"
generated: "2026-10-24T10:39:36.551410"
---

# Sloth AI Folder Tidier: Let Open-Source AI Clean Your Downloads Folder So You Don't Have To

## Overview

This is a submission for the Hacktoberfest Open-Source AI Challenge Week 3: Slow and Steady What I Built Let’s be honest about the Downloads folder. For most developers and students, it is a digital graveyard. Mine had accumulated exactly 962 files—a chaotic mix of university PDFs, C# snippets, .jar game mods, audio tracks, and 40 different setup_v2_final(1).exe installers. Why don't I clean it? Because of the Hoarder’s Paradox: I am way too lazy to sort nearly a thousand files manually. I am too paranoid to bulk-delete anything because "what if I need that random file from 4 months ago?!" To channel my inner sloth for International Sloth Day, I built Sloth AI Folder Tidier—an automated file organizer designed specifically for lazy digital hoarders. Instead of blindly sorting by file extension, it scans file age, size, and peeks at the first 150 characters of text/code files. Using open-weight models, it understands context and neatly organizes chaos into logical folders (University_& Docs, Code & Dev, Gaming & Mods, Media &_Music, etc.) with three golden safety rules: Zero-Deletion Policy: The script literally does not contain a delete function. Nothing is ever lost. The Sloth Vault (Sloth_Vault_Old): If an installer or archive hasn't been touched in over 30 days, the AI quarantines it. Out of sight, out of mind, but still there if you panic. 1-Click Undo (--undo) & Dry-Run (--dry-run): Every move is logged locally. One command reverts your entire folder back to its original messy state in 1 second. Demo Code Shadow16Ua / Sloth-Folder-Tidier How I Built It The project is a Python CLI built around fast, open-weight models (qwen/qwen3.8-27b and openai/gpt-oss-20b) running via the Groq API. Metadata & Micro-Context Extraction: Rather than uploading whole files, the script uses pathlib and os.stat to extract lightweight metadata (filename, extension, age in days, size) and reads a tiny 150-character preview for plain-text/code files. Structured JSON Batching: To process hundreds of files efficiently without hitting rate limits, the script chunks the files into batches of 15. These are passed to the model with response_format={"type": "json_object"}, forcing the open-weight model to act as a deterministic routing engine rather than a chatty assistant. State Reversibility: Every shutil.move operation is recorded in a sloth_history.json state file, allowing deterministic rollback. Why Does Open Innovation Matter? When building a tool that inspects your personal filesystem, open-source AI isn't just a nice-to-have — it’s mandatory: Privacy of Personal Files: Nobody wants to send a list of their private university documents, local source code, and personal filenames to a closed, proprietary corporate cloud that trains on user prompts. Because this architecture uses standard open-weight models, you can run it via fast zero-retention APIs (like Groq) or eventually swap the base URL to run it 100% offline via Ollama. Set It and Forget It (Zero Cost): A folder tidier is a background utility you run weekly. Using highly capable, smaller open models means inference is practically free, allowing a true "set it once and be lazy forever" workflow. Model Swappability: Closed APIs lock you in. While building this, several models were decommissioned on my inference provider. Because I was using open models, I simply swapped my array from gemma2-9b-it to qwen3.8-27b and gpt-oss-20b in exactly five seconds without rewriting a single line of parsing logic. The Lazy Payoff I am my own first user. My Downloads folder had 962 files spanning over a year of university assignments and freelance coding projects. Sorting that manually would have taken at least an hour of tedious dragging and dropping. With this script, I typed one command, leaned back, and watched the AI process 65 batches in a few seconds. My folder is completely clean, my old installers are quarantined in the vault, and I didn't have to lift a finger or make a single decision. Pure sloth perfection!

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/shadow16ua/sloth-ai-folder-tidier-let-open-source-ai-clean-your-downloads-folder-so-you-dont-have-to-g6m

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
