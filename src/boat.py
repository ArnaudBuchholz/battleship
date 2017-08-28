import random

class Boat:

    DIR_DOWN = 0
    DIR_UP = 1
    DIR_LEFT = 2
    DIR_RIGHT = 3

    _DIR_X = [0, 0, -1, 1]
    _DIR_Y = [1, -1, 0, 0]

    MAX_RANDOM_PLACING = 100

    def __init__(self, size):
        self.size = size

    def _place(self, grid, x, y, dir):
        dif_x = Boat._DIR_X[dir]
        dif_y = Boat._DIR_Y[dir]
        # Will simplify testing if the x, y coordinates hit the boat
        self.pos_x = []
        self.pos_y = []
        remaining = self.size
        while remaining > 0:
            grid.set(x, y, grid.BOAT)
            self.pos_x.append(x)
            self.pos_y.append(y)
            remaining -= 1
            x += dif_x
            y += dif_y

    def _placeIfPossible(self, grid, x, y, dir):
        pos_x = x
        dif_x = Boat._DIR_X[dir]
        pos_y = y
        dif_y = Boat._DIR_Y[dir]
        remaining = self.size
        try:
            while remaining > 0 and grid.get(pos_x, pos_y) == grid.EMPTY:
                remaining -= 1
                pos_x += dif_x
                pos_y += dif_y
                if remaining == 0:
                    self._place(grid, x, y, dir)
                    return True
        except:
            return False
        return False

    def _placeRandomly(self, grid):
        step = 0
        while step < Boat.MAX_RANDOM_PLACING:
            x = random.randint(0, grid.width - 1)
            y = random.randint(0, grid.width - 1)
            dir = random.randint(Boat.DIR_DOWN, Boat.DIR_RIGHT)
            if self._placeIfPossible(grid, x, y, dir):
                return True
            step += 1
        return False

    def place(self, grid, x = -1, y = -1, dir = -1):
        if x == -1 and y == -1 and dir == -1:
            return self._placeRandomly(grid)
        return self._placeIfPossible(grid, x, y, dir)

    def hit(self, x, y):
        remaining = len(self.pos_x)
        index = 0
        while index < remaining:
            if self.pos_x[index] == x and self.pos_y[index] == y:
                self.pos_x.pop(index)
                self.pos_y.pop(index)
                return True
            index += 1
        return False

    def getRemaining(self):
        return len(self.pos_x)
