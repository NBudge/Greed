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
        None
        """
        self._text = ""
        self._font_size = 20
        self._color = Color(255, 255, 255)
        self._position = Point(10, 10)
        self._velocity = Point(0, 0)

    def get_position(self):
        """Return the position where object should be displayed in the screen.

        Args:
            None
        """
        return self._position
    def get_text(self):
        """returns the text (object's shape).
        
        Args:
            None
        """
        return self._text
    def get_velocity(self):
        """returns the velocity of the object.
        
        Args:
            None
        """
        return self._velocity
    def set_position(self, position):
        """set velocity.
        
        Args:
            position(int,int): values of x and y
        """
        self._position = position
    def get_font_size(self):
        """returns the text size.
        
        Args:
            None
        """
        return self._font_size
    def get_color(self):
        """returns the object's color.
        
        Args:
            None
        """
        return self._color

    def set_text(self, text):
        """Set the text (object's shape).
        
        Args:
            text(int): shape of the object
        """
        self._text = text
    def set_color(self, color):
        """Set the object's color.
        
        Args:
            color(int): colors of the text
        """
        self._color = color
    def set_font_size(self, font_size):
        """set the text size.
        
        Args:
            font_size(int): size of the text
        """
        self._font_size = font_size
    def set_velocity(self, velocity):
        """set the velocity.
        
        Args:
            velocity(int): valeus of x and y
        """
        self._velocity = velocity

    def move_next(self, max_x, max_y):
        """change the position based on x and y
        
        Args:
            max_x(int) : maximum number of x
            max_y(int) : maximum number of y
        """
        # x = (self._position.get_x() + self._velocity.get_x()) % max_x
        # y = (self._position.get_y() + self._velocity.get_y()) % max_y
        self._position = Point(max_x, max_y)
