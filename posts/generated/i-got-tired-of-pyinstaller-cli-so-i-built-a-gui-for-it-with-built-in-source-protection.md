---
title: "I Got Tired of PyInstaller CLI, So I Built a GUI for It With Built-in Source Protection"
slug: "i-got-tired-of-pyinstaller-cli-so-i-built-a-gui-for-it-with-built-in-source-protection"
author: "ARIAN"
source: "devto_python"
published: "Tue, 28 Jul 2026 08:20:13 +0000"
description: "if you've ever tried to package a Python project into a .exe , you've probably wanted to throw your laptop out the window. pyinstaller --onefile works great ..."
keywords: "you, pyinstaller, pypack, your, build, project, import, one"
generated: "2026-07-28T08:43:31.569043"
---

# I Got Tired of PyInstaller CLI, So I Built a GUI for It With Built-in Source Protection

## Overview

if you've ever tried to package a Python project into a .exe , you've probably wanted to throw your laptop out the window. pyinstaller --onefile works great for a hello-world script. But the second your project gets real custom icons, data files, hidden imports, two different Qt bindings somehow it all falls apart. No helpful error messages either. Just a blank window staring back at you. I dealt with this for way too long. Eventually I just decided to fix it myself. That's how PyPack was born. Why PyInstaller Made Me Cry My project was a desktop app. CustomTkinter UI, custom .ico , a couple of config files bundled in. Nothing crazy. But to build it with PyInstaller, I needed something like this: pyinstaller --onefile --windowed --icon = app.ico --name = MyApp \ --add-data = "assets:assets" \ --hidden-import = module1 --hidden-import = module2 \ --exclude-module = PyQt5 \ --exclude-module = PyQt6 \ ... Forget one hidden import? Build breaks. No error. Just silence. Then you spend an hour on Stack Overflow figuring out that tkinter.ttk needs a separate flag. Yeah, I got real tired of that. So What Does PyPack Actually Do? It wraps PyInstaller in a GUI. Pick your project, pick your settings, click Build. Done. Sounds simple, but here's where it gets interesting — it's not just a paint job over CLI commands. It actually fixes things PyInstaller gets wrong. It catches imports PyInstaller misses PyInstaller uses modulefinder under the hood. Problem is, modulefinder is kinda bad at its job. It misses tkinter submodules, for example, and then your build silently breaks. PyPack runs a full AST scan on your project instead. Catches way more stuff. Builds don't break for random mysterious reasons anymore. It handles the Qt binding mess You know that thing where you have a try/except for PyQt5 and PyQt6 fallback? try : from PyQt6 import QtWidgets except ImportError : from PyQt5 import QtWidgets PyInstaller sees both and just gives up. PyPack notices it, keeps only the one you're actually using, and moves on. Real-time build log No more guessing if the build is frozen or actually working. You see every command, every step, and at the end you get a real success or failure status. PyPack Crypt — The Thing I'm Actually Excited About This started as a side experiment but it ended up being the most useful part. Here's the problem nobody talks about: when you ship a PyInstaller .exe , your raw .py source files are sitting right inside it. Anyone with a tool like pyinstxtractor can pull them out in seconds PyPack Crypt does this instead: Compiles all your modules to bytecode Encrypts them with AES-256-GCM At runtime, decrypts straight into memory never writes to disk What makes it different from other obfuscation tools: New encryption key every build no shared key hiding in a DLL somewhere Randomized container format two builds of the same project look totally different under a hex editor GCM authentication if someone tampers with the file, it won't decrypt at all Look, I'll be honest: nothing that runs Python bytecode on someone else's computer is truly unbreakable, But this kills the "download one tool, extract all source files in 30 seconds" approach. And for most real-world situations, that's enough. Quick Start git clone https://github.com/Arianlavi/PyPack.git cd PyPack pip install -r requirements.txt python pypack.py Steps: Point it at your project folder and entry script Add an icon if you have one Pick one-file or one-folder, windowed or console Flip on PyPack Crypt if you want source protection Click Build Your .exe shows up in dist/ If you'd rather script it: from pypack.builder import build build ( project_path = " /path/to/my/project " , entry_script = " main.py " , icon = " app.ico " , one_file = True , windowed = True , crypt = True , ) What's Coming Things I'm working on or thinking about: [ ] Batch builds for multiple projects at once [ ] PyArmor as an alternative encryption backend [ ] Auto-update mechanism [ ] Linux and macOS support Grab It Fully open source, MIT license, No strings attached GitHub: https://github.com/Arianlavi/PyPack Star it if it helps you out. Open an issue if something's broken, I actually read them. Made with Python, CustomTkinter, and an unhealthy amount of late nights fighting PyInstaller 🐍

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/arianlavi/i-got-tired-of-pyinstaller-cli-so-i-built-a-gui-for-it-with-built-in-source-protection-4olg

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
