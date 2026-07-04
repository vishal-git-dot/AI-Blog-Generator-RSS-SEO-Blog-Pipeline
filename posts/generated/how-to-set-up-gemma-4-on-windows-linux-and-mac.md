---
title: "How to Set Up Gemma 4 on Windows, Linux, and Mac"
slug: "how-to-set-up-gemma-4-on-windows-linux-and-mac"
author: "Agbo, Daniel Onuoha"
source: "devto_ai"
published: "Sat, 04 Jul 2026 19:12:19 +0000"
description: "Before running any model, you need Ollama (or llama.cpp) installed for your OS. Ollama is the simplest starting point across all three platforms. Windows Dow..."
keywords: "ollama, run, install, you, llama, cpp, download, build"
generated: "2026-07-04T19:22:30.080322"
---

# How to Set Up Gemma 4 on Windows, Linux, and Mac

## Overview

Before running any model, you need Ollama (or llama.cpp) installed for your OS. Ollama is the simplest starting point across all three platforms. Windows Download the installer from ollama.com/download and run the .exe file Follow the install wizard — Ollama adds itself to the system tray and starts automatically Open PowerShell or Command Prompt and verify: ollama -v Pull and run a model: ollama run gemma4:e4b If you have an NVIDIA GPU, install the latest CUDA drivers first so Ollama detects and uses it automatically — check with nvidia-smi in PowerShell. Linux Install via the official script: curl -fsSL https://ollama.com/install.sh | sh Start the service (it usually starts automatically, but you can also run it manually): ollama serve Verify installation and GPU detection: ollama -v nvidia-smi # for NVIDIA GPUs For a persistent background service, register systemd instead of running ollama serve in a terminal: sudo useradd -r -s /bin/false -U -m -d /usr/share/ollama ollama sudo usermod -a -G ollama $( whoami ) sudo systemctl daemon-reload sudo systemctl enable --now ollama Pull and run: ollama run gemma4:e4b AMD GPU users need the additional ROCm package ( ollama-linux-amd64-rocm.tar.zst ) alongside the base install. macOS Download the .dmg from ollama.com/download, open it, and drag Ollama into Applications — or install via Homebrew: brew install ollama brew services start ollama Launch Ollama from Applications once to grant permissions; you'll see its icon in the menu bar Verify and run: ollama --version ollama run gemma4:e4b Apple Silicon Macs (M1–M4) use Metal acceleration automatically — no extra driver setup needed, and unified memory determines the largest model size you can run comfortably. Choosing llama.cpp Instead If you need raw inference speed over convenience, build llama.cpp directly on any OS: git clone https://github.com/ggerganov/llama.cpp cd llama.cpp cmake -B build -DGGML_CUDA = ON # use -DGGML_METAL=ON on Mac, omit flag on CPU-only Linux/Windows cmake --build build --config Release ./build/bin/llama-cli -m gemma4-e4b-Q4_K_M.gguf -p "Explain Gemma 4 quantization" Download the GGUF weights separately from Hugging Face's Gemma 4 collection before running this command.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/shieldstring/how-to-set-up-gemma-4-on-windows-linux-and-mac-3caj

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
