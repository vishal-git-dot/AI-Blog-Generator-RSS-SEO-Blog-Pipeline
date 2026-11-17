---
title: "Automate Unpaid Invoice Follow Ups with Make and Gmail"
slug: "automate-unpaid-invoice-follow-ups-with-make-and-gmail"
author: "Stackscale"
source: "devto_ai"
published: "Tue, 17 Nov 2026 01:34:19 +0000"
description: "Stop chasing unpaid invoices by hand. Learn how to automate unpaid invoice follow ups — Make watches your invoice sheet, Gmail sends the right reminder at th..."
keywords: "invoice, due, reminder, date, make, sheet, client, unpaid"
generated: "2026-11-17T01:46:24.815108"
---

# Automate Unpaid Invoice Follow Ups with Make and Gmail

## Overview

Stop chasing unpaid invoices by hand. Learn how to automate unpaid invoice follow ups — Make watches your invoice sheet, Gmail sends the right reminder at the right time, and the chasing stops the moment a client replies or pays. This is the companion tutorial for the StackScale video above. No code, no live inbox, and no real client data — the whole flow runs on two fictional demo invoices so you can test it safely. What You Will Build A Make scenario that checks your invoice sheet every morning and sends the right Gmail reminder at the right time: gentle on day 3, firmer on day 7, final notice on day 14. The moment a client replies or pays, the reminders stop. Prerequisites / Tools A Make account (free plan is enough to start) A Gmail account A free Google Sheet with your invoices Two dummy invoices to test with — Northwind Bakery ($1,240) and Acme Studio ($860), both fictional demo names Disclosure: Some links below are affiliate links, meaning StackScale may earn a commission at no extra cost to you. Make: https://www.make.com/en/register?pc=stackscale&affiliateSource=devto Gmail: https://mail.google.com Google Sheets: https://sheets.google.com The Workflow Make reads your invoice sheet every morning, works out how many days have passed since each due date, and sends the reminder that matches the tier. Before sending anything, it checks Gmail for a reply from that client and checks the sheet for a paid status. Either one stops the chase. Step 1: Build the Invoice Sheet One row per invoice, with columns for client, amount, invoice date, due date, status, and last reminder sent. The due date is the trigger — every reminder is counted from it. Keep status simple: unpaid, paid, or replied. Step 2: Schedule the Make Scenario In Make, set the scenario to run every morning at nine. It opens the sheet, reads every row still marked unpaid, and works out the days since the due date. Only invoices due for a reminder move on. Step 3: Build the 3-Tier Escalation Copy this schedule as-is: Day 3 after the due date — Gentle reminder: a short, friendly note that the invoice is due. Day 7 after the due date — Firmer reminder: restates the amount and the due date. Day 14 after the due date — Final notice: asks the client to confirm payment or get in touch. Three tiers, three templates — the right tone at the right time. Step 4: Add the Reply Stop Before Make sends any reminder, it checks Gmail for a reply from that client and checks the sheet for a status of paid. If either one is true, the reminder is skipped. Copy this field mapping into the sheet module: { "Client" : "client name" , "Amount" : "invoice amount" , "Invoice date" : "invoice date" , "Due date" : "due date" , "Status" : "unpaid / paid / replied" , "Last reminder sent" : "last reminder sent" } Step 5: Test with Dummy Invoices Set Northwind Bakery three days past due and Acme Studio seven days past due, run the scenario once by hand, and watch: a gentle reminder goes to Northwind, a firmer one to Acme. Two emails, two tiers, zero typing. The Finished Result Every unpaid invoice chased on schedule, in the right tone, and stopped the moment a client replies or pays. Open the sheet each morning and you know exactly who was reminded. One Honest Limit This flow cannot see a payment made outside your sheet. If a client pays by bank transfer and nobody marks the invoice paid, Make keeps sending reminders — keep the sheet as your source of truth. Invoice-chaser flows are not new either: Make Community, n8n, and Apps Script versions all exist. The point is the route, the reply stop, and the three tiers. Watch the Full Tutorial The video at the top walks through the same five steps with the live mockups. All mockups in the video are synthetic, created for this tutorial, with dummy data only — no real client is shown, and no real email address appears anywhere. New automation tutorials every day on StackScale — subscribe on YouTube at https://www.youtube.com/@StackScaleHQ .

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/stackscale/automate-unpaid-invoice-follow-ups-with-make-and-gmail-2lbi

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
