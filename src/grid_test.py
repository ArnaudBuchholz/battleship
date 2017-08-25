import unittest
from grid import Grid

class TestGrid(unittest.TestCase):

    def test_constructor(self):
        grid = Grid(10, 10)
        self.assertEqual(grid.width, 10)
        self.assertEqual(grid.height, 10)

    def test_empty(self):
        grid = Grid(10, 10)
        self.assertEqual(grid.get(0, 0), Grid.EMPTY)

    def test_set(self):
        grid = Grid(10, 10)
        grid.set(5, 5, Grid.BOAT)
        self.assertEqual(grid.get(5, 5), Grid.BOAT)
        self.assertEqual(grid.get(4, 4), Grid.EMPTY)

    @unittest.expectedFailure
    def test_checkXCoordinatesMin(self):
        grid = Grid(10, 10)
        grid.get(-1, 0)

    @unittest.expectedFailure
    def test_checkXCoordinatesMax(self):
        grid = Grid(10, 10)
        grid.get(10, 0)

    @unittest.expectedFailure
    def test_checkYCoordinatesMin(self):
        grid = Grid(10, 10)
        grid.get(0, -1)

    @unittest.expectedFailure
    def test_checkYCoordinatesMax(self):
        grid = Grid(10, 10)
        grid.get(0, 10)

    def test_wasBombed(self):
        grid = Grid(10, 10)
        self.assertEqual(grid.wasBombed(5, 5), False)

    def test_wasBombed(self):
        grid = Grid(10, 10)
        self.assertEqual(grid.wasBombed(5, 5), False)

    def test_bombInWater(self):
        grid = Grid(10, 10)
        self.assertEqual(grid.bomb(5, 5), False)
        self.assertEqual(grid.wasBombed(5, 5), True)

    def test_bombOnBoat(self):
        grid = Grid(10, 10)
        grid.set(5, 5, Grid.BOAT)
        self.assertEqual(grid.bomb(5, 5), True)
        self.assertEqual(grid.wasBombed(5, 5), True)

    def test_setTwice(self):
        grid = Grid(10, 10)
        grid.set(5, 5, Grid.BOAT)
        self.assertEqual(grid.get(5, 5), Grid.BOAT)
        self.assertEqual(grid.get(4, 4), Grid.EMPTY)
        grid.set(5, 5, Grid.BOAT + Grid.BOMB)
        self.assertEqual(grid.get(5, 5), Grid.BOAT + Grid.BOMB)
        self.assertEqual(grid.get(4, 4), Grid.EMPTY)
