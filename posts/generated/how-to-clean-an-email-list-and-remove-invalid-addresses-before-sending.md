---
title: "How to clean an email list and remove invalid addresses before sending"
slug: "how-to-clean-an-email-list-and-remove-invalid-addresses-before-sending"
author: "Hay Equipos"
source: "devto_python"
published: "Fri, 02 Oct 2026 21:39:58 +0000"
description: "Every bounced email costs you a little sender reputation, and a list exported from a form, a CRM or an old spreadsheet is full of addresses that will bounce:..."
keywords: "domain, you, not, email, apify, com, run, verdict"
generated: "2026-10-02T22:01:18.331165"
---

# How to clean an email list and remove invalid addresses before sending

## Overview

Every bounced email costs you a little sender reputation, and a list exported from a form, a CRM or an old spreadsheet is full of addresses that will bounce: typos like gmial.com or .con , domains that no longer exist, throwaway inboxes and shared info@ addresses. You want to find those before you press send, not after. This guide shows how to check a whole list in one run with a small Apify Actor published by Hay Equipos called Email Validator: Syntax, MX, Disposable and Role Check . It works from public DNS only. It never sends an email and never connects to anyone's mail server. What the tool checks For every address you get one row that tells you: whether the syntax is valid whether the domain exists and accepts email (MX records, and the "null MX" record a domain uses to say it takes no mail) which mail provider runs it (Google Workspace, Microsoft 365, Proton, Zoho and others) whether it is a disposable provider (a list of about 9,000 domains) whether it is a role inbox such as info, sales, support or noreply (about 90 role names) whether it is free webmail such as Gmail or Yahoo a suggested fix when the domain looks like a typo optionally, the domain's SPF record and DMARC policy Each row ends in a verdict and a plain sentence reason : deliverable_domain : valid syntax, the domain accepts email, not disposable, not a role inbox. risky : the domain works, but the address is disposable, a role inbox, has no MX record, or the domain's name servers fail. invalid : bad syntax, the domain does not exist, or it publishes a null MX. unknown : the DNS lookup failed on the Actor's side. These rows are free; run them again. Two sample rows (values are illustrative): [ { "input" : "jane@example.con" , "email" : "jane@example.con" , "verdict" : "invalid" , "reason" : "The domain does not exist" , "isValidSyntax" : true , "domainExists" : false , "hasMx" : false , "isDisposable" : false , "isRoleAccount" : false , "suggestedEmail" : "jane@example.com" }, { "input" : "sales@example.org" , "verdict" : "risky" , "reason" : "Role account (a shared inbox such as info@ or sales@)" , "domainExists" : true , "hasMx" : true , "mxRecords" : [ "1 aspmx.l.google.com" ], "mailProvider" : "Google Workspace" , "isRoleAccount" : true , "isFreeProvider" : false } ] A summary with the count per verdict is saved in the run's key value store as SUMMARY . Step by step in the Apify Console Open the Actor from its Apify Store page and sign in to Apify Console. In the Input tab, add addresses to Emails , one per line, or paste a whole spreadsheet column into Or paste a list (new lines, commas and semicolons all work). Keep Check the domain in DNS on. Turn it off only if you want a syntax only check. Switch on Also return SPF and DMARC if you want those fields. It costs nothing extra. Leave Skip duplicates on so each address is checked once. Click Start , then export the results from the Output tab as CSV, JSON or Excel. Filter on verdict and keep the deliverable_domain rows. How to call it from code With curl, using your token from an environment variable: curl -X POST "https://api.apify.com/v2/acts/pistachio_implementation~email-validator-mx-check/run-sync-get-dataset-items" \ -H "Authorization: Bearer $APIFY_TOKEN " \ -H "Content-Type: application/json" \ -d '{"emails": ["jane@example.com", "info@example.org"], "checkSpfDmarc": true}' In Python, with the apify-client package: import os from apify_client import ApifyClient client = ApifyClient ( os . environ [ " APIFY_TOKEN " ]) run = client . actor ( " pistachio_implementation/email-validator-mx-check " ). call ( run_input = { " emails " : [ " jane@example.com " , " info@example.org " ]} ) keep = [ row [ " input " ] for row in client . dataset ( run [ " defaultDatasetId " ]). iterate_items () if row . get ( " verdict " ) == " deliverable_domain " ] print ( keep ) For large lists, prefer the Python client: the synchronous curl endpoint is meant for runs that finish within a few minutes. Pricing Pay per event: $0.0005 per email checked, which is $0.50 per 1,000 emails. There is no start fee and no platform usage charge on top. Rows with the verdict unknown are not charged, and SPF and DMARC come at no extra cost. If you turn DNS checks off, each row gets valid_syntax or invalid and is charged at the same price. You can cap the spend of any run with the maximum charge setting in Apify. Limits and what it does not do No mailbox probing. The Actor does not connect to mail servers to ask whether a specific mailbox exists (SMTP verification). It cannot tell you that jane@company.com exists while jnae@company.com does not. Catch all domains are not detected , because that also needs SMTP. A deliverable_domain verdict means the domain can receive mail, not that the person will. The disposable list is a snapshot of a public blocklist maintained on GitHub, updated with each release of the Actor, so a brand new throwaway service may not be on it yet. Up to 100,000 addresses per run, at roughly 1,000 addresses a minute. Lists with many repeated domains go faster because each domain is looked up once. What it does remove is everything that is certain to fail or likely to hurt you: broken syntax, dead domains, domains without mail, disposable and role addresses, and typos. If you need mailbox level certainty, run this first and send only the deliverable_domain rows to an SMTP verifier. Your list stays in your own Apify storage. Only the domain part of each address is looked up in public DNS. Try it on the Apify Store: https://apify.com/pistachio_implementation/email-validator-mx-check

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/hay_equipos/how-to-clean-an-email-list-and-remove-invalid-addresses-before-sending-kel

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
