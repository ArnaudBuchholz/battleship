import unittest
from player import Player
from constants import GRID_WIDTH, GRID_HEIGHT, FLEET_BOATS


class TestPlayer(unittest.TestCase):

    def test_constructor(self):
        player = Player("Player 1", GRID_WIDTH, GRID_HEIGHT, FLEET_BOATS)
        self.assertEqual(player.name, "Player 1")
        self.assertEqual(player.grid.width, GRID_WIDTH)
        self.assertEqual(player.grid.height, GRID_HEIGHT)
        self.assertEqual(player.fleet.size, len(FLEET_BOATS))
