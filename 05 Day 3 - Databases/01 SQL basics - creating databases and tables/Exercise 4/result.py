# Drop database if it already exists
DROP_DB = "DROP DATABASE IF EXISTS cinemas_db;"

# Create database
CREATE_DB = "CREATE DATABASE cinemas_db;"

# Cinemas table
CREATE_CINEMAS = """
CREATE TABLE cinemas (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    address VARCHAR(200)
);
"""

# Movies table
CREATE_MOVIES = """
CREATE TABLE movies (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    description TEXT,
    rating INT
);
"""

# Tickets table
CREATE_TICKETS = """
CREATE TABLE tickets (
    id SERIAL PRIMARY KEY,
    quantity INT,
    price DECIMAL(6,2)
);
"""

# Payments table
CREATE_PAYMENTS = """
CREATE TABLE payments (
    id SERIAL PRIMARY KEY,
    type VARCHAR(50),
    date DATE
);
"""