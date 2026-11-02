---
title: "Find Federal Contracts Before the RFP: Track SAM.gov Sources Sought Notices in Python"
slug: "find-federal-contracts-before-the-rfp-track-samgov-sources-sought-notices-in-python"
author: "Loomwise"
source: "devto_python"
published: "Mon, 02 Nov 2026 15:09:09 +0000"
description: "By the time a federal solicitation (RFP or RFQ) hits SAM.gov, the requirement is mostly written, and often written around whoever talked to the agency first...."
keywords: "notices, csv, sources, sought, you, date, responsedeadline, days"
generated: "2026-11-02T15:18:23.748184"
---

# Find Federal Contracts Before the RFP: Track SAM.gov Sources Sought Notices in Python

## Overview

By the time a federal solicitation (RFP or RFQ) hits SAM.gov, the requirement is mostly written, and often written around whoever talked to the agency first. The firms that win consistently show up earlier, at the Sources Sought and Special Notice stage, when the agency is still doing market research and asking "who out there can do this?" Answering a Sources Sought notice costs a few pages. It puts you on the contracting officer's radar, and if enough small businesses respond, it can push the agency to set the contract aside for small businesses. This post shows how to pull every Sources Sought and Special Notice from the last 14 days in your NAICS codes , with open response deadlines, from SAM.gov's free daily data file. No API key needed. Run on Oct 22, 2026: 1,397 early-stage notices in 14 days: 900 Sources Sought and 497 Special Notices. 169 were in the sample NAICS codes (IT services, consulting, building construction, building trades and facilities support) with a response date still open. The next deadlines included a FEMA deployment-management software requirement, Defense Department grounds maintenance in Pennsylvania, and range improvements for the Justice Department. The data source SAM.gov Contract Opportunities full extract : a free daily CSV, about 200 MB, sorted newest first. The script streams it and stops once it passes the date window, so it never downloads the whole file. The script import csv , io , sys , requests from collections import Counter from datetime import date , timedelta csv . field_size_limit ( sys . maxsize ) URL = " https://s3.amazonaws.com/falextracts/Contract%20Opportunities/datagov/ContractOpportunitiesFullCSV.csv " DAYS = 14 since = ( date . today () - timedelta ( days = DAYS )). isoformat () def recent_opportunities (): """ Stream SAM.gov ' s public daily extract (about 200 MB, newest first) and stop once rows get older than the window. """ with requests . get ( URL , stream = True , timeout = 300 ) as r : r . raise_for_status () r . raw . decode_content = True reader = csv . DictReader ( io . TextIOWrapper ( r . raw , encoding = " cp1252 " , errors = " replace " , newline = "" )) older = 0 for row in reader : if row [ " PostedDate " ][: 10 ] >= since : older = 0 yield row else : older += 1 if older > 300 : # small safety margin; the file is sorted newest first return NAICS_PREFIXES = ( " 5415 " , " 5416 " , " 2362 " , " 2382 " , " 5617 " ) # IT, consulting, building construction, building trades, facilities KEEP = [ " NoticeId " , " Title " , " Type " , " PostedDate " , " ResponseDeadLine " , " Department/Ind.Agency " , " Office " , " SetASide " , " NaicsCode " , " PopState " , " Link " ] # contact name/email/phone columns are deliberately skipped early = [{ k : r . get ( k , "" ) for k in KEEP } for r in recent_opportunities () if r [ " Type " ] in ( " Sources Sought " , " Special Notice " ) ] print ( Counter ( r [ " Type " ] for r in early )) today = date . today (). isoformat () # keep my NAICS codes, and drop notices whose response date already passed (some reposts carry old dates) mine = [ r for r in early if r [ " NaicsCode " ]. startswith ( NAICS_PREFIXES ) and ( not r [ " ResponseDeadLine " ] or r [ " ResponseDeadLine " ][: 10 ] >= today )] print ( len ( mine ), " early-stage notices in my NAICS codes; next deadlines: " ) for r in sorted (( r for r in mine if r [ " ResponseDeadLine " ]), key = lambda r : r [ " ResponseDeadLine " ])[: 5 ]: print ( " - " , r [ " ResponseDeadLine " ][: 10 ], r [ " NaicsCode " ], r [ " Title " ][: 60 ], " | " , r [ " Department/Ind.Agency " ][: 30 ]) with open ( " sources_sought.csv " , " w " , newline = "" ) as f : w = csv . DictWriter ( f , fieldnames = KEEP ); w . writeheader (); w . writerows ( mine ) It prints the soonest deadlines and saves the full list to sources_sought.csv . Three things that will trip you up Reposted notices carry old deadlines. Some recently posted notices still have a response date from a past year. Filter ResponseDeadLine >= today , as the script does, or you'll waste time on closed notices. Special Notices are mixed. They include industry days, draft RFPs and intent-to-sole-source notices. Intent-to-sole-source is worth reading: if you can do the work, you can often challenge it within the response window. NAICS prefixes beat exact codes. startswith("5415") catches all of 541511, 541512, 541513 and 541519. Agencies don't always pick the code you'd expect. A simple weekly workflow Run it Monday morning and open sources_sought.csv in a spreadsheet. Mark the notices that fit, then answer them with a 2 to 5 page capability statement that responds to the questions asked. Save the NoticeId values you answered. When the solicitation drops, it usually links back to the same notice history. Optional: I run this as a hosted, scheduled search with NAICS and state filters: Federal Sources Sought Notices (ready-made search) (paid per result). Disclosure: it's my tool. The script above does the same job for free.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/loomwise/find-federal-contracts-before-the-rfp-track-samgov-sources-sought-notices-in-python-4jnj

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
