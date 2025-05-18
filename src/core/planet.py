from .config import WIDTH, HEIGHT, NB_SHARK, NB_TUNA
from .fish import Fish
from .shark import Shark
from .tuna import Tuna
import random
class Planet:
    #création d'une grille vide
    def __init__(self):
        self.grid = [[None for _ in range (WIDTH)] for _ in range (HEIGHT)]
    
    # placer aléatoirement les poissons dans la gille

    def populate(self,x,y):
        self.grid = [[(x,y) for _ in range (WIDTH)] for _ in range (HEIGHT)]
        random.shuffle(self.grid)
        

        for _ in range (NB_TUNA):
            self.grid[x][y] = Tuna(x,y)
            
        
        for _ in range (NB_SHARK):
            self.grid[x][y] = Shark(x,y)

            







    

    
