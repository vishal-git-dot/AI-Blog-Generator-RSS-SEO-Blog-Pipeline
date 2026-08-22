---
title: "Your django-haystack Whoosh backend breaks on Python 3.13 — here's the one-line fix"
slug: "your-django-haystack-whoosh-backend-breaks-on-python-313-heres-the-one-line-fix"
author: "Priya Sundaram"
source: "devto_python"
published: "Sat, 22 Aug 2026 12:25:09 +0000"
description: "TL;DR: The Whoosh package Haystack installs is from 2016 and calls cgi.escape . The cgi module was removed in Python 3.13 , so highlighting (and sometimes im..."
keywords: "whoosh, haystack, python, django, cgi, pip, install, you"
generated: "2026-08-22T12:48:49.581341"
---

# Your django-haystack Whoosh backend breaks on Python 3.13 — here's the one-line fix

## Overview

TL;DR: The Whoosh package Haystack installs is from 2016 and calls cgi.escape . The cgi module was removed in Python 3.13 , so highlighting (and sometimes import) blows up. Swap in the maintained fork: pip install django-haystack whoosh3 — no code changes. Tested end-to-end on Haystack 3.4.0 + Django 6.1. If you run a Django site with django-haystack and the Whoosh backend, upgrading to Python 3.13 can hand you a surprise: ModuleNotFoundError: No module named 'cgi' It doesn't happen on import . It happens later — usually when Haystack renders a highlighted search result — which makes it extra confusing, because your app boots fine and then a search page 500s. Why it happens Haystack's [whoosh] extra pins Whoosh<3.0 , which resolves to Whoosh==2.7.4 — released in 2016 and unmaintained since. Deep inside it, whoosh/compat.py has a Python-2-era helper: def htmlescape ( s , quote = True ): # this is html.escape reimplemented with cgi.escape, # so it works for python 2.x, 3.0 and 3.1 import cgi s = cgi . escape ( s , quote ) ... That import cgi was fine for a decade. But cgi was deprecated in Python 3.11 and removed entirely in Python 3.13 ( PEP 594 ). The import is lazy — it only fires when the HTML formatter runs — so the failure shows up at highlight time, not at startup. The fix Whoosh was abandoned twice, but it's maintained again as a fork published to PyPI under the name whoosh3 . It installs the same top-level whoosh module, so it's a drop-in replacement — Haystack imports whoosh exactly as before and never knows the difference. Install it instead of Haystack's [whoosh] extra: pip install django-haystack whoosh3 # NOT: pip install "django-haystack[whoosh]" # that pins the old Whoosh 2.x If you already have the old one, remove it so the two don't collide on the shared whoosh import name: pip uninstall Whoosh pip install whoosh3 Your settings don't change at all: # settings.py HAYSTACK_CONNECTIONS = { " default " : { " ENGINE " : " haystack.backends.whoosh_backend.WhooshEngine " , " PATH " : os . path . join ( BASE_DIR , " whoosh_index " ), }, } Does it actually work? (I checked) I ran the full loop — a SearchIndex writing through WhooshSearchBackend , then querying it back — end-to-end on: django-haystack 3.4.0 whoosh3 3.42.0 Django 6.1 , Python 3.12 Index build, update, and search all pass, with no code changes and no shims. Every whoosh sub-module the backend touches resolves under whoosh3 ( index , analysis , fields , filedb.filestore , highlight , qparser , searching , sorting , writing , and even the obscure vendored whoosh.support.relativedelta ). And whoosh.__version__ is the (3, 42, 0) tuple that Haystack's >= (2, 5, 0) runtime guard expects. whoosh3 adds tested support for Python 3.9–3.14 , so the cgi landmine (and other latent 3.13 breakage in the old release) is gone. Why not just switch to Elasticsearch? You might not need to. If your search lives inside one Django app and you like not running a separate search server, Whoosh is still the pure-Python, zero-ops answer — BM25F ranking, faceting, highlighting, and "did you mean?" spelling correction, all from pip install . The only thing that had rotted was Python-3.13 compatibility, and that's fixed. If Whoosh-via-Haystack was working for you and only broke because of the interpreter bump, this is the smallest possible diff to get back to green. Repo (maintained fork, continues Matt Chaput's original Whoosh): https://github.com/priya-sundaram-dev/whoosh — pip install whoosh3 . I maintain the fork and I'm happy to take issues and PRs.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/priyasundaram/your-django-haystack-whoosh-backend-breaks-on-python-313-heres-the-one-line-fix-7gg

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
