---
title: "Check product photos against Amazon, Etsy and 96 other marketplace image rules with a free API (no key)"
slug: "check-product-photos-against-amazon-etsy-and-96-other-marketplace-image-rules-with-a-free-api-no-key"
author: "Herofab"
source: "devto_webdev"
published: "Fri, 20 Nov 2026 00:22:36 +0000"
description: "Every marketplace has its own image rules, and they rarely match. Amazon wants the longest side between 500 and 10,000 pixels and enables zoom above 1,000 px..."
keywords: "app, image, rules, api, platform, amazon, check, json"
generated: "2026-11-20T00:28:34.170877"
---

# Check product photos against Amazon, Etsy and 96 other marketplace image rules with a free API (no key)

## Overview

Every marketplace has its own image rules, and they rarely match. Amazon wants the longest side between 500 and 10,000 pixels and enables zoom above 1,000 px per side. Etsy recommends 2,000 px and accepts a first photo from 635 px. Walmart enables zoom at 1,500 px. Some platforms want a pure white main image, others accept a light background. If a store uploads the same photo set to several channels, a size or background mistake shows up as a rejected listing or a blurry zoom. We needed these rules in code for our own product, so we read each platform's official help page and put the result behind a small read-only API. It is free and needs no key. This post shows how to use it. 1. List the platforms curl https://app.herofab.app/api/agent/rules The response lists 98 platforms with a key, a name and a kind ( marketplace for sales channels, specs for ad and content placements): { "platforms" : [ { "key" : "about-you" , "name" : "ABOUT YOU" , "kind" : "marketplace" } , { "key" : "amazon" , "name" : "Amazon" , "kind" : "marketplace" } , ... ] } 2. Get the rules of one platform curl "https://app.herofab.app/api/agent/rules?platform=amazon" { "platform" : "amazon" , "name" : "Amazon" , "summary" : "500 to 10,000 pixels on the longest side; more than 1,000 pixels per side enables zoom." , "limits" : { "min_long_side_px" : 500 , "max_side_px" : 10000 , "formats" : [ "jpeg" , "png" , "gif" , "tiff" ] , "zoom_min_side_px" : 1001 } , "main_image" : { "background" : "pure-white" , "fill_min" : 0.85 , "whole_product" : true , "source_url" : "https://sellercentral.amazon.com/help/hub/reference/external/G1881" } , "source_url" : "https://sell.amazon.com/blog/product-photos" , "checked" : "2026-10-10" } (Shortened: limits that the platform does not state come back as null .) Every response carries the official source and the day it was read, so you can show the source next to the rule or re-check it. 3. Check an image before upload Send the image's measurements, not the image itself. Nothing is stored. curl -X POST https://app.herofab.app/api/agent/check \ -H "content-type: application/json" \ -d '{"platform":"amazon","width":2000,"height":2000,"format":"png","background":"light","product_fill":0.7}' { "platform" : "amazon" , "pass" : false , "fails" : [ { "rule" : "bg-pure-white" , "message" : "Main image needs a pure white background (RGB 255, 255, 255); given: light" } , { "rule" : "fill-min" , "message" : "The product fills 70%; the main image needs at least 85% of the frame" } ] , "not_checked" : [ { "rule" : "whole" , "message" : "Whole product in frame, nothing cut off: measured from the photo itself" } ] } width , height and format are required. file_size_bytes , background ( pure-white , white , light , coloured , busy , transparent ) and product_fill (0 to 1) are optional; a rule whose input is missing is listed under not_checked instead of failing silently. 4. In the browser or Node async function checkImage ( file , platform ) { const bitmap = await createImageBitmap ( file ) ; const format = file . type . split ( "/" ) [ 1 ] ; // "jpeg", "png", "webp"... const res = await fetch ( "https://app.herofab.app/api/agent/check" , { method : "POST" , headers : { "content-type" : "application/json" } , body : JSON . stringify ( { platform , width : bitmap . width , height : bitmap . height , format , file_size_bytes : file . size , } ) , } ) ; return res . json ( ) ; // { pass, fails, notes, not_checked } } The API sends CORS headers, so this works from a web page as well. 5. Python, for a whole folder import json , pathlib , urllib . request from PIL import Image def check ( path , platform = "etsy" ) : img = Image . open ( path ) body = json . dumps ( { "platform" : platform , "width" : img . width , "height" : img . height , "format" : ( img . format or "jpeg" ) . lower ( ) , "file_size_bytes" : path . stat ( ) . st_size , } ) . encode ( ) req = urllib . request . Request ( "https://app.herofab.app/api/agent/check" , data = body , # urllib's default user agent is blocked; any descriptive name works headers = { "content-type" : "application/json" , "user-agent" : "image-rules-check/1.0" } , ) return json . load ( urllib . request . urlopen ( req ) ) for p in sorted ( pathlib . Path ( "photos" ) . glob ( "*.jpg" ) ) : r = check ( p ) print ( p . name , "OK" if r [ "pass" ] else [ f [ "message" ] for f in r [ "fails" ] ] ) Limits and good manners The endpoints are rate limited. Responses to /rules can be cached for an hour ( cache-control: public, max-age=3600 ); fetch the rules once and check locally if you process thousands of images. If you get a 429 , wait and retry. The rules were read between 24 September and 12 October 2026. Platforms change them; the source_url in each response is the place to confirm. Background and product fill are what you declare; the API does not look at the pixels. Full data set If you would rather work offline, the same 98 platforms are published as a CSV and JSON data set under CC BY 4.0: Kaggle . A browsable table is at herofab.app/guides/marketplace-image-rules , and the OpenAPI description is at https://app.herofab.app/api/agent/openapi.json . Disclosure: this API is maintained by the team behind Herofab , an AI product photography tool. The rules API and the data set are free to use. This post was drafted with AI assistance and reviewed by the team.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/herofab/check-product-photos-against-amazon-etsy-and-96-other-marketplace-image-rules-with-a-free-api-no-5982

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
