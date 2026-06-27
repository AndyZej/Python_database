# Products table
QUERY_CREATE_PRODUCTS = """
CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    description TEXT,
    price DECIMAL(5,2)
);
"""

# Orders table
QUERY_CREATE_ORDERS = """
CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    description TEXT
);
"""

# Customers table
QUERY_CREATE_CUSTOMERS = """
CREATE TABLE customers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    surname VARCHAR(100)
);
"""