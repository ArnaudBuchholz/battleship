class Grid:

    EMPTY = 0
    BOAT = 2
    BOMB = 1

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self._cells = []

    def _at(self, x, y):
        if x < 0 or x >= self.width:
            raise Exception("x out of range")
        if y < 0 or y >= self.height:
            raise Exception("y out of range")
        return y * self.width + x

    def get(self, x, y):
        at = self._at(x, y)
        if at >= len(self._cells):
            return Grid.EMPTY
        return self._cells[at]

    def set(self, x, y, value):
        at = self._at(x, y)
        while at >= len(self._cells):
            self._cells.append(Grid.EMPTY)
        self._cells[at] = value

    def wasBombed(self, x, y):
        value = self.get(x, y)
        return value % 2 == 1

    def bomb(self, x, y):
        value = self.get(x, y)
        if value % 2 == 0:
            self.set(x, y, value + Grid.BOMB)
        return value > Grid.BOMB
