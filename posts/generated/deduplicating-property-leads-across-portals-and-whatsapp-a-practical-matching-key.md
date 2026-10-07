---
title: "Deduplicating Property Leads Across Portals and WhatsApp: A Practical Matching Key"
slug: "deduplicating-property-leads-across-portals-and-whatsapp-a-practical-matching-key"
author: "Ujjwal Dubey"
source: "devto_python"
published: "Wed, 07 Oct 2026 05:01:17 +0000"
description: "I co-founded NxFlowAI, an AI automation agency. This post is a standalone technique. One of the first things any AI automation for real estate lead deduplica..."
keywords: "lead, digits, phone, not, key, person, email, store"
generated: "2026-10-07T05:20:33.232371"
---

# Deduplicating Property Leads Across Portals and WhatsApp: A Practical Matching Key

## Overview

I co-founded NxFlowAI, an AI automation agency. This post is a standalone technique. One of the first things any AI automation for real estate lead deduplication project has to solve is boring and essential: the same buyer arrives from several sources, and each looks like a new lead. Portal notification emails, a website form, a Meta ad form and a direct WhatsApp message can all describe one person. If you route them separately, several agents call the same buyer. Here is a matching approach that works without any machine learning. 1. Normalise phone numbers first Phone is the strongest key in property leads, but formats vary wildly: with or without country code, spaces, leading zeros. Normalise to E.164. import re def normalise_phone ( raw : str , default_cc : str ) -> str | None : digits = re . sub ( r " \D " , "" , raw or "" ) if not digits : return None if digits . startswith ( " 00 " ): digits = digits [ 2 :] elif digits . startswith ( " 0 " ): digits = default_cc + digits [ 1 :] elif len ( digits ) <= 10 : digits = default_cc + digits return " + " + digits # default_cc is the agency's country code without '+', e.g. "971" or "91" Keep default_cc per agency, not per lead source. 2. Build a match key with fallbacks def match_keys ( lead : dict , default_cc : str ) -> list [ str ]: keys = [] phone = normalise_phone ( lead . get ( " phone " ), default_cc ) if phone : keys . append ( f " phone: { phone } " ) email = ( lead . get ( " email " ) or "" ). strip (). lower () if email : keys . append ( f " email: { email } " ) return keys Do not use name as a key on its own. Names repeat and are spelled differently across portals. 3. Decide what a match means A match on phone or email means "same person", not "same enquiry". A buyer may be interested in two different properties. Store the person once and attach enquiries to them: def upsert ( lead , store , default_cc ): for key in match_keys ( lead , default_cc ): person_id = store . index . get ( key ) if person_id : store . add_enquiry ( person_id , lead ) return person_id , " existing " person_id = store . create_person ( lead ) for key in match_keys ( lead , default_cc ): store . index [ key ] = person_id store . add_enquiry ( person_id , lead ) return person_id , " new " 4. Route by person, not by enquiry When the result is existing , route to the person's current owner. Only new people go through the assignment rule (area, project, language, rota). This single change stops most "three agents, one buyer" incidents. 5. Handle conflicts with a human If a phone matches one person and an email matches another, do not merge automatically. Flag it for a team lead. Automatic merges on conflicting keys cause quiet data loss. 6. Make it idempotent Portal notifications and webhooks get retried. Use a source-specific ID (or a hash of source, timestamp and phone) as an idempotency key so a retry does not create a second enquiry. What this does not solve It does not decide who should own a lead, and it does not write follow-up messages. It just makes sure everything after it works on one person instead of three. In practice it is one of the first things we check in a 72-hour first audit, before anything else is built. If you are deciding whether to build this yourself or rely on a CRM's built-in duplicate detection, our note on ready-made tools versus custom builds may help.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/ujjwal_dubey_9/deduplicating-property-leads-across-portals-and-whatsapp-a-practical-matching-key-4d9m

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
