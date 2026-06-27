-- Authors → Books (one-to-many)
ALTER TABLE Books
ADD COLUMN author_id INT REFERENCES Authors(id);


-- Books ↔ Categories (many-to-many)
CREATE TABLE Categories (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50)
);

CREATE TABLE Books_Categories (
    book_id INT REFERENCES Books(id),
    category_id INT REFERENCES Categories(id),
    PRIMARY KEY (book_id, category_id)
);


-- Customers ↔ Books (many-to-many with extra fields)
CREATE TABLE Loans (
    customer_id INT REFERENCES Customers(id),
    book_id INT REFERENCES Books(id),
    loan_date DATE NOT NULL,
    return_date DATE DEFAULT NULL,
    PRIMARY KEY (customer_id, book_id, loan_date)
);