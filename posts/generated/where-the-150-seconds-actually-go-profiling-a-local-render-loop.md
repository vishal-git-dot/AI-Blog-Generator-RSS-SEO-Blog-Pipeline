---
title: "Where the 150 seconds actually go: profiling a local render loop"
slug: "where-the-150-seconds-actually-go-profiling-a-local-render-loop"
author: "mujin"
source: "devto_ai"
published: "Thu, 12 Nov 2026 14:54:29 +0000"
description: "Splitting the 150 seconds into model load, sampling steps, and PNG encode with a stopwatch and cProfile, in a script short enough to paste My SD1.5 render lo..."
keywords: "model, time, render, image, import, wall, seconds, cprofile"
generated: "2026-11-12T14:55:17.820778"
---

# Where the 150 seconds actually go: profiling a local render loop

## Overview

Splitting the 150 seconds into model load, sampling steps, and PNG encode with a stopwatch and cProfile, in a script short enough to paste My SD1.5 render loop runs in fp32 with model offload on a 4GB GTX 1650. A 512x768 image takes about 150 seconds, but that total does not identify the bottleneck. I used perf_counter for the boundaries I control and cProfile for calls inside Diffusers. The script assumes the model is already cached locally, so network activity cannot contaminate model-load time. import cProfile import io import os from pathlib import Path from time import perf_counter import torch from diffusers import StableDiffusionPipeline wall_start = perf_counter ( ) profiler = cProfile . Profile ( ) profiler . enable ( ) load_start = perf_counter ( ) pipe = StableDiffusionPipeline . from_pretrained ( os . environ [ "MODEL" ] , torch_dtype = torch . float32 , local_files_only = True , ) pipe . enable_model_cpu_offload ( ) model_load = perf_counter ( ) - load_start step_marks = [ ] def mark_step ( pipe , step , timestep , callback_kwargs ) : step_marks . append ( perf_counter ( ) ) return callback_kwargs sample_start = perf_counter ( ) image , * _ = pipe ( prompt = os . environ [ "PROMPT" ] , width = 512 , height = 768 , callback_on_step_end = mark_step , ) . images sample_end = step_marks . pop ( ) if step_marks else perf_counter ( ) sampling_steps = sample_end - sample_start png_start = perf_counter ( ) buffer = io . BytesIO ( ) image . save ( buffer , format = "PNG" ) png_encode = perf_counter ( ) - png_start Path ( os . environ [ "OUTPUT" ] ) . write_bytes ( buffer . getvalue ( ) ) profiler . disable ( ) wall_seconds = perf_counter ( ) - wall_start profiler . dump_stats ( "render.prof" ) print ( { "model_load" : model_load , "sampling_steps" : sampling_steps , "png_encode" : png_encode , "wall_seconds" : wall_seconds , } ) I inspect the profile with: python -m pstats render.prof sort cumtime stats The stopwatch gives stable phase boundaries. cProfile then shows whether time inside the sampling phase belongs to model execution, scheduler work, tensor transfers, or Python callbacks. I keep wall time as the control because the phase totals intentionally omit some setup and file-write overhead. What the profile changed: the two fixes that cut wall-clock, and the one “optimization” that only moved the cost to disk Fix A was moving pipeline construction outside the per-image function. The daemon now loads SD1.5 once, enables model offload once, and reuses the pipeline. This removes repeated model loading from subsequent renders without pretending that loading became faster. Fix B was eliminating a PNG round trip. The old path saved the image, reopened it to calculate the content hash, and then read it again for the next pipeline stage. The current path encodes once into BytesIO . The same byte string is hashed and written to disk. The false optimization was avoiding PNG compression by writing a large intermediate image. CPU time fell, but file-write time and storage traffic increased. The profile looked better only when I stopped measuring before the write. End-to-end wall time did not receive the same benefit. The decision rule is simple: an optimization stays only if wall_seconds falls when measured from the same start and end points. A faster inner function is not sufficient. The single per-run number worth writing to a text file, so a slow week is visible before it is a mystery I record total wall seconds for every successful 512x768 render. I do not use sampling time alone because that would hide regressions in model loading, encoding, or disk writes. with open ( "render-wall-seconds.txt" , "a" , encoding = "utf-8" ) as log : log . write ( f "{wall_seconds}\n" ) This file is deliberately plain. It works with shell tools, survives daemon restarts, and makes a sustained slowdown visible without requiring a monitoring service. The detailed profile is diagnostic output; total wall time is the trend. The rendered work feeds the collection at https://thunderous-sunflower-a910b4.netlify.app , but the same measurement applies to any local image pipeline. Practical takeaway: wrap your render at the process boundary, append total wall seconds to a text file, and reject any optimization that improves only an internal timer.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/mujin/where-the-150-seconds-actually-go-profiling-a-local-render-loop-341h

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
