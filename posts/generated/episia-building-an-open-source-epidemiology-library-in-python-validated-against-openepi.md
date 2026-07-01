---
title: "Episia: Building an Open-Source Epidemiology Library in Python, Validated Against OpenEpi"
slug: "episia-building-an-open-source-epidemiology-library-in-python-validated-against-openepi"
author: "Ariel Shadrac OUEDRAOGO"
source: "devto_python"
published: "Wed, 01 Jul 2026 19:22:05 +0000"
description: "Why Episia I am an MD candidate and a self-taught Python developer. Over the past year, working with epidemiological surveillance data in a resource-limited ..."
keywords: "episia, data, result, report, not, surveillance, design, what"
generated: "2026-07-01T20:03:10.698746"
---

# Episia: Building an Open-Source Epidemiology Library in Python, Validated Against OpenEpi

## Overview

Why Episia I am an MD candidate and a self-taught Python developer. Over the past year, working with epidemiological surveillance data in a resource-limited setting exposed a recurring gap: solid statistical epidemiology tooling exists (OpenEpi, R packages), but nothing brought compartmental modeling, biostatistics, surveillance data handling, and reporting together in a single, modern Python API with offline-first design. Episia is my attempt to close that gap. What it does Episia covers the full analytical workflow, from raw surveillance data to epidemic modeling and automated reporting. from episia import epi # Compartmental model model = epi . seir ( N = 1_000_000 , I0 = 10 , E0 = 50 , beta = 0.35 , sigma = 1 / 5.2 , gamma = 1 / 14 ) result = model . run () print ( result ) # SEIR Model # R0 : 4.900 # Peak infected : 331,751 at t=84.5 # Final size : 99.2% # Biostatistics rr = epi . risk_ratio ( a = 40 , b = 10 , c = 20 , d = 30 ) print ( rr ) # Risk Ratio: 2.667 (1.514-4.696) # Automated HTML report report = epi . report ( result , title = " SEIR Burkina Faso 2024 " ) report . save_html ( " report.html " ) Design decisions worth explaining Unified result objects. Every function, whether it is a risk ratio or a full SEIR run, returns a rich, serializable result object. This keeps plotting, export, and reporting consistent across the entire library rather than each module inventing its own return shape. Validated, not just tested. Unit tests confirm the code does what I intended. They do not confirm the statistics are correct. So beyond the test suite (1490+ tests, 84% coverage), Episia's core statistical functions are systematically validated against OpenEpi, an established reference implementation in epidemiology. The full comparison notebook is in the repository, since a validation claim without a reproducible notebook is not worth much. Offline by design. Episia has zero runtime network dependencies outside an optional DHIS2 connector used to pull surveillance data. In many of the field settings this is built for, connectivity is not something you can assume. Dual visualization backend. Every plot function accepts backend="plotly" for interactive exploration or backend="matplotlib" for publication-quality figures, same code path either way. Current state Episia is at v0.1.3, on PyPI ( pip install episia ), currently going through pyOpenSci peer review (issue #317), with a preprint on medRxiv. Source is on GitHub under MIT license. Repository: https://github.com/Xcept-Health/episia PyPI: https://pypi.org/project/episia/ Preprint: https://doi.org/10.64898/2026.04.17.26350337 What I am looking for I would value input on the API design itself, particularly whether the result-object pattern and the module structure ( models , stats , viz , data , dhis2 ) hold up under real use. Testers running it against their own data are especially useful for surfacing edge cases I have not hit yet. Contributions, issues, and pull requests are welcome, and any general recommendations for what would strengthen the library ahead of a 1.0 release are appreciated.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/iamshadrac/episia-building-an-open-source-epidemiology-library-in-python-validated-against-openepi-4ap1

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
