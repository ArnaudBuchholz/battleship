import unittest
from game import Game
from constants import GRID_WIDTH, GRID_HEIGHT, FLEET_BOATS


class TestGame(unittest.TestCase):

    def test_constructor(self):
        game = Game(GRID_WIDTH, GRID_HEIGHT, FLEET_BOATS)
        game.addPlayer("Player 1")
        self.assertEqual(game.players[0].name, "Player 1")
        self.assertEqual(game.players[0].grid.width, GRID_WIDTH)
        self.assertEqual(game.players[0].grid.height, GRID_HEIGHT)
        self.assertEqual(game.players[0].fleet.size, len(FLEET_BOATS))
