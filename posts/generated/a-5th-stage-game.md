---
title: "A 5th stage game"
slug: "a-5th-stage-game"
author: "Ando"
source: "devto_python"
published: "Sat, 03 Oct 2026 11:03:03 +0000"
description: "I Built a 5-Stage Pipeline Game in Python — And Finally Lost to My Own Branch Predictor When I started CS101: Introduction to Programming on Codecademy, the ..."
keywords: "pipeline, game, you, cpu, own, why, python, branch"
generated: "2026-10-03T11:24:45.495425"
---

# A 5th stage game

## Overview

I Built a 5-Stage Pipeline Game in Python — And Finally Lost to My Own Branch Predictor When I started CS101: Introduction to Programming on Codecademy, the portfolio project sounded simple: "Build a basic terminal game." Everyone was making Blackjack and Tic-Tac-Toe. I wanted something that actually teaches how computers really think. So I remembered my previous project - building a CPU from scratch - and thought: what if I turn the CPU's biggest enemy into a game? Introducing PIPELINE PANIC - CPU Hazard Defender. You're a Pipeline Engineer and your job is to keep a 5-stage pipeline alive while hazards try to kill it. The Result (Proof it Works) Here's my game running a real program with RAW hazards and branch mispredictions: ![ - Pipeline Panic running Cycle 5 with forwarding and stall detection] This is actual terminal output from python main.py (Menu 2 - PLAY): It loads instructions from program.asm or from interactive input: It runs a full IF → ID → EX → MEM → WB simulation It shows Stalls, Flushes, Forwarding in real-time It tracks Branch Predictor Accuracy live - in this run, 75.0%! Yes, I tied with a 2-bit saturating counter. That's humbling. How My Python Code Works I split the game into 5 core OOP modules to meet the Codecademy requirement for clean architecture - just like real hardware: AssemblyParser (The File Parser) A 3-pass parser pipeline - yes, a pipeline inside a pipeline simulator: Pass 1: Collect all labels ( LOOP: , TARGET: ) Pass 2: Tokenize with strict Regex for R-type ( ADD R1,R2,R3 ), I-type ( LW R5,R2,100 ), B-type ( BEQ ), J-type Pass 3: Resolve label → instruction index, with nice error reporting: It supports # comments , empty lines, and both file and text input. HazardDetectionUnit + ForwardingUnit (The Brains) This is the part that makes decisions by itself - the "otak" I wanted: Two Big-O implementations for education: detect_naive() - O(n²) - checks every pair in the 3-instruction window detect_optimized() - O(n) - uses a last_write hashmap Benchmark in Menu 1 shows O(n) is ~40% faster even for 7 instructions. Imagine for 1000. The ForwardingUnit automatically decides if it can forward EX→EX or MEM→EX or must insert a bubble. BranchPredictor (The One That Beat Me) This is the "nebak cabang" brain. It implements 3 strategies: always_taken always_not_taken 2-bit - 4-state FSM: Strong NT (00) → Weak NT (01) → Weak T (10) → Strong T (11) It learns from history and tracks its own accuracy. In Battle Mode, you play against it. Spoiler: it's good. CPUPipeline (The 5-Stage Pipeline) Classic RISC pipeline: 1 IF (Fetch) → ID (Decode) → EX (Execute) → MEM → WB Each step() moves pipeline registers. It handles stalls and flushes: GameEngine (The Terminal Game) Meets Codecademy's input() requirement with 5 modes: LEARN - Big-O demo + hazard visualization PLAY - Live pipeline visualization CHALLENGE - Compiler optimization puzzle: reorder instructions to minimize stalls (my favorite - you have ADD R1,R2,R3 / SUB R4,R1,R5 / ADD R6,R7,R8 and you must move the independent one up!) BATTLE - You vs 2-bit predictor PARSER - Load your own .asm file Check Out The Code All the code is open source and ready to run. I fixed the Git case from last time, but this time I fought with program.asm not being found - classic Windows PowerShell moment! GitHub: https://github.com/ikaroshunt/pipeline_panic.git (create this repo!) To run it yourself: Files: main.py - All-in-one game (OOP, Pipeline, Brains, Parser) program.asm - Sample program with intentional hazards Conclusion My first CPU simulator taught me why cache exists. This one taught me why pipelines are hard. I finally understand: Why a simple ADD can stall the whole CPU (RAW hazard) Why branch prediction is 30% of CPU performance Why O(n) vs O(n²) matters when you check hazards for thousands of instructions Why forwarding is cheaper than stalling It was frustrating at first - ParseError: Undefined label LOOP (yes, I forgot to define my own label!), fatal: pathspec did not match , and tying with my own AI. But each error was a lesson. If you're taking CS101, don't just make Blackjack. Make something that makes you lose to your own code. There's no better feeling than seeing === Cycle 10 === Stalls=2 and knowing you built that logic. This project was built as part of Codecademy's Computer Science Career Path (CS101: Python Terminal Game Portfolio Project) - Level 2 of my CPU series. Tools: Python 3, Git, VS Code, PowerShell, OOP, Big-O Analysis, 2-bit Branch Prediction

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/ikaroshunt/a-5th-stage-game-1bjl

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
