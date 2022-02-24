

from classes.object import Object


class Score(Object):

    def __init__(self):
        super().__init__()
        self._value = 0

    def get_actual_score(self):
        return self._value
    
    def set_actual_score(self, value):    
        self._value = value

    def print_score(self):
        self._text = f"Your Score is {self.get_actual_score()}"
