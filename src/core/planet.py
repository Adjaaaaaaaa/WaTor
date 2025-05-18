from .config import WIDTH, HEIGHT, NB_TUNA, NB_SHARK, TUNA_REPRODUCTION_TIME, SHARK_REPRODUCTION_TIME
from .tuna import Tuna
from .shark import Shark
import random

class Planet:
    """
    Represents the simulation world as a 2D toroidal grid populated with Tuna and Sharks.

    Attributes:
    grid : 2D list representing the simulation grid. 
    Each cell may contain a Tuna, Shark, or None.
    """
    def __init__(self)-> None:
        """
        Initializes the planet with an empty grid based on the configured WIDTH and HEIGHT.

        Returns:
        None
        """
        self.grid = [[None for _ in range(WIDTH)] for _ in range(HEIGHT)]

    def populate(self)-> None:
        """
        Populates the grid randomly with Tuna and Shark instances based on
        configuration values (NB_TUNA and NB_SHARK).

        Tuna and Sharks are created with their respective reproduction times and
        assigned to random empty positions in the grid.

        Returns:
        None
        """
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

            







    

    
