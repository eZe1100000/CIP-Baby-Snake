# CIP-Baby-Snake

<img width="1017" height="635" alt="babySnake" src="https://github.com/user-attachments/assets/c0b6abc5-485e-4592-847e-6cec1dd6cb0e" />

👉 [Click Here to Play the Game!](https://codeinplace.stanford.edu/cip6/share/jo1ex3EgH0xHZTGrIvlg)

Baby Snake is a simple endless arcade game built with Python, inspired by the classic Snake game.
The objective is to control the blue snake, eat the targets, avoid randomly spawning obstacles, and survive as long as possible while achieving the highest score.

One of the main goals of this project was to create a clean, responsive game grid where the difficulty increases dynamically as the player progresses.

## Features
* Endless gameplay
* Randomly generated obstacles that block your path
* Increasing difficulty (game speed increases over time)
* Score tracking system
* Clean, minimalist grid-based graphics
* Smooth movement mechanics
  
## Gameplay
* The snake starts moving to the right automatically at the beginning.
* Control the snake to eat the pink goals.
* Earn points by successfully reaching the goals.
* Every time you score, the game gets slightly faster.
* Every 5 points, a new permanent obstacle spawns on the map, making navigation more challenging.
*The game ends immediately if you hit an obstacle or the screen boundaries.

## Graphics
All visual elements in the game are generated programmatically using Python code, maintaining a retro and clean arcade look:
* Player: A blue square representing the snake.
* Goal: A pink square that changes its position randomly once eaten.
* Obstacles: Purple rectangles that block the grid.
* User Interface: A dynamic final score text displayed upon game over.

## Controls

| Key | Action |
| :---: | :--- |
| <kbd>ARROW KEYS</kbd> | Move Snake (Up, Down, Left, Right) |

## Main Functions

### main()
Controls the overall game flow, initializes the player and the goal, tracks the direction/score, and manages the main game loop including game-over conditions.

### create_player(canvas)
Draws and initializes the player character as a blue square at the starting coordinates.

### create_goal(canvas)
Draws the initial target (pink square) on the grid for the player to collect.

### move_goal(canvas, goal)
Calculates a new random grid cell and repositions the goal to that coordinate after it is eaten.

### create_obstacle(canvas, player, goal, obstacles)
Generates a new purple obstacle at a random grid position. It ensures the obstacle does not spawn directly on top of the player or the current goal.

### has_reached_goal(canvas, player, goal)
Uses overlap detection to check if the player has successfully collided with the goal. If true, it triggers the goal relocation.

### check_out_of_bounds(canvas, obj)
Checks whether the player has crossed any of the four screen boundaries (top, bottom, left, right).

### has_collided_obstacle(canvas, player, obstacles)
Checks if the player's current position overlaps with any of the purple obstacles existing in the array.

### create_score_text(canvas, score)
Displays the final score in a clear text format on the screen when the game ends.
