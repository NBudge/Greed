import os
import random

from sympy import true

from classes.keyboard import Keyboard
from classes.video import Video
from classes.director import Director
from classes.board import Board

from classes.constants import CAPTION
from classes.constants import MAX_X
from classes.constants import MAX_Y
from classes.constants import CELL_SIZE
from classes.constants import FRAME_RATE



def main():
    board = Board()
    keyboard = Keyboard()
    video = Video(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard, video)
    director.prep_game(board)
    director.start_game(board)

##while (GAME == true):
if __name__ == "__main__":
    main()