import os
import random
from sympy import true
from classes.object import Object
from classes.score import Score
from shared.color import Color
from shared.point import Point
from classes.keyboard import Keyboard
from classes.video import Video
from classes.director import Director
from classes.player import Player
from classes.board import Board

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
GREEN = Color(45, 245, 45)
color_list = [Color(245, 45, 45),Color(45, 245, 45),Color(45, 45, 255),Color(255, 255, 255)]

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
    board.add_actor("player", player)

    banner = Score()
    banner.set_actual_score(0)
    banner.set_text("Your Score is 0")
    banner.set_font_size(FONT_SIZE)
    banner.set_color(RED)
    board.add_actor("banner", banner)

    # Start the game
    keyboard = Keyboard()
    video = Video(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard, video)
    director.start_game(board)

if __name__ == "__main__":
    main()