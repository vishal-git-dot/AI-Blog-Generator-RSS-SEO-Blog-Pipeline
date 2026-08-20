---
title: "So... Vercel doesn't have built-in email?"
slug: "so-vercel-doesnt-have-built-in-email"
author: "PabloDevRel"
source: "devto_webdev"
published: "Thu, 20 Aug 2026 12:51:32 +0000"
description: "Vercel is great for deploying web apps. But there's one thing it doesn't do: email. If you have a side project on a custom domain and want a professional add..."
keywords: "amelu, dns, you, vercel, your, email, domain, app"
generated: "2026-08-20T12:58:10.477093"
---

# So... Vercel doesn't have built-in email?

## Overview

Vercel is great for deploying web apps. But there's one thing it doesn't do: email. If you have a side project on a custom domain and want a professional address like hello@yourdomain.com , you need an external mail provider. I went through the options. Cloudflare only forwards (no sending), Zoho locks you into their web client, and Migadu killed their free tier. Then I found Amelu . Free tier, 3 mailboxes, full IMAP/SMTP support, hosted in Europe. Here's how I set it up for moviekombat.app . The DNS problem Right now, DNS routes all moviekombat.app traffic to Vercel. That's fine for the website, but I need email to go somewhere else. The goal: tell DNS that any mail sent to @moviekombat.app should be handled by Amelu, not Vercel. Step 1. Create an Amelu account Go to app.amelu.org Click "Login with Ordnary account" Log in with your email. A first-time login automatically creates your account and organization. You land on the Email Domains page, empty and ready Step 2. Add your domain Click Email Domains → New domain Fill in: Domain name: your domain (just yourdomain.com , no www ) DNS Nameservers: "Use external nameservers" (this doesn't change anything, you keep your existing DNS provider) Default Email Addresses: leave checked. This creates admin , postmaster , and abuse (required by email standards) Click "Add Email Domain" Amelu creates the domain and three default mailboxes. Copy the passwords, they're shown only once. Step 3. Download and fix the DNS Zone file Open DNS Configuration > DNS Config in Amelu. Those are the records you need to add to your domain's DNS provider. In our case, Vercel. We could add each record one by one in Vercel's DNS Records form. Tedious for 19 records. So let's use the zone file import feature instead: Download the zone file from Amelu (BIND format .zone file) If you upload the zone file as-is in Vercel, you'll get an error. [!CAUTION] Error: No fully qualified domain name found in $ORIGIN directive or SOA record. To fix that, open the zone file with a text editor and add this line at the top (after the comment header) $ORIGIN moviekombat.app . This is how my zone file looks: ; Amelu DNS zone file for moviekombat.app ; Generated 2026-08-15T12:02:27Z ; Import this into your DNS provider (e.g. Cloudflare > DNS > Import and Export). $ORIGIN moviekombat.app. @ IN SOA marduk.mx.amelu.org. postmaster.moviekombat.app. ( ... Step 4. Import the zone file into Vercel In Vercel, go to Domains → select moviekombat.app → DNS Records Click the Upload Zone File button and upload the zone file Done! All records appear in your DNS table. Step 5. Verify DNS in Amelu Go back to Amelu DNS Configuration → DNS Config and click Recheck DNS . Most records come back Matched immediately. A few things to know: SRV records show "Not verified" : that's normal. Amelu only live-checks MX, TXT, and CNAME. SRV/CAA are unchecked by design and don't block activation. RSA DKIM might show mismatch : if Vercel's importer mangled the multi-line TXT record (split it with a literal " " in the middle), delete that record in Vercel and re-add it as a single concatenated string. Once all required records match, the domain goes active . Step 6. Configure your mail client This is where Amelu's admin panel stops and your mail client starts. Amelu isn't a mail client, it manages domains and mailboxes. To read and send mail, you need IMAP/SMTP settings. Find them in Amelu: Mailboxes → Usage Instructions : IMAP: marduk.mx.amelu.org , port 993 , SSL/TLS SMTP: marduk.mx.amelu.org , port 465 , SSL/TLS Username: full email address ( admin@yourdomain.com ) Password: the mailbox password What else is out there? Before landing on Amelu, I looked at the usual suspects: Cloudflare Email Routing : free, but it only forwards. You can receive mail, but you can't send from your domain. No IMAP/SMTP, no inbox. It looks easy until you realize it's a one-way street. Zoho Mail : has a free tier, but blocks IMAP on the free plan. You're stuck using their web client or mobile app. If you want to use Outlook or Thunderbird, you're paying. Migadu : closest competitor. Full IMAP/SMTP, unlimited mailboxes, flat pricing. But they killed their free tier in 2020, and the cheapest plan is $19/year. Amelu isn't perfect. There's no web client, so you read and send mail through Outlook, Thunderbird, or your phone's mail app. Auto-configuration doesn't work yet, so you'll set up the client manually the first time. But the free tier is real, the protocols are open, and the setup takes about 5 minutes. For a Vercel side project where you just need hello@yourdomain.com to work, it gets the job done.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/pablodevrel/so-vercel-doesnt-have-built-in-email-2dpd

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
