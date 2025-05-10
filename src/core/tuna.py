from .fish import Fish
from .config import TUNA_REPRODUCTION_TIME

class Tuna(Fish):
    """ 
    creation of the prey class
    """
    def __init__(self, x, y):
        super().__init__(x, y)
