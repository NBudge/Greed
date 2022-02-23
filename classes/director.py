from random import randint
from classes.gem import Gem
from classes.rock import Rock
import time

class Director:
 
    def __init__(self, keyboard, video):
        self._keyboard_service = keyboard
        self._video_service = video
        
    def start_game(self, board):
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
                        gem.set_new()
                        board.add_actor("gems", gem)
                    for _ in range(randint(1,2)):    
                        rock = Rock()
                        rock.set_new()
                        board.add_actor("rocks", rock)

                    last_time = time.perf_counter()
                    # print (last_time)
                self._do_updates_elements(board)

            self._do_outputs(board)
        # self._video_service.close_window()

    def _get_inputs(self, board):
        player = board.get_first_actor("player")
        velocity = self._keyboard_service.get_direction()
        player.set_velocity(velocity)        

    def _do_updates_player(self, board):
        player = board.get_first_actor("player")
        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        player.move_next(max_x, max_y)
        
    def _do_updates_elements(self, board):
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