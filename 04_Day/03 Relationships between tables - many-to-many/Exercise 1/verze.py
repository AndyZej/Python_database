create_products_orders = """
CREATE TABLE IF NOT EXISTS products_orders (
        id SERIAL PRIMARY KEY,
        product_id INT NOT NULL UNIQUE,
        order_id INT NOT NULL UNIQUE,
    FOREIGN KEY(product_id)
    REFERENCES products(id) ON DELETE CASCADE,
    FOREIGN KEY(order_id)
    REFERENCES orders(id) ON DELETE CASCADE
);
"""


add_product_order_1 = """
INSERT INTO products_orders(product_id, order_id) VALUES
(1, 2),
(2, 3),
(3, 4),
(4, 5),
(5, 6),
(6, 7),
(7, 8),
(8, 9),
(9, 10),
(10, 1);

"""

query = """
SELECT * FROM orders
JOIN products_orders
ON orders.id = products_orders.order_id
JOIN products
ON products_orders.product_id = products.id;
"""

query = """
SELECT 
    orders.id AS order_id,
    orders.description AS order_description,
    products.name AS product_name,
    products.price AS product_price
FROM orders
JOIN products_orders ON orders.id = products_orders.order_id
JOIN products ON products_orders.product_id = products.id;
"""