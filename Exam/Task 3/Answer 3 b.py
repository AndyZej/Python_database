# 1. Readers table
query_1 = """
CREATE TABLE Readers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(60),
    email VARCHAR(60) UNIQUE,
    is_active BOOLEAN NOT NULL DEFAULT TRUE
);
"""

# 2. PublishingHouses table
query_2 = """
CREATE TABLE PublishingHouses (
    id SERIAL PRIMARY KEY,
    name VARCHAR(60),
    city VARCHAR(20),
    address VARCHAR(120)
);
"""

# 3. Books table
query_3 = """
CREATE TABLE Books (
    id SERIAL PRIMARY KEY,
    title VARCHAR(60),
    price DECIMAL(5,2),
    author VARCHAR(60),
    publishing_houses_id INT REFERENCES PublishingHouses(id)
);
"""

# 4. Readers–Books many-to-many table
query_4 = """
CREATE TABLE Readers_Books (
    reader_id INT,
    book_id INT
);
"""

# 5. Books with price > 10
query_5 = """
SELECT * FROM Books WHERE price > 10;
"""

# 6. Insert publishing house
query_6 = """
INSERT INTO PublishingHouses VALUES
(DEFAULT, 'Super Books', 'Wilderness', '120 Main Road');
"""

# 7. Delete book with id 12
query_7 = """
DELETE FROM Books WHERE id = 12;
"""

# 8. Readers who borrowed books
query_8 = """
SELECT DISTINCT reader_id FROM Readers_Books;
"""

# 9. Deactivate reader with id 2
query_9 = """
UPDATE Readers SET is_active = FALSE WHERE id = 2;
"""

# 10. Add date_of_birth column
query_10 = """
ALTER TABLE Readers ADD date_of_birth DATE;
"""