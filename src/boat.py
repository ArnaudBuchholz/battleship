class Boat:

    DIR_DOWN = 0
    DIR_UP = 1
    DIR_LEFT = 2
    DIR_RIGHT = 3

    _DIR_X = [0, 0, -1, 1]
    _DIR_Y = [1, -1, 0, 0]

    def __init__(self, size):
        self.size = size
        self.remaining = size

    def _place(self, grid, x, y, dir):
        dif_x = Boat._DIR_X[dir]
        dif_y = Boat._DIR_Y[dir]
        # Will simplify testing if the x, y coordinates hit the boat
        self.min_x = x
        self.min_y = y
        self.max_x = x + dif_x * (self.size - 1)
        self.max_y = y + dif_y * (self.size - 1)
        remaining = self.size
        while remaining > 0:
            grid.set(x, y, grid.BOAT)
            remaining -= 1
            x += dif_x
            y += dif_y

    def place(self, grid, x, y, dir):
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

    def hit(self, x, y):
        if (x < self.min_x or x > self.max_x or y < self.min_y or y > self.max_y):
            return False
        self.remaining -= 1
        return True
