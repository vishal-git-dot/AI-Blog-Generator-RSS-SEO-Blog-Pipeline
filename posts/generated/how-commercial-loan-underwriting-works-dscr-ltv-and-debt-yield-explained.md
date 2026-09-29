---
title: "How Commercial Loan Underwriting Works: DSCR, LTV and Debt Yield Explained"
slug: "how-commercial-loan-underwriting-works-dscr-ltv-and-debt-yield-explained"
author: "Commercial Lending Guides"
source: "devto_python"
published: "Tue, 29 Sep 2026 21:31:31 +0000"
description: "Disclosure: I work with a commercial loan brokerage, so I see these numbers regularly; this article is general education, not financial advice. If you have e..."
keywords: "loan, dscr, noi, debt, ltv, property, income, value"
generated: "2026-09-29T22:04:59.849613"
---

# How Commercial Loan Underwriting Works: DSCR, LTV and Debt Yield Explained

## Overview

Disclosure: I work with a commercial loan brokerage, so I see these numbers regularly; this article is general education, not financial advice. If you have ever built a loan calculator, you know the math is simple. What is less obvious is which numbers a commercial lender actually cares about. Unlike most home mortgages, commercial loans are typically underwritten against the property's income, not just the borrower's paycheck. Three ratios do much of the work: DSCR, LTV, and debt yield. The Input Everything Depends On: NOI Net operating income (NOI) is a property's annual income minus its operating expenses. Expenses typically include property taxes, insurance, maintenance, utilities, and management. NOI generally excludes loan payments, depreciation, and income taxes. NOI = effective gross income - operating expenses Lenders often adjust the figures a borrower submits, for example by applying a vacancy allowance or normalizing expenses, so their NOI may differ from yours. The Three Formulas Debt service coverage ratio (DSCR) asks whether income can cover the loan payments. For a general definition, see Investopedia's DSCR explainer . DSCR = NOI / annual debt service Annual debt service is the total of principal and interest payments over a year. A value of 1.00 means income just covers payments. Lenders typically want a cushion above that, often somewhere around 1.20 to 1.35, though this varies widely. Loan-to-value (LTV) measures how much of the property's value is financed. LTV = loan amount / appraised value (or purchase price, depending on the lender) Commercial LTV limits commonly fall in the 60% to 80% range, depending on property type and loan program. Debt yield measures the loan against income, without involving interest rates or amortization. Debt yield = NOI / loan amount Because it ignores rate and term, it is a blunt check that some lenders use alongside DSCR. Thresholds vary; figures near 8% to 10% or higher are sometimes cited. A Worked Example Say a small apartment building has these characteristics: Appraised value: $2,000,000 Requested loan: $1,300,000 NOI: $150,000 Assumed rate: 7.0% with a 25-year amortization (illustrative only) The monthly payment comes out to about $9,188, or roughly $110,258 per year. That gives: DSCR = 150,000 / 110,258 = about 1.36 LTV = 1,300,000 / 2,000,000 = 65% Debt yield = 150,000 / 1,300,000 = about 11.5% On paper, that profile looks reasonably comfortable against the ranges above, but a real lender would also review the borrower, the property condition, the market, and the loan program's own rules. A Small Python Snippet def monthly_payment ( principal , annual_rate , years ): r = annual_rate / 12 n = years * 12 return principal * r / ( 1 - ( 1 + r ) ** - n ) def underwrite ( noi , value , loan , rate , years ): debt_service = monthly_payment ( loan , rate , years ) * 12 return { " dscr " : noi / debt_service , " ltv " : loan / value , " debt_yield " : noi / loan , } print ( underwrite ( 150_000 , 2_000_000 , 1_300_000 , 0.07 , 25 )) # {'dscr': 1.36, 'ltv': 0.65, 'debt_yield': 0.115} (approximately) Why the Ratios Pull in Different Directions Each metric catches something the others can miss. DSCR is rate-sensitive. If rates rise, debt service rises and DSCR falls, even though the property has not changed. LTV depends on valuation. Appraisals rest on assumptions such as cap rates, so value can shift with the market. Debt yield is stable. It depends only on NOI and loan size, which is why it is often used as a check when rates or valuations look generous. In practice, the tightest of the three tends to set the maximum loan amount. Try changing the rate in the snippet: you will typically see DSCR move while debt yield stays put. Practical Takeaways Clean, documented financials matter, because NOI is the base of two of the three ratios. Run the numbers at a few rate scenarios before you apply. Expect lender-specific requirements; property type, location, and borrower experience all typically influence the limits. If you want to see how different structures compare, you can review commercial loan options for investors . Nothing here is a rate quote or a promise of approval, since outcomes depend on the lender, the property, and current market conditions. Wrap-Up DSCR tests payment coverage, LTV tests leverage against value, and debt yield tests the loan against raw income. All three are a few lines of code, and understanding how they interact makes commercial loan terms much easier to reason about.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/commerciallendingguides/how-commercial-loan-underwriting-works-dscr-ltv-and-debt-yield-explained-43lc

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
