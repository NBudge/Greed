
import sys
sys.path.append('../shared')
from shared.color import Color
from shared.point import Point

class Player:
    """The object on the board that the user will move to collect the gems.
    
    The responsibility of the actor is to get gems and avoid the rocks.

    """

    def _init_(self):
        """Constructs the Board

        Args:
            None
        """
        self._text = ""
        self._font_size = 20
        self._color = Color(255, 255, 255)
        self._position = Point(10, 10)
        self._velocity = Point(0, 0)

    def get_position(self):
        """get the position of the player

        Args:
            None
        """
        return self._position
    def get_text(self):
        """get the text that the user will move as player

        Args:
            None
        """
        return self._text
    def get_velocity(self):
        """speed of the player

        Args:
            None
        """
        return self._velocity
    def set_position(self, position):
        """set the position of the player

        Args:
            position: an object Point that will set the x,y position
        """
        self._position = position
    def get_font_size(self):
        """get the font size of the player

        Args:
            None
        """
        return self._font_size
    def get_color(self):
        """get the color of the player

        Args:
            None
        """
        return self._color

    def set_text(self, text):
        """set how the player will be look at.

        Args:
            text: the text to be display
        """
        self._text = text
    def set_color(self, color):
        """set the color of the player

        Args:
            color: a color selected for the player
        """
        self._color = color
    def set_font_size(self, font_size):
        """get the font size of the player

        Args:
            font_size: the font used on the player
        """
        self._font_size = font_size
    def set_velocity(self, velocity):
        """set the speed of the player

        Args:
            velocity: the speed that the player will move on every time the user press a key
        """
        self._velocity = velocity

    def move_next(self, max_x, max_y):
        """the new position of the player

        Args:
            max_x: the x coordinates
            max_y: the y coordinates
        """
        x = (self._position.get_x() + self._velocity.get_x()) % max_x
        y = (self._position.get_y() + self._velocity.get_y()) % max_y
        self._position = Point(x, y)