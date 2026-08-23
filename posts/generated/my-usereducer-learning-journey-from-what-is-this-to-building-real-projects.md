---
title: "My useReducer Learning Journey: From 'What is this?' to Building Real Projects"
slug: "my-usereducer-learning-journey-from-what-is-this-to-building-real-projects"
author: "Karthick (k)"
source: "devto_webdev"
published: "Sun, 23 Aug 2026 06:45:09 +0000"
description: "My useReducer Learning Journey: From "What is this? ' to Building Real Projects. A few days ago, I couldn't tell you what UseReducer was. Today I have built ..."
keywords: "state, question, usereducer, answer, app, const, options, river"
generated: "2026-08-23T06:49:22.752463"
---

# My useReducer Learning Journey: From 'What is this?' to Building Real Projects

## Overview

My useReducer Learning Journey: From "What is this? ' to Building Real Projects. A few days ago, I couldn't tell you what UseReducer was. Today I have built a TODO list and a Quiz app with it. I want to share exactly how that happened- confusion and all -- because I think a lot of beginners hit the same wall I did. const [state, dispatch] = useReducer(reducerFunction, initialState); Project 1: Quiz App import { useReducer, useState } from 'react' import reactLogo from './assets/react.svg' import viteLogo from './assets/vite.svg' import heroImg from './assets/hero.png' import './App.css' const Question = [ { Question: "What is the capital of India?", Options: ["Mumbai", "Delhi", "Chennai", "Kolkata"], answer: "Delhi" }, { Question: "Which hook is used for complex state?", Options: ["useState", "useReducer", "useEffect", "useRef"], answer: "useReducer" }, { Question: "React is a", Options: ["Library", "Language", "Database", "Frameworks"], answer: "Library" }, { Question: "What is the longest river in the world?", Options: ["Amazon River", "The Nile River", "The Yangtze River", "The Mississippi River"], answer: "The Nile River" }, { Question: "Which country is home to the most natural lakes in the world?", Options: ["Canada", "United States", "Russia", "Australia"], answer: "Canada" }, ]; const initialState = { currentQuestion: 0, score: 0, showResults: false }; function QuizReducer(state, action) { switch (action.type) { case "Answer": const isCorrect = action.payload === Question[state.currentQuestion].answer; return { ...state, score: isCorrect ? state.score + 1 : state.score, currentQuestion: state.currentQuestion + 1 } default: return state; }; } function App() { const [state, dispatch] = useReducer(QuizReducer, initialState); if (state.currentQuestion >= Question.length) { return ( <div> <h2>Quiz App</h2> <p> Your Score : {state.score} /{Question.length}</p> </div> ); } const current = Question[state.currentQuestion]; return ( <div> <h2>Quiz App</h2> <h3>{current.Question}</h3> {current.Options.map((option) => ( <button key={option} onClick={() => dispatch({ type: "Answer", payload: option })} > {option} </button> ))} </div> ); } export default App This is the expected output:

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/karthick_07/my-usereducer-learning-journey-from-what-is-this-to-building-real-projects-4e48

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
