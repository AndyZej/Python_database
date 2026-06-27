CREATE_AUTHORS = """
CREATE TABLE author (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100)
);
"""

CREATE_BOOKS = """
CREATE TABLE book (
    id SERIAL PRIMARY KEY,
    isbn VARCHAR(13),
    name VARCHAR(100),
    description TEXT,
    is_loaned BOOLEAN DEFAULT FALSE
);
"""

CREATE_CLIENTS = """
CREATE TABLE client (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(100),
    last_name VARCHAR(100)
);
"""

CREATE_CATEGORIES = """
CREATE TABLE category (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100)
);
"""