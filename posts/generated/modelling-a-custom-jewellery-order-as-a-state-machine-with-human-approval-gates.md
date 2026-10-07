---
title: "Modelling a Custom Jewellery Order as a State Machine (with Human Approval Gates)"
slug: "modelling-a-custom-jewellery-order-as-a-state-machine-with-human-approval-gates"
author: "Ujjwal Dubey"
source: "devto_python"
published: "Wed, 07 Oct 2026 05:02:13 +0000"
description: "Custom jewellery orders are a nice, small example of why "add a chatbot" is the wrong first move for retail automation. The real problem is state: the custom..."
keywords: "order, state, approvals, approval, delayed, transitions, outbox, custom"
generated: "2026-10-07T05:20:33.232090"
---

# Modelling a Custom Jewellery Order as a State Machine (with Human Approval Gates)

## Overview

Custom jewellery orders are a nice, small example of why "add a chatbot" is the wrong first move for retail automation. The real problem is state: the customer wants to know where their order is, and the answer lives in someone's head or a paper order book. This post shows a tiny state machine for a custom order, with approval gates on the steps that touch money or promises. It is the pattern we use when we build AI automation for custom jewellery orders for Indian stores, stripped down to the standard library. The states ENQUIRY -> DESIGN_SHARED -> DESIGN_APPROVED -> ADVANCE_RECEIVED -> IN_MAKING -> READY_FOR_TRIAL -> ALTERATION (optional loop) -> READY_FOR_PICKUP -> DELIVERED Plus two side exits: DELAYED (needs a human message) and CANCELLED . The rules Every transition is made by a named staff member. Some transitions trigger a customer message automatically from an approved template. Some transitions only draft a message, which a person must approve: anything about price, balance due or delay. The code from dataclasses import dataclass , field from datetime import datetime TRANSITIONS = { " ENQUIRY " : { " DESIGN_SHARED " , " CANCELLED " }, " DESIGN_SHARED " : { " DESIGN_APPROVED " , " CANCELLED " }, " DESIGN_APPROVED " : { " ADVANCE_RECEIVED " , " CANCELLED " }, " ADVANCE_RECEIVED " : { " IN_MAKING " }, " IN_MAKING " : { " READY_FOR_TRIAL " , " DELAYED " }, " DELAYED " : { " IN_MAKING " , " READY_FOR_TRIAL " }, " READY_FOR_TRIAL " : { " ALTERATION " , " READY_FOR_PICKUP " }, " ALTERATION " : { " READY_FOR_TRIAL " }, " READY_FOR_PICKUP " : { " DELIVERED " }, } AUTO_SEND = { " DESIGN_APPROVED " , " IN_MAKING " , " READY_FOR_TRIAL " , " READY_FOR_PICKUP " } NEEDS_APPROVAL = { " ADVANCE_RECEIVED " , " DELAYED " , " DELIVERED " } # money, promises, final balance @dataclass class Order : order_id : str customer_phone : str language : str state : str = " ENQUIRY " history : list = field ( default_factory = list ) def move ( order , new_state , staff , outbox , approvals ): if new_state not in TRANSITIONS . get ( order . state , set ()): raise ValueError ( f " { order . state } -> { new_state } not allowed " ) order . history . append (( datetime . now (). isoformat (), order . state , new_state , staff )) order . state = new_state msg = { " to " : order . customer_phone , " template " : f " { new_state . lower () } _ { order . language } " , " ref " : f " { order . order_id } : { new_state } : { len ( order . history ) } " } if new_state in AUTO_SEND : outbox . append ( msg ) elif new_state in NEEDS_APPROVAL : approvals . append ({ ** msg , " requested_by " : staff }) outbox , approvals = [], [] o = Order ( " JO-0001 " , " +910000000000 " , " hi " ) for s , who in [( " DESIGN_SHARED " , " asha " ), ( " DESIGN_APPROVED " , " asha " ), ( " ADVANCE_RECEIVED " , " owner " ), ( " IN_MAKING " , " ravi " ), ( " DELAYED " , " ravi " )]: move ( o , s , who , outbox , approvals ) print ( " auto: " , [ m [ " template " ] for m in outbox ]) print ( " waiting for approval: " , [ m [ " template " ] for m in approvals ]) Output: auto: [ 'design_approved_hi' , 'in_making_hi' ] waiting for approval: [ 'advance_received_hi' , 'delayed_hi' ] Why the ref field matters WhatsApp providers and webhooks retry. The ref (order, state, step) lets your sender drop duplicates, so a retry never sends "your order is ready" twice. What I left out Persistence, the provider API call, language detection and the approval UI. In production the approvals list is a one-tap screen on the owner's phone. The interesting part is the design decision, not the code: which transitions may talk to a customer on their own, and which must wait for a person. If you are mapping a workflow like this for a client, the hard work is before the code. Here is the pre-build audit checklist we use; our own first audit takes 72 hours.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/ujjwal_dubey_9/modelling-a-custom-jewellery-order-as-a-state-machine-with-human-approval-gates-3a6c

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
