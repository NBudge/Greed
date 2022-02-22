from random import randint

from classes.gem import Gem
from classes.rock import Rock
from classes.player import Player
from classes.constants import FONT_SIZE
from classes.constants import BLUE
from classes.constants import MAX_X
from classes.constants import MAX_Y
from classes.constants import WHITE
from classes.constants import RED


from shared.point import Point



class Director:
 

    def __init__(self, keyboard, video):
       
        self._keyboard_service = keyboard
        self._video_service = video

    def _add_gems(self, board):
        for _ in range(100):
            gem = Gem()
            gem.set_position(Point(randint(0, 800), randint(0, 600)))
            gem.set_font_size(FONT_SIZE)
            gem.set_color(BLUE)
            board.add_actor("gems", gem)

    def prep_game(self, board):
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
        self._add_gems(board)

        board.add_actor("player", player)
        board.add_actor("rocks", rock)
        
            
    def start_game(self, board):
        self._video_service.open_window()
        while self._video_service.is_window_open():
            self._get_inputs(board)
            self._do_updates(board)
            self._do_outputs(board)
        self._video_service.close_window()

    def _get_inputs(self, board):
        player = board.get_first_actor("player")
        velocity = self._keyboard_service.get_direction()
        player.set_velocity(velocity)        

    def _do_updates(self, board):
        player = board.get_first_actor("player")
        rocks = board.get_actors("rocks")
        gems = board.get_actors("gems")

        
        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        player.move_next(max_x, max_y)

        
    def _do_outputs(self, board):
        """Draws the actors on the screen.
        
        Args:
            board (board): The board of actors.
        """
        self._video_service.clear_buffer()
        actors = board.get_all_actors()
        self._video_service.draw_actors(actors)
        self._video_service.flush_buffer()