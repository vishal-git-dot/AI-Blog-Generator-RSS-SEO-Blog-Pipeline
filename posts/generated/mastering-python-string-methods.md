---
title: "Mastering Python String Methods"
slug: "mastering-python-string-methods"
author: "Alex Murithi"
source: "devto_python"
published: "Wed, 23 Sep 2026 10:45:21 +0000"
description: "Python String Methods: Indexing , Slicing , Case , Splitting , Joining , and More Strings are one of the most common data types in Python - and they come wit..."
keywords: "print, output, name, city, nairobi, age, data, split"
generated: "2026-09-23T11:11:45.084876"
---

# Mastering Python String Methods

## Overview

Python String Methods: Indexing , Slicing , Case , Splitting , Joining , and More Strings are one of the most common data types in Python - and they come with powerful built-in methods for manipulation, formatting, and validation. 1. Indexing and Slicing Strings are sequences, so you can access individual characters or slices using indexes. city = ' Nairobi ' print ( city [ 0 ]) # First character print ( city [ - 1 ]) # Last character Output N i Slicing city = ' Nairobi ' print ( city [ 0 : 3 ]) # Nai print ( city [ 3 :]) # robi print ( city [:: - 1 ]) # Reverse Output Nai robi iboriaN 2. Concatenation and Repetition You can combine strings with + and repeat them with *. first = ' Nai ' second = ' robi ' print ( first + second ) print ( " = " * 30 ) print ( " Ha " * 3 ) Output Nairobi ============================== HaHaHa 3. Strings Are Immutable You can’t change characters directly - you must create a new string. city = ' Nairobi ' # city[0] = 'K' # TypeError city = ' K ' + city [ 1 :] print ( city ) Output Kairobi 4. Changing Case String methods help standardize text before comparison. name = ' nancy wanjiku ' print ( name . upper ()) print ( name . lower ()) print ( name . capitalize ()) print ( name . title ()) Output NANCY WANJIKU nancy wanjiku Nancy wanjiku Nancy Wanjiku swapcase() greeting = ' Hello WORLD ' print ( greeting . swapcase ()) Output hELLO world 5. Removing Extra Spaces name = ' Faith ' print ( len ( name )) print ( f ' [ { name . strip () } ] ' ) print ( f ' [ { name . lstrip () } ] ' ) print ( f ' [ { name . rstrip () } ] ' ) Output 9 [Faith] [Faith ] [ Faith] Removing Specific Characters code = ' ###PROMO2025### ' print ( code . strip ( ' # ' )) Output PROMO2025 6. Splitting Text Break a string into a list using split(). sentence = " Python is greater for data " words = sentence . split () print ( f " Word count: { len ( words ) } " ) Output Word count: 5 Split by Separator csv_line = " Moses,23,Nairobi,Data Science " csv_split = csv_line . split ( ' , ' ) print ( csv_split ) Output ['Moses', '23', 'Nairobi', 'Data Science'] Split Lines notes = " Buy bread \n Go for walk \n Ride Bike " lines = notes . splitlines () print ( lines ) Output ['Buy bread', 'Go for walk', 'Ride Bike'] Practical Example route_info = ' Route46,Nairobi,50 ' r_info = route_info . split ( ' , ' ) print ( f " { r_info [ 0 ] } costs KES { r_info [ 2 ] } " ) Output Route46 costs KES 50 7. join() - The Opposite of split() items = [ ' Bread ' , ' Milk ' , ' Sugar ' ] shopping_text = ' , ' . join ( items ) print ( shopping_text ) Output Bread,Milk,Sugar Custom Separator parts = [ ' Nairobi ' , ' Mombasa ' , ' Kisumu ' ] result = " | " . join ( parts ) print ( result ) Output Nairobi | Mombasa | Kisumu Real Use Case - Cleaning Text dirty = " Moses, 23 , Nairobi , Data Science " dirty_list = dirty . split ( ' , ' ) clean_list = [ i . strip () for i in dirty_list ] clean = ' , ' . join ( clean_list ) print ( clean ) Output Moses,23,Nairobi,Data Science 8. find(), index(), count(), and replace() Checking Existence message = " Your M-pesa transaction of KES 500 was successful. " print ( ' M-pesa ' in message ) print ( ' failed ' in message ) Output True False Finding Position print ( message . find ( ' KES ' )) print ( message . find ( ' failed ' )) Output 26 -1 Counting and Replacing text = " banana " print ( text . count ( ' a ' )) new_message = message . replace ( ' successful ' , ' reversed ' ) print ( new_message ) Output 3 Your M-pesa transaction of KES 500 was reversed. 9. Validation Methods Check if a string contains digits, letters, or both. print ( " 12345 " . isdigit ()) print ( " Joan " . isalpha ()) print ( " Joan123 " . isalnum ()) print ( " Joan 123 " . isalnum ()) Output True True True False Input Validation Example age = input ( " Enter your age: " ) while not age . isdigit (): print ( " Enter a valid whole number " ) age = input ( " Enter your age: " ) age = int ( age ) print ( f " You are { age } years old " ) Sample Output Enter your age: abc Enter a valid whole number Enter your age: 25 You are 25 years old 10. Prefixes, Suffixes, and Alignment startswith() and endswith() phone = ' 0712345678 ' print ( phone . startswith ( ' 07 ' )) print ( phone . endswith ( ' 678 ' )) Output True True Padding and Alignment name = ' Otieno ' print ( f " [ { name : < 10 } ] " ) # Left align print ( f " [ { name : > 10 } ] " ) # Right align print ( f " [ { name : ^ 10 } ] " ) # Center align Output [Otieno ] [ Otieno] [ Otieno ] Table Formatting Example employee = [ ( " Brian " , " Developer " , 102000 ), ( " Otieno " , " Finance " , 78000 ), ( " Njeri " , " Data Engineer " , 95000 ) ] print ( f " { ' Name ' : < 12 } { ' Role ' : < 18 } { ' Salary ' : > 12 } " ) print ( " - " * 40 ) for name , role , salary in employee : print ( f " { name : < 12 } { role : < 18 } Ksh { salary : > 8 } " ) Output Name Role Salary ---------------------------------------- Brian Developer Ksh 102000 Otieno Finance Ksh 78000 Njeri Data Engineer Ksh 95000 Conclusion String methods make text manipulation in Python simple and powerful. You can: Slice and combine text easily Clean and format data Validate user input Search and replace efficiently Mastering these methods will make your Python programs cleaner, smarter, and more professional.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/alex_murithi/mastering-python-string-methods-3gm9

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
