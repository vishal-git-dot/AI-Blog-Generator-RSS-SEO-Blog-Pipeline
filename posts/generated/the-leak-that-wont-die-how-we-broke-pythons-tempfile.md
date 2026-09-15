---
title: "The Leak That Won't Die: How We Broke Python's tempfile"
slug: "the-leak-that-wont-die-how-we-broke-pythons-tempfile"
author: "Flude team"
source: "devto_python"
published: "Tue, 15 Sep 2026 03:52:53 +0000"
description: "Production crashes always happen suddenly. This time, the alarm was raised by the core C++ SDK developers. Their scheduled nightly build failed on the CI run..."
keywords: "folder, our, engine, cleanup, garbage, but, its, deleted"
generated: "2026-09-15T04:21:15.142504"
---

# The Leak That Won't Die: How We Broke Python's tempfile

## Overview

Production crashes always happen suddenly. This time, the alarm was raised by the core C++ SDK developers. Their scheduled nightly build failed on the CI runner with a classic diagnosis: No space left on device . We ran out of disk space. A quick post-mortem revealed that the /tmp folder was bursting with thousands of temporary directories. Their names all started the same way: ude_xml_ . It was our code. The Architecture of the Crash As we've mentioned before, our engine handles Doxygen in a tricky way. We feed it source code, it spits out a massive XML dump, and we parse that dump. For every run, the engine created a temporary folder using tempfile.mkdtemp() . A dynamically generated Doxyfile was placed there, and Doxygen would dump hundreds of megabytes of XML into it. The plan was simple: at the very end of the pipeline, a cleanup() function would run, executing an honest shutil.rmtree() on that folder. But the plan had a flaw. If the parsing failed with an exception, the pipeline aborted, cleanup() was never called, and a folder filled with megabytes of garbage was left stranded in /tmp forever. Complaints started pouring in from teams building massive projects. The error was flaky. We tried wrapping the call in a try/finally block, but the engine's logic was smeared across dozens of classes. The leak persisted. A False Sense of Security: Trusting the GC How do you solve the problem of forgotten resource cleanup in Python? "Delegate the cleanup to the Garbage Collector (GC)!" we thought. Instead of mkdtemp , we rewrote the logic to use the tempfile.TemporaryDirectory object. Its main advantage is that when the object is deleted from memory, its finalizer ( __del__ ) automatically triggers the folder's deletion on disk. To ensure the folder lived exactly as long as the engine needed it, we saved a reference to the object in a global list inside the manager class: temp_dir_obj = tempfile . TemporaryDirectory ( prefix = " ude_xml_ " ) self . _active_temp_dirs . append ( temp_dir_obj ) It seemed like elegant, "pythonic" code. The object lives in the manager's memory and is automatically deleted when the script finishes. The Fatal Mistake We rolled out this "fix" to production. For a few days, the complaints stopped. We patted ourselves on the back and closed the issue. And then the CI runners started crashing again. We missed one "tiny" detail. Hoping that objects are always deleted, and that the Garbage Collector works immediately , is a ticking time bomb. In the case of giant C++ projects like Flude, the engine parsed dozens of modules sequentially. A new directory was created for each module. Because of a complex web of circular references in our parsers (e.g., an AST node referenced its parent class, and the class held a list of its children), the engine's objects weren't deleted immediately. They hung in memory, waiting for a full garbage collection cycle. And, of course, _active_temp_dirs stayed in memory too. TemporaryDirectory objects piled up in RAM by the hundreds. But the worst part was this: when the GC finally got to them and called cleanup() , it triggered a massive synchronous deletion of files from the disk , blocking the main execution thread for several minutes. Because of this, other services on the server began failing due to timeouts. The Real Fix The conclusion of our investigation was grim: using finalizers to free heavy system resources is an anti-pattern. We couldn't control when the GC would trigger, which meant we couldn't control the disk I/O load. we had to rewrite the pipeline's architecture so that the lifecycle of temporary folders was managed by strict with context managers, not the GC. We introduced a strict rule: creating the folder and calling cleanup() must happen in the same place. If any part of the engine needs these files, it accesses them inside a with block, guaranteeing that upon exiting the block (even via an exception), the folder is deleted immediately. To protect against regressions, we also added a "janitor"—a mechanism that forcibly checks /tmp before a build starts and cleans up any orphaned garbage. logger . warning ( f " Orphaned temporary directory found: { td . name } . " " Caller failed to invoke cleanup(). Force-cleaning now. " ) Conclusion We learned a harsh lesson. Shifting the responsibility for system resources to Python's garbage collector is a direct path to disaster. But our victory over the garbage was just the beginning. While we were wrestling with Python, the real enemy was lurking in the very heart of our infrastructure. We thought we had tamed Doxygen, but it soon took its revenge, forcing us to rewrite the entire parser from scratch. How a simple C++ construct drove the documentation generator insane—read about it in the next episode. Originally published on our blog: https://blog.flude.guide/blog/the-leak-that-wont-die Also read us: Telegram channel RSS feed

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/flude_team/the-leak-that-wont-die-how-we-broke-pythons-tempfile-95o

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
