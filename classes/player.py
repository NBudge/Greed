
import sys
sys.path.append('../shared')
from shared.color import Color
from shared.point import Point

class Player:


    def _init_(self):
        self._text = ""
        self._font_size = 20
        self._color = Color(255, 255, 255)
        self._position = Point(10, 10)
        self._velocity = Point(0, 0)


    def get_position(self):
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
        x = (self._position.get_x() + self._velocity.get_x()) % max_x
        y = (self._position.get_y() + self._velocity.get_y()) % max_y
        self._position = Point(x, y)