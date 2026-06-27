bread = Product('Bread', 2.70)
ham = Product('Ham', 8.40)
cheese = Product('Cheese', 4.40)
chives = Product('Chives', 1.50)
pepper = Product('Pepper', 2.35)

cart = ShoppingCart()

cart.add_product(bread)
cart.add_product(bread)
cart.add_product(bread)
cart.add_product(pepper)
cart.add_product(chives)
cart.change_product_quantity(pepper, 2)

cart.remove_product(bread)

print(cart.get_receipt())