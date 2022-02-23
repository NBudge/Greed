from classes.object import Object
from shared.point import Point
from shared.color import Color
import random

color_list = [Color(245, 45, 45),Color(45, 245, 45),Color(45, 45, 255),Color(255, 255, 255)]


class Rock(Object):
    def _init_(self):
        self.text = "o"

    def set_new(self):
        #super().__init__()
        #gem = Object()
        self.set_position(Point(random.randint(10,790), 15))
        self.set_text("o")
        self.set_font_size(20)
        self.set_color(color_list[random.randint(0,len(color_list)-1)])