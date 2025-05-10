
class Fish:
    """ 
    Create an abstract class Fish to represent a living entity in the ecosystem 
    (tuna or shark), with common methods.
      """
    # donne à l'entité créeé une position dans la grille
    def __init__(self, x, y):
        self.age = 0
        self.x = x
        self.y = y
        self.neighbors = []
        self.last_x = None
        self.last_y = None
        

    # retourne les déplacements possibles:
    # les directions possibles par rapport à l'entité:  droit, gauche, haut et bas (0,1), (0,-1), (-1,0),(1,0)

    def get_neighbors(self):
        self.neighbors = [(self.x,self.y+1), (self.x,self.y-1), (self.x-1,self.y),(self.x+1,self.y)]
        return self.neighbors

