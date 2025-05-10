from .config import SHARK_ENERGY_GAIN,SHARK_REPRODUCTION_TIME, SHARK_INITIAL_ENERGY
from core.fish import Fish

class Shark (Fish):
    """
    creation of the predator class
    """
    def __init__(self, x, y):
        super().__init__(x, y)