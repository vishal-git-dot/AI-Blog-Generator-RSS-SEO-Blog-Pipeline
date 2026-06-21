---
title: "I built an open-source tool that turns workcell incidents into evidence bundles and regression tests"
slug: "i-built-an-open-source-tool-that-turns-workcell-incidents-into-evidence-bundles-and-regression-tests"
author: "Miko"
source: "devto_python"
published: "Sun, 21 Jun 2026 18:59:40 +0000"
description: "I built MetriPlane v0.2.0 , an open-source physical-observability tool for bounded workcells. The short version: A missing tool in a workcell becomes a physi..."
keywords: "metriplane, pass, bundle, atlas, regression, evidence, test, physical"
generated: "2026-06-21T19:51:26.683062"
---

# I built an open-source tool that turns workcell incidents into evidence bundles and regression tests

## Overview

I built MetriPlane v0.2.0 , an open-source physical-observability tool for bounded workcells. The short version: A missing tool in a workcell becomes a physical event log, a Cell Truth Report, a verified evidence bundle, and a generated regression test. 3-minute demo: Repository: https://github.com/Miko997/metriplane Zenodo DOI: https://doi.org/10.5281/zenodo.20736619 The problem Robotics and manufacturing systems often have cameras, logs, dashboards, and simulators. But when something physically goes wrong, there is still a hard question: What actually happened? What proves it? Can we replay it? Can we turn the incident into a repeatable software check? MetriPlane focuses on that narrow layer: replayable physical evidence for bounded workcells . What the v0.2.0 demo shows The demo uses a camera-free assembly-cell replay where a required torque driver is missing long enough to delay a process step. MetriPlane turns that replayed state into: missing torque driver → physical event log → Cell Truth Report → incident evidence bundle → local bundle verification → generated regression test → regression PASS The important part is not just detecting an event. The important part is that the event becomes a verifiable artifact that can be reviewed, replayed, and reused as a software test. What MetriPlane generates MetriPlane v0.2.0 produces: physical event logs Cell Truth Reports incident evidence bundles manifest and checksums local bundle verification generated regression tests static review/dashboard artifacts The demo evidence chain is: 6 physical events 1 incident 35.0 second missing-tool delay INC-0001 evidence bundle bundle verify: pass=true generated regression test: PASS Camera-free reproduction I am preparing a SoftwareX research-software paper while finishing my MSc thesis, and I am looking for external technical reproduction feedback. Public reproduction issue: https://github.com/Miko997/metriplane/issues/6 A useful reproduction comment would include: OS: Python version: doctor: pass/fail deterministic replay: pass/fail Atlas run: pass/fail bundle verify: pass/fail regression test: pass/fail Technical relevance: 2–5 sentences Main limitation: 1–2 sentences Main reproduction commands git clone https://github.com/Miko997/metriplane.git cd metriplane git checkout v0.2.0 python3 -m venv .venv source .venv/bin/activate pip install -e . python -m metriplane.cli doctor PYTEST_DISABLE_PLUGIN_AUTOLOAD = 1 python -m pytest -q ./tools/mp.sh deterministic-replay metriplane atlas validate-pack configs/domain_packs/assembly_cell metriplane atlas run \ --session-jsonl datasets/demo/atlas/assembly_cell_missing_tool.jsonl \ --pack configs/domain_packs/assembly_cell \ --out runs/atlas/assembly_cell_missing_tool metriplane atlas bundle verify \ runs/atlas/assembly_cell_missing_tool/evidence_bundles/INC-0001.zip metriplane atlas test \ runs/atlas/assembly_cell_missing_tool/regression_tests/INC-0001.yaml Expected high-level result: doctor: pass pytest: 580 passed deterministic replay: pass=true, 0.0 cm position difference, 0 event mismatches Atlas run: events=6, incidents=1 bundle verify: pass=true regression test: PASS missing_tool_caused_delay_INC-0001 Scope MetriPlane v0.2.0 is intentionally bounded. It is: observe-only local-first camera/replay-oriented planar/tagged-asset scoped research-software oriented It does not claim: robot or machine control safety certification quality-release approval people recognition marker-free tracking full 3D reconstruction production-factory validation factory-wide deployment readiness Feedback wanted I am especially interested in: Does the camera-free reproduction path work on another machine? Is the incident → evidence bundle → regression test loop useful? Are the observe-only boundaries clear enough? What should be validated next before this is useful beyond a deterministic demo fixture? Would this be useful around robotics, simulation, digital-twin, or manufacturing review workflows? Critical feedback is more useful than praise.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/miko997/i-built-an-open-source-tool-that-turns-workcell-incidents-into-evidence-bundles-and-regression-tests-55ll

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
