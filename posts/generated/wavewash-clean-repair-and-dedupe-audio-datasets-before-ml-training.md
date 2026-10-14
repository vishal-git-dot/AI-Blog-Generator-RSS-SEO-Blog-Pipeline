---
title: "WaveWash: Clean, Repair, and Dedupe Audio Datasets Before ML Training"
slug: "wavewash-clean-repair-and-dedupe-audio-datasets-before-ml-training"
author: "Boobalan Arjunan"
source: "devto_python"
published: "Wed, 14 Oct 2026 11:09:26 +0000"
description: "Training speech models (Whisper, TTS, voice cloning) often breaks down because of dirty audio data: clipping, DC offset, background noise, low SNR, and dupli..."
keywords: "wavewash, audio, clipping, files, clean, training, whisper, tts"
generated: "2026-10-14T11:32:22.305305"
---

# WaveWash: Clean, Repair, and Dedupe Audio Datasets Before ML Training

## Overview

Training speech models (Whisper, TTS, voice cloning) often breaks down because of dirty audio data: clipping, DC offset, background noise, low SNR, and duplicate samples quietly inflating validation metrics. I built WaveWash to automate audio quality control and data prep so developers don't have to write one-off scripts or manually listen to thousands of audio files. What WaveWash Does Tuned Presets: Built-in profiles for ASR (Whisper), TTS, Speaker ID, and Music Generation. Safe Auto-Repairs: Corrects DC offset, mild clipping, and normalizes loudness (EBU R128). Automated Segregation: clean/ : Audio that passed all checks. _error/ : Rejected files categorized by reason ( low_snr/ , clipping/ , etc.). _duplicates/ : Exact and near-duplicates set aside (nothing is deleted). _logs/ : Complete audit logs (CSV, JSON, and Markdown summaries). Zero-Config Local Web UI: Ships directly inside the Python package — no Node.js build required. Non-Destructive: Your original files are never modified. Quick Start Install and launch the local web UI in two commands: bash pip install wavewash wavewash app It opens your browser at http://127.0.0.1:8420. You can also run it directly from the terminal: wavewash run --input ./raw_audio --output ./clean_audio --purpose asr Links PyPI: https://pypi.org/project/wavewash/ GitHub: https://github.com/BoobalanArjunan/wavewash It's currently in early alpha (v0.1.0a1). Feedback, issues, and feature suggestions are very welcome!

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/boobalan_arjunan/wavewash-clean-repair-and-dedupe-audio-datasets-before-ml-training-4jk4

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
