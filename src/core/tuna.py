from .fish import Fish
from .config import TUNA_REPRODUCTION_TIME

class Tuna(Fish):
    def __init__(self, x, y, reproduction_time=TUNA_REPRODUCTION_TIME, planet=None):
        super().__init__(x, y, reproduction_time, planet)

    def act(self):
        self.age += 1
        self.reproduce()
        self.basic_move()
