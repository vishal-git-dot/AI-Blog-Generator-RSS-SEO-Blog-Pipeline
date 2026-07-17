---
title: "How to Accept Payments in a Telegram Bot Using Python"
slug: "how-to-accept-payments-in-a-telegram-bot-using-python"
author: "guardlabs_team"
source: "devto_python"
published: "Fri, 17 Jul 2026 08:00:10 +0000"
description: "How to Accept Payments in a Telegram Bot Using Python Telegram allows bots to accept payments for goods and services directly within the chat interface. This..."
keywords: "telegram, update, bot, payment, your, payments, message, payload"
generated: "2026-07-17T08:19:05.879703"
---

# How to Accept Payments in a Telegram Bot Using Python

## Overview

How to Accept Payments in a Telegram Bot Using Python Telegram allows bots to accept payments for goods and services directly within the chat interface. This guide demonstrates how to implement Telegram Payments using Python and the python-telegram-bot library (v20+). 1. Obtain Your API Tokens To process payments, you need two tokens from Telegram's @botfather : - **Bot Token:** The standard token used to control your bot. - **Payment Provider Token:** Obtained by linking a payment provider (like Stripe, Paycom, or Tranzzo) to your bot. For development, use the "Test" version of any provider to get a test token. 2. Install Dependencies Install the required asynchronous Telegram library via pip: pip install python-telegram-bot 3. Python Implementation This script sets up a command to send an invoice, handles the mandatory pre-checkout verification step, and confirms successful payments. import logging from telegram import LabeledPrice , Update from telegram.ext import ( Application , CommandHandler , ContextTypes , PreCheckoutQueryHandler , MessageHandler , filters , ) # Enable logging logging . basicConfig ( level = logging . INFO ) BOT_TOKEN = " YOUR_BOT_TOKEN " PAYMENT_TOKEN = " YOUR_PAYMENT_PROVIDER_TOKEN " # e.g., "284543444:TEST:ey..." async def start ( update : Update , context : ContextTypes . DEFAULT_TYPE ): await update . message . reply_text ( " Use /buy to purchase a test item. " ) async def send_invoice ( update : Update , context : ContextTypes . DEFAULT_TYPE ): chat_id = update . message . chat_id title = " Premium Subscription " description = " Unlock premium features for 1 month " payload = " internal-subscription-payload " currency = " USD " # Prices are defined in the smallest currency unit (e.g., cents for USD) # 1000 cents = $10.00 prices = [ LabeledPrice ( " Monthly Sub " , 1000 )] await context . bot . send_invoice ( chat_id = chat_id , title = title , description = description , payload = payload , provider_token = PAYMENT_TOKEN , currency = currency , prices = prices , start_parameter = " premium-signup " ) async def precheckout_callback ( update : Update , context : ContextTypes . DEFAULT_TYPE ): """ Telegram sends this query right before processing the payment. You must answer within 10 seconds to approve or reject the charge. """ query = update . pre_checkout_query # Verify the payload matches your database/records if query . invoice_payload != " internal-subscription-payload " : await query . answer ( ok = False , error_message = " Something went wrong. Please try again. " ) else : await query . answer ( ok = True ) async def successful_payment_callback ( update : Update , context : ContextTypes . DEFAULT_TYPE ): """ Handles the final confirmation message after successful payment. """ payment_info = update . message . successful_payment await update . message . reply_text ( f " Thank you! Payment of { payment_info . total_amount / 100 } { payment_info . currency } received. " ) def main (): app = Application . builder (). token ( BOT_TOKEN ). build () # Handlers app . add_handler ( CommandHandler ( " start " , start )) app . add_handler ( CommandHandler ( " buy " , send_invoice )) app . add_handler ( PreCheckoutQueryHandler ( precheckout_callback )) app . add_handler ( MessageHandler ( filters . SUCCESSFUL_PAYMENT , successful_payment_callback )) # Start the bot app . run_polling () if __name__ == " __main__ " : main () 4. Key Components Explained - send_invoice: Constructs and sends the payment UI. The payload parameter is a unique internal identifier you define to track the transaction. It is not shown to the user. PreCheckoutQueryHandler: This is a critical security step. When a user clicks "Pay", Telegram sends a PreCheckoutQuery . Your bot must validate the order (e.g., check inventory or user status) and call query.answer(ok=True) within 10 seconds, or the payment fails. filters.SUCCESSFUL_PAYMENT: A message filter that catches the receipt message automatically sent to the chat after successful processing. Use this to provision the digital goods or update your database. Testing Your Integration When using a TEST payment token, Telegram will not charge real money. During checkout, use the dummy card details provided by your payment provider (for example, Stripe's standard test card numbers) to complete the transaction flow. Need this done fast? order a Telegram bot on Kwork ( https://kwork.com/chatbots/52990068/telegram-bot-done-for-you-requests-payments-auto-replies ).

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/guardlabs_team/how-to-accept-payments-in-a-telegram-bot-using-python-2bp2

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
