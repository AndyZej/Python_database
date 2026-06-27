# SQL

CREATE TABLE Loans (
    customer_id INT REFERENCES Customers(id),
    book_id INT REFERENCES Books(id),
    loan_date DATE NOT NULL,
    return_date DATE DEFAULT NULL,
    PRIMARY KEY (customer_id, book_id, loan_date)
);