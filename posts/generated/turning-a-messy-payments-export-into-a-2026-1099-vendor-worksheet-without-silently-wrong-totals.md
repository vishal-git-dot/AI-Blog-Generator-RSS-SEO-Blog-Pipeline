---
title: "Turning a messy payments export into a 2026 1099 vendor worksheet (without silently wrong totals)"
slug: "turning-a-messy-payments-export-into-a-2026-1099-vendor-worksheet-without-silently-wrong-totals"
author: "Peter (The Trillium Company)"
source: "devto_python"
published: "Fri, 23 Oct 2026 03:22:08 +0000"
description: "For 2026 payments, the Form 1099-NEC reporting threshold goes from USD 600 to USD 2,000 (1099-MISC thresholds still vary by payment type, and backup withhold..."
keywords: "name, vendor, cells, review, total, none, amt, not"
generated: "2026-10-23T04:12:22.347949"
---

# Turning a messy payments export into a 2026 1099 vendor worksheet (without silently wrong totals)

## Overview

For 2026 payments, the Form 1099-NEC reporting threshold goes from USD 600 to USD 2,000 (1099-MISC thresholds still vary by payment type, and backup withholding can require reporting below a threshold; see the IRS page ). If you keep the books for a small business, or write scripts for someone who does, this year's vendor list needs a fresh pass. The awkward part isn't the threshold; it's the export. Here's a small, defensive way to turn a messy payments export into a reviewable vendor worksheet. This is data preparation, not tax advice. The problems in a typical export The same vendor appears as Acme Plumbing LLC , ACME PLUMBING and Acme Plumbing, L.L.C. QuickBooks reports (e.g. Transaction List by Vendor ) put title lines above the header, put the vendor name on its own "group" row, and add Total for … rows, which double-count if you sum naively Dates in several formats, some blank or TBD Amounts like $1,200.00 , (450.00) and -$75 Payments from other years mixed in Rules that keep the totals honest Find the real header row. Skip leading lines until a row has at least two header-like cells (date, amount, name, vendor, memo). Inherit the vendor from group rows and skip Total for / TOTAL rows . Group by vendor ID if you have one; otherwise by exact name (case, punctuation and spacing normalised). Don't merge Acme LLC and Acme Inc automatically. Flag them as possible same vendor and let a human confirm. Never guess a date. Unparseable or missing dates go to a review list, not into the year's total. Never drop a bad amount silently. Invalid amounts go to the review list too. Reconcile. Input total = this year's total + other years + review rows. If that doesn't hold, stop. Report TIN presence, not TIN values. The worksheet only needs a yes/no. A compact Python version import csv , re , datetime , collections def money ( s ): s = ( s or "" ). replace ( " $ " , "" ). replace ( " , " , "" ). replace ( " USD " , "" ). strip () neg = s . startswith ( " ( " ) and s . endswith ( " ) " ) or s . startswith ( " - " ) s = s . strip ( " ()- " ) try : return - float ( s ) if neg else float ( s ) except ValueError : return None def year_of ( s ): for fmt in ( " %Y-%m-%d " , " %m/%d/%Y " , " %m/%d/%y " , " %b %d, %Y " , " %d %b %Y " ): try : return datetime . datetime . strptime (( s or "" ). strip (), fmt ). year except ValueError : pass return None # -> review, never assumed def key ( name ): k = re . sub ( r " [ ' \u2019`.] " , "" , name . lower ()) return re . sub ( r " [^a-z0-9]+ " , " " , k ). strip () raw = list ( csv . reader ( open ( " payments.csv " , encoding = " utf-8-sig " ))) hi = next ( i for i , r in enumerate ( raw ) if sum ( bool ( re . search ( r " date|amount|name|vendor|memo " , c , re . I )) for c in r ) >= 2 ) hdr = [ h . strip () for h in raw [ hi ]] iD , iA = hdr . index ( " Date " ), hdr . index ( " Amount " ) iN = hdr . index ( " Name " ) if " Name " in hdr else None totals , review , group = collections . defaultdict ( float ), [], "" tin_total = inc = other = rev = 0.0 for line , r in enumerate ( raw [ hi + 1 :], start = hi + 2 ): cells = [ c . strip () for c in r ] if not any ( cells ): continue first = next ( c for c in cells if c ) if re . match ( r " ^(total|grand total)\b " , first , re . I ): continue if sum ( bool ( c ) for c in cells ) == 1 and money ( first ) is None : group = first continue name = ( cells [ iN ] if iN is not None else "" ) or group amt , yr = money ( cells [ iA ]), year_of ( cells [ iD ]) if amt is not None : tin_total += amt if amt is None or yr is None or not name : review . append (( line , name , cells [ iA ], cells [ iD ])) rev += amt or 0 continue if yr != 2026 : other += amt continue totals [ key ( name )] += amt inc += amt assert abs ( tin_total - ( inc + other + rev )) < 0.005 , " totals don ' t reconcile " for k , v in sorted ( totals . items (), key = lambda kv : - kv [ 1 ]): print ( f " { k : 40 s } { v : 12 ,. 2 f } { ' AT/OVER 2,000 ' if v >= 2000 else '' } " ) print ( len ( review ), " rows need review " ) Swap the column names for your export. In real use you'd also keep the original spelling for display, add the look-alike check (strip llc|inc|ltd|co|corp and compare) as a flag rather than a merge, and carry a tin_present column if the export has one. Don't want to run Python? Disclosure: we built a browser version of exactly these rules: https://csv.thetrilliumcompany.com/1099/tool/ . It runs entirely in the browser, so the file is never uploaded. The preview is free; downloading the worksheet, the review list and the change log is USD 19. There's a before/after sample with fictional data at https://csv.thetrilliumcompany.com/1099/ . I'm Peter at The Trillium Company (Waterloo, Ontario); questions are welcome in the comments.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/trilliumcompany/turning-a-messy-payments-export-into-a-2026-1099-vendor-worksheet-without-silently-wrong-totals-1988

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
