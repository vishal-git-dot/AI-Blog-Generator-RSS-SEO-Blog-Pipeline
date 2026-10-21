---
title: "How to validate an email list in Python without SMTP (syntax, MX, disposable)"
slug: "how-to-validate-an-email-list-in-python-without-smtp-syntax-mx-disposable"
author: "PennyData"
source: "devto_python"
published: "Wed, 21 Oct 2026 04:00:32 +0000"
description: "Disclosure: I publish the Apify actor used below (pennydata/bulk-email-validator-no-smtp) and it was built with AI assistance (Claude). This is a how-to, not..."
keywords: "com, email, true, false, disposable, smtp, actor, valid"
generated: "2026-10-21T04:08:31.253070"
---

# How to validate an email list in Python without SMTP (syntax, MX, disposable)

## Overview

Disclosure: I publish the Apify actor used below (pennydata/bulk-email-validator-no-smtp) and it was built with AI assistance (Claude). This is a how-to, not a benchmark. Short answer: this runs syntax, DNS/MX, disposable and role-address checks on a list of emails, without ever opening a connection to a mail server. from apify_client import ApifyClient client = ApifyClient ( " YOUR_APIFY_TOKEN " ) run = client . actor ( " pennydata/bulk-email-validator-no-smtp " ). call ( run_input = { " emails " : [ " test@gmail.com " , " info@example.com " , " bob@mailinator.com " ]} ) rows = list ( client . dataset ( run [ " defaultDatasetId " ]). iterate_items ()) keep = [ r [ " email " ] for r in rows if r [ " valid " ] and not r [ " isRole " ]] Before a newsletter send you want to drop malformed addresses, dead domains and throwaway inboxes. Many validators do this by opening SMTP connections to the recipient's mail server, which is slow and can get your IP flagged. This actor never contacts a mail server: it checks syntax and DNS only. 1. Input { "emails" : [ "test@gmail.com" , "info@example.com" ] } You can also pass csvUrl (a public CSV; it uses the column whose header contains "email"), maxEmails and concurrency . Duplicates are validated once. (Full call shown at the top.) Actor page: https://apify.com/pennydata/bulk-email-validator-no-smtp 3. Output Real rows from running the validation code locally (MX lists shortened, checkedAt omitted): { "email" : "test@gmail.com" , "valid" : true , "status" : "deliverable_domain" , "reason" : null , "domain" : "gmail.com" , "hasMx" : true , "hasARecord" : true , "isDisposable" : false , "isRole" : false , "isFreeProvider" : true , "didYouMean" : null } { "email" : "info@example.com" , "valid" : false , "status" : "invalid_domain" , "reason" : "null_mx" , "domain" : "example.com" , "mxRecords" : [], "hasMx" : false , "hasARecord" : true , "isDisposable" : false , "isRole" : true , "isFreeProvider" : false , "didYouMean" : null } { "email" : "bob@mailinator.com" , "valid" : false , "status" : "disposable" , "reason" : "disposable_domain" , "domain" : "mailinator.com" , "hasMx" : true , "isDisposable" : true , "isRole" : false } Statuses: deliverable_domain , fallback_a_record , disposable , invalid_domain , invalid_syntax , unknown (DNS failed after retries). A SUMMARY record holds counts per status. isRole flags info@ , admin@ , noreply@ style addresses and didYouMean suggests fixes for typos of big providers. Honest limits It cannot tell whether a specific mailbox exists. valid: true means well-formed with a domain that accepts mail. Catch-all domains and non-existent users on real domains pass. Disposable detection uses the open disposable-email-domains list (CC0); brand-new throwaway services are missed until it updates. Role, free-provider and typo lists are short, hand-curated lists. DNS answers change over time, so rerun before a big send. Pricing is pay per event ($0.0008 per validated email at the time of writing; unknown rows are not charged). Check the actor page for the current price. Written with AI (Claude).

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/jeezleweez_71e2a581f71298/how-to-validate-an-email-list-in-python-without-smtp-syntax-mx-disposable-546f

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
