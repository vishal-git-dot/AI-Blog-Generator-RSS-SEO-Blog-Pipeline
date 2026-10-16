---
title: "Firefox DevTools for Rust Developers: Wasm Debugging, wasm-pack, and API Testing"
slug: "firefox-devtools-for-rust-developers-wasm-debugging-wasm-pack-and-api-testing"
author: "Weather Clock Dash"
source: "devto_webdev"
published: "Fri, 16 Oct 2026 10:52:13 +0000"
description: "Rust developers building web applications or working with WebAssembly benefit from Firefox DevTools in specific ways. Here's the developer guide. Firefox for..."
keywords: "wasm, firefox, rust, devtools, web, source, console, debugging"
generated: "2026-10-16T11:05:26.347795"
---

# Firefox DevTools for Rust Developers: Wasm Debugging, wasm-pack, and API Testing

## Overview

Rust developers building web applications or working with WebAssembly benefit from Firefox DevTools in specific ways. Here's the developer guide. Firefox for Rust Web Development Axum / Actix-Web API Debugging The Network panel in Firefox DevTools is the primary tool for debugging Rust web framework endpoints. Axum example : use axum ::{ routing :: get , Router , Json }; #[derive(serde::Serialize)] struct User { id : u32 , name : String } async fn get_user () -> Json < User > { Json ( User { id : 1 , name : "Alice" .to_string () }) } let app = Router :: new () .route ( "/user" , get ( get_user )); In Firefox DevTools → Network → click the /user request → Response tab shows the JSON with automatic formatting and collapsible tree. Headers tab shows Content-Type, which should be application/json . CORS for Rust APIs When your Axum or Actix-web server serves a separate frontend: Axum CORS setup: use tower_http :: cors ::{ CorsLayer , Any }; use http :: Method ; let cors = CorsLayer :: new () .allow_origin ( "http://localhost:3000" .parse :: < HeaderValue > () .unwrap ()) .allow_methods ([ Method :: GET , Method :: POST , Method :: PUT ]) .allow_headers ([ header :: CONTENT_TYPE , header :: AUTHORIZATION ]); let app = Router :: new () .route ( "/api/data" , get ( handler )) .layer ( cors ); Firefox's CORS errors are specific: "CORS header 'Access-Control-Allow-Origin' missing" means the header wasn't set at all. "Does not match" means the origin is wrong. This helps diagnose which part of the config is wrong. Rust + WebAssembly in Firefox Firefox is the best browser for Wasm development due to: Mature Wasm debugging in DevTools Leading Wasm proposals support (GC, Exception Handling, Relaxed SIMD) SpiderMonkey's two-tier JIT for Wasm wasm-pack Projects The typical Rust → Wasm pipeline uses wasm-pack: wasm-pack build --target web This produces .wasm + JavaScript glue code. Testing in Firefox : Serve the package locally with a simple HTTP server Open in Firefox DevTools → Debugger → look for your .wasm source Set breakpoints in the WAT disassembly (if no source maps) For better debugging : Add source maps via wasm-pack's debug profile: wasm-pack build --dev --target web The debug build includes DWARF debug info embedded in the Wasm module. Firefox's debugger reads this and shows Rust source files. Viewing Wasm in Firefox DevTools Open DevTools → Debugger In the Sources panel, look for files with .wasm extension Click to open — Firefox shows either the WAT disassembly or Rust source (with debug info) Set breakpoints, step through code, inspect Wasm local variables Wasm locals show as typed values (i32, f64, etc.) in the Scopes panel. Memory Inspection For Rust Wasm, linear memory often contains your application data. In Firefox DevTools: Memory tab → take snapshot Look for "WebAssembly.Memory" in the snapshot Can inspect raw bytes For structured memory inspection, add #[wasm_bindgen] functions that return debug-formatted strings: #[wasm_bindgen] pub fn debug_state () -> String { format! ( "{:?}" , STATE .lock () .unwrap ()) } Call from browser console: debug_state() prints your app state. Rust wasm-bindgen Console Logging From Rust to browser console: use web_sys :: console ; console :: log_1 ( & "Hello from Rust!" .into ()); console :: log_2 ( & "Value:" .into (), & JsValue :: from ( 42 )); These appear in Firefox's Console tab just like JavaScript console.log calls, with Rust source attribution if debug info is present. WASI in Firefox (Current State) WASI (WebAssembly System Interface) for the browser is in early stages. Rust code targeting wasm32-wasi doesn't run directly in Firefox — it needs a WASI runtime. The ecosystem is evolving: @bytecodealliance/jco can compile WASI components for browser execution, but this is cutting-edge. For standard Rust → browser Wasm: target wasm32-unknown-unknown (the standard web target) via wasm-pack. Firefox Profiler for Wasm The Firefox Profiler (profiler.firefox.com) can profile Wasm code: Open Firefox Profiler Capture a profile while running your Wasm Flame chart shows Wasm functions (with Rust names if debug info present) Identify hot functions in your Rust code Upload profile to profiler.firefox.com for a shareable profile link — useful when collaborating on Wasm performance issues. Tab Management for Rust Projects Multiple Rust web service windows open at once is common: Localhost frontend API documentation (doc.rs or local cargo doc ) Error monitoring Wasm playground or test page Tab Manager & Session Saver (Firefox) saves these as a named "project-rust-web" session. Restore the complete development context across restarts. Firefox's Advantage for Rust/Wasm Firefox's SpiderMonkey has had strong Wasm support since the early days — the Wasm spec was co-developed by Mozilla researchers. Combined with mature DevTools debugging of Wasm, Firefox is the natural choice for Rust/Wasm development. The debugging story (source maps from DWARF, Wasm source view, memory inspector) is also more mature in Firefox's debugger than Chrome's for Wasm-specific features.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/weatherclockdash/firefox-devtools-for-rust-developers-wasm-debugging-wasm-pack-and-api-testing-ppc

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
