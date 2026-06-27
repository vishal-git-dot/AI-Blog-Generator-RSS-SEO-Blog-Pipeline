---
title: "A practical GitHub Actions baseline for Python projects"
slug: "a-practical-github-actions-baseline-for-python-projects"
author: "Thomas Reid"
source: "devto_python"
published: "Sat, 27 Jun 2026 18:55:15 +0000"
description: "Most Python projects do not need a complicated CI/CD setup on day one. They need a workflow that answers a few basic questions every time code changes: Does ..."
keywords: "python, name, run, actions, github, workflow, install, tests"
generated: "2026-06-27T19:36:59.126816"
---

# A practical GitHub Actions baseline for Python projects

## Overview

Most Python projects do not need a complicated CI/CD setup on day one. They need a workflow that answers a few basic questions every time code changes: Does the project install in a clean environment? Does linting catch obvious mistakes? Do the tests run before the code is merged? Is deployment kept separate from ordinary pull request checks? Here is the small baseline I usually start with. name : Python CI on : push : branches : - main - master pull_request : permissions : contents : read jobs : quality-and-tests : name : Quality checks and tests runs-on : ubuntu-latest strategy : fail-fast : false matrix : python-version : - " 3.11" - " 3.12" steps : - name : Check out repository uses : actions/checkout@v4 - name : Set up Python uses : actions/setup-python@v5 with : python-version : ${{ matrix.python-version }} cache : pip - name : Install dependencies run : | python -m pip install --upgrade pip if [ -f requirements.txt ]; then pip install -r requirements.txt; fi pip install ruff pytest - name : Lint with ruff run : ruff check . - name : Check formatting with ruff run : ruff format --check . - name : Run tests run : pytest That is not a full release process. It is a starting point. The important part is the separation of concerns. Pull requests run checks. Deployment comes later, after the test workflow is trusted. Secrets and cloud credentials should not be added to a basic PR workflow unless the job genuinely needs them. For a small Python project, this is often enough to catch the common mistakes: a dependency missing from requirements.txt a formatting or import issue that only shows up on another machine tests that pass locally but fail in a clean runner accidental changes to code paths that are not usually exercised manually I have put a small public sample repo here: https://github.com/taupirho/github-actions-python-ci-sample It includes the workflow, a minimal pyproject.toml , a tiny package, and a pytest example. If you want the fuller version, I have also packaged a GitHub Actions CI/CD Starter Pack for Python on Gumroad. It includes two walkthrough PDFs, reusable workflow/config files, a release gate, a readiness checklist, and troubleshooting notes for common GitHub Actions failures. Pack: https://thomasreid4.gumroad.com/l/pafvzf?utm_source=devto&utm_medium=article&utm_campaign=github_actions_pack_launch&utm_content=article_footer

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/thomas_reid_ebd566e4d12ce/a-practical-github-actions-baseline-for-python-projects-276a

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
