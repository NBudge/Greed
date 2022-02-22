import os
import random

from sympy import true

from shared.color import Color
from shared.point import Point

from classes.keyboard import Keyboard
from classes.video import Video
from classes.director import Director
from classes.player import Player
from classes.board import Board
from classes.gem import Gem
from classes.rock import Rock
from classes.score import Score



FRAME_RATE = 10
MAX_X = 800
MAX_Y = 600
CAPTION = "GREED"

CELL_SIZE = 20
FONT_SIZE = 20

COLS = MAX_Y
ROWS = 30
GAME = true
WHITE = Color(255, 255, 255)
BLUE = Color(45, 45, 255)
RED = Color(245, 45, 45)
DEFAULT_ROCKS = 10
DEFAULT_GEMS = 10

def main():
    board = Board()

    
    player_x = int(MAX_X / 2)
    player_y = int(MAX_Y - 50)
    player_position = Point(player_x, player_y)

    score_x = int(MAX_X / 125)
    score_y = int(MAX_Y / 100)
    score_position = Point(score_x, score_y)

    player  = Player()
    player.set_position(player_position)
    player.set_text("#")
    player.set_font_size(FONT_SIZE)
    player.set_color(WHITE)

    score = Score()
    score.set_position(score_position)
    score.set_text("Score: ")
    score.set_font_size(FONT_SIZE)
    score.set_color(WHITE)

    for n in range(DEFAULT_ROCKS):
        x = random.randint(1, COLS - 1)
        bar_position = Point(x, 25)
        rock = Rock()
        rock.set_position(bar_position)
        rock.set_text("o")
        rock.set_font_size(FONT_SIZE)
        rock.set_color(RED)
        board.add_actor("rocks", rock)

    for n in range(DEFAULT_GEMS):
        x = random.randint(1, COLS - 1)
        bar_position = Point(x, 25)
        gem = Gem()
        gem.set_position(bar_position)
        gem.set_text("*")
        gem.set_font_size(FONT_SIZE)
        gem.set_color(BLUE)
        board.add_actor("gems", gem)

    board.add_actor("player", player)
    board.add_actor("score", score)
    print("main")
    # Start the game
    keyboard = Keyboard()
    video = Video(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard, video)
    director.start_game(board)



##while (GAME == true):
    


if __name__ == "__main__":
    main()