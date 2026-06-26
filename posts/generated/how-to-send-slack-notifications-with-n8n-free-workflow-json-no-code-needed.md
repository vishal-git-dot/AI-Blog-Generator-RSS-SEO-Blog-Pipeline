---
title: "How to send Slack notifications with n8n (free workflow JSON, no code needed)"
slug: "how-to-send-slack-notifications-with-n8n-free-workflow-json-no-code-needed"
author: "Pirate Prentice"
source: "devto_webdev"
published: "Fri, 26 Jun 2026 19:30:06 +0000"
description: "If you're running n8n workflows, you probably want to know when something important happens — a new lead, a failed payment, a form submission, a cron job fin..."
keywords: "slack, webhook, json, trigger, name, type, text, workflow"
generated: "2026-06-26T19:58:27.780905"
---

# How to send Slack notifications with n8n (free workflow JSON, no code needed)

## Overview

If you're running n8n workflows, you probably want to know when something important happens — a new lead, a failed payment, a form submission, a cron job finishing. Slack notifications close that loop instantly. This is the exact setup I use. Free workflow JSON at the end. What you'll build Triggers on any event (webhook, schedule, form, API call) Sends a formatted Slack message to a channel or DM Includes dynamic data from the trigger (name, amount, email, etc.) Takes under 10 minutes to set up Step 1: Get a Slack incoming webhook URL Go to api.slack.com/apps and click "Create New App" Choose "From scratch" → name it (e.g. "n8n Notifier") → pick your workspace In the left sidebar, click Incoming Webhooks Toggle "Activate Incoming Webhooks" ON Click "Add New Webhook to Workspace" → pick a channel → Allow Copy the webhook URL (starts with https://hooks.slack.com/services/.. .) Step 2: Build the workflow in n8n Add a trigger node Pick whichever fits your use case: Webhook — for form submissions or external events Schedule Trigger — for daily/weekly reports Stripe Trigger — for payment events Add a Slack node Add a Slack node after your trigger Set Resource to Message, Operation to Send Under Authentication, choose Webhook and paste your Slack webhook URL In the Text field, use n8n expressions: New lead: {{ $json.name }} ({{ $json.email }}) Source: {{ $json.source }} Time: {{ $now.format('YYYY-MM-DD HH:mm') }} Test it Click Test Workflow in n8n, then send a POST to your webhook URL: { "name" : "Jane Smith" , "email" : "jane@example.com" , "source" : "landing page" } The Slack message should appear in seconds. Step 3: Better formatting with Block Kit Switch from plain text to JSON blocks for clean, scannable messages: { "blocks" : [ { "type" : "section" , "text" : { "type" : "mrkdwn" , "text" : "*New lead:* {{ $json.name }} \n *Email:* {{ $json.email }}" } }, { "type" : "context" , "elements" : [{ "type" : "plain_text" , "text" : "{{ $now.format('YYYY-MM-DD HH:mm') }}" }] } ] } Common patterns Payment received: 💰 Payment: ${{ $json.amount }} from {{ $json.customer_email }} Error alert: Error Trigger → Slack. Get pinged when any workflow fails. Daily digest: Schedule Trigger (9am) → HTTP Request (pull data) → Slack summary. Troubleshooting Message not sending? Test with curl: curl -X POST -H 'Content-type: application/json' --data '{"text":"test"}' YOUR_WEBHOOK_URL Expression showing undefined? Check field names in the Input panel — keys are case-sensitive. Rate limits? Slack allows ~1 msg/sec per webhook. Add a Wait node for high-volume workflows. Free workflow JSON Webhook trigger → Slack notification, ready to import: { "name" : "Webhook to Slack Notification" , "nodes" : [ { "parameters" : { "httpMethod" : "POST" , "path" : "slack-notify" , "responseMode" : "onReceived" , "options" : {} }, "name" : "Webhook" , "type" : "n8n-nodes-base.webhook" , "typeVersion" : 1 , "position" : [ 250 , 300 ] }, { "parameters" : { "authentication" : "webhook" , "webhookUrl" : "YOUR_SLACK_WEBHOOK_URL" , "resource" : "message" , "operation" : "post" , "text" : "=Event: {{JSON.stringify($json)}}" }, "name" : "Slack" , "type" : "n8n-nodes-base.slack" , "typeVersion" : 1 , "position" : [ 500 , 300 ] } ], "connections" : { "Webhook" : { "main" : [[{ "node" : "Slack" , "type" : "main" , "index" : 0 }]] } } } To import: Workflows → Import from clipboard in n8n. Replace YOUR_SLACK_WEBHOOK_URL with your own, then activate. I keep a pack of 10+ pre-built n8n workflows (Slack alerts, Stripe receipts, CRM lead capture, scheduled reports) at pirateprentice.gumroad.com/l/sxcoe — $29 one-time, import and go. What are you using n8n + Slack for? Drop it in the comments.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/pirateprentice/how-to-send-slack-notifications-with-n8n-free-workflow-json-no-code-needed-eoa

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
