---
title: "DOM In JavaScript"
slug: "dom-in-javascript"
author: "Abimanyu P"
source: "devto_webdev"
published: "Thu, 03 Sep 2026 16:05:04 +0000"
description: "DOM in JavaScript When we create a webpage using HTML, the browser needs a way to understand and manage all the elements on that page. For this, the browser ..."
keywords: "document, javascript, elements, can, dom, heading, html, hello"
generated: "2026-09-03T16:11:07.917137"
---

# DOM In JavaScript

## Overview

DOM in JavaScript When we create a webpage using HTML, the browser needs a way to understand and manage all the elements on that page. For this, the browser creates a structure called the DOM . DOM stands for Document Object Model . It represents an HTML document as a tree of objects , where elements like <html> , <body> , <h1> , <p> , and <button> become nodes that JavaScript can access and modify. What is the DOM? Consider this HTML: <!DOCTYPE html> <html> <body> <h1> Hello </h1> <p> This is a paragraph. </p> </body> </html> The browser represents it approximately like this: Document │ └── html │ └── body ├── h1 │ └── "Hello" │ └── p └── "This is a paragraph." This tree-like representation is called the DOM tree . JavaScript can interact with this tree to select elements, change their content, modify their styles, create new elements, remove elements, and respond to user actions. The basic process is: HTML ↓ Browser ↓ DOM ↓ JavaScript modifies DOM ↓ Webpage gets updated The document Object The main way JavaScript interacts with the DOM is through the document object. console . log ( document ); The document object represents the current HTML document and provides many methods for finding and manipulating elements. For example: let heading = document . getElementById ( " title " ); Here, JavaScript uses the document object to find an element from the DOM. Selecting Elements Before modifying an element, we usually need to select it. getElementById() It selects an element using its id . <h1 id= "title" > Hello </h1> let heading = document . getElementById ( " title " ); The heading variable now refers to the <h1> element. querySelector() querySelector() selects the first element that matches a CSS selector. let heading = document . querySelector ( " h1 " ); It can also be used with classes and IDs: let box = document . querySelector ( " .box " ); let title = document . querySelector ( " #title " ); querySelectorAll() querySelectorAll() selects all elements matching a CSS selector. <p> Hello </p> <p> World </p> <p> JavaScript </p> let paragraphs = document . querySelectorAll ( " p " ); Now paragraphs contains all three <p> elements. You can access individual elements using their index: console . log ( paragraphs [ 0 ]); console . log ( paragraphs [ 1 ]); Changing Content After selecting an element, JavaScript can change its content. <h1 id= "title" > Hello </h1> let heading = document . getElementById ( " title " ); heading . textContent = " Hello JavaScript " ; The heading on the webpage changes from Hello to Hello JavaScript . textContent and innerHTML textContent treats the assigned value as plain text. heading . textContent = " <b>Hello</b> " ; The browser displays: <b>Hello</b> It does not create a bold element. innerHTML interprets the value as HTML: heading . innerHTML = " <b>Hello</b> " ; Now the <b> element is created inside the heading. For plain text, textContent is generally the safer and simpler choice. Changing CSS JavaScript can also modify an element's inline styles. heading . style . color = " red " ; heading . style . fontSize = " 40px " ; This changes the heading's color and font size. For larger styling changes, it is often better to use CSS classes: heading . classList . add ( " active " ); This allows CSS to control the actual styling while JavaScript controls which class is applied. Changing Attributes HTML elements can have attributes such as src , href , id , and class . JavaScript can read and modify these attributes. For example: <img id= "photo" src= "old.jpg" > We can change the image source: let image = document . getElementById ( " photo " ); image . setAttribute ( " src " , " new.jpg " ); We can also read the value: console . log ( image . getAttribute ( " src " )); Creating Elements The DOM isn't only used to modify existing elements. JavaScript can also create completely new elements. let paragraph = document . createElement ( " p " ); paragraph . textContent = " This paragraph was created using JavaScript. " ; The paragraph has been created, but it is not yet attached to the webpage. We can add it to the page using appendChild() : document . body . appendChild ( paragraph ); Now the new paragraph appears inside the <body> . Removing Elements JavaScript can also remove elements from the DOM. let paragraph = document . querySelector ( " p " ); paragraph . remove (); The selected paragraph is removed from the webpage. DOM and Events Another important use of the DOM is handling user actions. For example, we can listen for a button click: <button id= "btn" > Click Me </button> let button = document . getElementById ( " btn " ); button . addEventListener ( " click " , function () { console . log ( " Button clicked " ); }); addEventListener() tells JavaScript to listen for a particular event. In this example, when the button is clicked, the function runs. We can also use the event to modify the webpage: button . addEventListener ( " click " , function () { document . body . style . backgroundColor = " lightblue " ; }); Now clicking the button changes the background color of the page.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/abimanyu_p_9e75124634d2a4/dom-in-javascript-2iog

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
