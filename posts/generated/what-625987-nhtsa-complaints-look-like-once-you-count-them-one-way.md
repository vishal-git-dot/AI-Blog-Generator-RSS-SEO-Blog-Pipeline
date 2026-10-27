---
title: "What 625,987 NHTSA complaints look like once you count them one way"
slug: "what-625987-nhtsa-complaints-look-like-once-you-count-them-one-way"
author: "Iqbal Taher"
source: "devto_python"
published: "Tue, 27 Oct 2026 11:49:07 +0000"
description: "Every car owner in the US can file a safety complaint with NHTSA, and every one of those complaints is public. The catch is the format. The flat file is abou..."
keywords: "model, one, complaint, complaints, can, most, nhtsa, file"
generated: "2026-10-27T11:53:35.652093"
---

# What 625,987 NHTSA complaints look like once you count them one way

## Overview

Every car owner in the US can file a safety complaint with NHTSA, and every one of those complaints is public. The catch is the format. The flat file is about 1.6 GB of tab-separated text, one row per complaint per component , written for investigators rather than for anyone trying to answer a simple question like "which models draw the most complaints?" I wanted that answer for model years 2010 to 2025, and I wanted it in a form other people could check and cite. Here is what I learned turning the raw file into a small, citable dataset. One complaint, one vehicle, counted once The first trap is double counting. A single complaint can sit on several rows, because the owner ticked more than one component (say, "steering" and "electrical system"). If you count rows, a busy complaint looks like three. So the rule is simple and written down before any counting starts: Each complaint is counted once per make, model and model year , keyed on its complaint number. It is counted once per component it names, so component totals can add up to more than the vehicle total. Writing the rule first matters more than the code. It is what lets someone else rebuild the numbers and get the same result. Keep NHTSA's own names It is tempting to tidy model names that appear under several spellings, or merge sub-components. I didn't. Model names and components stay exactly as NHTSA records them. Merging feels cleaner, but every merge is a judgment call someone else can't reproduce. When I tested merging the common name variants anyway, none of the top 25 rows moved. Counts are not failure rates The file has no sales figures. A model that sold in huge numbers can collect more complaints than a rarer car with a worse record. That is the single most important caveat, so it goes in the dataset card, the report and the CSV notes, not in a footnote. What came out From the copy of the file dated August 25, 2026: 625,987 complaints across 4,087 make, model and model-year combinations. The 2010 Ford Fusion has the most of any vehicle, 5,126, with steering named most. Ford holds 17 of the 25 most complained-about vehicles. The only vehicle from model year 2023 or newer in the top 100 is the 2023 Tesla Model Y. Making it citable A dataset nobody can cite is a dataset nobody uses. So the CSV (one row per make, model, model year and component, 90,254 rows), a JSON summary and the build script are archived on Zenodo with a DOI (10.5281/zenodo.23685716), and mirrored on GitHub, Hugging Face and Kaggle under CC BY 4.0. Each edition stays frozen at its own address, so a number quoted today still points to the same number next year. If you want the charts, the full ranking and the method written out for non-developers, the write-up is here: the most complained-about cars ranked by NHTSA complaints . I'm Iqbal Taher. I write for Oil & Miles , where we turn federal car records into plain-English guides.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/iqbaltaher/what-625987-nhtsa-complaints-look-like-once-you-count-them-one-way-f72

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
