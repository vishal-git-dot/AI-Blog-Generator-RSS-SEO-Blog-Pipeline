---
title: "WooCommerce Variations Not Showing? A 10-Step Debugging Checklist"
slug: "woocommerce-variations-not-showing-a-10-step-debugging-checklist"
author: "Amanur Rahman"
source: "devto_webdev"
published: "Mon, 12 Oct 2026 14:50:48 +0000"
description: "You add sizes or colors to a WooCommerce product, save it, and open the page. No dropdowns. Or the dropdowns show but a choice is greyed out. Or you get "Sor..."
keywords: "product, woocommerce, you, variation, variations, page, can, step"
generated: "2026-10-12T14:59:14.188188"
---

# WooCommerce Variations Not Showing? A 10-Step Debugging Checklist

## Overview

You add sizes or colors to a WooCommerce product, save it, and open the page. No dropdowns. Or the dropdowns show but a choice is greyed out. Or you get "Sorry, no products matched your selection." After fixing this on many stores, I run the same checks in the same order. Start with settings, then templates and conflicts, then JavaScript and code. Jumping straight to deactivating plugins wastes time. Back up your database and files first, and test on staging if you can. Quick diagnosis What you see Likely cause No dropdowns, only a normal add to cart Product is not set to Variable product Dropdown missing for one attribute Attribute not marked "Used for variations" An option has no price or cannot be selected Variation has no price, is disabled or out of stock "No products matched your selection" Missing combination or variation limit Layout broken after an update Outdated theme template Works logged in, fails for visitors Caching or minification Steps 1 to 4: configuration 1. Product type. In Product data, the dropdown must say Variable product, and the product must be published and visible in the catalog. 2. Attributes. On the Attributes tab, tick "Used for variations" for every attribute you want as a dropdown, then click Save attributes. For global attributes, make sure the terms you need are attached to this product. 3. Each variation. Open the Variations tab and check that every variation is enabled, has a regular price, and has a valid stock status. WooCommerce treats a variation without a price as not purchasable, so it disappears. If you renamed attribute terms after creating variations, delete and regenerate them. 4. Stock settings. Under WooCommerce > Settings > Products > Inventory, check the option that hides out-of-stock items. If every variation is out of stock, the whole product can vanish from the shop. Step 5: "No products matched your selection" Two common causes. First, a missing combination: the customer picked Large and Blue but you only created Large and Red. Second, the variation limit. By default WooCommerce loads variation data in the page for products with up to 30 variations and switches to AJAX above that, which some themes and caching setups handle badly. You can raise the threshold: add_filter ( 'woocommerce_ajax_variation_threshold' , function ( $qty , $product ) { return 100 ; }, 10 , 2 ); Raise it only as far as you need. Very high values make the product page heavier. Steps 6 and 7: templates and conflicts 6. Template overrides. Go to WooCommerce > Status and check the Templates section for outdated overrides. Test with a default theme such as Storefront on staging. If variations appear there, the fix is in your theme or child theme templates. 7. Plugin and builder conflicts. Common culprits are swatch plugins, product table plugins, caching plugins and anything that changes the add-to-cart area. If you built a custom single-product template in a page builder, it must include the Add to Cart element, because that element prints the dropdowns. Deactivate everything except WooCommerce, test, then reactivate one by one. Step 8: JavaScript, caching and minification The dropdowns depend on JavaScript. Open the browser console and reload the page. Red errors mentioning jQuery point to a broken or blocked script. Then purge every cache layer (plugin, host, CDN), pause minify, combine and defer options, and test in a private window. If that fixes it, re-enable optimization with exclusions for jQuery and WooCommerce scripts instead of switching it off everywhere. Step 9: transients and lookup tables Under WooCommerce > Status > Tools, run the tool that clears WooCommerce transients, then run the tools that regenerate the product lookup tables. This fixes wrong price ranges and products missing from filters. On large catalogs, run them at a quiet time. Step 10: read the logs Add these to wp-config.php : define ( 'WP_DEBUG' , true ); define ( 'WP_DEBUG_LOG' , true ); define ( 'WP_DEBUG_DISPLAY' , false ); Reload the product page and check wp-content/debug.log for fatal errors or warnings that name WooCommerce, your theme or a plugin. Turn debugging off afterwards. Prevention Test one variable product on the live site after every update Make changes on staging first Use a child theme instead of editing the parent Retest product pages as a logged-out visitor after changing cache settings FAQ Why does a variation without a price disappear? WooCommerce treats it as not purchasable and hides it or shows an unavailable message. Add a regular price. How many variations can a product have? There is no hard cap, but the default in-page handling stops at 30 and then uses AJAX. Very large numbers can slow the page. Can caching break variation dropdowns? Yes. Combined, minified or delayed JavaScript can stop the script from running, and cached pages can serve stale data. When should I get a developer involved? When you have worked through every step, when the problem started with a theme update, when you need complex options like bundles or conditional fields, or when each day of delay costs sales. I wrote the longer version, with a decision table for DIY versus hiring and more detail on each step, on my site: When WooCommerce Variations Won't Show Up .

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/amanhstu/woocommerce-variations-not-showing-a-10-step-debugging-checklist-26il

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
