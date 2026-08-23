---
title: "When Python is Too Slow"
slug: "when-python-is-too-slow"
author: "Aidas Bendoraitis"
source: "devto_python"
published: "Sun, 23 Aug 2026 12:17:08 +0000"
description: "Python is a perfect language for Agile development, where requirements might change on the go. Especially if you are in a startup business, you will need to ..."
keywords: "python, rust, you, can, code, library, package, when"
generated: "2026-08-23T12:50:17.232283"
---

# When Python is Too Slow

## Overview

Python is a perfect language for Agile development, where requirements might change on the go. Especially if you are in a startup business, you will need to experiment and change things fast. However, Python is an interpreted language, and in certain situations you might need faster performance than what an interpreted language can provide. A common practice in these cases is using python-to-binary bindings, where the binary code is built with Rust, C++, or Go. In this article, I will explore bindings to Rust-based code. How do the bindings work The idea behind bindings is that you create a module with functions of a specific domain in a language that compiles to binary, and build it as a C-compatible dynamic library ( .so on Linux, .dylib on macOS, .dll on Windows). Then a Python wrapper is built as a Python package and installed together with the dynamic library, allowing you to import and use functions that pass control to the corresponding functions in the dynamic library. On some occasions, classes can be used instead of functions. If any parameters are complex, they must be serialized in the wrapper and passed to the dynamic library as a JSON string or as a set of individual primitive parameters. An experiment with benchmarks To try this Python-Rust communication, I vibe coded an experiment that reads a large CSV file and builds a new one with duplicates stripped out based on specified column indexes. In my test case, it was a 3 MB CSV file with data about European NGOs for the donation platform I am building, where I wanted to remove the NGOs that don't have website URLs listed. As benchmarked, the file was processed 4.3x faster with the Rust binding than directly with Python. Here is the repo to get a first glimpse into the code and structure. What is there to know about Rust A few things about Rust: Rust packages are built with Cargo, which is the equivalent of pip, virtualenv, and setuptools combined. A single package is called a crate, and it can be published to crates.io, the equivalent of PyPI. To create a Python-to-Rust binding, the standard approach is to use Rust's PyO3 library together with maturin , a build tool installable as a PyPI package. Rust syntax is not the most developer-friendly compared to Python or Go, but with today's AI agents, most Python-native code can be ported to it fairly easily. The good thing about Rust and Go compared to C++ is that you don't have to manage memory at a low level or work with pointers directly. The package structure The common file structure can be: thepackage_rs/ # the package — self-contained and installable ├── Cargo.toml # crate manifest (pyo3, etc.) ├── pyproject.toml # maturin build backend config ├── src/lib.rs # Rust implementation └── python/ └── thepackage_rs/ └── __init__.py # Python wrapper Once the code is ready, you build it with: ( .venv ) maturin develop --release This builds the Python package and installs it into the current virtual environment. You can also get the wheel at thepackage_rs/target/*.whl , built for your specific operating system. Rust in Django When developing Django websites, the biggest bottlenecks are usually not in the language itself, but in the connections to databases, file systems or object storage, and APIs. Still, in cases where you need to process large amounts of data or do heavier calculations, using a binary instead of Python makes sense. The orjson library, and DRF renderers built on top of it such as django-orjson or drf-orjson-renderer , are good examples of this — Rust boosts the speed of building or parsing JSON 2-10x compared to a Python-native implementation. The best places to use Rust replacements are background tasks, management commands, template parsing (see the experimental django-rusty-templates ), and occasionally views or middleware. Final words So Python itself is good enough, especially when it comes to code readability and speed of development. However, when needed, certain parts can be boosted 2 to 10x just by rewriting them as Python-Rust bindings. Just keep in mind that when it comes to views with data from the database or Elasticsearch, post-processing — such as reordering in Python or Rust — is an antipattern; do that directly in the queries instead. Finally, keep in mind, that building with Rust will need extra dependencies and maintenance in your workflows. Cover photo by Alex Tepetidis

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/djangotricks/when-python-is-too-slow-228n

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
