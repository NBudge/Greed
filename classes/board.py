from ctypes.wintypes import RGB
from shared.color import Color

class Board:
    """The board on which the game is player
    
    The responsibility of the board is to provide a grid layout on which the objects (players gems and rocks) can move on

    """

    def __init__(self):
        """Constructs the Board

        Args:
            None
        """
        self._actors = {}
        self._score = ""

    def add_score(self, score):
        """Constructs the director
        
        Args:
            score: the amount of score to add
        """
        self._score = score

    def add_actor(self, group, actor):
        """adds in the actors into a list
        
        Args:
            group: location of actor
            actor: what actor is being added
        """
        if not group in self._actors.keys():
            self._actors[group] = []
            
        if not actor in self._actors[group]:
            self._actors[group].append(actor)

    def get_actors(self, group):
        """returns actors
        
        Args:
            group: location of actor
        """
        results = []
        if group in self._actors.keys():
            results = self._actors[group].copy()
        return results
    
    def get_all_actors(self):
        """returns all actors
        
        Args:
            none
        """
        results = []
        for group in self._actors:
            results.extend(self._actors[group])
        return results

    def get_first_actor(self, group):
        """returns the first actor
        
        Args:
            group: location of actor
        """
        result = None
        if group in self._actors.keys():
            result = self._actors[group][0]
        return result
    def move_all_elements_actors(self):
        """moves rocks and gems and does the collision detection and add of substract poinst from the score.
        
        Args:
            none
        """
        player_x = 0
        player_y = 0
        banner = self.get_first_actor("banner")
        
        for actor in self._actors.items():
            if actor[0] == "gems" or actor[0] == "rocks":
                for element in actor[1]:
                    player_x = self._actors["player"][0]._position._x
                    player_y = self._actors["player"][0]._position._y

                    if player_x in range(element._position._x - 10, element._position._x + 10) and player_y in range(element._position._y - 5, element._position._y + 5):
                        # print("bingo")
                        element.set_color(Color(0, 0, 0))
                        if actor[0] == "gems":
                            banner.set_actual_score(banner.get_actual_score() + 100)
                        elif actor[0] == "rocks":
                            banner.set_actual_score(banner.get_actual_score() - 100)
                        actor[1].remove(element)
                        banner.print_score()
                            
                    if element._position._y + 5 >= 590:
                        actor[1].remove(element)
                    else:
                        element.move_next(element._position._x,element._position._y + 5)
                    

    def remove_actor(self, group, actor):
        """removes actor from the list
        
        Args:
            group: location of actor
            actor: actor to be removed
        """
        if group in self._actors:
            self._actors[group].remove(actor)