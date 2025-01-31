# Snake Class Documentation

## Table of Contents

* [1. Overview](#1-overview)
* [2. Class Structure: `Snake`](#2-class-structure-snake)
    * [2.1 `__init__(self)`](#21-__init__self)
    * [2.2 `create_snake(self)`](#22-create_snake-self)
    * [2.3 `add_segment(self, position)`](#23-add_segment-self-position)
    * [2.4 `extend(self)`](#24-extend-self)
    * [2.5 `move(self)`](#25-move-self)
    * [2.6 `up(self)`](#26-up-self)
    * [2.7 `down(self)`](#27-down-self)
    * [2.8 `left(self)`](#28-left-self)
    * [2.9 `right(self)`](#29-right-self)
    * [2.10 `reset(self)`](#210-reset-self)
* [3. Constants](#3-constants)


<a name="1-overview"></a>
## 1. Overview

This document details the `Snake` class, designed to represent a snake in a simple game.  The snake is composed of multiple segments, controlled through user input, and capable of growing and resetting its position.  The class utilizes the `turtle` graphics library.


<a name="2-class-structure-snake"></a>
## 2. Class Structure: `Snake`

<a name="21-__init__self"></a>
### 2.1 `__init__(self)`

The constructor initializes the snake. It creates an empty list `self.segments` to store the snake segments and calls `create_snake()` to create the initial snake body. Finally, it sets `self.head` to the first segment of the snake.

```python
def __init__(self):
    self.segments = []
    self.create_snake()
    self.head = self.segments[0]
```

<a name="22-create_snake-self"></a>
### 2.2 `create_snake(self)`

This method creates the initial three segments of the snake at the starting positions defined in `STARTING_POSITIONS`. It iterates through the starting positions and calls `add_segment()` for each position.

```python
def create_snake(self):
    for position in STARTING_POSITIONS:
        self.add_segment(position)
```

<a name="23-add-segment-self-position"></a>
### 2.3 `add_segment(self, position)`

This method adds a new segment to the snake at the given `position`. It creates a `Turtle` object with a square shape, white color, and adds it to the `self.segments` list.

```python
def add_segment(self, position):
    snake_segment = Turtle("square")
    snake_segment.color("white")
    snake_segment.pu() # Pen up to prevent drawing lines while moving.
    snake_segment.goto(position)
    self.segments.append(snake_segment)
```

<a name="24-extend-self"></a>
### 2.4 `extend(self)`

This method extends the snake by adding a new segment at the tail. The position of the new segment is determined by the position of the last segment in the snake.

```python
def extend(self):
    #add a new segment to the snake:
    self.add_segment(self.segments[-1].position())
```

<a name="25-move-self"></a>
### 2.5 `move(self)`

This method moves the snake. It iterates through the snake segments from tail to head. Each segment moves to the position of the segment in front of it. Finally, the head moves forward by `MOVE_DISTANCE`. This creates the snake's movement animation. The algorithm efficiently updates the positions of all segments by shifting them one-by-one.

```python
def move(self):
    for seg_num in range(len(self.segments) - 1, 0, -1):
        new_x = self.segments[seg_num - 1].xcor()
        new_y = self.segments[seg_num - 1].ycor()
        self.segments[seg_num].goto(new_x, new_y)
    self.head.forward(MOVE_DISTANCE)
```

<a name="26-up-self"></a>
### 2.6 `up(self)`

This method changes the snake's heading to upwards (90 degrees), but only if the snake is not currently heading downwards (270 degrees). This prevents the snake from immediately reversing direction.

```python
def up(self):
    if self.head.heading() != DOWN:
        self.head.setheading(UP)
```

<a name="27-down-self"></a>
### 2.7 `down(self)`

This method changes the snake's heading to downwards (270 degrees), but only if the snake is not currently heading upwards (90 degrees).

```python
def down(self):
    if self.head.heading() != UP:
        self.head.setheading(DOWN)
```

<a name="28-left-self"></a>
### 2.8 `left(self)`

This method changes the snake's heading to the left (180 degrees), unless it's already heading right (0 degrees).

```python
def left(self):
    if self.head.heading() != RIGHT:
        self.head.setheading(LEFT)
```

<a name="29-right-self"></a>
### 2.9 `right(self)`

This method changes the snake's heading to the right (0 degrees), unless it's already heading left (180 degrees).

```python
def right(self):
    if self.head.heading() != LEFT:
        self.head.setheading(RIGHT)
```

<a name="210-reset-self"></a>
### 2.10 `reset(self)`

This method resets the snake to its initial state.  It moves all segments off-screen, clears the `segments` list, recreates the snake using `create_snake()`, and updates `self.head`.

```python
def reset(self):
    for seg in self.segments:
        seg.goto(1000, 1000)
    self.segments.clear()
    self.create_snake()
    self.head = self.segments[0]
```

<a name="3-constants"></a>
## 3. Constants

| Constant Name       | Value | Description                                  |
|----------------------|-------|----------------------------------------------|
| `STARTING_POSITIONS` | List  | Initial positions of snake segments.       |
| `MOVE_DISTANCE`     | Integer| Distance moved by snake per step.            |
| `UP`                | Integer| Angle representing upward direction (90).   |
| `DOWN`              | Integer| Angle representing downward direction (270). |
| `LEFT`              | Integer| Angle representing left direction (180).    |
| `RIGHT`             | Integer| Angle representing right direction (0).     |

