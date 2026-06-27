class ShoppingCart:
    def __init__(self):
        self.products = {}     # {product_id: Product}
        self.quantities = {}   # {product_id: quantity}

    def add_product(self, product):
        if product.id not in self.products:
            self.products[product.id] = product
            self.quantities[product.id] = 1
        else:
            self.quantities[product.id] += 1

    def remove_product(self, product):
        if product.id in self.products:
            del self.products[product.id]
            del self.quantities[product.id]

    def change_product_quantity(self, product, new_quantity):
        if new_quantity < 0:
            raise ValueError("Quantity cannot be negative")

        if product.id not in self.products:
            return

        if new_quantity == 0:
            self.remove_product(product)
        else:
            self.quantities[product.id] = new_quantity

    def get_receipt(self):
        if not self.products:
            return "Total: 0 EUR"

        lines = []
        total_sum = 0

        for product_id, product in self.products.items():
            quantity = self.quantities[product_id]
            unit_price = product.price

            # Part 3: 30% discount for 3 or more items
            if quantity >= 3:
                unit_price *= 0.7

            total_price = unit_price * quantity
            total_sum += total_price

            lines.append(
                f"{product.name} - quantity: {quantity}, "
                f"price: {round(unit_price, 2)} EUR, "
                f"total: {round(total_price, 2)} EUR"
            )

        lines.append(f"\nTotal: {round(total_sum, 2)} EUR")
        return "\n".join(lines)