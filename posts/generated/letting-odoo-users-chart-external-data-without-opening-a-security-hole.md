---
title: "Letting Odoo users chart external data without opening a security hole"
slug: "letting-odoo-users-chart-external-data-without-opening-a-security-hole"
author: "Nadia Atiq"
source: "devto_python"
published: "Tue, 10 Nov 2026 14:25:12 +0000"
description: "Our Odoo dashboard module can now chart data that does not live in Odoo: a CSV someone exports every Monday, a JSON endpoint, a read-only view in another dat..."
keywords: "can, odoo, not, only, view, url, dashboard, module"
generated: "2026-11-10T14:38:48.359674"
---

# Letting Odoo users chart external data without opening a security hole

## Overview

Our Odoo dashboard module can now chart data that does not live in Odoo: a CSV someone exports every Monday, a JSON endpoint, a read-only view in another database. Building it took a day. Making it safe took three. Notes for anyone doing the same. 1. A URL field is an SSRF hole by default. If any user can type a URL and your server fetches it, they can point it at http://127.0.0.1:8069/web/database/manager or your cloud metadata IP. We resolve the hostname first and refuse private, loopback, link-local and reserved addresses: for info in socket . getaddrinfo ( host , None ) : ip = ipaddress . ip_address ( info [ 4 ] [ 0 ] ) if ip . is_private or ip . is_loopback or ip . is_link_local or ip . is_reserved : raise UserError ( 'Internal network addresses are not allowed.' ) Also allow_redirects=False , otherwise a public URL can just 302 you to an internal one. 2. Who may create the source matters more than who may view it. Regular dashboard managers can upload a file. Only Settings admins can create URL, database or Python sources. We check this in create and write , not only in the view, because the view is not a security layer. 3. Secrets get field-level groups. Headers (API tokens) and the DB password have groups='base.group_system' . Everyone else can use the source, nobody else can read the secret back. 4. External databases: read-only and a timeout. PostgreSQL connections get set_session(readonly=True) and statement_timeout=30000 . We still reject anything that is not a single SELECT, belt and braces. 5. Cap everything. 50,000 rows, 30 second HTTP timeout, errors stored on the record instead of crashing the cron. One bad source should never stop the hourly refresh of the others. 6. The Python transform runs in safe_eval. Users can add a column or filter rows, but they get rows and a few builtins, nothing else. None of this is exotic, but every item was missing in at least one module we reviewed for clients. If you build anything that fetches URLs from user input inside Odoo, start with point 1. The module is here if you want to see it in action: https://technoversesystems.com/odoo-dashboard-studio

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/nadia_atiq_4378032d154159/letting-odoo-users-chart-external-data-without-opening-a-security-hole-4o82

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
