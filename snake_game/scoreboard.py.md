# Scoreboard Class Documentation

[Linked Table of Contents](#linked-table-of-contents)

## Linked Table of Contents

* [1. Introduction](#1-introduction)
* [2. Class `Scoreboard`](#2-class-scoreboard)
    * [2.1 `__init__(self)`](#21-__init__self)
    * [2.2 `score_increase(self)`](#22-score_increaseself)
    * [2.3 `update_scoreboard(self)`](#23-update_scoreboardself)
    * [2.4 `reset(self)`](#24-resetself)


## 1. Introduction

This document details the `Scoreboard` class, responsible for managing and displaying the score in a game.  The class interacts with a data file ("data.txt") to store and retrieve the high score.


## 2. Class `Scoreboard`

The `Scoreboard` class inherits from the `Turtle` class, allowing it to display text on the screen.  It manages the current score and the high score, updating the display accordingly.

### 2.1 `__init__(self)`

This is the constructor for the `Scoreboard` class.

| Parameter | Type | Description |
|---|---|---|
| `self` | `Scoreboard` |  Instance of the class |


**Functionality:**

1. Initializes the `score` attribute to 0.
2. Reads the high score from the "data.txt" file.  If the file doesn't exist or is empty, it defaults to 0 (implicit in how the file is handled).
3. Sets the turtle's color to white and hides the turtle itself (only the text is shown).
4. Lifts the pen (`pu()`) to prevent drawing while moving.
5. Positions the turtle at coordinates (0, 270).
6. Calls `update_scoreboard()` to display the initial score and high score.

### 2.2 `score_increase(self)`

This method increases the current score by 1 and updates the scoreboard display.

| Parameter | Type | Description |
|---|---|---|
| `self` | `Scoreboard` | Instance of the class |

**Functionality:**

1. Increments the `score` attribute by 1.
2. Calls `update_scoreboard()` to refresh the display.


### 2.3 `update_scoreboard(self)`

This method clears the previous scoreboard display and writes the updated score and high score to the screen.

| Parameter | Type | Description |
|---|---|---|
| `self` | `Scoreboard` | Instance of the class |

**Functionality:**

1. Clears the previous text using `self.clear()`.
2. Writes the string "Score: {self.score} High score: {self.high_score}" to the screen using the specified alignment, font, and `write()` method inherited from the `Turtle` class.  The `False` argument prevents moving the turtle after writing.


### 2.4 `reset(self)`

This method resets the score to 0 and updates the high score if the current score exceeds it.  The high score is then written back to the data file.

| Parameter | Type | Description |
|---|---|---|
| `self` | `Scoreboard` | Instance of the class |

**Functionality:**

1. Checks if the current `score` is greater than the high score (`self.high_score`).
2. If the current score is higher, it updates the `high_score` attribute.
3. Writes the new high score to "data.txt", overwriting the previous value.
4. Resets the `score` attribute to 0.
5. Calls `update_scoreboard()` to reflect the changes on the screen.

The algorithm used for updating the high score is a simple comparison: if the current score exceeds the stored high score, the high score is updated.  The file I/O is straightforward, writing the updated high score as a string to the file.
