import unittest
from .src.grid import Grid

class TestGrid(unittest.TestCase):

    def test_constructor(self):
        grid = Grid(10, 10)
        self.assertEqual(grid.width, 10)
        self.assertEqual(grid.height, 10)

if __name__ == '__main__':
    unittest.main()
