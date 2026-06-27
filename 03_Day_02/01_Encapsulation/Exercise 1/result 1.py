import math


class Square:
    def __init__(self, side):
        self._side = side
        self._update()

    # internal helper to keep data consistent
    def _update(self):
        self._perimeter = 4 * self._side
        self._area = self._side ** 2
        self._diagonal = self._side * math.sqrt(2)

    # getters
    def get_side(self):
        return self._side

    def get_perimeter(self):
        return self._perimeter

    def get_area(self):
        return self._area

    def get_diagonal(self):
        return self._diagonal

    # setters
    def set_side(self, new_length):
        self._side = new_length
        self._update()

    def set_perimeter(self, new_perimeter):
        self._side = new_perimeter / 4
        self._update()

    def set_area(self, new_area):
        self._side = math.sqrt(new_area)
        self._update()

    def set_diagonal(self, new_diagonal):
        self._side = new_diagonal / math.sqrt(2)
        self._update()