from classes.object import Object
from shared.point import Point
from shared.color import Color
import random

color_list = [Color(245, 45, 45),Color(45, 245, 45),Color(45, 45, 255),Color(255, 255, 255)]


class Rock(Object):
    """ Subclass of Object 

    This class inheritent of Superclass (Object) and change some of methods for creating Gem class

    Attributes:
        _text (string): Shape of the Rock
        set_position(class): position fo the Rock
        set_font_size(int): size of the Rock
        set_color(class): color of the Rock
    """
    def __init__(self):
        """ Constructor of Object Rock. Inheritant Object class' methods
        
        Args:
        None
        """
        super().__init__()
        self._text = "o"
        self.set_position(Point(random.randint(10,790), 15))
        self.set_font_size(20)
        self.set_color(color_list[random.randint(0,len(color_list)-1)])