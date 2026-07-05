---
title: "How to Generate Dummy Data for Excel Spreadsheets Using FakerForge (Free CSV Export)"
slug: "how-to-generate-dummy-data-for-excel-spreadsheets-using-fakerforge-free-csv-export"
author: "Kwasi Baidoo"
source: "devto_ai"
published: "Sun, 05 Jul 2026 19:16:00 +0000"
description: "You've built a spreadsheet template. Maybe it's an inventory tracker, a customer list, or a sales report mockup. Now you need it to look real — filled with r..."
keywords: "you, column, your, fakerforge, rows, product, step, data"
generated: "2026-07-05T19:25:51.386902"
---

# How to Generate Dummy Data for Excel Spreadsheets Using FakerForge (Free CSV Export)

## Overview

You've built a spreadsheet template. Maybe it's an inventory tracker, a customer list, or a sales report mockup. Now you need it to look real — filled with realistic names, dates, prices, and IDs — so you can test formulas, build a demo, or show a client what the finished product will look like. The usual options aren't great: Typing fake rows by hand (slow, repetitive, and always ends up looking like "John Doe" fifty times) Copying real customer data into a spreadsheet (a compliance headache, and overkill for a mockup) Using a generic "lorem ipsum" data generator that has no idea what an "order date" or "SKU" column is supposed to contain FakerForge solves this by letting you describe your columns in plain terms, generating realistic rows that actually match each column's purpose, and exporting the result as a CSV file you can open directly in Excel (or Google Sheets, Numbers, LibreOffice Calc — any tool that reads CSV). Example Scenario: A Sample Product Inventory Sheet Let's say you're building an inventory tracking spreadsheet and you want it pre-filled with realistic sample data to test your formulas and pivot tables. Your sheet needs these columns: Column Description product_id Unique identifier for each product product_name Name of the product category Product category (e.g., Electronics, Apparel, Home Goods) unit_price Price per unit in USD quantity_in_stock Number of units currently in stock supplier_email Contact email for the supplier date_added Date the product was added to inventory Instead of typing 100 fake rows by hand, here's how to get this filled in with FakerForge in a few minutes. Step-by-Step: From Column List to a Filled Excel Sheet Step 1: Describe your columns as a schema Go to fakerforge.com/generate and paste your column list in as a simple schema — you don't need real SQL syntax, a plain table definition works fine. For the inventory example, you could paste something like: Table: products - product_id (unique identifier) - product_name (text) - category (text) - unit_price (decimal, USD) - quantity_in_stock (integer) - supplier_email (email) - date_added (date) FakerForge parses this into a table with recognized fields, ready for the next step. Step 2: Let FakerForge detect and map each column Once your schema is parsed, FakerForge assigns a faker mapping to each column based on its name and type — an email -style column gets realistic email formats, a date column gets valid dates, and so on. You can review and adjust these mappings before generating anything, so a column like category can be constrained to a specific set of values (Electronics, Apparel, Home Goods) instead of random text. Step 3: Set your row count Decide how many sample rows you want — 20 rows to sanity-check your formulas, or a few hundred to properly stress-test a pivot table. On the free plan you can generate up to 100 rows per table, which is plenty for most spreadsheet mockups and demos. Step 4: Generate Run the generation step. FakerForge streams the rows in and shows you a live preview, so you can catch anything that looks off before exporting. Step 5: Export as CSV and open in Excel Once you're happy with the preview, export your table as CSV. Open the downloaded file directly in Excel — File → Open, or just double-click it — and you'll have a fully populated sheet with realistic product IDs, names, categories, prices, stock counts, supplier emails, and dates, all ready for your formulas, charts, and pivot tables. Why This Beats Manually Typing Sample Data It's actually realistic. A supplier_email column gets real-looking email addresses, not " test1@test.com " repeated 100 times. A unit_price column gets sensible decimal values instead of round numbers that don't stress-test your rounding formulas. It respects your column names. FakerForge reads what each column is called and generates data that fits — dates in date columns, numbers in numeric columns, categories that make sense for a category field. It scales instantly. Need 20 rows for a quick check and then 500 rows for a bigger demo? Just change the row count and regenerate — no retyping. No real data involved. Every value is synthetic, so there's no risk of accidentally putting a real customer's name, email, or price data into a spreadsheet you're going to share around the office or with a client. Beyond a Single Sheet If your spreadsheet needs multiple related tabs — say, a products sheet and an orders sheet where each order references a real product ID — FakerForge's relationship-aware generation handles that too. Parent tables (like products ) generate first, and child tables (like orders ) reference valid parent rows, so you don't end up with an order pointing to a product that doesn't exist. Getting Started You can try this entire workflow on FakerForge's free tier: 100 rows per table 10 tables per database CSV, JSON, or SQL export That's enough to fill out a realistic sample spreadsheet in a few minutes. Generate your first dummy dataset for Excel →

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/kwasii/how-to-generate-dummy-data-for-excel-spreadsheets-using-fakerforge-free-csv-export-a1j

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
