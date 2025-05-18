from .fish import Fish
from .config import SHARK_REPRODUCTION_TIME, SHARK_INITIAL_ENERGY, SHARK_ENERGY_GAIN
from .tuna import Tuna
import random

class Shark(Fish):
    def __init__(self, x, y, reproduction_time=SHARK_REPRODUCTION_TIME, planet=None):
        super().__init__(x, y, reproduction_time, planet)
        self.energy = SHARK_INITIAL_ENERGY

    def eat(self) -> bool:
        tuna_neighbors = [(nx, ny) for (nx, ny) in self.get_neighbors() if isinstance(self.grid[ny][nx], Tuna)]
        if tuna_neighbors:
            nx, ny = random.choice(tuna_neighbors)
            self.energy += SHARK_ENERGY_GAIN
            self.grid[ny][nx] = self
            self.grid[self.y][self.x] = None
            self.x, self.y = nx, ny
            return True
        return False

    def act(self):
        self.energy -= 1
        if self.energy <= 0:
            # meurt de faim
            self.grid[self.y][self.x] = None
            return
        ate = self.eat()
        if not ate:
            self.basic_move()
        self.reproduce()

