---
title: "Build a Marketing Campaign Tracker App with JavaScript"
slug: "build-a-marketing-campaign-tracker-app-with-javascript"
author: "Arhan Khan"
source: "devto_webdev"
published: "Tue, 17 Nov 2026 15:44:19 +0000"
description: "If you run a small business, an Instagram page, or a YouTube channel, you probably run small marketing campaigns — a discount week, a launch, a festival offe..."
keywords: "campaign, spend, campaigns, revenue, you, document, add, name"
generated: "2026-11-17T15:45:53.611799"
---

# Build a Marketing Campaign Tracker App with JavaScript

## Overview

If you run a small business, an Instagram page, or a YouTube channel, you probably run small marketing campaigns — a discount week, a launch, a festival offer. The problem is remembering what you tried and whether it worked. In this tutorial, we will build a Campaign Tracker: add a campaign, record what you spent and what you earned, and see the return on each one at a glance. Before you build the tracker, it helps to understand what good marketing actually is — the thinking behind it, not just the ads. This best marketing books for beginners guide covers seven books that teach you the fundamentals, from finding your smallest audience to writing a message people remember. Let us start with the HTML — a form to add a campaign and a table to show them: <form id = "campaignForm" > <input id = "name" placeholder = "Campaign name" required > <input id = "spend" type = "number" placeholder = "Spend (₹)" min = "0" required > <input id = "revenue" type = "number" placeholder = "Revenue (₹)" min = "0" required > <button> Add Campaign </button> </form> <table> <thead> <tr><th> Campaign </th><th> Spend </th><th> Revenue </th><th> ROI </th><th></th></tr> </thead> <tbody id = "campaignList" ></tbody> </table> <p id = "totals" ></p> Now the JavaScript. We store campaigns in an array, save them to localStorage , and compute the ROI (return on investment) for each one: let campaigns = JSON . parse ( localStorage . getItem ( 'campaigns' ) ) || [ { name : 'Diwali Offer' , spend : 5000 , revenue : 12000 } , { name : 'Instagram Reel Boost' , spend : 2000 , revenue : 3500 } ] ; function roi ( campaign ) { if ( campaign . spend === 0 ) return '—' ; const value = ( ( campaign . revenue - campaign . spend ) / campaign . spend ) * 100 ; return value . toFixed ( 0 ) + '%' ; } function render ( ) { const list = document . getElementById ( 'campaignList' ) ; list . innerHTML = '' ; let totalSpend = 0 ; let totalRevenue = 0 ; campaigns . forEach ( ( c , index ) => { totalSpend += c . spend ; totalRevenue += c . revenue ; const row = document . createElement ( 'tr' ) ; row . innerHTML = ` <td>${c.name}</td> <td>₹${c.spend}</td> <td>₹${c.revenue}</td> <td>${roi(c)}</td> <td><button data-index="${index}">Delete</button></td> ` ; list . appendChild ( row ) ; } ) ; document . getElementById ( 'totals' ) . textContent = `Total spend: ₹${totalSpend} | Total revenue: ₹${totalRevenue} | Overall ROI: ${totalSpend ? (((totalRevenue - totalSpend) / totalSpend) * 100).toFixed(0) + '%' : '—'}` ; } document . getElementById ( 'campaignList' ) . addEventListener ( 'click' , ( e ) => { if ( e . target . tagName === 'BUTTON' ) { campaigns . splice ( Number ( e . target . dataset . index ) , 1 ) ; localStorage . setItem ( 'campaigns' , JSON . stringify ( campaigns ) ) ; render ( ) ; } } ) ; document . getElementById ( 'campaignForm' ) . addEventListener ( 'submit' , ( e ) => { e . preventDefault ( ) ; campaigns . push ( { name : document . getElementById ( 'name' ) . value . trim ( ) , spend : Number ( document . getElementById ( 'spend' ) . value ) , revenue : Number ( document . getElementById ( 'revenue' ) . value ) } ) ; localStorage . setItem ( 'campaigns' , JSON . stringify ( campaigns ) ) ; e . target . reset ( ) ; render ( ) ; } ) ; render ( ) ; How it works: render() rebuilds the table from the campaigns array every time something changes — add or delete, then re-render. The ROI formula is (revenue - spend) / spend × 100 , so a campaign that spent ₹5,000 and earned ₹12,000 shows 140%. The totals row does the same calculation across all campaigns, so you can see at a glance whether your marketing as a whole is paying for itself. A few ideas to extend it: add a channel field (Instagram, WhatsApp, Google Ads) and filter by it, add a date so you can compare months, draw a simple bar chart of revenue per campaign, or add a "best campaign" highlight that picks the highest ROI automatically. Each of those is a small feature — and each one makes the tool genuinely useful for a real small business.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/arhan_khan/build-a-marketing-campaign-tracker-app-with-javascript-436m

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
