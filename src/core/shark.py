from .fish import Fish
from .config import SHARK_REPRODUCTION_TIME, SHARK_INITIAL_ENERGY, SHARK_ENERGY_GAIN
from .tuna import Tuna
import random

class Shark(Fish):
    """
    Represents a Shark in the Wa-Tor simulation.

    Sharks are predators that seek out Tuna to eat, reproduce after a set time, and die if their energy reaches zero.

    Attributes:
    energy (int): Current energy level of the shark.
    """
    def __init__(self, x:int, y:int, reproduction_time:int=SHARK_REPRODUCTION_TIME, planet=None)-> None:
        """
        Initializes a Shark at a specific position with a given reproduction time and energy level.

        Args:
        x (int): X-coordinate on the grid.
        y (int): Y-coordinate on the grid.
        reproduction_time (int): Number of chronons before the shark can reproduce.
        planet (optional): Reference to the planet/grid environment.

        Returns:
        None
        """
        super().__init__(x, y, reproduction_time, planet)
        self.energy = SHARK_INITIAL_ENERGY

    def eat(self) -> bool:
        """
        Searches for Tuna in adjacent cells and eats one if found.
        The shark gains energy and moves to the Tuna's cell.

        Returns:
        bool: True if a Tuna was eaten, False otherwise.
        """
        tuna_neighbors = [(nx, ny) for (nx, ny) in self.get_neighbors() if isinstance(self.grid[ny][nx], Tuna)]
        if tuna_neighbors:
            nx, ny = random.choice(tuna_neighbors)
            self.energy += SHARK_ENERGY_GAIN
            self.grid[ny][nx] = self
            self.grid[self.y][self.x] = None
            self.x, self.y = nx, ny
            return True
        return False

    def act(self)-> None:
        """
        Defines the behavior of the shark for a single chronon.

        The shark:
        - Loses one unit of energy.
        - Dies if energy is depleted.
        - Attempts to eat an adjacent Tuna.
        - Moves to a random empty cell if no Tuna is found.
        - Tries to reproduce if eligible.

        Returns:
        None
        """
        self.energy -= 1
        if self.energy <= 0:
            # meurt de faim
            self.grid[self.y][self.x] = None
            return
        ate = self.eat()
        if not ate:
            self.basic_move()
        self.reproduce()

