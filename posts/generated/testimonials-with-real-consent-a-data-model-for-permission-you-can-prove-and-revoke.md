---
title: "Testimonials with real consent: a data model for permission you can prove and revoke"
slug: "testimonials-with-real-consent-a-data-model-for-permission-you-can-prove-and-revoke"
author: "Nazma Akter"
source: "devto_webdev"
published: "Thu, 22 Oct 2026 11:18:20 +0000"
description: ""Best candle I've ever bought." A customer quote is only worth putting on your homepage if the customer said you could, and only as long as they still agree...."
keywords: "text, consent, not, null, customer, boolean, permission, can"
generated: "2026-10-22T11:30:26.386134"
---

# Testimonials with real consent: a data model for permission you can prove and revoke

## Overview

"Best candle I've ever bought." A customer quote is only worth putting on your homepage if the customer said you could, and only as long as they still agree. In ProofLoom testimonials are built around that rule. The one-minute reel shows the flow from the customer's side and the owner's. Here's how the data model keeps it honest. 1. One link, used anywhere A collection link is a public form at /review/<form_id> . The owner can send it straight to customers or put it on any page as a "Write a review" button. The form has a hidden honeypot field, and the same text sent to the same form within a short window is treated as a duplicate instead of a second testimonial. 2. Permissions are separate columns, and paid ads can't be granted Every grant is a row in testimonial_consents : website_publication BOOLEAN NOT NULL , social_publication BOOLEAN NOT NULL , name_display BOOLEAN NOT NULL , avatar_display BOOLEAN NOT NULL , paid_advertising BOOLEAN NOT NULL DEFAULT false CHECK ( paid_advertising = false ), wording_version TEXT NOT NULL , evidence_source TEXT NOT NULL CHECK ( evidence_source IN ( 'customer_form' , 'owner_attested' )), granted_at TIMESTAMPTZ NOT NULL DEFAULT now (), revoked_at TIMESTAMPTZ There's no single "I agree" flag. The paid_advertising column exists for the audit trail, and a CHECK constraint makes sure nothing can ever set it to true. wording_version records the exact consent text the customer saw. evidence_source says whether the customer ticked the boxes themselves or the owner recorded permission for a review received elsewhere. 3. Consent belongs to a version of the text Testimonial text is versioned ( testimonial_versions ), and each consent row points at one version through a foreign key on (testimonial_id, testimonial_version) . Fix a typo or add a translation and you get a new version. The original is kept, and the old consent no longer covers the current text. The dashboard shows "Text changed — needs renewed permission" until a new grant is recorded. 4. Showing it is a query, not a flag The website wall doesn't read a "published" boolean. It asks the database every time: t . status = 'approved' AND c . revoked_at IS NULL AND c . testimonial_version = t . current_version AND c . website_publication c is the latest consent row for that testimonial. Approval is the owner's decision, permission is the customer's, and both have to hold for the current text. Name and role are only included in the feed when name_display is true. Nothing has to be "unpublished" by hand, because the feed is derived from current state. 5. Withdrawal: a hashed token in the URL fragment On submit the customer gets a one-time token ( plwd_… ), shown once and emailed to them if they gave an address. Only its hash is stored ( withdraw_token_hash BYTEA UNIQUE ). The link is /review/withdraw#<token> : the token sits in the fragment, so it never shows up in server logs or referrer headers, and no account is needed. Withdrawing runs one transaction: the testimonial's status becomes revoked every consent row gets revoked_at and revoked_by ( customer , business or deletion ) unsent Social exports are cancelled, and an outbox event tells the Social app to flag drafts already created from it The wall query stops returning it right away. Posts that were already published can't be pulled back automatically, so the business is notified to remove them. What we'd tell someone building the same thing Store each permission separately, with the wording version and where it came from. Tie consent to a version of the text. An edited quote is a new quote. Work out publication from current state at read time instead of keeping a "published" flag you have to remember to update. Make withdrawal work without an account, and keep the token out of logs. Try it with a 14-day free trial, no card: VeloxonHub ProofLoom Happy to go deeper into the consent model or the Social hand-off in the comments.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/nazma_akter/testimonials-with-real-consent-a-data-model-for-permission-you-can-prove-and-revoke-2ckh

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
