---
title: "URL Encoding (Percent-Encoding) Explained: encodeURIComponent, Spaces, and Double Encoding"
slug: "url-encoding-percent-encoding-explained-encodeuricomponent-spaces-and-double-encoding"
author: "pulkitgovrani"
source: "devto_webdev"
published: "Wed, 14 Oct 2026 16:30:00 +0000"
description: "URLs can only contain a limited set of characters. To include anything else, such as spaces, accented letters, or symbols with special meaning, they are conv..."
keywords: "encoding, url, characters, encodeuricomponent, percent, space, query, value"
generated: "2026-10-14T16:54:47.642684"
---

# URL Encoding (Percent-Encoding) Explained: encodeURIComponent, Spaces, and Double Encoding

## Overview

URLs can only contain a limited set of characters. To include anything else, such as spaces, accented letters, or symbols with special meaning, they are converted to percent-encoding: a percent sign followed by two hexadecimal digits representing the byte. How it works Text is first converted to bytes using UTF-8, and each byte that isn't allowed is written as %XX. A space is the byte 0x20, so it becomes %20. The letter e with an acute accent takes two bytes in UTF-8, so it becomes %C3%A9. hello world -> hello%20world a&b=c -> a%26b%3Dc café -> caf%C3%A9 Reserved characters Characters like : / ? # [ ] @ ! $ & ' ( ) * + , ; = have special roles in URLs. If you want one of them as data (for example, an ampersand inside a query value), it must be encoded so it isn't mistaken for structure. Unreserved characters (letters, digits, - . _ ~) never need encoding. encodeURI vs encodeURIComponent encodeURI() encodes a whole URL and leaves structural characters like : / ? & = # alone. encodeURIComponent() encodes a single value and does encode those characters, which is what you want for a query parameter or path segment. Use encodeURIComponent for values you insert into a URL; using encodeURI on a value would leave & and = unescaped and can corrupt the query string. const q = " cats & dogs " ; const url = " /search?q= " + encodeURIComponent ( q ); // /search?q=cats%20%26%20dogs %20 vs + In a query string produced by an HTML form (application/x-www-form-urlencoded), spaces are written as +. In other parts of a URL, and in most modern APIs, a space is %20. Decoders for form data treat + as a space, so a literal plus sign must be sent as %2B. Double encoding and other pitfalls Double encoding: encoding an already-encoded string turns %20 into %2520. Encode raw values exactly once. Decode once as well; decoding twice can change meaning and is a source of security bugs. Encode the value, not the whole URL with its structure. Let your HTTP client or URL builder handle it when possible instead of concatenating strings. Debugging If a link breaks, paste the URL into an encoder/decoder to see the raw text. Do it locally if the URL contains tokens or personal data. Frequently asked questions What is percent-encoding? A way to represent special or unsafe characters in URLs as a percent sign followed by two hex digits, such as %20 for a space. What is the difference between encodeURI and encodeURIComponent? encodeURI leaves URL structure characters intact, while encodeURIComponent encodes them, making it correct for individual parameter values. Is a space %20 or +? %20 works everywhere in URLs. The + form is used only in form-encoded query strings. What is double encoding? Encoding a value twice, turning %20 into %2520. It causes garbled data and should be avoided by encoding exactly once. Try it: Base64 & URL Encoder — free, runs in your browser, nothing is uploaded. Originally published at ilovekit.app .

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/pulkitgovrani/url-encoding-percent-encoding-explained-encodeuricomponent-spaces-and-double-encoding-22kl

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
