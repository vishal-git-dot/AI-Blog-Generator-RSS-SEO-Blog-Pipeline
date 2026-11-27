---
title: "Introducing Bord: a Rails engine for your dashboard"
slug: "introducing-bord-a-rails-engine-for-your-dashboard"
author: "Rails Designer"
source: "devto_webdev"
published: "Fri, 27 Nov 2026 07:30:00 +0000"
description: "Time for something new again! It is called Bord (Dutch for—you guessed it right—board, though it also could mean “plate”). It is in short a Rails engine for ..."
keywords: "bord, action, value, you, can, config, widget, actions"
generated: "2026-11-27T07:44:07.270087"
---

# Introducing Bord: a Rails engine for your dashboard

## Overview

Time for something new again! It is called Bord (Dutch for—you guessed it right—board, though it also could mean “plate”). It is in short a Rails engine for a dashboard with metrics, lists, categories and pages . Every widget runs your own code: ActiveRecord queries, Stripe calls, Good Job stats, Action Mailbox records. This gem’s code has lived (in a less configurable) setup in my apps for some time and is the screen I check for new signups and run quick actions (log in as user, re-run webhook using Fuik ). What it can do A metric shows one value, such as MRR, signups today, failed jobs or the Stripe balance. Add href and the value becomes a link. A list shows recent records, such as new users, recent charges or failed jobs. Each item can link to a record and have its own actions. A category groups widgets and sets their order on the page. A page lists records and can show one record in detail. I use one for customers and one for charges. An action calls a method on a record: refund a charge, retry a job, log in as a user. You add it to a widget or to an item in a list, and Bord renders a button. I use Bord to see the most important stats for my app. How to configure bundle add bord bin/rails generate bord:install The installer creates config/bord/dashboard.rb and mounts the engine at /bord . Bord loads every file under config/bord/**/*.rb , so you can split widgets across files. # config/bord/dashboard.rb Bord . draw do title "Spinal Labs" category :financials , label : "Financials" , position : 1 do metric :mrr , label : "MRR" , value : -> { Current . account . mrr . format } list :recent_users , label : "Recent users" , items : -> { User . order ( created_at : :desc ) . limit ( 5 ) } end end Add categories, metrics and lists to that file. Pages use Bord.page . Set the parent controller in an initializer: # config/initializers/bord.rb Bord . configure do | config | config . parent_controller = "Admin::BaseController" config . brand_hue = 250 end In production, /bord returns 404 until parent_controller is set. That controller is the only authorization gate. Anyone with access to it can use the dashboard. Development and test work without configuration. bin/rails generate bord:presets lists presets for Solid Queue, Good Job, Sidekiq, Stripe, Active Storage, Action Mailbox and plain users. Pick the ones you want, and the generator appends their code to config/bord/presets.rb . A preset is a JSON file, so other gems can ship one. How it works [AD] Spinal CMS: Git-based CMS for static site generators Bord is a small engine. Most of it is just Ruby objects and ERB templates. value and items are lambdas. Bord runs them per request with instance_exec in the controller’s view context, so Current , route helpers and bord.page_path work inside. If you want a number, you write a query. The page loads empty. Each widget renders its label and an empty value or list. On mount, Attractive.js requests /bord/data . The server responds with a list of actions: { action : "replace" , target : "widget-mrr-value" , template : "bord-value" , data : { value : "$28,400" } } The Attract addon renders a cached <template> for each action and applies it. A widget can replace a value, append an entry or set a link. . An action names a record by GlobalID and a method: { label : "Refund" , confirm : "Refund this charge?" , variant : :danger , action : { record : charge . to_gid . to_s , method : :refund , customer_id : charge . id } } On submit, Bord finds the record, calls the method with the other parameters, and refreshes the widget. Bord checks the submitted action against the actions you declared. Lists accept model instances. If a model defines to_bord , Bord uses it for the title, description and link. Future ideas Things I think of adding are: an API layer (widgets are queries and actions are records plus methods, so exposing them as JSON is simple). Actions could need more input. Today an action is a method plus flat parameters. I want forms: add a note to a refund, pick a reason, enter an amount. Then a refund action can take a note and a reason as well as the charge id. I also want charts next to metrics and authorization per action instead of one controller gate. This is, as I often do, a pre-v1/initial release to see what you think of this idea. Have a play with it and see if the DSL/API for adding widgets makes sense. I just released 0.5.0 of Bord. Give it a try and then a star . ✨😊

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/railsdesigner/introducing-bord-a-rails-engine-for-your-dashboard-jmp

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
