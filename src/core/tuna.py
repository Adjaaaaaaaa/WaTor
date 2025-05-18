from .fish import Fish
from .config import TUNA_REPRODUCTION_TIME

class Tuna(Fish):
    """
    Represents a Tuna in the Wa-Tor simulation.

    Tuna are prey animals that move randomly to adjacent empty cells and reproduce after a certain number of chronons.
    """
    def __init__(self, x:int, y:int, reproduction_time:int=TUNA_REPRODUCTION_TIME, planet=None)-> None:
        """
        Initializes a Tuna at a given position with a specified reproduction time.

        Args:
        x (int): X-coordinate of the Tuna on the grid.
        y (int): Y-coordinate of the Tuna on the grid.
        reproduction_time (int): Number of chronons before the Tuna can reproduce. Default is TUNA_REPRODUCTION_TIME.
        planet (Planet, optional): Reference to the simulation grid (planet).

        Returns:
        None
        """
        super().__init__(x, y, reproduction_time, planet)

    def act(self)->None:
        """
        Defines the Tuna's behavior in a single chronon:
        - Increases age.
        - Reproduces if reproduction conditions are met.
        - Moves to a random empty adjacent cell.

        Returns:
        None
        """
        self.age += 1
        self.reproduce()
        self.basic_move()
