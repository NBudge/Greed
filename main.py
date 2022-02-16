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



FRAME_RATE = 10
MAX_X = 800
MAX_Y = 600
CAPTION = "GREED"

CELL_SIZE = 20
FONT_SIZE = 20

COLS = 40
ROWS = 30
GAME = true
WHITE = Color(255, 255, 255)
BLUE = Color(45, 45, 255)
RED = Color(245, 45, 45)


def main():
    board = Board()

    
    x = int(MAX_X / 2)
    y = int(MAX_Y - 50)
    position = Point(x, y)

    player  = Player()
    player.set_position(position)
    player.set_text("#")
    player.set_font_size(FONT_SIZE)
    player.set_color(WHITE)


    rock = Rock()
    rock.set_position(Point(210, 360))
    rock.set_text("o")
    rock.set_font_size(FONT_SIZE)
    rock.set_color(RED)
    gem = Gem()
    gem.set_position(Point(240, 300))
    gem.set_text("*")
    gem.set_font_size(FONT_SIZE)
    gem.set_color(BLUE)

    board.add_actor("player", player)
    board.add_actor("rocks", rock)
    board.add_actor("gems", gem)
    print("main")
    # Start the game
    keyboard = Keyboard()
    video = Video(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard, video)
    director.start_game(board)



##while (GAME == true):
    


if __name__ == "__main__":
    main()