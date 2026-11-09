---
title: "A remote job digest in about 100 lines of Python (no API key)"
slug: "a-remote-job-digest-in-about-100-lines-of-python-no-api-key"
author: "ixilig"
source: "devto_python"
published: "Mon, 09 Nov 2026 15:39:29 +0000"
description: "Job boards are noisy. I wanted one short list: remote jobs from the last few days that match my keywords, with the titles I do not want filtered out. RemoteO..."
keywords: "python, jobs, days, job, one, not, feed, remote"
generated: "2026-11-09T15:46:00.537837"
---

# A remote job digest in about 100 lines of Python (no API key)

## Overview

Job boards are noisy. I wanted one short list: remote jobs from the last few days that match my keywords, with the titles I do not want filtered out. RemoteOK publishes a public JSON feed, so a small script with only the standard library is enough. What it does Downloads the public feed and skips the first entry (a legal notice, not a job). Keeps jobs newer than N days that match at least one keyword and do not contain excluded words in the title. Writes a markdown list or a CSV, with the original link on every row. Usage python jobdigest.py --keywords python,javascript,react,node,web,automation --exclude senior,staff,principal -o jobs.md python jobdigest.py --format csv -o jobs.csv A real run Output of one live run (3 jobs matched out of the last 7 days): # Remote jobs, last 7 days (3 found) - AI Developer at Salvo Software (2.6 d ago) | dev, grafana, infosec, python, docker - Feltsense AI Engineer at Silver.dev (4.0 d ago) | $60,000-$110,000 | design, sys admin, exec - Operations Expert with Python for AI Supply Chain Task Design at Toptal (4.0 d ago) | Docker, Git, Python The part worth copying The filter is a pure function: parse(feed, now, days, keywords, exclude). It takes the clock as an argument, so tests do not depend on today's date. The tests cover the age cutoff, keyword and exclude logic, names with non-ASCII letters, jobs without a timestamp or tags, and an empty result. Limits It depends on the RemoteOK feed format; if the format changes the script needs an update. Keyword matching is simple substring matching on title, tags and company. Please keep request rates low and link back to the job pages, as RemoteOK asks. Get it JobDigest is one of three small tools (with a price tracker and a portfolio template) in a bundle on Gumroad for $9: https://ixilig.gumroad.com/l/jwxoxh Built together with Claude (an AI assistant); I ran and checked the code myself.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/ixilig/a-remote-job-digest-in-about-100-lines-of-python-no-api-key-1f4h

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
