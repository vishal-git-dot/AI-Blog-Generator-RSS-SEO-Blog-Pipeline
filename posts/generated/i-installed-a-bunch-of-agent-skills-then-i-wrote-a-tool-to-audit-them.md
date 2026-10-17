---
title: "I installed a bunch of agent skills. Then I wrote a tool to audit them."
slug: "i-installed-a-bunch-of-agent-skills-then-i-wrote-a-tool-to-audit-them"
author: "TECHDEV"
source: "devto_ai"
published: "Sat, 17 Oct 2026 10:02:54 +0000"
description: "Every week a new agent skills pack shows up on GitHub Trending. I installed a few. Then a few more. Then I copied skills from three different packs into one ..."
keywords: "skill, name, skills, description, missing, audit, frontmatter, you"
generated: "2026-10-17T10:24:53.459865"
---

# I installed a bunch of agent skills. Then I wrote a tool to audit them.

## Overview

Every week a new agent skills pack shows up on GitHub Trending. I installed a few. Then a few more. Then I copied skills from three different packs into one folder. That is when things got weird. Two skills had the same name. The agent picked one at random. Two more had almost identical descriptions, so both triggered on the same prompt. One skill had no description at all, so the agent never picked it. I had no idea until I started reading every SKILL.md by hand. So I built a tiny tool to do that reading for me: skill-audit . What it does One command audits a whole skills folder: skill-audit check --path ~/.claude/skills It checks for: Duplicate names — two skills declaring the same name Invalid names — anything that is not kebab-case Missing name / description — the description is how the agent decides when to trigger a skill Missing frontmatter — a SKILL.md with no --- block Duplicate / overlapping descriptions — identical text, or >=70% token overlap, so two skills fight over the same prompt Description too short / too long — under 20 chars, or over 1024 Thin body — a header, not a skill Missing SKILL.md — a folder agents will never discover No version — so you can tell whether you have the latest Exit code 0 means no errors. Warnings never fail the run on their own, so you can use it in CI. Demo $ skill-audit check --path examples/messy [ERROR] duplicate-name: Duplicate skill name 'dup-skill' [ERROR] invalid-name: 'Bad Name' must be kebab-case [ERROR] missing-description: no-desc has no 'description' [ERROR] missing-description: (unnamed) has no 'description' [ERROR] missing-name: no-frontmatter/SKILL.md has no 'name' [WARN ] frontmatter-parse: no-frontmatter/SKILL.md missing frontmatter block [WARN ] no-version: (unnamed) has no 'version' in frontmatter Summary: 5 error(s), 2 warning(s), 5 skill(s). Try it git clone https://github.com/techdevfun/skill-audit.git cd skill-audit PYTHONPATH = src python -m skill_audit check --path examples/good PYTHONPATH = src python -m skill_audit check --path examples/messy || true Zero dependencies, Python 3.9+ stdlib only. Tests + CI included. Repo: https://github.com/techdevfun/skill-audit Existing skill packs add more skills. This one tells you whether the ones you already have are healthy. If you maintain a pack, running this in CI catches the duplicate-name / missing-description breakage before your users do.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/techdevfun/i-installed-a-bunch-of-agent-skills-then-i-wrote-a-tool-to-audit-them-4e2h

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
