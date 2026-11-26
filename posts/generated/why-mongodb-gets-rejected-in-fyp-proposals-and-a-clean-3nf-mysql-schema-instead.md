---
title: "Why MongoDB Gets Rejected in FYP Proposals (And a Clean 3NF MySQL Schema Instead)"
slug: "why-mongodb-gets-rejected-in-fyp-proposals-and-a-clean-3nf-mysql-schema-instead"
author: "Fyp Services"
source: "devto_webdev"
published: "Thu, 26 Nov 2026 07:33:53 +0000"
description: "If your FYP proposal says "we will use MongoDB because it is modern and flexible", expect the panel to push back. In Pakistani universities, supervisors and ..."
keywords: "not, null, key, your, varchar, fyp, mongodb, schema"
generated: "2026-11-26T07:44:38.396686"
---

# Why MongoDB Gets Rejected in FYP Proposals (And a Clean 3NF MySQL Schema Instead)

## Overview

If your FYP proposal says "we will use MongoDB because it is modern and flexible", expect the panel to push back. In Pakistani universities, supervisors and external examiners check your database design against one thing first: normalisation. A document store makes that check almost impossible to pass, because there is no fixed schema to normalise. This is not about MongoDB being bad. It is about what an FYP viva can grade. Why panels reject the MongoDB pitch No schema to examine. The examiner cannot verify 1NF, 2NF and 3NF if every document can have different fields. Duplication by design. Embedding copies of the same student, course or product data in many documents is exactly the redundancy normalisation exists to remove — and viva questions target it. "Flexibility" reads as "we have not designed it yet." Panels hear that sentence from every group, every semester. Unless your project is genuinely document-shaped (logs, sensor data, chat messages at scale) and you can defend that, a relational database is the safer proposal for an FYP. The same system, as a clean 3NF MySQL schema Take a simple FYP example: students submit project proposals, supervisors review them. CREATE TABLE students ( student_id INT PRIMARY KEY AUTO_INCREMENT , reg_no VARCHAR ( 20 ) UNIQUE NOT NULL , full_name VARCHAR ( 100 ) NOT NULL , email VARCHAR ( 120 ) UNIQUE NOT NULL ) ; CREATE TABLE supervisors ( supervisor_id INT PRIMARY KEY AUTO_INCREMENT , full_name VARCHAR ( 100 ) NOT NULL , email VARCHAR ( 120 ) UNIQUE NOT NULL , department VARCHAR ( 80 ) NOT NULL ) ; CREATE TABLE proposals ( proposal_id INT PRIMARY KEY AUTO_INCREMENT , student_id INT NOT NULL , supervisor_id INT NULL , title VARCHAR ( 200 ) NOT NULL , status ENUM ( 'pending' , 'approved' , 'rejected' ) DEFAULT 'pending' , submitted_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP , FOREIGN KEY ( student_id ) REFERENCES students ( student_id ) , FOREIGN KEY ( supervisor_id ) REFERENCES supervisors ( supervisor_id ) ) ; Why this passes the 3NF questions: 1NF: every column holds one value. No comma-separated lists of group members or technologies — those go in their own tables with foreign keys. 2NF: no column depends on only part of a key. Student name lives only in students, never repeated in proposals. 3NF: no column depends on another non-key column. Department belongs to the supervisor record, not copied into every proposal row. The viva questions this prepares you for "Where is your data duplicated?" Nowhere — each fact is stored once, everything else is a foreign key. "What happens if a supervisor changes department?" One row updates, not hundreds. "Show me your ERD." This schema draws directly into an ERD with two clean relationships, which is exactly what Chapter 3 of the report needs. When MongoDB is actually defensible If your core data is unstructured — IoT sensor readings, scraped listings, chat logs — say that, show the document shape, and explain why joins and normalisation do not apply. That answer passes. "It is modern and flexible" does not. For a standard management-system, portal or e-commerce FYP, go relational, normalise to 3NF, and let the examiner's checklist work in your favour.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/fyp_services/why-mongodb-gets-rejected-in-fyp-proposals-and-a-clean-3nf-mysql-schema-instead-5905

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
