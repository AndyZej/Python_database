
# 1. Create Readers table (email must be unique)
query_1 = """
CREATE TABLE Readers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(60),
    email VARCHAR(60) UNIQUE,
    is_active BOOLEAN NOT NULL DEFAULT TRUE
);
"""

# 2. Create PublishingHouses table
query_2 = """
CREATE TABLE PublishingHouses (
    id SERIAL PRIMARY KEY,
    name VARCHAR(60),
    city VARCHAR(20),
    address VARCHAR(120)
);
"""

# 3. Create Books table with relationship to PublishingHouses
query_3 = """
CREATE TABLE Books (
    id SERIAL PRIMARY KEY,
    title VARCHAR(60),
    price DECIMAL(5, 2),
    author VARCHAR(60),
    publishing_houses_id INT,
    FOREIGN KEY (publishing_houses_id) REFERENCES PublishingHouses(id)
);
"""

# 4. Create many-to-many relationship between Readers and Books
query_4 = """
CREATE TABLE Readers_Books (
    reader_id INT,
    book_id INT,
    FOREIGN KEY (reader_id) REFERENCES Readers(id),
    FOREIGN KEY (book_id) REFERENCES Books(id),
    PRIMARY KEY (reader_id, book_id)
);
"""

# 5. Retrieve all books with price greater than 10
query_5 = """
SELECT * FROM Books
WHERE price > 10;
"""

# 6. Insert a new publishing house
query_6 = """
INSERT INTO PublishingHouses (name, city, address)
VALUES ('Super Books', 'Wilderness', '120 Main Road');
"""

# 7. Remove the book with id 12
query_7 = """
DELETE FROM Books
WHERE id = 12;
"""

# 8. Select all readers who have ever borrowed a book
query_8 = """
SELECT DISTINCT r.*
FROM Readers r
JOIN Readers_Books rb ON r.id = rb.reader_id;
"""

# 9. Deactivate user with id 2
query_9 = """
UPDATE Readers
SET is_active = FALSE
WHERE id = 2;
"""

# 10. Add date_of_birth field to Readers table
query_10 = """
ALTER TABLE Readers
ADD COLUMN date_of_birth DATE;
"""