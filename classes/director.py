from random import randint
from classes.gem import Gem
from classes.rock import Rock
from classes.constants import FONT_SIZE
from classes.constants import BLUE
from classes.constants import MAX_X
from classes.constants import MAX_Y
from classes.constants import WHITE
from classes.constants import RED
from shared.point import Point

import time

class Director:
    """Used to direct many aspects of the game
    
    The responsibility of the director is to help simplify and direct the flow of the game, making the main py file cleaner and easier to read

    Attributes:
        self._keyboard_service -> This imports the keyboard service created in the main py file
        self._video_service -> same but video service
    """
 
    def __init__(self, keyboard, video):
        """Constructs the director
        
        Args:
            self._keyboard_service -> This imports the keyboard service created in the main py file
            self._video_service -> same but video service
        """
        self._keyboard_service = keyboard
        self._video_service = video

    def _add_gems(self, board):
        """adds gems to the board
        
        Args:
            board: the board it places the gems on
        """
        for _ in range(100):
            gem = Gem()
            gem.set_position(Point(randint(0, 800), randint(0, 600)))
            gem.set_font_size(FONT_SIZE)
            gem.set_color(BLUE)
            board.add_actor("gems", gem)

    def prep_game(self, board):
        """sets the position for the character
        
        Args:
            board: the board it places the character on
        """
        x = int(MAX_X / 2)
        y = int(MAX_Y - 50)
        position = Point(x, y)
        
            
    def start_game(self, board):
        """starts the game and creates the main game loop
        
        Args:
            board: the board the game will be played on
        """
        self._video_service.open_window()
        last_time = 0
        while self._video_service.is_window_open():
            self._get_inputs(board)
            self._do_updates_player(board) #player
            if time.perf_counter() - 0.03 > last_time or last_time == 0:
                  #    move all gems poimt.y + 10
                board.move_all_elements_actors()        
                if time.perf_counter() - 3 > last_time or last_time == 0:
                    # print (f'Start:{last_time}')
                    for _ in range(randint(1,2)):
                        gem = Gem()
                        board.add_actor("gems", gem)
                    for _ in range(randint(1,2)):    
                        rock = Rock()
                        board.add_actor("rocks", rock)

                    last_time = time.perf_counter()
                    # print (last_time)
                self._do_updates_elements(board)

            self._do_outputs(board)
        # self._video_service.close_window()

    def _get_inputs(self, board):
        """keeps track of the inputs in the game loop
        
        Args:
            board: the board the game will be played on
        """
        player = board.get_first_actor("player")
        velocity = self._keyboard_service.get_direction()
        player.set_velocity(velocity)        

    def _do_updates_player(self, board):
        """updates and keeps track of what is happening to the player
        
        Args:
            board: the board the game will be played on
        """
        player = board.get_first_actor("player")
        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        player.move_next(max_x, max_y)
        
    def _do_updates_elements(self, board):
        """updates and keeps track of what is happening to the rocks and gems
        
        Args:
            board: the board the game will be played on
        """
        rocks = board.get_actors("rocks") 
        gems = board.get_actors("gems")
        

    def _do_outputs(self, board):
        """Draws the actors on the screen.
        
        Args:
            board (board): The board of actors.
        """
        self._video_service.clear_buffer()
        actors = board.get_all_actors()
        self._video_service.draw_actors(actors)
        self._video_service.flush_buffer()