class Director:
 

    def __init__(self, keyboard, video):
       
        self._keyboard_service = keyboard
        self._video_service = video
        
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