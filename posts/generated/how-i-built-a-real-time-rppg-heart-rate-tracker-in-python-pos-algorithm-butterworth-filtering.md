---
title: "How I Built a Real-Time rPPG Heart Rate Tracker in Python (POS Algorithm & Butterworth Filtering)"
slug: "how-i-built-a-real-time-rppg-heart-rate-tracker-in-python-pos-algorithm-butterworth-filtering"
author: "Shakeel Ahmed"
source: "devto_python"
published: "Sat, 26 Sep 2026 19:46:52 +0000"
description: "Continuous biometric monitoring usually requires dedicated contact hardware like smartwatches or pulse oximeters. However, standard laptop webcams can captur..."
keywords: "pos, skin, signal, tracker, python, standard, noise, light"
generated: "2026-09-26T20:53:25.484619"
---

# How I Built a Real-Time rPPG Heart Rate Tracker in Python (POS Algorithm & Butterworth Filtering)

## Overview

Continuous biometric monitoring usually requires dedicated contact hardware like smartwatches or pulse oximeters. However, standard laptop webcams can capture subtle skin color variations caused by blood volume pulses (BVP). To explore non-contact vital signs monitoring without specialized sensors, I built BioSense Tracker Pro—a real-time remote photoplethysmography (rPPG) framework in Python. Here is a breakdown of the core signal processing behind the project and how to overcome ambient camera noise. The Challenge: Ambient Noise & Specular Reflection When light strikes skin, the reflected signal contains two components: Specular Reflection: Light reflecting directly off the skin surface (contains no blood volume data). Diffuse Reflection: Light penetrating skin tissue, absorbed/reflected by hemoglobin fluctuations during heartbeats. In standard RGB video streams, lighting changes, head movement, and camera auto-exposure introduce heavy noise that masks the diffuse pulse signal. Simple RGB averaging across facial regions isn't enough for clean signal extraction. The Architecture: POS Algorithm + Bandpass Filtering To isolate the blood volume pulse from optical interference without requiring heavy neural networks or GPUs, I combined spatial-temporal color projection with bandpass frequency selection: Plane-Orthogonal-to-Skin (POS) Algorithm: POS projects temporal RGB signals onto a plane orthogonal to the skin tone vector. By defining two orthogonal signals that separate intensity variations from pulsatile variations, POS eliminates specular reflections caused by light fluctuations. Butterworth Bandpass Filtering: Human resting heart rates fall between 45 BPM and 240 BPM (0.75 Hz to 4.0 Hz). The raw POS signal passes through a Butterworth Bandpass Filter to eliminate high-frequency sensor noise and low-frequency motion drift before computing Fast Fourier Transform (FFT) peaks for instantaneous BPM estimation. Tech Stack & Performance Core Stack: Python 3.10+, OpenCV, NumPy, SciPy Processing: Low-latency pipeline running on standard CPU threads. Hardware: Works with standard, off-the-shelf webcams. Code & Executable Setup Source Code: You can inspect the source code and implementation on my GitHub Repository. https://github.com/ShakeelAhmed-NeuroAI/BioSense-Tracker-Pro Standalone Package: If you want to test it without setting up Python environments or OpenCV dependencies, I packaged a launcher available as a 1-Click Executable on Gumroad. https://shakeelengineer27.gumroad.com/l/biosense-tracker

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/shakeelahmedneuroai/how-i-built-a-real-time-rppg-heart-rate-tracker-in-python-pos-algorithm-butterworth-filtering-1koe

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
