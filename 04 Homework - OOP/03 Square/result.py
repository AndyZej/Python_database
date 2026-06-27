import math

class Square:
    def __init__(self, side):
        self._side = side

    # ----- existing methods -----
    def get_side(self):
        return self._side

    def set_side(self, side):
        self._side = side

    def get_area(self):
        return self._side ** 2

    def set_area(self, area):
        self._side = math.sqrt(area)

    def get_perimeter(self):
        return self._side * 4

    def set_perimeter(self, perimeter):
        self._side = perimeter / 4

    def get_diagonal(self):
        return self._side * math.sqrt(2)

    def set_diagonal(self, diagonal):
        self._side = diagonal / math.sqrt(2)

    # ----- properties -----
    @property
    def side(self):
        return self.get_side()

    @side.setter
    def side(self, value):
        self.set_side(value)

    @property
    def area(self):
        return self.get_area()

    @area.setter
    def area(self, value):
        self.set_area(value)

    @property
    def perimeter(self):
        return self.get_perimeter()

    @perimeter.setter
    def perimeter(self, value):
        self.set_perimeter(value)

    @property
    def diagonal(self):
        return self.get_diagonal()

    @diagonal.setter
    def diagonal(self, value):
        self.set_diagonal(value)