from abc import ABC
import random
class Fish(ABC):
    """ 
     Create an abstract class Fish to represent a living entity in the ecosystem 
     (tuna or shark), with common methods.

    """
    reproduction_time: int = 0
    age: int = 0
   
    # donne à l'entité créeé une position dans la grille
    def __init__(self, x: int, y:int) -> None:
        self.x = x
        self.y = y
        self.neighbors = []
        self.last_x = None
        self.last_y = None
       
        

    # retourne les déplacements possibles: les directions possibles par rapport à l'entité:  droit, gauche, haut et bas (0,1), (0,-1), (-1,0),(1,0)

    def get_neighbors(self) -> list[tuple]:
        self.neighbors = [(self.x,self.y+1), (self.x,self.y-1), (self.x-1,self.y),(self.x+1,self.y)]
        return self.neighbors
    
    # placement des poissons à la nouvelle position après 
    def basic_move(self):
        neighbors = self.get_neighbors()
        empty_neighbors = [(nx,ny) for (nx,ny) in neighbors if self.grid[nx][ny] is None]
        random.choice(empty_neighbors)
        if empty_neighbors:
            self.x, self.y = self.nx, self.ny
            self.grid[nx][ny] = self
            self.grid[x][y] is None
            



       
