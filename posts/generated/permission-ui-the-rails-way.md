---
title: "Permission UI the Rails way"
slug: "permission-ui-the-rails-way"
author: "Rails Designer"
source: "devto_webdev"
published: "Fri, 10 Jul 2026 14:30:00 +0000"
description: "I’ve built many a SaaS . And most have pricing tiers: the higher the plans the more widgets you can create or features are allowed. Typically there are two w..."
keywords: "render, end, allowed, you, html, helper, content, current"
generated: "2026-07-10T14:40:05.900077"
---

# Permission UI the Rails way

## Overview

I’ve built many a SaaS . And most have pricing tiers: the higher the plans the more widgets you can create or features are allowed. Typically there are two ways to approach this: hide the feature if the customer does not have access; show all features, to all customers, but guard them with some, optional, upsell. I have succesfully implementated the latter approach with a helper that quacks like Rails itself. The helper lets you wrap content and decide what happens when access is denied. Hide it, redirect to a link, render content or render a partial. It’s small but flexible. This is how it looks (added a toggle allowed/denied states): As always view on GitHub for a ready-to-copy code. The API is elegant. Let’s look at some examples: <%= allowed? Current . user . premium? do %> <%= link_to "Create project" , projects_path %> <% end %> When Current.user.premium? is true, the link renders. When false, nothing shows. That’s the default behavior. But you can do more. Redirect to a link instead: <%= allowed? Current . user . premium? , redirect_to: upgrade_path do %> <%= link_to "Advanced analytics" , analytics_path %> <% end %> The content becomes a clickable link pointing to your upgrade page. Show plain text as a fallback: <%= allowed? Current . user . premium? , render: { plain: "Upgrade to unlock this." } do %> <%= button_to "Delete project" , project_path , method: :delete %> <% end %> Or render HTML: <%= allowed? Current . user . premium? , render: { html: "Upgrade to the <strong>Pro plan</strong>." } do %> <%= button_to "Delete project" , project_path , method: :delete %> <% end %> And render a partial for complex fallbacks: <%= allowed? Current . user . premium? , render: "upsell" do %> <%= button_to "Advanced settings" , settings_path %> <% end %> The helper Here’s the full helper in app/helpers/allowed_helper.rb : module AllowedHelper def allowed? ( condition , options = {}) return yield if condition if options [ :redirect_to ] content = capture { yield } link_to strip_tags ( content ), options [ :redirect_to ] elsif options . key? ( :render ) render_options = options [ :render ] if render_options . is_a? ( Hash ) && render_options . key? ( :html ) render_options [ :html ]. html_safe elsif render_options . is_a? ( Hash ) && render_options . key? ( :plain ) render_options [ :plain ] else render ({ partial: render_options . to_s }) if render_options . is_a? ( String ) || render_options . is_a? ( Symbol ) end end end end The logic is straightforward. If the condition is true, render the block. If false, check your options and handle it accordingly. When you pass redirect_to , it captures the block content, strips HTML tags and wraps it in a link. When you pass render , it supports three formats: plain text, raw HTML or a partial name as a string or symbol. This helper did, ~10 years ago, not start like this. Over the years, after working on many dozens Rails-based SaaS apps, my aim became to make helpers “quack” more like Rails methods. You’re familiar with render plain: , render html: and partial rendering. This helper just extends that familiar syntax to conditional rendering. I like it. What do you think of this?

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/railsdesigner/permission-ui-the-rails-way-5fme

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
