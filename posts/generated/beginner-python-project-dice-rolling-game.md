---
title: "Beginner Python Project: Dice Rolling Game"
slug: "beginner-python-project-dice-rolling-game"
author: "Tochi"
source: "devto_python"
published: "Fri, 31 Jul 2026 08:47:55 +0000"
description: "Big shout out to Mosh Hamedani for compiling beginner projects for python developers. Understanding the Problem Before writing any code, I first broke the pr..."
keywords: "choice, dice, game, player, input, print, number, roll"
generated: "2026-07-31T08:56:54.066063"
---

# Beginner Python Project: Dice Rolling Game

## Overview

Big shout out to Mosh Hamedani for compiling beginner projects for python developers. Understanding the Problem Before writing any code, I first broke the problem down into smaller steps. Solving the problem becomes much easier once the overall flow is clear. The requirements are: The player rolls a pair of dice. The program returns the numbers rolled. The program asks if the player wants to roll again. If the answer is yes , roll the dice again. If the answer is no , end the game. Since the same process repeats until the player decides to stop, this problem naturally requires a loop. To make the game work, we also need to get input from the user, so we use Python's input() function. Since a real dice produces random numbers, we use Python's random.randint() function to generate numbers between 1 and 6 . The first version of the solution looks like this: def rolling_dice (): choice = ' y ' while choice == ' y ' : dice_1 = random . randint ( 1 , 6 ) dice_2 = random . randint ( 1 , 6 ) print ( f ' ( { dice_1 } , { dice_2 } ) ' ) choice = input ( " Roll again? (y/n) " ) print ( " Game ended " ) At this point, the game is functional. It rolls two dice, displays the results, and keeps rolling until the user enters 'n' . Validating User Input The next improvement is making sure the player only enters 'y' or 'n' . If they enter anything else, the program should display an error message and ask them to try again. To do this, I created two constants: VALID_CHOICES stores the only acceptable inputs. MAX_ATTEMPTS stores the maximum number of invalid attempts allowed. The validation initially looked like this: VALID_CHOICES = ( ' y ' , ' n ' ) MAX_ATTEMPTS = 3 while choice not in VALID_CHOICES : print ( " Not a valid choice " ) choice = input ( " Try again? (y/n) " ) Now the program prevents unexpected input from causing problems. Improving the Game The original task asked us to keep track of how many times the player rolled the dice. Instead of only counting the number of rolls, I decided to extend the program by adding a maximum number of rolls a player is allowed to make. I also limited the number of invalid inputs the player can enter before the game ends. To achieve this, I introduced two variables: valid_attempts keeps track of the number of successful rolls. invalid_attempts keeps track of invalid user inputs. After every successful roll, valid_attempts increases by one. Likewise, every time the player enters an invalid option, invalid_attempts increases. Once either value reaches the maximum allowed attempts, the game ends. Separating the Validation Logic Rather than writing the validation code inside the game loop every time, I moved it into its own function called validate_choice() . def validate_choice ( choice , invalid_attempts ): while choice not in VALID_CHOICES and invalid_attempts < MAX_ATTEMPTS : print ( " Not a valid choice " ) invalid_attempts += 1 choice = input ( " Try again? (y/n) " ) return choice , invalid_attempts Separating the validation into its own function makes the main game loop easier to read and avoids repeating the same code. Allowing Multiple Dice The final modification was allowing the player to choose how many dice they want to roll. Instead of always rolling two dice, I passed the number of dice as a parameter called number_of_dice . Using a for loop, the program generates one random number for each die and stores the values in a list. Once all the dice have been rolled, the list is converted into a tuple and displayed to the player. dice_rolled = [] for _ in range ( number_of_dice ): dice_rolled . append ( random . randint ( 1 , 6 )) print ( tuple ( dice_rolled )) This makes the program much more flexible because it can roll any number of dice without changing the rest of the code. Final Solution import random VALID_CHOICES = ( ' y ' , ' n ' ) MAX_ATTEMPTS = 3 def validate_choice ( choice , invalid_attempts ): while choice not in VALID_CHOICES and invalid_attempts < MAX_ATTEMPTS : print ( " Not a valid choice " ) invalid_attempts += 1 choice = input ( " Try again? (y/n) " ) return choice , invalid_attempts def dice_rolling ( number_of_dice ): choice = ' y ' valid_attempts = 0 invalid_attempts = 0 while choice == ' y ' and valid_attempts < MAX_ATTEMPTS : dice_rolled = [] for _ in range ( number_of_dice ): dice_rolled . append ( random . randint ( 1 , 6 )) print ( tuple ( dice_rolled )) valid_attempts += 1 choice = input ( " Roll again? (y/n) " ) choice , invalid_attempts = validate_choice ( choice , invalid_attempts ) if invalid_attempts >= MAX_ATTEMPTS : break if valid_attempts >= MAX_ATTEMPTS : print ( " You have exceeded your limit. " ) elif invalid_attempts >= MAX_ATTEMPTS : print ( " You have exceeded your number of invalid attempts. " ) else : print ( " Game ended " ) Conclusion This solution starts with a simple dice rolling game and gradually improves it by validating user input, separating repeated logic into a reusable function, limiting the number of rolls and invalid attempts, and finally allowing the player to choose how many dice to roll. Breaking the problem into smaller pieces made it easier to implement and test each feature before moving on to the next. Here is the Javascript Solution.

## Key Insights

This article was discovered from the latest RSS feeds and automatically transformed into a readable blog post.

### What You Should Know

- Trending topic in the developer community
- Relevant technology discussion
- Worth exploring for deeper research

## Original Source

https://dev.to/tochi_/beginner-python-project-dice-rolling-game-2a7n

## Conclusion

Technology moves quickly. Following curated RSS feeds helps developers stay informed about emerging tools, frameworks, and industry trends.
