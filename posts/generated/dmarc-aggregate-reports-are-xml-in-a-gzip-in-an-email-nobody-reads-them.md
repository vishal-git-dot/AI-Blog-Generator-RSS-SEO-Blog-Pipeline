---
title: "DMARC aggregate reports are XML, in a gzip, in an email. Nobody reads them."
slug: "dmarc-aggregate-reports-are-xml-in-a-gzip-in-an-email-nobody-reads-them"
author: "Email Campaign LLC"
source: "devto_python"
published: "Sat, 19 Sep 2026 20:08:59 +0000"
description: "Publishing a DMARC record with rua= is the easy part. You add the TXT record, reports start arriving, and then you discover what a report actually is: a gzip..."
keywords: "you, domain, not, reports, your, com, record, example"
generated: "2026-09-19T20:21:54.586089"
---

# DMARC aggregate reports are XML, in a gzip, in an email. Nobody reads them.

## Overview

Publishing a DMARC record with rua= is the easy part. You add the TXT record, reports start arriving, and then you discover what a report actually is: a gzipped XML attachment on an email, sent daily by every receiver that got mail claiming to be from your domain. So the reports pile up in a mailbox nobody opens, the domain stays at p=none forever, and the record that was supposed to stop people spoofing you protects nothing at all. Monitoring mode is not a policy. It is the absence of one. What is actually in the file Under the gzip it is a <feedback> document. The parts that matter: <policy_published> <domain> example.com </domain> <p> none </p> <adkim> r </adkim> <aspf> r </aspf> </policy_published> <record> <row> <source_ip> 203.0.113.10 </source_ip> <count> 12 </count> <policy_evaluated> <dkim> pass </dkim> <spf> pass </spf> </policy_evaluated> </row> <identifiers> <header_from> example.com </header_from> </identifiers> <auth_results> <dkim><domain> example.com </domain><result> pass </result></dkim> <spf><domain> example.com </domain><result> pass </result></spf> </auth_results> </record> Two things about this structure trip people up. policy_evaluated is not auth_results . The first is alignment, the second is raw authentication. You can have auth_results showing dkim=pass and policy_evaluated showing dkim=fail , and that combination is common: the message was validly signed, just by somebody else's domain. Your ESP signs with d=esp.example.net , the signature verifies perfectly, and it aligns with nothing. DMARC fails. If you only read auth_results , every one of those looks fine. count is not 1. Each <record> is an aggregate over a source IP, so a single record can represent thousands of messages. Summing records instead of counts will quietly understate the traffic. The question you are actually asking Nobody reads these reports for fun. There is exactly one question: can I move off p=none without quarantining my own mail? That reduces to: is every source sending as my domain aligned, and if not, which ones are not, and are they mine? So I wrote the smallest thing that answers it: $ dmarc_report.py ~/Maildir/new ~/Maildir/cur Domain : example.com Published p= : none Reporters : google.com Reports read : 3 (13 messages) SOURCE IP ALIGNED FAILING HEADER FROM 203.0.113.199 0 1 mail-1.example.com why: SPF none; no DKIM signature 203.0.113.10 12 0 example.com Aligned: 12 of 13 (92.3%) VERDICT: 1 message(s) did not align. Identify each source above before enforcing, or you will quarantine your own mail. A subdomain in HEADER FROM can be spared with sp=none. It reads .xml , .gz , .zip , a raw .eml , or a whole Maildir, and it is Python standard library only — no dependencies, no network calls, nothing uploaded anywhere. That last point matters more than it sounds: DMARC reports name every IP that sends as you, which is an infrastructure map you probably do not want to paste into a web form. github.com/coldemailmarketing/dmarc-report-parser — MIT. Two details worth stealing even if you write your own Deduplicate by report_id . The same report routinely arrives twice. If you are counting messages to decide whether enforcement is safe, duplicates inflate your confidence in exactly the wrong direction. Treat a subdomain failure differently from an organizational-domain failure. Subdomains inherit the organizational policy unless you publish an sp= tag. So a stray subdomain failing alignment does not have to block enforcement on your brand domain — you enforce p=quarantine and set sp=none , then deal with the subdomain separately. That one distinction is the difference between enforcing this month and enforcing next year. The limit of the whole exercise A verdict of "safe to enforce" is only as good as the sample. Aggregate reports cover mail that receivers chose to report on. If your invoicing runs through a vendor whose mail happened not to reach a reporting receiver that week, it will not appear, and it will not be in the verdict. Before you enforce, write down every system that puts your domain in a From: header — app, billing, helpdesk, newsletter, anything a vendor sends on your behalf — and confirm each one appears in the reports as aligned. The parser tells you what the reports say. It cannot tell you what they left out. If you want the records themselves checked against live DNS rather than after the fact, this does SPF, DKIM and DMARC in one pass — it counts every v=spf1 record on the host rather than the first one, which is its own separate trap.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/emailcampaignai/dmarc-aggregate-reports-are-xml-in-a-gzip-in-an-email-nobody-reads-them-1i0i

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
