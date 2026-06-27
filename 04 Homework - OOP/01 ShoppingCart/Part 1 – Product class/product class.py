class Product:
    _next_id = 1

    def __init__(self, name, price):
        self.id = Product._next_id
        Product._next_id += 1
        self.name = name
        self.price = price