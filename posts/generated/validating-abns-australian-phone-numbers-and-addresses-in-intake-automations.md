---
title: "Validating ABNs, Australian Phone Numbers and Addresses in Intake Automations"
slug: "validating-abns-australian-phone-numbers-and-addresses-in-intake-automations"
author: "Ujjwal Dubey"
source: "devto_python"
published: "Sun, 25 Oct 2026 11:01:00 +0000"
description: "If you build intake or invoicing automations for Australian businesses, three fields cause most of the bad data: the ABN, the phone number and the address. V..."
keywords: "australian, digits, raw, return, you, abn, number, checksum"
generated: "2026-10-25T11:03:34.771946"
---

# Validating ABNs, Australian Phone Numbers and Addresses in Intake Automations

## Overview

If you build intake or invoicing automations for Australian businesses, three fields cause most of the bad data: the ABN, the phone number and the address. Validating them at the edge saves a lot of manual clean-up later. These are checks worth adding to any AI automation agency builds for Australian businesses project. (Disclosure: I co-founded NxFlowAI, a Mumbai-based agency that works remotely.) ABN: check the checksum before you look it up An Australian Business Number has 11 digits and a published checksum. Subtract 1 from the first digit, multiply each digit by its weight, sum, and the total must divide evenly by 89. ABN_WEIGHTS = [ 10 , 1 , 3 , 5 , 7 , 9 , 11 , 13 , 15 , 17 , 19 ] def abn_is_valid ( raw : str ) -> bool : digits = [ int ( c ) for c in raw if c . isdigit ()] if len ( digits ) != 11 : return False digits [ 0 ] -= 1 total = sum ( d * w for d , w in zip ( digits , ABN_WEIGHTS )) return total % 89 == 0 A valid checksum only means the number is well formed. If the business status matters (for example, before invoicing), look it up through the official ABN Lookup service and check its terms of use. Phones: store +61 in E.164 Australian numbers arrive as 0412 345 678 , +61 412 345 678 or 61412345678 . Normalise once: def au_phone_e164 ( raw : str ): d = "" . join ( c for c in raw if c . isdigit ()) if d . startswith ( " 61 " ): d = d [ 2 :] if d . startswith ( " 0 " ): d = d [ 1 :] if len ( d ) != 9 : return None return " +61 " + d For anything beyond simple cases, use a maintained library such as phonenumbers with region AU . Addresses: state and postcode Store state as one of NSW, VIC, QLD, WA, SA, TAS, ACT, NT. Store postcode as a four-character string. Keep the original full address for whoever drives there. If you add a validation service, read its terms and pricing yourself. Where it runs Validate in the form or webhook handler. If a field fails, do not reject the enquiry; flag it for a person and continue. A lost lead is worse than a messy one. The step before code is knowing which fields the business really needs; our field-by-field workflow mapping notes cover that.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/ujjwal_dubey_9/validating-abns-australian-phone-numbers-and-addresses-in-intake-automations-17kd

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
