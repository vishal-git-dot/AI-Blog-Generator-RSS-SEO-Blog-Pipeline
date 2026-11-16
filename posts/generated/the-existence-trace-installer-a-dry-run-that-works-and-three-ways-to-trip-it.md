---
title: "The existence-trace installer: a dry run that works, and three ways to trip it"
slug: "the-existence-trace-installer-a-dry-run-that-works-and-three-ways-to-trip-it"
author: "Ming"
source: "devto_ai"
published: "Mon, 16 Nov 2026 15:10:22 +0000"
description: "I maintain two small open-source CLIs for working with AI agents. aisync is a local CLI for Multi-Agent Context Management, Coordination & Observability acro..."
keywords: "run, install, dry, github, bash, existence, trace, python"
generated: "2026-11-16T15:22:11.711039"
---

# The existence-trace installer: a dry run that works, and three ways to trip it

## Overview

I maintain two small open-source CLIs for working with AI agents. aisync is a local CLI for Multi-Agent Context Management, Coordination & Observability across AI coding tools. existence-trace is a journal that an AI reads, and it has to prove it used what it learned. This post is about the second one's installer, the first thing a new user runs. Its README promises that it "never edits your shell config without asking". I read the script, ran only its dry run, and tried the ways a user could trip over it. I used a temporary HOME and TMPDIR , so nothing on my machine could change. The script is the one served at https://maxont.github.io/existence-trace/install.sh (4,382 bytes, the same bytes as docs/install.sh on main ). I read the whole script before running anything. The machine had Python 3.14.8, uv and pipx . What the script does It checks that python3 is 3.11 or newer, asks the GitHub API for the latest release, and installs the wheel with uv tool install , pipx install or pip install --user , in that order of preference. I found no line that writes to a shell config file. When etrace is not on PATH afterwards it prints a command for you to run instead. I did not run the real install, so I did not check what uv tool install itself does to your shell setup. The dry run works, in the right form cat install.sh | bash -s -- --dry-run [1/3] Checking Python (needs 3.11 or newer) ok: Python 3.14.8 [2/3] Getting existence-trace asking GitHub for the latest release... latest: existence_trace-0.4.6-py3-none-any.whl [dry-run] download https://github.com/MaxonT/existence-trace/releases/download/v0.4.6/existence_trace-0.4.6-py3-none-any.whl [3/3] Installing installer: uv [dry-run] uv tool install --force ... dry-run finished: nothing was changed. Exit code 0, and the temp HOME was empty afterwards. It does contact the GitHub API to find the latest release. Trip 1: the README's --dry-run after the pipe Under the curl ... | bash line, the README says "Add --dry-run to see what it would do first." It does not say where. The obvious reading fails: cat install.sh | bash --dry-run bash: --dry-run: invalid option Exit code 2 and nothing runs, so it is harmless. The flag has to go through bash -s -- , as above. The install page on the site, which reads as instructions for an agent, shows the other working form: download the file with curl -o /tmp/etrace-install.sh , then bash /tmp/etrace-install.sh --dry-run . Trip 2: --help only works from a file bash install.sh --help # prints the header, exit 0 cat install.sh | bash -s -- --help # prints nothing, exit 1 The help text comes from sed -n '2,11p' "$0" . Under a pipe $0 is bash , there is no file to read, and the script exits 1 without a word. A mistyped flag is handled well: --dryrun prints unknown option: --dryrun and exits 2. Trip 3: an old system Python stops it, even with uv installed The Python check looks only at python3 on PATH . I put a fake python3 first on PATH that reports 3.9.6, with uv still available: error: Python 3.11+ required, found Python 3.9.6. Exit code 1. This is a simulation and not a real old machine. I did not test whether uv tool install would have found a suitable Python on its own, so the strict check may be a deliberate choice. What this does not show No real install. I ran --dry-run only, and I did not exercise the pipx , pip --user or git+ fallbacks. One machine (macOS, arm64), with uv and pipx present. The old Python is a fake. I changed nothing in the installer or the README. Each trip is filed as an issue with the commands above: the piped --dry-run form is https://github.com/MaxonT/existence-trace/issues/5 , the silent piped --help is https://github.com/MaxonT/existence-trace/issues/6 , and the old system Python is https://github.com/MaxonT/existence-trace/issues/7 . If you ship an installer Show every flag in the form people will paste, which for curl | bash is bash -s -- <flag> , and make --help work when the script comes from a pipe. Repo (MIT): https://github.com/MaxonT/existence-trace Site: https://maxont.github.io/existence-trace/ Sibling project: https://github.com/MaxonT/aisync (Multi-Agent Context Management, Coordination & Observability) This post and the test runs were written and run by an AI agent (Claude Code) for the maintainer. The outputs above are copied from those runs.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/maxont/the-existence-trace-installer-a-dry-run-that-works-and-three-ways-to-trip-it-bp8

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
