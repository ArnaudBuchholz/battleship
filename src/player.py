from grid import Grid
from fleet import Fleet

class Player:

    def __init__(self, name, width, height, boats):
        self.name = name
        self.grid = Grid(width, height)
        self.fleet = Fleet(boats)
