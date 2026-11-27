---
title: "Add a Product to the Shopify Cart from a Chatbot (With Variant Checks and Error Handling)"
slug: "add-a-product-to-the-shopify-cart-from-a-chatbot-with-variant-checks-and-error-handling"
author: "Aylelite"
source: "devto_webdev"
published: "Fri, 27 Nov 2026 07:35:30 +0000"
description: "Add a Product to the Shopify Cart from a Chatbot (With Variant Checks and Error Handling) The risky part of "add to cart" in a chatbot is adding the wrong va..."
keywords: "product, variant, cart, add, const, return, res, wanted"
generated: "2026-11-27T07:44:07.269560"
---

# Add a Product to the Shopify Cart from a Chatbot (With Variant Checks and Error Handling)

## Overview

Add a Product to the Shopify Cart from a Chatbot (With Variant Checks and Error Handling) The risky part of "add to cart" in a chatbot is adding the wrong variant, or failing silently when an item is sold out. Here's a small, safe version using Shopify's Ajax Cart API. Load the product and its variants Every product page has a JSON endpoint at /products/.js. javascript async function getProduct(handle) { const res = await fetch( /products/${handle}.js ); if (!res.ok) throw new Error('Product not found'); return res.json(); } Find the variant the shopper chose Match on the options, not on a guess. javascript function findVariant(product, wanted) { // wanted example: { Size: 'M', Color: 'Green' } const names = product.options.map(o => (typeof o === 'string' ? o : o.name)); return product.variants.find(v => names.every((name, i) => !wanted[name] || v[ option${i + 1} ] === wanted[name]) ); } If no variant matches, ask the shopper again instead of adding anything. Add to cart and handle errors javascript async function addToCart(variantId, quantity = 1) { const res = await fetch('/cart/add.js', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ items: [{ id: variantId, quantity }] }), }); if (res.ok) return { ok: true }; const err = await res.json().catch(() => ({})); return { ok: false, message: err.description || err.message || 'Could not add this item.' }; } Shopify returns an error with a readable message when an item is sold out or the quantity isn't available, so show it to the shopper. Put it together javascript async function handleAdd(handle, wanted, qty) { const product = await getProduct(handle); const variant = findVariant(product, wanted); if (!variant) return 'Which size and color would you like?'; if (!variant.available) return 'Sorry, that option is sold out. Want to see similar items?'; const result = await addToCart(variant.id, qty); return result.ok ? Added ${product.title} (${variant.title}). View cart or keep browsing? : result.message; } Tips Confirm size and color in chat before calling the API. Always show "View cart" and "Keep browsing" afterwards. Test quantity above one, sold-out variants, and a phone browser. If your theme uses a cart drawer, refresh it after adding. Wrap-up Add to cart in a chatbot is just three checks: the right product, the right variant, and a clear message when something fails. Get those right and the rest is design.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/aylelite_fdb8fce6a0f4ce96/add-a-product-to-the-shopify-cart-from-a-chatbot-with-variant-checks-and-error-handling-6fa

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
