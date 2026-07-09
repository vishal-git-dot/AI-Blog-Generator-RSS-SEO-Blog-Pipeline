---
title: "Pytest Pt1 - Fundamentals for Data Engineers"
slug: "pytest-pt1-fundamentals-for-data-engineers"
author: "Felipe de Godoy"
source: "devto_python"
published: "Thu, 09 Jul 2026 03:18:17 +0000"
description: "Pytest Fundamentals for Data Engineers Data engineering code is still software, and software that doesn't have tests is a liability. If you've ever had a pro..."
keywords: "you, test, pytest, data, assert, your, code, bucket"
generated: "2026-07-09T03:49:54.083750"
---

# Pytest Pt1 - Fundamentals for Data Engineers

## Overview

Pytest Fundamentals for Data Engineers Data engineering code is still software, and software that doesn't have tests is a liability. If you've ever had a production pipeline silently produce wrong numbers because a downstream transformation made an assumption about a column that changed upstream, you know the pain. Testing isn't just about "does the pipeline run" — it's about verifying that every transformation, every branch of logic, and every edge case behaves exactly as you expect. This post lays the groundwork for testing data pipelines with pytest. I'll cover why testing matters, the fundamental pattern every test follows, how to write your first tests and assertions, how to verify that your code raises the right exceptions, and how to mock external dependencies so your tests stay fast and deterministic. By the end, you'll have a solid foundation for writing unit tests that catch regressions before they reach production. Testing 101 for Data Pipelines If you're new to testing or have only ever written a few scripts, the core idea is simple: a test is a small piece of code that exercises another piece of code and checks that the result is what you expected. In pytest, that looks like a function whose name starts with test_ and which contains an assert statement. The Fundamental Pattern: Arrange, Act, Assert Almost every test follows three steps: Arrange – set up the input data and any necessary context. Act – call the function or method you want to test. Assert – verify the output is correct. For a data pipeline transformation, that might be: def test_clean_amount (): # Arrange raw_data = " 1,200.50 " # what you might get from a CSV # Act result = clean_amount ( raw_data ) # Assert assert result == 1200.50 clean_amount is a pure function — no file I/O, no database calls. It just takes an input string and returns a number. That makes it straightforward to test. Assert Raises: Expecting Exceptions Data pipelines often deal with invalid data that should trigger an exception. pytest.raises verifies that your code raises the right exception and, optionally, that the error message contains a specific string: def test_validate_schema_raises_on_missing_column ( spark ): df = spark . createDataFrame ([( 1 ,)], [ " id " ]) with pytest . raises ( ValueError , match = " Missing required column: amount " ): validate_schema ( df , required_cols = [ " id " , " amount " ]) The match parameter is useful to ensure you're hitting the exact error you expect, not just any ValueError . Marking Expected Failures Sometimes you know a test currently fails — maybe there's a known bug you can't fix yet. @pytest.mark.xfail marks the test as expected to fail. If it fails, pytest reports it as xfailed (yellow X) instead of a red failure. If it unexpectedly passes, it's reported as a surprise: @pytest.mark.xfail ( reason = " Known issue with currency conversion rounding " , strict = True ) def test_currency_conversion_precision (): assert convert_currency ( " EUR " , " USD " , 100.0 ) == 118.31 # assumes exact rate strict=True tells pytest to treat an unexpected pass as a failure, which reminds you to remove the mark once the bug is fixed. Mocking: Replacing External Dependencies But what if your function reads from an S3 bucket or queries a database? In a unit test, you don't want to hit real infrastructure. That's where mocking comes in. Mocks are fake objects that pretend to be the real thing. They let you control exactly what your code "sees" when it calls an external system, so you can test your logic in isolation. The Python standard library provides unittest.mock . Here's a short example: suppose you have a function that reads a CSV from S3 and parses it: import boto3 def read_order_amounts ( bucket , key ): s3 = boto3 . client ( " s3 " ) obj = s3 . get_object ( Bucket = bucket , Key = key ) csv_data = obj [ " Body " ]. read (). decode () # … parse csv_data, return a list of amounts In a unit test, you don't want to talk to S3. You mock boto3.client so it returns a fake S3 client that gives back a canned response: from unittest.mock import patch @patch ( " my_pipeline.reader.boto3.client " ) def test_read_order_amounts ( mock_boto_client ): # Arrange fake_s3 = mock_boto_client . return_value fake_s3 . get_object . return_value = { " Body " : b " amount \n 100 \n 200 " } # Act amounts = read_order_amounts ( " my-bucket " , " orders.csv " ) # Assert assert amounts == [ 100.0 , 200.0 ] fake_s3 . get_object . assert_called_once_with ( Bucket = " my-bucket " , Key = " orders.csv " ) The @patch decorator replaces boto3.client inside the my_pipeline.reader module with a mock. mock_boto_client is the mock object, and you configure what its .return_value (the fake client) does. The decorator form is clean because the mocking setup sits at the top and the test body reads straight through. A common need in data engineering is mocking Spark reads — you can patch the DataFrameReader.load method to return a pre-built DataFrame, avoiding the need for actual data files. Conclusion You've now seen the core building blocks: Arrange‑Act‑Assert, assertions for expected results, pytest.raises for expected failures, and @patch for isolating your code from external dependencies. These fundamentals alone will let you test most of the transformation logic in your pipelines. But writing setup code inside every test function gets repetitive fast. In the next post, we'll look at pytest fixtures — a feature that lets you define reusable test data and shared resources once, then inject them into any test that needs them.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/felipe_de_godoy/pytest-fundamentals-for-data-engineers-43o9

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
