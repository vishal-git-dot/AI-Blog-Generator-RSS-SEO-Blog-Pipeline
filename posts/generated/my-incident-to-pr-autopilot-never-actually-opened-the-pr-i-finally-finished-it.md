---
title: "My 'Incident-to-PR Autopilot' Never Actually Opened the PR. I Finally Finished It."
slug: "my-incident-to-pr-autopilot-never-actually-opened-the-pr-i-finally-finished-it"
author: "Aliza Ali"
source: "devto_python"
published: "Sun, 07 Jun 2026 18:48:00 +0000"
description: "This is a submission for the GitHub Finish-Up-A-Thon Challenge What I Built FixForward — an incident-to-PR autopilot powered by GitHub Copilot CLI. One comma..."
keywords: "fixforward, copilot, fix, github, confidence, tests, build, open"
generated: "2026-06-07T19:40:41.522971"
---

# My 'Incident-to-PR Autopilot' Never Actually Opened the PR. I Finally Finished It.

## Overview

This is a submission for the GitHub Finish-Up-A-Thon Challenge What I Built FixForward — an incident-to-PR autopilot powered by GitHub Copilot CLI. One command turns a failing test suite into a verified, ready-to-merge pull request : it detects the failures, classifies them, asks GitHub Copilot for a minimal fix, applies it on a safe branch, re-runs the tests to prove the fix works, and opens a labelled PR — locally or automatically in CI. It started life as my submission to an earlier GitHub Copilot CLI challenge . It placed well… and then I left it one step short. The tool literally had "PR" in its name , but it stopped at printing a PR description and made you git push and gh pr create by hand. I got busy, and that last mile sat unfinished for months. This challenge was the push to finally land the plane. FixForward is the tool I actually want sitting in my repos: when a build breaks, a fix PR should just appear . pip install fixforward Demo Diagnosis — FixForward detects the failing tests and classifies them: Outcome — Copilot's fix, verified green, opened as a labelled PR automatically: 🎥 Watch it open a real PR, live: And here's the pull request FixForward opened on a clean demo repo — Copilot's fix, the before/after verification table, and the high-confidence label, all generated automatically: Try it yourself: # locally: fix a broken build AND open the PR fixforward run --open-pr --min-confidence 0.7 # in CI: end-to-end, hands-off fixforward ship --min-confidence 0.6 The repo ships with intentionally-broken Python/Node/Rust demos so you can watch the whole loop, plus a one-click "Demo – Auto-fix a broken build" GitHub Action. 🔗 Repo: https://github.com/stackmasteraliza/fixforward 📦 PyPI: https://pypi.org/project/fixforward/ The Comeback Story Where it was: FixForward did almost everything it promised — detect, classify, fix, verify, and even generate a polished PR title and body. Then it printed them to the terminal and stopped. The old code literally ended by telling you to finish: # display.py (v0.1) " [dim]Review the branch, then push and open a PR.[/] " There were also no automated tests — ironic for a tool that auto-fixes other people's tests. What I changed — before → after: v0.1 (before) v0.2 (after) Detect + classify failures ✅ ✅ Copilot generates the fix ✅ ✅ Verify tests pass ✅ ✅ Write the PR description ✅ ✅ Push the branch ❌ you did it ✅ automatic Open the PR ❌ you did it ✅ gh pr create Label by confidence ❌ ✅ high / needs-review / low Run in CI, hands-off ❌ laptop only ✅ GitHub Action I gave myself one rule: finish the original promise, don't bolt on unrelated features. Everything in v0.2.0 serves one sentence — go from a red build to a ready-to-merge PR with no human in the loop. The last mile — a new shipper.py . Pushes the fixforward/auto-* branch and opens the PR via gh pr create , reusing the title/body the tool already generated. The thing the name always promised. Trust, made explicit. The confidence score was computed but never used . Now every PR is labelled high-confidence / needs-review / low-confidence , --min-confidence refuses to open a PR it doesn't trust, and --auto-merge lets high-confidence fixes squash-merge once CI is green. Off the laptop — a GitHub Action. A composite Action so a failing build opens its own fix PR: - name : FixForward if : steps.tests.outcome == 'failure' uses : stackmasteraliza/fixforward@v1 with : min-confidence : " 0.6" github-token : ${{ secrets.GITHUB_TOKEN }} The proof — tests + CI. Added a unit suite for the confidence/labelling policy and the PR-report generator, plus CI on Python 3.9 / 3.11 / 3.13. The hard part of "almost done" isn't the missing code — it's that the last 5% is the unglamorous, failure-prone part (auth, remotes, CI permissions) that's easy to defer forever. Finishing FixForward meant treating that last mile as the whole point . My Experience with GitHub Copilot Two honest layers, no hand-waving. Copilot is the engine. FixForward's fix generation is a call to gh copilot — not a wrapper claim, it's the core of copilot.py : cmd = [ " gh " , " copilot " , " -- " , " -p " , prompt , # failure context + source files " --allow-all-tools " , " --add-dir " , str ( project_path ), " --silent " , ] It hands Copilot the classified failures and the relevant source and asks for the smallest change that makes the suite pass. FixForward then applies it and verifies it against real tests — so a Copilot fix only ships if it actually turns the build green. Copilot helped me finish it, too. The fiddliest part of the last mile was the gh pr create plumbing — long markdown bodies, label creation, base/head branches, and the dozen ways it fails in CI (no remote, no auth, missing scopes) — plus making the parser robust to the agentic CLI's ANSI output and its habit of editing files directly. I worked through those edge cases with Copilot, then verified each path against real gh behaviour. Built in Python. Fix engine powered by GitHub Copilot CLI. MIT licensed.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/stackmasteraliza/my-incident-to-pr-autopilot-never-actually-opened-the-pr-i-finally-finished-it-a4j

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
