# SQL

CREATE TABLE Categories (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50)
);

CREATE TABLE Books_Categories (
    book_id INT REFERENCES Books(id),
    category_id INT REFERENCES Categories(id),
    PRIMARY KEY (book_id, category_id)
);