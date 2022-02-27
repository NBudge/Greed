from shared.point import Point
from classes.object import Object

class Score(Object):
    """ Subclass of Object 

    This class inheritent of Superclass (Object) and change some of methods for creating Gem class

    Attributes:
        _value(int): number of score
        set_position(method): position fo the Score
    """

    def __init__(self):
        """ Constructor of Object Score. Inheritant Object class' methods, but also have attribute for score value.
        
        Args:
        None
        """
        self._value = 0
        super().__init__()
        self.set_position(Point(10, 2))

    def get_actual_score(self):
        """Return actual score

        Args:
            None
        """
        return self._value
    
    def set_actual_score(self, value):  
        """Set actual score
        
        Args:
            value(int) : score after calculation
        """  
        self._value = value

    def print_score(self):
        """Print actual score on the screen

        Args:
            None
        """
        self._text = f"Your Score is {self.get_actual_score()}"
