from abc import ABC, abstractmethod
import random

class Fish(ABC):
    def __init__(self, x: int, y: int, reproduction_time: int, planet=None) -> None:
        self.age = 0
        self.reproduction_time = reproduction_time
        self.x = x
        self.y = y
        self.planet = planet
        self.grid = planet.grid if planet else None
        self.energy = None  # utile pour Shark

    def set_context(self, x, y, planet):
        self.x = x
        self.y = y
        self.planet = planet
        self.grid = planet.grid

    def get_neighbors(self):
        neighbors = []
        for dx, dy in [(0,1),(0,-1),(-1,0),(1,0)]:
            nx, ny = self.x + dx, self.y + dy
            if 0 <= nx < len(self.grid[0]) and 0 <= ny < len(self.grid):
                neighbors.append((nx, ny))
        return neighbors

    def basic_move(self):
        empty_neighbors = [(nx, ny) for (nx, ny) in self.get_neighbors() if self.grid[ny][nx] is None]
        if empty_neighbors:
            nx, ny = random.choice(empty_neighbors)
            self.grid[ny][nx] = self
            self.grid[self.y][self.x] = None
            self.x, self.y = nx, ny

    def reproduce(self):
        self.age += 1
        if self.age >= self.reproduction_time:
            empty_neighbors = [(nx, ny) for (nx, ny) in self.get_neighbors() if self.grid[ny][nx] is None]
            if empty_neighbors:
                nx, ny = random.choice(empty_neighbors)
                # crée un nouveau poisson à côté
                baby = self.__class__(nx, ny, self.reproduction_time, planet=self.planet)
                self.grid[ny][nx] = baby
                self.age = 0

    @abstractmethod
    def act(self):
        pass
