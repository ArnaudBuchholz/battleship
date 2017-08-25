import unittest
from boat import Boat
from grid import Grid

class TestGrid(unittest.TestCase):

    def test_constructor(self):
        boat = Boat(5)
        self.assertEqual(boat.size, 5)

    def test_placingBoatDown(self):
        boat = Boat(5)
        grid = Grid(10, 10)
        # Can't
        self.assertEqual(boat.place(grid, 0, 9, boat.DIR_DOWN), False)
        self.assertEqual(grid.get(0, 9), Grid.EMPTY)
        # Can
        self.assertEqual(boat.place(grid, 0, 0, boat.DIR_DOWN), True)
        self.assertEqual(grid.get(0, 0), Grid.BOAT)
        self.assertEqual(grid.get(0, 1), Grid.BOAT)
        self.assertEqual(grid.get(0, 2), Grid.BOAT)
        self.assertEqual(grid.get(0, 3), Grid.BOAT)
        self.assertEqual(grid.get(0, 4), Grid.BOAT)
        # Can't anymore
        self.assertEqual(boat.place(grid, 0, 0, boat.DIR_DOWN), False)

    def test_placingBoatUp(self):
        boat = Boat(5)
        grid = Grid(10, 10)
        # Can't
        self.assertEqual(boat.place(grid, 0, 0, boat.DIR_UP), False)
        self.assertEqual(grid.get(0, 0), Grid.EMPTY)
        # Can
        self.assertEqual(boat.place(grid, 6, 6, boat.DIR_UP), True)
        self.assertEqual(grid.get(6, 6), Grid.BOAT)
        self.assertEqual(grid.get(6, 5), Grid.BOAT)
        self.assertEqual(grid.get(6, 4), Grid.BOAT)
        self.assertEqual(grid.get(6, 3), Grid.BOAT)
        self.assertEqual(grid.get(6, 2), Grid.BOAT)
        # Can't anymore
        self.assertEqual(boat.place(grid, 6, 6, boat.DIR_UP), False)

    def test_placingBoatLeft(self):
        boat = Boat(5)
        grid = Grid(10, 10)
        # Can't
        self.assertEqual(boat.place(grid, 0, 7, boat.DIR_LEFT), False)
        self.assertEqual(grid.get(0, 7), Grid.EMPTY)
        # Can
        self.assertEqual(boat.place(grid, 7, 7, boat.DIR_LEFT), True)
        self.assertEqual(grid.get(7, 7), Grid.BOAT)
        self.assertEqual(grid.get(6, 7), Grid.BOAT)
        self.assertEqual(grid.get(5, 7), Grid.BOAT)
        self.assertEqual(grid.get(4, 7), Grid.BOAT)
        self.assertEqual(grid.get(3, 7), Grid.BOAT)
        # Can't anymore
        self.assertEqual(boat.place(grid, 7, 7, boat.DIR_LEFT), False)

    def test_placingBoatRight(self):
        boat = Boat(5)
        grid = Grid(10, 10)
        # Can't
        self.assertEqual(boat.place(grid, 9, 2, boat.DIR_RIGHT), False)
        self.assertEqual(grid.get(9, 2), Grid.EMPTY)
        # Can
        self.assertEqual(boat.place(grid, 2, 2, boat.DIR_RIGHT), True)
        self.assertEqual(grid.get(2, 2), Grid.BOAT)
        self.assertEqual(grid.get(3, 2), Grid.BOAT)
        self.assertEqual(grid.get(4, 2), Grid.BOAT)
        self.assertEqual(grid.get(5, 2), Grid.BOAT)
        self.assertEqual(grid.get(6, 2), Grid.BOAT)
        # Can't anymore
        self.assertEqual(boat.place(grid, 0, 2, boat.DIR_RIGHT), False)

    def test_hit(self):
        boat = Boat(5)
        grid = Grid(10, 10)
        self.assertEqual(boat.place(grid, 2, 2, boat.DIR_RIGHT), True)
        self.assertEqual(boat.remaining, 5)
        # Miss
        self.assertEqual(boat.hit(1, 2), False)
        self.assertEqual(boat.hit(2, 1), False)
        self.assertEqual(boat.hit(2, 3), False)
        self.assertEqual(boat.hit(7, 2), False)
        # Hit
        self.assertEqual(boat.hit(2, 2), True)
        self.assertEqual(boat.remaining, 4)



