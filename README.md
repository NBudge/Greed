# Greed
Simon Carless once described robotfindskitten as "less a game and more a way of life ... It's fun to wander around until you find a kitten, at which point you feel happy and can start again". I don't think I could have said it better myself!

## Getting Started
---
Make sure you have Python 3.8.0 and download packages to run this game
```
pip install -r requirements.txt
```
Arter finishing download requirements.txt, please go to __main__.py and hit 'run' icon

## Project Structure
---
The project files and folders are organized as follows:
```
GREED  (project root folder)
+--shared               (has color and point files for game)
+--classes              (source classes for game)
  +-- board             (file for the board)
  +-- constants         (file for keep displaying the color of gems)
  +-- director          (file for connecting classes together and run game logics)
  +-- gem               (file for subclass of object, gem * )
  +-- keyboard          (file for keyboard)
  +-- object            (file for positions of the gem and color of them)
  +-- player            (file for player's movement)
  +-- rock              (specific game classes)
  +-- score             (specific game classes)
  +-- video             (specific game classes)
  +-- __main__.py       (entry point for program)
+-- requirements.txt    (download requirements)
+-- __main__.py         (main file to run the game)
+-- README.md           (general info)
```

## Required Technologies
---
* Python 3.8.0
* Packages in the requirements.txt

## Authors
* Mallory Lee : Fixed the code(constructors and subclasses) and cleaned up the code. Created constants and director class, requirements.txt
* Cristian Fernandez : I got the rocks and gems falling from the top and the score keeper. After them, added them into director class.
* Zachary Thompson : I entered random generation for gem/rock spawn, and made sure they appeared in a line at the top of the game board.
* Nathanael Budge : Got the basics of the file set up. Got the GUI working initially. Got the player moving. Good tries on score.py
