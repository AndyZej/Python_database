import copy

Product = tuple[float, str]

class Cart:
    def __init__(self):
        self.products: list[Product] = []

    def add(self, price: int | float, name: str):
        self.products.append((price, name))

    def my_summary(self) -> float:
        total = 0
        for product in self.products:
            total += product[0]

        return total

    def summary(self) -> list[Product]:
        return copy.deepcopy(self.products)


class Discount20PercentCart(Cart):
    def my_summary(self) -> float:
        total = Cart.my_summary(self)
        return total * 0.8

    def summary(self) -> list[Product]:
        total: list[Product] = []
        for product in self.products:
            total.append((product[0] * 0.8, product[1]))

        return total


class Above3ProductsCheapestFreeCart(Cart):
    def summary(self) -> list[Product]:
        if len(self.products) < 4:
            return Cart.summary(self)

        cheapest = 0
        for i in range(len(self.products)):
            if self.products[i][0] < self.products[cheapest][0]:
                cheapest = i

        output = copy.deepcopy(self.products)
        output[cheapest] = (0, self.products[cheapest][1])

        return output




"""
Class Above3ProductsCheapestFreeCart
Write an Above3ProductsCheapestFreeCart class that inherits from Cart.

The summary method of the Above3ProductsCheapestFreeCart class should return a list of tuples; 
if there are more than 3 products in the list, the price of the cheapest one should be changed to zero.
"""