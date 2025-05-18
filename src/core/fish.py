from abc import ABC, abstractmethod
import random

class Fish(ABC):
    """
    Abstract base class representing a generic fish entity in the Wa-Tor simulation.

    Attributes:
    x (int): X-coordinate of the fish on the grid.
    y (int): Y-coordinate of the fish on the grid.
    reproduction_time (int): Number of chronons before the fish can reproduce.
    age (int): Current age of the fish (in chronons).
    planet: Reference to the simulation world (Planet object).
    grid: 2D list representing the simulation grid.
    
    """
    def __init__(self, x: int, y: int, reproduction_time: int, planet=None) -> None:

        """
        Initializes a fish object with its position, reproduction timer, and optional planet.

        Args:
        x (int): X-coordinate on the grid.
        y (int): Y-coordinate on the grid.
        reproduction_time (int): Time before reproduction.
        planet: Reference to the planet/world object containing the grid.
        """
        self.age = 0
        self.reproduction_time = reproduction_time
        self.x = x
        self.y = y
        self.planet = planet
        self.grid = planet.grid if planet else None
       

    def set_context(self, x, y, planet)-> None:
        """
        Updates the fish's position and environment.

        Args:
        x (int): New X-coordinate.
        y (int): New Y-coordinate.
        planet: Reference to the planet/world object.
        """
        self.x = x
        self.y = y
        self.planet = planet
        self.grid = planet.grid

    def get_neighbors(self)-> list[tuple[int, int]]:
        """
        Retrieves the coordinates of the four adjacent neighbors.

        Returns:
        list[tuple[int, int]]: List of valid neighbor coordinates within grid bounds.
        """
        neighbors = []
        for dx, dy in [(0,1),(0,-1),(-1,0),(1,0)]:
            nx, ny = self.x + dx, self.y + dy
            if 0 <= nx < len(self.grid[0]) and 0 <= ny < len(self.grid):
                neighbors.append((nx, ny))
        return neighbors

    def basic_move(self)-> None:
        """
        Moves the fish to a randomly selected adjacent empty cell, if any.

        Returns:
        None
        """
        empty_neighbors = [(nx, ny) for (nx, ny) in self.get_neighbors() if self.grid[ny][nx] is None]
        if empty_neighbors:
            nx, ny = random.choice(empty_neighbors)
            self.grid[ny][nx] = self
            self.grid[self.y][self.x] = None
            self.x, self.y = nx, ny

    def reproduce(self)-> None:
        """
        Attempts to reproduce if the fish has reached its reproduction age.
        Spawns a new fish in an adjacent empty cell, if available.

        Returns:
        None
        """
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
        """
        Defines the behavior of the fish at each simulation step.
        Must be implemented by subclasses.

        Returns:
        None
        """
        pass