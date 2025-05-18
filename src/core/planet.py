from .config import WIDTH, HEIGHT, NB_TUNA, NB_SHARK, TUNA_REPRODUCTION_TIME, SHARK_REPRODUCTION_TIME
from .tuna import Tuna
from .shark import Shark
import random

class Planet:
    def __init__(self):
        self.grid = [[None for _ in range(WIDTH)] for _ in range(HEIGHT)]

    def populate(self):
        # place NB_TUNA thons aléatoirement
        empty_cells = [(x, y) for y in range(HEIGHT) for x in range(WIDTH)]
        random.shuffle(empty_cells)

        for _ in range(NB_TUNA):
            if empty_cells:
                x, y = empty_cells.pop()
                tuna = Tuna(x, y, TUNA_REPRODUCTION_TIME, planet=self)
                self.grid[y][x] = tuna

        for _ in range(NB_SHARK):
            if empty_cells:
                x, y = empty_cells.pop()
                shark = Shark(x, y, SHARK_REPRODUCTION_TIME, planet=self)
                self.grid[y][x] = shark

            







    

    
