---
title: "Adding a Python extension to a photogrammetry application: the documented workflow"
slug: "adding-a-python-extension-to-a-photogrammetry-application-the-documented-workflow"
author: "enzo cocca"
source: "devto_python"
published: "Fri, 30 Oct 2026 12:13:51 +0000"
description: "This walkthrough describes the plugin interface in my PyArchInit Photogrammetry project. It follows the existing plugin documentation: generating a package, ..."
keywords: "plugin, application, chunk, command, project, context, python, interface"
generated: "2026-10-30T12:30:58.220293"
---

# Adding a Python extension to a photogrammetry application: the documented workflow

## Overview

This walkthrough describes the plugin interface in my PyArchInit Photogrammetry project. It follows the existing plugin documentation: generating a package, registering it through a Python entry point, developing it locally, and distributing a wheel. The core repository contains the photogrammetry application and API. The plugin repository contains the plugin index, a template and specialist extensions. Keeping these separate lets a plugin have its own repository and releases. 1. Start with a generated package In an environment with a compatible installation of the application, the documented generator command is: ppg plugins new chunk-summary --dir . --parts command The generator supports several starting components: action , background , command and exporter . It creates a package, tests, documentation and a release workflow. Pick the components the extension needs rather than adding a user interface to a command-only task. For a minimal manually created package, discovery is configured in pyproject.toml : [ project . entry-points . "pyarchinit_photogrammetry.plugins" ] chunk-summary = "ppg_chunk_summary:SummaryPlugin" The entry-point group is the application's discovery mechanism. The value points to the plugin class in the Python package; it does not require adding an import to the application's core. 2. Register a command when the plugin activates The documented base class receives a context in activate . This small example adapts the summary example in the plugin guide: from pyarchinit_photogrammetry.plugins import Plugin class SummaryPlugin ( Plugin ): title = " Chunk summary " description = " Counts the photos and markers in a project chunk " def activate ( self , context ): context . add_command ( " summary " , self . command , help = " Summarize a project chunk " ) def command ( self , project ): import pyarchinit_photogrammetry as ppg chunk = ppg . Document . open ( project ). chunk print ( f " Photos: { len ( chunk . cameras ) } " ) print ( f " Aligned photos: { len ( chunk . aligned_cameras ) } " ) print ( f " Markers: { len ( chunk . markers ) } " ) return 0 context.add_command makes the callback available through the application's plugin command group. Its positional arguments arrive as strings, and an integer return value becomes the exit code. An action uses context.add_action , and an export format uses context.add_exporter . These are separate registrations, so an extension can expose one or several ways to use the same underlying operation. 3. Develop in the application's Python environment From the plugin project directory, the guide's local development steps are: pip install -e . pytest -q tests ppg plugin The editable installation must use the Python environment running the application. ppg plugin lists the registered plugin commands. After installing a desktop extension, restart the application so it can discover the package. These are documented instructions and an illustrative code adaptation, rather than a report of a fresh execution or benchmark for this article. 4. Keep background work separate from widgets For longer tasks, the context provides run(title, function, done=None) . The work function receives a progress callback; the completion callback runs in the interface thread. The plugin guide specifically keeps widget access in interface callbacks rather than the worker function. A useful consequence is that numerical processing can remain separate from interface updates. The same extension can provide a CLI command while adding a progress-reporting action to the desktop application. 5. Distribute with explicit compatibility metadata For installation through the application's plugin manager, build a pure-Python wheel: python -m build --wheel The index entry records the plugin's entry-point name, version, API version, minimum application version, dependencies, download URL and SHA-256. The application checks the wheel against the index hash. Plugins execute with the application's permissions; a matching hash verifies the downloaded artifact, not whether its code is safe. A plugin using a newer context method must declare a minimum application version that provides it. The guide annotates those methods with their introduction versions. For the full interface and distribution procedure, see the plugin guide . The plugin repository provides the template and examples of terrain, geophysics, geoarchaeology and GIS archive extensions. Disclosure: this article was generated by an AI agent using the author's existing project documentation. The code is adapted from the documented example.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/enzo_cocca_d5689569fc7186/adding-a-python-extension-to-a-photogrammetry-application-the-documented-workflow-3nim

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
