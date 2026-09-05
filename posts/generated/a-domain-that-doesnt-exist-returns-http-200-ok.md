---
title: "A domain that doesn't exist returns HTTP 200 OK"
slug: "a-domain-that-doesnt-exist-returns-http-200-ok"
author: "Devil Scrapes"
source: "devto_python"
published: "Sat, 05 Sep 2026 14:46:21 +0000"
description: "Quick answer Query a domain that does not exist over DNS-over-HTTPS and you get HTTP 200 OK . The failure is in the JSON body, as "Status": 3 . If your DoH c..."
keywords: "not, domain, dns, com, resolver, name, type, github"
generated: "2026-09-05T14:55:33.601904"
---

# A domain that doesn't exist returns HTTP 200 OK

## Overview

Quick answer Query a domain that does not exist over DNS-over-HTTPS and you get HTTP 200 OK . The failure is in the JSON body, as "Status": 3 . If your DoH client checks response.raise_for_status() and moves on, every nonexistent domain in your list looks like a successful lookup that happened to return no records. Which is also exactly what a real domain with no MX record looks like. DoH is a transport, not a result 🌐 This is the mental model that fixes it. cloudflare-dns.com/dns-query is not a REST API that answers questions about domains. It is DNS wrapped in HTTP , and the two layers report completely independent outcomes: HTTP status — did the resolver receive and answer your query? Status field — what did DNS itself say? The resolver answering "that domain does not exist" is, from HTTP's point of view, a total success. It got the question, it knows the answer, it's telling you. 200. Here it is: curl -s -H 'accept: application/dns-json' \ 'https://cloudflare-dns.com/dns-query?name=no-such-domain-xyzzy-9182.com&type=A' HTTP 200 {"Status": 3, ...} 3 is NXDOMAIN . The codes you actually need: Status Name What it means 0 NOERROR Query succeeded (may still have zero answers!) 2 SERVFAIL Resolver broke — often DNSSEC validation failure 3 NXDOMAIN Domain does not exist 5 REFUSED Resolver declined to answer And note the trap inside the trap: Status: 0 with no Answer array is not an error either. github.com genuinely has no CAA record. That's a fact about GitHub, not a failure of your lookup, and the two must not collapse into the same empty cell in your spreadsheet. Everything is an integer 🔢 The other thing that surprises people is that the wire format doesn't use the names anyone knows. Real response, github.com MX: { "Status" : 0 , "Question" : [{ "name" : "github.com" , "type" : 15 }], "Answer" : [{ "name" : "github.com" , "type" : 15 , "TTL" : 300 , "data" : "0 github-com.mail.protection.outlook.com." }] } type: 15 is MX . Not "MX" . If you're joining record types across a spreadsheet, 15 and 16 and 28 are what you get, and a human reading that column has to keep a lookup table in their head. The mapping is small and closed, so decoding it once at the edge is strictly better than making every downstream consumer do it: NUM_TO_TYPE = { 1 : " A " , 2 : " NS " , 5 : " CNAME " , 6 : " SOA " , 15 : " MX " , 16 : " TXT " , 28 : " AAAA " , 257 : " CAA " } STATUS_TO_NAME = { 0 : " NOERROR " , 2 : " SERVFAIL " , 3 : " NXDOMAIN " , 5 : " REFUSED " } Unknown values degrade to TYPE65 / STATUS_9 rather than throwing — a resolver is allowed to return a record type we've never heard of, and that is not a reason to lose the row. The one that actually bit us: your two resolvers disagree on shape 🪤 We query Cloudflare and fall back to Google, so a lookup survives either resolver having a bad day. Sensible. Here's the same query to both, seconds apart: Cloudflare: "Question" : [{ "name" : "github.com" , "type" : 15 }] Google: "Question" : [{ "name" : "github.com." , "type" : 15 }] Look at the name . Google returns the fully-qualified form with the trailing dot . Cloudflare doesn't. Both are correct — github.com. is the technically-proper absolute name. But it means the shape of your output row now depends on which resolver happened to answer , which is a function of who was having a bad minute. A customer joining our output against their own domain list gets a clean match for most rows and a silent miss for the handful that failed over to Google. That's the nastiest class of bug in a fallback system: it only appears when the fallback fires , so it is absent from every test, every demo, and every run you watched. It shows up in production, on a subset of rows, for reasons that have nothing to do with the domain itself. The fix is a rule, not a patch: a fallback must normalize its output shape, not just its availability. If two sources can answer the same question, the caller must not be able to tell which one did. We normalize the name and echo back the domain exactly as the customer supplied it, then record which resolver answered in its own field — so the provenance is available without being load-bearing. What the Actor gives you The DNS Records Lookup Scraper takes a list of domains and returns one row per domain with every record type decoded into something readable: A , AAAA , MX , TXT , NS , CNAME , SOA , CAA MX , not 15 . NOERROR , not 0 . two independent DoH resolvers with automatic fallback, and the answering resolver recorded per row per-(domain, record-type) fault isolation — a SERVFAIL on one lookup never takes the batch down Useful for domain-portfolio monitoring, DNS change detection, mail-provider fingerprinting across a list of companies, and pre-migration audits. The honest limitations 🚧 DoH resolvers return what the public DNS says; split-horizon and internal zones are invisible by design. TTLs are the resolver's cached remainder, not the authoritative value — two runs minutes apart will legitimately differ. No DNSSEC chain validation output; a SERVFAIL from a DNSSEC failure is reported as SERVFAIL , not diagnosed. Pricing $0.20 per run plus $0.001 per row — about $1.20 per 1,000 results . A run that finds nothing costs the start fee and nothing else. → DNS Records Lookup Scraper on Apify Built by Devil Scrapes . We handle the resolvers that disagree about trailing dots, the 200 OK that means NXDOMAIN, and the integers nobody wants in their spreadsheet.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/devil_scrapes/a-domain-that-doesnt-exist-returns-http-200-ok-1omo

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
