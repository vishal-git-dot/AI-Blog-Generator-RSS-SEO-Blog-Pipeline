---
title: "React Hooks And useState"
slug: "react-hooks-and-usestate"
author: "Abimanyu P"
source: "devto_webdev"
published: "Thu, 24 Sep 2026 16:47:08 +0000"
description: "React Hooks Hooks are special functions in React that allow functional components to use React features such as state. Before hooks were introduced, state an..."
keywords: "usestate, value, react, state, hooks, used, const, count"
generated: "2026-09-24T16:53:21.336096"
---

# React Hooks And useState

## Overview

React Hooks Hooks are special functions in React that allow functional components to use React features such as state. Before hooks were introduced, state and other React features were mainly used with class components. Hooks made it possible to use these features inside functional components in a simpler way. A hook is usually a function that starts with the word use . Some commonly used hooks are useState , useEffect , and useContext . Each hook has a specific purpose. useState is used to store and update data that can change inside a component. useState useState is a React hook used to create a state variable in a functional component. It returns two values: the current state value and a function used to update that value. import { useState } from " react " ; function App () { const [ count , setCount ] = useState ( 0 ); return ( < div > < h1 > Count: { count } </ h1 > < button onClick = { () => setCount ( count + 1 ) } > + </ button > </ div > ); } Here, count stores the current value and setCount changes the value. The 0 passed to useState is the initial value. useState can also be used with different types of data. For example: const [ name , setName ] = useState ( "" ); const [ isVisible , setIsVisible ] = useState ( false ); const [ likes , setLikes ] = useState ( 0 ); When the state is updated, React re-renders the component and displays the updated value. For input fields, useState can store the value entered by the user: const [ name , setName ] = useState ( "" ); < input value = { name } onChange = { ( event ) => setName ( event . target . value ) } /> event.target.value gets the current value from the input and setName updates the state. State can also control whether something is displayed: const [ isVisible , setIsVisible ] = useState ( false ); < button onClick = { () => setIsVisible ( ! isVisible ) } > Show / Hide </ button > { isVisible && < p > Hello! </ p >} Here, the boolean state controls the visibility of the paragraph. Think of it as: If isVisible is true, show <p>Hello!</p> . Otherwise, show nothing. Ex: {false && <p>Hello!</p>} The paragraph is not displayed. {true && <p>Hello!</p>} React displays: Hello! This is called conditional rendering using the "&&" operator. useState is useful whenever a component needs to remember changing information, such as counters, input values, likes, messages, or whether an element should be visible.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/abimanyu_p_9e75124634d2a4/react-hooks-and-usestate-35h1

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
