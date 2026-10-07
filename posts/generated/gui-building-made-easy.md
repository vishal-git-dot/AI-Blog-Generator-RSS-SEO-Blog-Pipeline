---
title: "GUI Building made EASY!!"
slug: "gui-building-made-easy"
author: "fahh3344"
source: "devto_python"
published: "Wed, 07 Oct 2026 21:45:54 +0000"
description: "Build standalone executables with Pylerium Choose Workshop → Build EXE after saving your project. Select an application name, output folder and build Python...."
keywords: "icon, options, build, project, gui, folder, picker, workshop"
generated: "2026-10-07T22:56:27.547906"
---

# GUI Building made EASY!!

## Overview

Build standalone executables with Pylerium Choose Workshop → Build EXE after saving your project. Select an application name, output folder and build Python. That interpreter needs pyinstaller PyQt6 numpy trimesh pillow moderngl glcontext . Builds run in a separate process with live output, cancellation and an Open Output action. GUI applications hide the terminal; console tools can keep it. Existing executables require an explicit replacement choice. The exporter packages the complete shared GUI SDK and stylesheet, model renderer, a portable interpreter for background tools, and the project's companion files. Include the asset library and installed plugin sources using the build options; the enabled-plugin list is captured from the current workspace. Imported dependencies in project and plugin source are discovered. Use Additional imports for packages loaded dynamically by name. Optional scientific/ML engines are included when directly imported or explicitly requested rather than pulled in solely through Trimesh's optional adapters. Each exported application keeps its own database and writable project data under %LOCALAPPDATA%/<application name>/ , or an explicit PYLERIUM_HOME . Project companion files seed the writable working directory on first launch; subsequent launches retain edits. Updated executables run the newly bundled entry code. Shared state persists in orchestration_data/shared.sqlite3 ; source workspace databases are not shipped. Relative resource/data paths use the writable project directory. Model/image assignments come from the bundled manifest. Executable branding and advanced options Workshop's Build EXE dialog includes an icon picker and collapsible branding/packaging controls. ICO, PNG, JPEG, WebP and BMP icons become a transparent multi-resolution Windows icon (16–256 pixels). The icon is embedded in the executable and applied to GUI windows using the shared toolkit. Choose a single executable or application folder, GUI/console mode, Windows version/company/product/description/copyright, debug mode, optimization, cache cleaning, compression and administrator launch behavior. Advanced JSON exposes extra data/binaries, import paths, exclusions, package collections, hooks, runtime hooks, splash screen, Windows manifest, version resource file and temporary extraction directory. extra_args is a list of individual arguments for any other PyInstaller options; no shell command is constructed. Build options persist per project. Some advanced options require additional tools or resources supported by the selected PyInstaller installation. Running build_exe.py directly opens the icon picker before building Pylerium. Cancel selects the default icon. Use --icon path/to/icon.png to supply one explicitly, or --no-icon-picker for unattended builds. --onedir selects folder packaging, and --options-file build-options.json supplies the same advanced options outside Workshop. Workshop always passes --no-icon-picker because it already provides its own picker. For folder builds distribute the entire output folder, including _internal , alongside the executable.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/donnnnn14/gui-building-made-easy-b78

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
