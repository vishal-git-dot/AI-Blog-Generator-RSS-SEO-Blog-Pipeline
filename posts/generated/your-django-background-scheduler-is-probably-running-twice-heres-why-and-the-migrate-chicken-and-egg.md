---
title: "Your Django background scheduler is probably running twice. Here's why, and the migrate chicken-and-egg."
slug: "your-django-background-scheduler-is-probably-running-twice-heres-why-and-the-migrate-chicken-and-egg"
author: "ひとし 田畑"
source: "devto_python"
published: "Mon, 22 Jun 2026 11:40:12 +0000"
description: "I needed periodic background work in a Django app — scan AWS every N minutes, sync remote tfstate, refresh data daily. No Celery, no Redis, no extra moving p..."
keywords: "scheduler, migrate, ready, true, django, runs, apscheduler, job"
generated: "2026-06-22T12:15:23.443866"
---

# Your Django background scheduler is probably running twice. Here's why, and the migrate chicken-and-egg.

## Overview

I needed periodic background work in a Django app — scan AWS every N minutes, sync remote tfstate, refresh data daily. No Celery, no Redis, no extra moving parts for a one-person ops tool. django-apscheduler with a BackgroundScheduler started in AppConfig.ready() is perfect for that scale. And then it ran every job twice. Then it crashed on a fresh database. Both have boring, specific causes that every "apscheduler in Django" tutorial skips, so here they are. Gotcha #1: runserver starts your app twice AppConfig.ready() feels like "run once at startup." Under runserver it isn't — the autoreloader forks a parent watcher and a child that actually serves, and ready() runs in both . Start your scheduler there naively and you get two schedulers, every job fires twice. Django leaves you a tell: the child process has RUN_MAIN=true . So the scheduler only starts in the child: if ' runserver ' in sys . argv : return os . environ . get ( ' RUN_MAIN ' ) == ' true ' Gotcha #2: it also starts during migrate , test , and shell ready() runs for every management command. python manage.py migrate , collectstatic , shell , and your test run all import the app, all fire ready() , all happily spin up a background thread pool you never wanted. During tests it pollutes state and leaks threads; during migrate it's actively dangerous (more on that below). So the real entry point isn't "start the scheduler," it's "should I even be allowed to?" — a guard that inspects how the process was launched: _NO_SCHEDULER_COMMANDS = frozenset ({ ' migrate ' , ' makemigrations ' , ' collectstatic ' , ' shell ' , ' dbshell ' , ' check ' , ' createsuperuser ' , ' flush ' , ' loaddata ' , ' dumpdata ' , ... }) def should_start_scheduler () -> bool : if ' pytest ' in sys . modules or ' test ' in sys . argv : return False # never in tests if _NO_SCHEDULER_COMMANDS . intersection ( sys . argv ): return False # never during one-off mgmt commands if ' runserver ' in sys . argv : return os . environ . get ( ' RUN_MAIN ' ) == ' true ' # child only return True # gunicorn / prod ready() calls this before touching apscheduler. The principle: a process that exists to run a migration or a shell has no business launching a recurring job engine. Gotcha #3: the migrate chicken-and-egg django-apscheduler persists jobs in a database table ( DjangoJobStore ). But that table is created by a migration — and on a brand-new database, ready() runs before you've migrated. So the scheduler tries to register a job, queries a table that doesn't exist yet, and the whole app faceplants on first boot. The migrate guard above helps, but a fresh runserver before migrating still hits it. The fix is to look before you leap: from django.db import connection if ' django_apscheduler_djangojob ' not in connection . introspection . table_names (): logger . warning ( " Scheduler skipped: tables not found — run migrate first. " ) return If my own jobstore tables aren't there yet, don't start; log it and move on. The next boot after migrate starts cleanly. Don't let a slow tick stack up Even with a single scheduler, a job that runs every minute but occasionally takes longer than a minute will pile up overlapping runs. apscheduler has the knobs; the job just has to ask: scheduler . add_job ( _tick , IntervalTrigger ( minutes = 1 ), id = ' boto3_scan_tick ' , max_instances = 1 , # never two ticks at once coalesce = True , # missed runs collapse into one, not a backlog burst replace_existing = True , # re-registering replaces, doesn't duplicate ) max_instances=1 + coalesce=True means a scan that overruns just delays the next tick instead of running concurrently with itself — which matters a lot when the tick makes AWS API calls and writes rows. Takeaways AppConfig.ready() is not "once at startup." Under runserver it runs in both the reloader parent and child — gate the scheduler on RUN_MAIN == 'true' . ready() also runs for migrate / test / shell . Guard with a should_start_scheduler() that inspects sys.argv / sys.modules , so one-off commands don't spin up jobs. If your jobstore lives in the DB, check the table exists before registering jobs — otherwise a fresh, un-migrated database crashes on boot. Use max_instances=1 + coalesce=True so a slow tick delays the next run instead of stacking overlapping ones. This scheduler drives the periodic AWS drift scans in a self-hosted tool that reconciles tfstate against live AWS — no Celery, no broker, just apscheduler in the web process. Open source (MIT), one docker compose up : syncvey.com . What's your Django background-job setup — apscheduler, Celery beat, or an external cron hitting a management command?

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/hitoshi1964/your-django-background-scheduler-is-probably-running-twice-heres-why-and-the-migrate-453c

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
