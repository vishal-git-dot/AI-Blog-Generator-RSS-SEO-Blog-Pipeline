---
title: "Put a Dash app behind Google sign-in"
slug: "put-a-dash-app-behind-google-sign-in"
author: "nwon19"
source: "devto_python"
published: "Tue, 24 Nov 2026 08:58:39 +0000"
description: "Dash is Plotly's Python framework for interactive data dashboards, and AI coding tools write it well. This is how to make sure only people in your company ca..."
keywords: "app, google, dash, sign, your, auth, check, cloud"
generated: "2026-11-24T09:19:58.417443"
---

# Put a Dash app behind Google sign-in

## Overview

Dash is Plotly's Python framework for interactive data dashboards, and AI coding tools write it well. This is how to make sure only people in your company can open what they write. Where the app comes from The steps are the same whichever tool wrote the app. Tool Where the app is Before you start Claude on the web or desktop In the conversation Ask Claude for the full project as files, including requirements.txt . A Dash app needs a Python server, so it cannot run as an Artifact. Claude Code In a folder on your machine Ask it to add the sign-in below and to read secrets from environment variables, never from the code. Codex or Cursor In your repository or a cloud task The same. Their own app sharing signs visitors in with their own accounts, so this guide applies when viewers should use your Google sign-in. The rule that matters Signing someone in with Google proves they have a Google account. It does not prove they work for you. Every option below needs a second check that limits sign-in to your organization, and that check is where most mistakes happen. Google's OpenID Connect documentation is direct about two traps: The hd request parameter only shortcuts the sign-in screen for one domain. Google says not to rely on it to control access, "as client-side requests can be modified". The domain of the email claim does not identify members of a Google Workspace organization. Check the hd claim inside the ID token instead. Google says that claim "can be trusted", because it is part of a token Google signed. Option 1: sign-in inside the app, with dash-auth dash-auth is Plotly's authentication package for Dash. Version 2.3.0 (March 2024, per PyPI ) includes OIDCAuth , which works with any OpenID Connect provider, Google included. Plotly describes the package as feature-complete: it takes bug fixes but no new features. In Google Cloud In a Google Cloud project that belongs to your organization, set the app's audience to Internal . Google's audience page says this limits sign-in "to members of the organization". People outside it get an org_internal error. Create an OAuth client of type Web application. Add the redirect URI: your app's address followed by /oidc/callback (for local testing, http://localhost:8050/oidc/callback ). Google requires an exact match. Keep the client ID and secret out of the code. Put them in environment variables. Step 1 is the access rule, and it is the simplest one to get right. If the project cannot be Internal, the app has to check the hd claim of every ID token itself. dash-auth's README does not show how to read claims, so confirm how your version exposes them before you rely on that check. In the app pip install dash-auth import os from dash import Dash , html from dash_auth import OIDCAuth app = Dash ( __name__ ) app . layout = html . Div ( "Revenue by region" ) auth = OIDCAuth ( app , secret_key = os . environ [ "SESSION_SECRET" ] ) auth . register_provider ( "google" , token_endpoint_auth_method = "client_secret_post" , client_id = os . environ [ "GOOGLE_CLIENT_ID" ] , client_secret = os . environ [ "GOOGLE_CLIENT_SECRET" ] , server_metadata_url = "https://accounts.google.com/.well-known/openid-configuration" , ) if __name__ == "__main__" : app . run ( debug = False ) Anyone who opens the app is sent to Google first. SESSION_SECRET signs the session cookie: a long random string, the same on every server, kept out of the repository. Things to know Public pages are opt-in. dash-auth has public_routes and add_public_routes for pages anyone may see. Leave them out unless you mean it. Groups need your own wiring. dash-auth has group helpers ( check_groups , protected_callback ), but its README shows them only with fixed lists of users. Google's ID token claims list has no groups claim, so restricting to a Google group means calling Google's Admin SDK yourself. Each app is its own client. Ten apps means ten OAuth clients, ten secrets and ten redirect URIs to keep track of. Option 2: sign-in in front of the app, with oauth2-proxy oauth2-proxy runs beside the app, sends people to Google, and passes only signed-in requests through. The app has no login code. --email-domain limits sign-in to addresses on your domain. --google-group limits it to members of one or more Google groups. Per the Google provider page , this needs a service account with domain-wide delegation, the Admin SDK API turned on, and an admin account to impersonate. Membership is checked at sign-in and again each time the token refreshes, about once an hour. The group check is worth the setup. It means removing someone from the group closes the app to them within the hour, without anyone editing the app. Option 3: Identity-Aware Proxy, if the app runs on Google Cloud If the app runs on Cloud Run, App Engine or behind a Google Cloud load balancer, Identity-Aware Proxy can sit in front of it. Access is granted per person or group with the "IAP-secured Web App User" role. Google's own caveat: check that the app cannot also be reached directly, around the proxy. What none of the options solves Sign-in answers who can open the app. A security team will ask more: Where is the database password? Usually in an environment variable the builder set, and knows. Keeping database credentials out of apps covers the alternatives. Who owns this app, and what happens to it when they leave? What did it ship with? Nobody scanned the code for leaked keys or vulnerable packages. How many are there? Each app is set up by hand, and nothing lists them. First published on intrium.dev . intrium is governed hosting for the apps your team builds themselves. The steps above work with or without it.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/nwon19/put-a-dash-app-behind-google-sign-in-5bmh

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
