# Rogueday - Following along with Y.A.R.T

https://rogueliketutorials.com/tutorials/tcod/v2/

* Part 0 - Setting Up [no tag]
* Part 1 - Drawing the '@' symbol and moving it around [v1.1.0]
* Part 2 - The generic Entity, the render functions, and the map [v1.2.0]
* Part 3 - Generating a dungeon [v1.3.0]
* Part 4 - Field of View [v1.4.0]
* Part 5 - Placing Enemies and kicking them (harmlessly) [v1.5.0]


## Notes

### Part 2

1. "from __future__ import annotations" seems to confuse 3.8
2. Why use numpy except for the slice syntax?
3. I got a circular reference using the type annotations

### Part 3

1. I'm still not having much luck with the type annotations and I think they might be confusing for a tutorial.
2. Some of the functions have a lot of arguments.It might be easier to keep them all in a config object.

### Part 4

1. I rushed through this because I'm catching up but the results are very cool.
2. The Numpy stuff might be overcomplicated for a tutorial though.

### Part 5

1. Still playing catch up
2. I've just about given up on the type annotations. They may be useful but they do obscure the code's meaning.


### 5.1 Refactoring

1. Aaargh!
2. I'm removing the type annotations as I revisit code

