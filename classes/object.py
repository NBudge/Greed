from shared.color import Color
from shared.point import Point

class Object:
    """ Set the basic setting for the object. 

    This class will set basic setting for the text, font_size, color, position on the screen, and velocity of the object.
    This will be our Superclass so didn't get the default text (object shape)

    Attributes:
        _text (string): Shape of the text.
        _font_size (int): Size of the object.
        _color (class): Color of the object.
        _position (class): Position (where in the display) of the object.
        _velocity (class): Velocity of the object.
    """
    def __init__(self):
        """ Constructor of Object class
        
        Args:
        self._text (string): None for default.
        self._font_size (int): 20
        self._color (class): White
        self._position (class): x = 10, y = 10
        self._velocity (class): x = 0, y = 0
        """
        self._text = ""
        self._font_size = 20
        self._color = Color(255, 255, 255)
        self._position = Point(10, 10)
        self._velocity = Point(0, 0)

    def get_position(self):
        """Gets the position where object should be displayed in the screen.

        Returns:
            selef._position : value of x and y
        """
        return self._position
    def get_text(self):
        return self._text
    def get_velocity(self):
        return self._velocity
    def set_position(self, position):
        self._position = position
    def get_font_size(self):
        return self._font_size
    def get_color(self):
        return self._color

    def set_text(self, text):
        self._text = text
    def set_color(self, color):
        self._color = color
    def set_font_size(self, font_size):
        self._font_size = font_size
    def set_velocity(self, velocity):
        self._velocity = velocity

    def move_next(self, max_x, max_y):
        # x = (self._position.get_x() + self._velocity.get_x()) % max_x
        # y = (self._position.get_y() + self._velocity.get_y()) % max_y
        self._position = Point(max_x, max_y)
