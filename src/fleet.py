from boat import Boat


class Fleet:

    def __init__(self, boatSizes):
        self.size = len(boatSizes)
        self.boats = []
        for size in boatSizes:
            self.boats.append(Boat(size))

    def hit(self, x, y):
        for boat in self.boats:
            if boat.hit(x, y):
                if boat.remaining == 0:
                    self.size -= 1
                return True
        return False

    def place(self, grid):
        for boat in self.boats:
            if not boat.place(grid):
                return False
        return True
