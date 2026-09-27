---
title: "11 - Multi-Tool Orchestration in PHP - One Agent, Many Tools, One Answer"
slug: "11-multi-tool-orchestration-in-php-one-agent-many-tools-one-answer"
author: "Khaled Hammrouni"
source: "devto_ai"
published: "Sun, 27 Sep 2026 20:56:16 +0000"
description: "A single tool is easy to reason about. The interesting problem is an agent with several specialized tools that has to figure out which to call, in what order..."
keywords: "city, agent, tool, tools, weather, events, new, name"
generated: "2026-09-27T21:09:51.534878"
---

# 11 - Multi-Tool Orchestration in PHP - One Agent, Many Tools, One Answer

## Overview

A single tool is easy to reason about. The interesting problem is an agent with several specialized tools that has to figure out which to call, in what order , and how to combine the results into one answer. This example is a personal concierge with three tools - location, weather, events - and the user's request needs all three chained together: "Check where I am, get the weather there, and see if there are any jazz events tonight." Three focused tools The first tool takes no input at all - it just reports where the (simulated) user is: use NanoAgent\Agent ; use NanoAgent\Tools\FunctionTool ; $locationTool = new FunctionTool ( name : 'detect_user_location' , description : 'Determines the user\'s current city and country.' , parameters : [ 'type' => 'object' , 'properties' => new stdClass ()], // no params callable : fn () => [ 'city' => 'Paris' , 'country' => 'France' ] ); The second and third tools both take a city - the value the location tool just produced is what will get passed into these two: $weatherTool = new FunctionTool ( name : 'get_current_weather' , description : 'Fetches the live weather forecast for a given city.' , parameters : [ 'type' => 'object' , 'properties' => [ 'city' => [ 'type' => 'string' , 'description' => 'The city name' ]], 'required' => [ 'city' ] ], callable : function ( array $args ) { $obs = [ 'Paris' => 'Cloudy, 14°C' , 'London' => 'Rainy, 11°C' , 'New York' => 'Sunny, 22°C' ]; return $obs [ $args [ 'city' ]] ?? 'Weather data unavailable.' ; } ); $eventTool = new FunctionTool ( name : 'search_local_events' , description : 'Searches for upcoming cultural events or concerts in a specific city.' , parameters : [ 'type' => 'object' , 'properties' => [ 'city' => [ 'type' => 'string' , 'description' => 'The city name' ]], 'required' => [ 'city' ] ], callable : function ( array $args ) { if ( $args [ 'city' ] === 'Paris' ) { return [ [ 'name' => 'Jazz Festival at Le Caveau' , 'time' => '20:00' ], [ 'name' => 'Monet at Grand Palais' , 'time' => '10:00-18:00' ] ]; } return "No specific events found for { $args [ 'city' ] } today." ; } ); The agent decides the order $agent = new Agent ( llm : $llmConfig , systemPrompt : "You are a personal concierge with location, weather, and event tools. " . "When answering, first describe the location and weather, then list any " . "relevant events." , tools : [ $locationTool , $weatherTool , $eventTool ] ); $agent -> enableActivityLogging (); $response = $agent -> chat ( "Check where I am, get the weather there, and see if there are any jazz events tonight." ); echo $response ; You did not script the sequence. The model: Calls detect_user_location (no args) → Paris . Calls get_current_weather with city: "Paris" → Cloudy, 14°C . Calls search_local_events with city: "Paris" → the jazz festival. Composes the final answer in the order the prompt asked for. The dependency is implicit. The model reads the location result, then passes that city into the next two tools. You gave it the pieces and the goal; it built the pipeline. The two things that make this work Each tool is narrow and well-described. description is what the model reads to choose a tool. "Determines the user's current city and country" tells it this is the first step. Vague descriptions = wrong tool picks. The prompt sets the shape of the answer , not the tool calls. "First describe location and weather, then list events" steers the composition while leaving the orchestration to the model. Tool with no parameters - the stdClass() trick detect_user_location takes no input. In JSON Schema an object with no properties is {'type':'object','properties':{}} - in PHP you write new stdClass() for that empty object. Small gotcha, easy to miss: a [] (empty array) encodes as a JSON array , not an object. When to use this vs. an agent chain Multi-tool, one agent (this): the steps are interdependent and the model should choose the path. Good for concierges, assistants, anything open-ended. Agent chain ( this article ): the stages are fixed and you want different models/prompts per stage. Good for deterministic pipelines. Rule of thumb: if the path is fixed, use a chain; if the path depends on the input, give one agent many tools and let it decide. Part of the NanoAgent examples series. Landing + demos .

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/hammrouni/11-multi-tool-orchestration-in-php-one-agent-many-tools-one-answer-5c7f

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
