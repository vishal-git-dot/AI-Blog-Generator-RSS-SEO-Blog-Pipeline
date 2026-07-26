---
title: "How to Free Up Disk Space as a Developer: Clear Hugging Face, npm, conda, and Docker Caches"
slug: "how-to-free-up-disk-space-as-a-developer-clear-hugging-face-npm-conda-and-docker-caches"
author: "Ripon C Malo"
source: "devto_python"
published: "Sun, 26 Jul 2026 19:00:41 +0000"
description: "If you write code — and especially if you work with machine learning — your disk is quietly filling up with data you downloaded once and forgot about. A mode..."
keywords: "you, cache, model, caches, every, jharu, space, one"
generated: "2026-07-26T19:18:43.418557"
---

# How to Free Up Disk Space as a Developer: Clear Hugging Face, npm, conda, and Docker Caches

## Overview

If you write code — and especially if you work with machine learning — your disk is quietly filling up with data you downloaded once and forgot about. A model you tried for an afternoon. Package caches from five virtualenvs. Docker images from a project you finished months ago. This guide covers where that space goes, how to reclaim it manually, and how to do it all from one place. Where a developer's disk space actually goes The biggest offenders almost never show up in Finder or Explorer, because they're hidden in cache directories: Machine learning model caches These are the heavyweights. A single large language model can be several gigabytes, and most people accumulate dozens. Hugging Face — ~/.cache/huggingface Ollama — ~/.ollama/models PyTorch hub — ~/.cache/torch Whisper — ~/.cache/whisper To clear the Hugging Face cache manually: rm -rf ~/.cache/huggingface/hub The catch: this deletes every model, including the ones you actually use. They'll re-download on demand, but that's a lot of bandwidth if you only wanted to remove one abandoned model. Package manager caches Every language ecosystem keeps a cache to speed up reinstalls. They regenerate automatically, so they're safe to clear: npm cache clean --force # ~/.npm/_cacache pip cache purge # pip download cache conda clean --all # conda packages and tarballs cargo cache --autoclean # Rust crate registry (needs cargo-cache) go clean -cache # Go build cache docker system prune -a # dangling images, containers, build cache Build artifacts and IDE caches Xcode DerivedData — ~/Library/Developer/Xcode/DerivedData (can hit tens of GB) Gradle — ~/.gradle/caches JetBrains IDEs — ~/Library/Caches/JetBrains node_modules in dead projects — often gigabytes each The stuff manual commands miss Two categories that no clean command touches: Duplicated Python packages. Install torch in eight virtualenvs and you have eight copies — often 2–3 GB each. App leftovers. Uninstalling an app on macOS usually leaves its Application Support , Caches , and Preferences behind forever. The problem with cleaning it manually Running these commands works, but it has real downsides: You have to remember every location across every tool you use. rm -rf on a cache is all or nothing — you can't keep the models you use. You can't easily see what's actually taking up space before deleting. It's different on Windows , where the paths change ( %LOCALAPPDATA%\pip\Cache , the registry-based uninstaller, etc.). Doing it all from one place: Jharu Jharu is a free, open-source disk cleaner built specifically for this problem. It runs on macOS and Windows and understands the developer and AI locations above — but instead of blunt deletion, it tells you what each thing is and whether you've used it. Per-model ML cleanup. Jharu lists every Hugging Face, Ollama, PyTorch, and Whisper model individually , with its size and — crucially — whether you've actually loaded it since downloading. So you can reclaim the 6 GB model you tried once without touching the ones you use daily. Shared Ollama layers are preserved, so removing one model never breaks another. Deep cache scan. It scans 25+ known locations (npm, pip, uv, yarn, pnpm, conda, Cargo, Go, Gradle, Maven, NuGet, Docker, Xcode, JetBrains, Playwright, and more), each rated safe to clear , re-downloadable , or review first . Python environment analyzer. It finds every virtualenv and conda environment and quantifies duplication across them — the "torch is installed eleven times" problem, in one view. A treemap of your whole disk. See every folder sized by what it holds, so the biggest space-eater is literally the biggest block. Click to drill in. Clean uninstaller. Removes an app and the leftovers it scattered across your system. Safe by design Nothing is ever permanently deleted — everything goes to the Trash or Recycle Bin, and a dialog tells you the real consequence first. No telemetry, no tracking, no subscription. No registry "cleaner" (it doesn't work), and if Jharu can't read a folder it says so instead of silently hiding it. Get it Jharu is free and open source under Apache 2.0. Download: jharu.matily.org (macOS Apple Silicon + Intel, and Windows 64-bit) Source: github.com/riponcm/Jharu Run one scan and you'll usually find tens of gigabytes you didn't know were there. If you reclaim some space, drop a comment with how much.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/riponcm/how-to-free-up-disk-space-as-a-developer-clear-hugging-face-npm-conda-and-docker-caches-3h21

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
