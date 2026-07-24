---
title: "From 2800-Line Monolith to Modular FastAPI — Refactoring an AI Geolocation Tool"
slug: "from-2800-line-monolith-to-modular-fastapi-refactoring-an-ai-geolocation-tool"
author: "Nguyễn Công Thuận Huy"
source: "devto_python"
published: "Fri, 24 Jul 2026 08:28:55 +0000"
description: "From 2800-Line Monolith to Modular FastAPI — Refactoring an AI Geolocation Tool Netryx Nova is a complete modular rewrite of Netryx Astra V2 , an open-source..."
keywords: "gpu, modal, netryx, original, cloud, pipeline, modular, tests"
generated: "2026-07-24T08:34:24.200307"
---

# From 2800-Line Monolith to Modular FastAPI — Refactoring an AI Geolocation Tool

## Overview

From 2800-Line Monolith to Modular FastAPI — Refactoring an AI Geolocation Tool Netryx Nova is a complete modular rewrite of Netryx Astra V2 , an open-source image geolocation system that finds GPS coordinates from a single photo using MegaLoc (CVPR 2025) + MASt3R (ECCV 2024). The original worked — but it was a 2800-line Tkinter monolith. Here's how we broke it into clean modules, added a web UI, cloud GPU support, and 3 execution engines. The Problem The original test_super.py was 2794 lines of inline Tkinter GUI + pipeline logic + indexing + file I/O. Making any change meant scrolling through a massive file, guessing which section to touch, and hoping nothing else broke. There was no separation of concerns, no async, no tests. Symptoms: Single file with everything mixed together Tkinter desktop GUI only (no remote access) Blocking operations freeze the UI No test coverage No engine abstraction (GPU-only, no fallback) The Architecture Before (Monolith) test_super.py (2794 lines) ├── GUI (Tkinter widgets, event handlers) ├── Pipeline (retrieval → matching → consensus) ├── Index builder (PCA fitting, FAISS build) ├── Model loading (MegaLoc, MASt3R) ├── File I/O (.netryx bundles) └── Community Hub (Hugging Face upload/download) After (Modular) app.py # FastAPI entrypoint ├── core/ # Business logic │ ├── pipeline.py # Async pipeline controller │ ├── retrieval.py # FAISS vector search │ ├── matching.py # MASt3R dense matcher │ └── consensus.py # Grid clustering (pure NumPy) ├── engines/ # Backend abstraction │ ├── base.py # EngineBase ABC │ ├── local_gpu.py # CUDA/MPS │ ├── local_cpu.py # CPU fallback │ └── cloud_modal.py # Modal.com T4 GPU ├── ui/ # Web frontend │ ├── web_app.py # FastAPI router (7 endpoints + WS) │ ├── templates/ # Jinja2 HTML │ └── static/ # JS (Leaflet, WebSocket) + CSS ├── utils/ # Helpers │ ├── tile_downloader.py │ ├── geo_utils.py │ └── netryx_loader.py ├── modal_app/ # Cloud deployment │ └── mast3r_worker.py └── tests/ # 23 pytest tests Key Decisions 1. EngineBase — Abstract Backend Instead of hardcoding GPU inference, we defined an abstract EngineBase class with run_stage2() . Three implementations: LocalGPUEngine — CUDA/MPS, loads models at startup LocalCPUEngine — same pipeline, runs on CPU CloudModalEngine — HTTP client to a Modal.com T4 worker Auto-detection chain: GPU → Cloud → CPU. If you have no GPU but Modal is configured, it uses the cloud transparently. class EngineBase ( ABC ): @abstractmethod def run_stage2 ( self , query_img , candidates , progress_callback = None , cancel_event = None , ... ) -> dict : ... 2. Async Job Model The original blocked the UI for minutes during Stage 2. The modular version uses: POST /search returns 202 Accepted with a job_id The client connects via WebSocket at /ws/{job_id} PipelineController runs the job on a background thread, streaming progress through an asyncio.Queue Each engine slot (default 2) processes candidates in parallel # Post search → get job_id, then stream results via WS ws = new WebSocket ( `/ws/${jobId}` ); ws . onmessage = ( e ) => { const msg = JSON . parse ( e . data ); if ( msg . type === " progress " ) updateProgress ( msg . current , msg . total ); if ( msg . type === " result " ) showMap ( msg . result ); }; 3. Spatial Consensus with NumPy The original had a fragile inline consensus loop. We rewrote it as pure NumPy: def cluster_matches ( matches , cell_size_deg = 0.00045 ): grid = np . floor ( np . column_stack ([ lats , lons ]) / cell_size_deg ). astype ( int ) unique_cells , counts = np . unique ( grid , axis = 0 , return_counts = True ) # Score each cell: sqrt(inliers) summed per grid cell # Winner = densest cluster, not highest single score This eliminated an entire class of false positives from repetitive architecture. 4. On-the-Fly FAISS Instead of pre-built index files, we load a .netryx bundle on startup and build a FAISS index in memory: class FAISSRetrieval : def __init__ ( self , bundle_path ): data = load_netryx_bundle ( bundle_path ) self . index = faiss . IndexFlatIP ( 1024 ) self . index . add ( normalize ( data . descriptors )) self . metadata = data . metadata What Changed vs. Original Aspect Original (Astra V2) Nova Lines of code ~2800 in one file ~1500 across 20+ files UI Tkinter desktop FastAPI + Leaflet + WebSocket Engine GPU-only GPU / Cloud GPU / CPU Async Blocking 202 + WS streaming Tests None 23 tests, ruff + mypy clean Setup pip install -r requirements.txt pyproject.toml with dev tooling Consensus Inline heuristic NumPy grid clustering Cloud None Modal.com T4 GPU ($30 free credits) The Cloud GPU Bonus No GPU? Modal gives $30 free credits on signup — deploy the MASt3R worker on a T4 in one command: pip install modal modal setup modal deploy modal_app/mast3r_worker.py The engine auto-detects Modal tokens and falls back gracefully. Results 21/23 tests pass (2 skipped — faiss not installed in CI) ruff zero warnings, mypy strict mode clean Response times identical to the monolith (same models, same pipeline) Repo is publish-ready with .gitignore , .env.example , and updated README Check It Out https://github.com/mangodxd/Netryx-Nova Netryx Nova is a modular fork of Sairaj Balaji's Netryx Astra V2 . All geolocation credit goes to the original pipeline.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/mangodxd/from-2800-line-monolith-to-modular-fastapi-refactoring-an-ai-geolocation-tool-27gg

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
