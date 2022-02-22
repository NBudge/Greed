import sys
sys.path.append('../shared')
from shared.color import Color
from shared.point import Point

class Score:
    def __init__(self):
        self._text = ""
        self._font_size = 20
        self._color = Color(255, 255, 255)
        self._position = Point(10, 10)

    def get_position(self):
        return self._position
    def get_text(self):
        return self._text
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