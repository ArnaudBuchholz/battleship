import unittest
from boat import Boat
from grid import Grid
from fleet import Fleet

class TestFleet(unittest.TestCase):

    def test_constructor(self):
        fleet = Fleet([5, 4, 3, 3, 2])
        self.assertEqual(fleet.size, 5)
        # Boats should be built
        boats = fleet.boats
        self.assertEqual(len(boats), 5)
        for boat in boats:
            self.assertIsInstance(boat, Boat)

    def test_hit(self):
        fleet = Fleet([2, 2])
        grid = Grid(10, 10)
        fleet.boats[0].place(grid, 0, 0, Boat.DIR_DOWN)
        fleet.boats[1].place(grid, 1, 0, Boat.DIR_DOWN)
        self.assertEqual(fleet.hit(9, 9), False)
        # Starts shooting down one boat
        self.assertEqual(fleet.hit(0, 0), True)
        self.assertEqual(fleet.size, 2)
        # Finish him
        self.assertEqual(fleet.hit(0, 1), True)
        self.assertEqual(fleet.size, 1)
