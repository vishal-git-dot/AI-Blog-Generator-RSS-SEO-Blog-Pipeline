---
title: "A Spider Robot Designed by AI: Code Is the New CAD"
slug: "a-spider-robot-designed-by-ai-code-is-the-new-cad"
author: "pablo padlo"
source: "devto_ai"
published: "Wed, 07 Oct 2026 12:52:56 +0000"
description: "A Spider Robot Designed by AI: Code Is the New CAD Somebody just designed a full spider robot without opening a single CAD program. No sketches, no solids, n..."
keywords: "code, not, robot, description, can, spider, cad, geometry"
generated: "2026-10-07T13:01:31.117358"
---

# A Spider Robot Designed by AI: Code Is the New CAD

## Overview

A Spider Robot Designed by AI: Code Is the New CAD Somebody just designed a full spider robot without opening a single CAD program. No sketches, no solids, no feature tree. Every part was written as a line of code, and the whole machine fell out of a text description. The project, shared by @MirrortekUK on X , used Claude Opus end to end. The result is a six-legged robot with two additional arms, built from five hundred parts and thirty joints. Each part is defined by a short Python program, and all of the parameters live together in a single YAML file. https://x.com/MirrortekUK/status/2107790410969976859 What was actually built The interesting part is not the robot itself — hexapods are old news. It is the pipeline. Because every component is code, the same description can be exported into formats that the rest of the engineering world already uses: STEP for geometry exchange, URDF for robotics, and a MuJoCo scene for physics simulation. That is the quiet shift. A description is not a picture of a robot; it is a machine that produces the picture, the simulation, and the manufacturing files at the same time. Change a parameter — a link length, a joint limit — and the geometry, the kinematic tree, and the simulated dynamics all update together, because they were never separate things in the first place. Code-defined hardware is a real movement This is not a first. For years, tools like CadQuery and build123d have let engineers script solid models in Python instead of clicking through a GUI. Open-source robotics stacks have long paired a URDF description with a MuJoCo model so that one source of truth drives both control and simulation. What is new is who writes the code. Until recently, code-defined CAD was a discipline you had to learn — a specialist skill on top of mechanical engineering. Now the model can draft the geometry program from a plain description, and the engineer reviews and refines it. The bottleneck moves from "can I model this?" to "is this the right design?" Why the export formats matter more than the render A pretty image proves nothing. What makes a code-defined robot real is that its output is not an image but a set of files with meaning: STEP is the neutral exchange format every machining and manufacturing shop can read. If your design can emit STEP, it can leave the design tool and enter a supply chain. URDF is how a robot describes its own body to its software — links, joints, limits, the kinematic tree. It is the bridge between the mechanical design and the control stack. MuJoCo is a physics engine. A scene exported from the same source lets the designers test how the machine behaves before any hardware exists — how it stands, walks, and recovers. When one description produces all three, you have a closed loop: describe, simulate, refine, and only then cut metal. The honest caveats It would be easy to overclaim here, so let us not. A model that drafts geometry still produces geometry that has to be checked: tolerances, materials, manufacturability, and load paths are engineering judgments a language model does not own. The claim is not that AI replaces the mechanical engineer. It is that the engineer's starting point is now a working draft instead of a blank canvas. It is also worth noting that this is a single project, shared publicly and not yet independently verified. Treat the headline as a direction of travel, not a finished product. Why this matters beyond one spider Hardware has always lagged software in iteration speed, because hardware lives in drawings. Drawings are slow to change, hard to diff, and impossible to test without building. Code is none of those things. The moment a machine is a program, it inherits everything software is good at: version control, review, parameter sweeps, automated tests, and instant simulation. That is why a small open-source spider robot is a better signal than a dozen flashy humanoid demos. It points at a different future: not robots that look impressive, but robots that are cheap to describe, cheap to change, and verifiable before they exist. Code is the new CAD.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/gptbrunch/a-spider-robot-designed-by-ai-code-is-the-new-cad-5e54

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
