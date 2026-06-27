# Insert data into products
INSERT_PRODUCTS = """
INSERT INTO products (name, description, price) VALUES
('Laptop', '15-inch business laptop', 3499.99),
('Mouse', 'Wireless optical mouse', 79.99),
('Keyboard', 'Mechanical keyboard', 299.50);
"""

# Insert data into customers
INSERT_CUSTOMERS = """
INSERT INTO customers (name, surname) VALUES
('John', 'Smith'),
('Anna', 'Brown'),
('Mark', 'Taylor');
"""

# Insert data into orders
INSERT_ORDERS = """
INSERT INTO orders (description) VALUES
('Order for office equipment'),
('Order for accessories'),
('Order for computer parts');
"""