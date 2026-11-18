---
title: "Django: Block GET Requests from Deleting Data with @require_POST in 5 Minutes"
slug: "django-block-get-requests-from-deleting-data-with-requirepost-in-5-minutes"
author: "Linh Fish Dev"
source: "devto_python"
published: "Wed, 18 Nov 2026 15:14:49 +0000"
description: "A view that deletes data and accepts GET is a silent security bug: any link, crawler, or image tag can trigger a delete without anyone clicking a button. The..."
keywords: "post, get, delete, django, view, views, request, method"
generated: "2026-11-18T15:25:47.037527"
---

# Django: Block GET Requests from Deleting Data with @require_POST in 5 Minutes

## Overview

A view that deletes data and accepts GET is a silent security bug: any link, crawler, or image tag can trigger a delete without anyone clicking a button. The neatest fix is to put the @require_POST decorator from django.views.decorators.http on the view — every non-POST request gets a 405 Method Not Allowed. This rule applies to every view that changes data: deleting a post, approving a comment, changing an order status, or activating an account. The Problem Suppose you have a view that deletes a post like this: # views.py — DANGEROUS: deleting a post with a GET link from django . shortcuts import get_object_or_404 , redirect def delete_post ( request , post_id ) : post = get_object_or_404 ( Post , id = post_id ) post . delete ( ) return redirect ( "post_list" ) # urls.py from django . urls import path from . import views urlpatterns = [ path ( "posts/<int:post_id>/delete/" , views . delete_post , name = "delete_post" ) , ] The delete URL is now just an ordinary GET link. Crawlers, link preview tools, or a malicious img tag pointing at this URL all send GET requests — and the post disappears without anyone noticing. The browser doesn’t ask first either: the CSRF token only protects “unsafe” requests like POST, not GET. The Solution Adding two decorators makes the delete view safe: # views.py — only POST may delete from django . contrib . auth . decorators import login_required from django . shortcuts import get_object_or_404 , redirect from django . views . decorators . http import require_POST @login_required @require_POST def delete_post ( request , post_id ) : post = get_object_or_404 ( Post , id = post_id , author = request . user ) post . delete ( ) return redirect ( "post_list" ) <!-- template : the delete button must be a POST form , not a link --> < form method = "post" action = "{% url 'delete_post' post.id %}" > { % csrf_token % } < button type = "submit" > Delete post </ button > </ form > Now a GET request gets 405 Method Not Allowed with an Allow: POST header, while a valid POST still works normally. Two details worth remembering: put @login_required above @require_POST so an unauthenticated request is redirected to the login page first instead of getting a 405; and @require_POST doesn’t replace the CSRF token — the POST form still needs {% csrf_token %} to block forged requests from other sites. It also doesn’t replace the ownership check: filter author=request.user so a user can only delete their own posts. Three sibling decorators in the same module cover the remaining cases: @require_http_methods(["GET", "POST"]) for a view that both shows a form and handles its submit; @require_safe for read-only views, accepting both GET and HEAD; class-based views use method_decorator(require_POST, name="dispatch") . Apply It to Your Project Open your project and list every view that changes data: delete, change status, send email, activate an account. Put @require_POST on each one, turn the links that call them into POST forms with {% csrf_token %} , then test with curl -X GET — the server must return 405 instead of performing the action. One afternoon of review, and a whole class of “delete by link” holes is gone. Related Posts Django: Fetch Objects Safely with get_object_or_404 — Skip try/except DoesNotExist in 5 Minutes Django: Protect Views for Logged-in Users Only with @login_required and LoginRequiredMixin in 5 Minutes Django: Test Views with TestCase and Client — Catch Bugs Before Deploy in 5 Minutes FAQ Does @require_POST replace the CSRF token? No. @require_POST only blocks the wrong method; a forged POST from another site still needs the CSRF token to be blocked. The two layers complement each other; neither replaces the other. What does the server return for a wrong-method request? A 405 Method Not Allowed error, with an Allow header listing the permitted methods — for example Allow: POST . The client immediately understands this is a wrong-method error, not a server error. How do I use it with a class-based view? Use method_decorator(require_POST, name="dispatch") on the class to apply it to the whole view. Putting @require_POST directly on the post() method works too, but dispatch covers the other methods as well. What about a view that both shows a form and handles its submit? Use @require_http_methods(["GET", "POST"]) . GET shows the form, POST processes the data, and PUT or DELETE both get a 405. How do @require_GET and @require_safe differ? @require_GET only allows GET, while @require_safe allows both GET and HEAD. Use @require_safe for read-only views, because many link-checking tools send HEAD requests to probe. 💬 Have you tried this in your own project? If you hit an error or have a shorter way, leave a comment below — I read them all and will fold the good ideas into the post. References Django documentation — View decorators Django documentation — Cross Site Request Forgery protection

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/linhfishdev/django-block-get-requests-from-deleting-data-with-requirepost-in-5-minutes-2hed

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
