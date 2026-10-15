---
title: "Convert STEP to GLB and enforce a 3D asset budget"
slug: "convert-step-to-glb-and-enforce-a-3d-asset-budget"
author: "Michal Žídek"
source: "devto_webdev"
published: "Thu, 15 Oct 2026 10:59:03 +0000"
description: "A CAD file is useful for manufacturing. A web page needs a mesh it can download and display. Between those two steps, it helps to put a limit on the asset yo..."
keywords: "budget, sample, step, build, glb, glbscope, not, baseline"
generated: "2026-10-15T11:10:31.555317"
---

# Convert STEP to GLB and enforce a 3D asset budget

## Overview

A CAD file is useful for manufacturing. A web page needs a mesh it can download and display. Between those two steps, it helps to put a limit on the asset you ship. This walkthrough uses two MIT-licensed tools I maintain: step2glb for STEP conversion and glbscope for GLB inspection and build budgets. The first runs on Node.js. The second is written in Rust. The example uses a small public test fixture, so you can reproduce the result without uploading private CAD files to a service. It demonstrates the workflow; it is not a performance benchmark. 1. Install the published versions Use Node.js 22 or later and a current Rust toolchain: mkdir cad-to-web cd cad-to-web npm init -y npm install --save-exact step2glb@0.2.0 cargo install glbscope --version 0.3.0 --locked Keep package-lock.json in your project. Use npm ci on later build runs. Download the two-tetrahedra fixture from a fixed source revision: curl -fL https://raw.githubusercontent.com/M1chlCZ/step2glb/2a19b844150b7057aa4b425577b4f8881754b655/test/fixtures/two-tetrahedra.step -o sample.step You can use your own .step or .stp file instead. Both tools process files locally. Installing the packages and downloading this fixture need network access. 2. Convert the model npx step2glb inspect sample.step npx step2glb build sample.step --out sample.glb --preset web inspect prints an assembly manifest. build writes a Draco-compressed GLB and prints a JSON summary. The web preset uses coarser tessellation and lower quantization precision than the high-detail preset. Check the result visually before you use it for a real product. In my local run with these published versions, the output was 3,356 bytes , with 8 triangles , 24 vertices , and 5 nodes . A second build of the same fixture produced identical bytes. Those numbers describe this tiny fixture, not a typical CAD assembly. The output uses metres. Occurrence IDs come from hierarchy paths, so renaming a part does not change its ID. Moving a part to a different hierarchy path can change it. 3. Set a budget Create budget.toml : max_bytes = 2_000_000 max_triangles = 120_000 max_nodes = 400 These are example limits. Choose limits for your users and viewer. A small product preview and a detailed assembly viewer have different needs. Run the check: glbscope --budget budget.toml sample.glb The sample passes. To prove that the gate works, temporarily set max_bytes = 3_000 and run it again. The 3,356-byte sample fails with exit code 1 and a finding that identifies the exceeded byte budget. The exit codes make this usable in CI: Code Meaning 0 No findings or baseline regression 1 A budget finding or baseline regression 2 An input, parse, or argument error Keep the check as a normal build step so a nonzero result stops the job. One detail matters for compressed assets: step2glb requires KHR_draco_mesh_compression in its output. If you set allowed_extensions in the budget, include that extension. A viewer also needs a Draco decoder to display the model. 4. Keep a readable build report glbscope --format markdown --budget budget.toml sample.glb > model-report.md glbscope --json sample.glb > baseline.json The Markdown report is convenient as a build artifact. Commit a baseline when you want to review later growth: glbscope --baseline baseline.json sample.glb A file-size increase, triangle-count increase, or new finding causes a regression result. Run from the same working directory with the same paths, and update the baseline only when the change is intended. SARIF output is also available for code-scanning integrations. What this check does not prove An asset budget measures structural properties. It does not measure frame rate, confirm visual quality, or replace a full glTF validator and a test in your actual viewer. Draco reduces download size but adds decoding work. A low triangle count alone does not guarantee a fast page. step2glb also has hard limits, including 2 million triangles and a 16 MiB output file. It converts STEP geometry to a web mesh; it does not preserve the editable CAD feature history. For a real model, inspect the converted shape, test it on a representative device, and then set your budget. The useful automation is catching unintended growth before it reaches that device. Source and full options: step2glb · glbscope . Reproducible files that expose conversion or reporting problems are welcome. AI disclosure: this article was prepared with AI assistance. The commands, budget pass/fail, decoded mesh bounds, and repeated-build result were checked locally with the published package versions on October 15, 2026.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/m1chlcz18/convert-step-to-glb-and-enforce-a-3d-asset-budget-53fk

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
