from player import Player


class Game:

    def __init__(self, grid_width, grid_height, boats):
        self.grid_width = grid_width
        self.grid_height = grid_height
        self.boats = boats
        self.players = []

    def addPlayer(self, name):
        self.players.append(Player(name, self.grid_width, self.grid_height, self.boats))
