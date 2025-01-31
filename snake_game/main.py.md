# Snake Game Code Documentation

## Table of Contents

* [1. Introduction](#1-introduction)
* [2. Game Setup](#2-game-setup)
* [3. Game Loop and Logic](#3-game-loop-and-logic)
    * [3.1. Snake Movement](#31-snake-movement)
    * [3.2. Food Collision Detection](#32-food-collision-detection)
    * [3.3. Wall Collision Detection](#33-wall-collision-detection)
    * [3.4. Self-Collision Detection](#34-self-collision-detection)
* [4. Scoreboard](#4-scoreboard)
* [5. Resetting the Game](#5-resetting-the-game)


## 1. Introduction

This document details the code for a classic Snake game implemented using Python's Turtle graphics library.  The game involves controlling a snake to eat food and grow longer, avoiding collisions with walls and itself.


## 2. Game Setup

The game initializes by importing necessary modules: `turtle`, `time`, `Snake`, `Food`, and `Scoreboard`. These modules are assumed to contain the respective classes for screen management, game timing, snake object, food object, and scoreboard.

The game screen is set up with a width and height of 600 pixels, a black background, and the title "Snake". `screen.tracer(0)` disables automatic screen updates, allowing for manual updates within the game loop for smoother animation.

A `Snake` object, a `Food` object, and a `Scoreboard` object are created.  Event listeners are set up to control the snake's movement using the Up, Down, Left, and Right arrow keys.


## 3. Game Loop and Logic

The main game loop (`while game_is_on:`) runs continuously until the game ends.

### 3.1. Snake Movement

The `snake.move()` function (defined within the `Snake` class, not shown here) is responsible for updating the snake's position on the screen.  This likely involves moving each segment of the snake to the position of the segment in front of it, and updating the head's position based on the current direction.


### 3.2. Food Collision Detection

The game checks for collisions between the snake's head and the food using `snake.head.distance(food) < 15`. If the distance is less than 15 pixels, it's considered a collision.  The `score_text.score_increase()` function (part of the `Scoreboard` class) updates the score, the `food.refresh()` function moves the food to a new random location, and the `snake.extend()` function adds a new segment to the snake, increasing its length.

### 3.3. Wall Collision Detection

The game checks for collisions with the walls by checking the coordinates of the snake's head (`snake.head.xcor()`, `snake.head.ycor()`). If the head's x or y coordinate exceeds the screen boundaries (280 or -280), a collision is detected. The `score_text.reset()` function resets the score, and `snake.reset()` resets the snake's position and length back to the initial state.


### 3.4. Self-Collision Detection

The game checks for self-collisions by iterating through each segment of the snake's body (excluding the head).  If the head's distance to any segment is less than 10 pixels, a collision is detected. Similar to wall collision, the `score_text.reset()` and `snake.reset()` functions are called to reset the game state.


## 4. Scoreboard

The `Scoreboard` class (not shown) handles displaying the score and game over messages.  `score_text.score_increase()` increments the score and updates the display. `score_text.reset()` resets the score to zero.  The commented-out code suggests there was initially functionality for `score_text.game_over()`, which would likely display a "Game Over" message.


## 5. Resetting the Game

When a wall or self-collision occurs, the game is reset using `score_text.reset()` and `snake.reset()`. This returns the score to zero and the snake to its initial state, allowing the player to restart the game.  The game loop continues, enabling immediate restart without explicit player action beyond continued game play.
