# 1. Create Opinions table (one-to-many with Products)
query_1 = """
CREATE TABLE Opinions (
    id SERIAL PRIMARY KEY,
    description VARCHAR(255),
    product_id INT REFERENCES Products(id)
);
"""

# 2. Add opinions to existing products
query_2 = """
INSERT INTO Opinions (description, product_id)
VALUES ('Very good quality', 1);
"""

query_3 = """
INSERT INTO Opinions (description, product_id)
VALUES ('Worth the price', 1);
"""

query_4 = """
INSERT INTO Opinions (description, product_id)
VALUES ('Poor durability', 2);
"""

# 3. Retrieve all opinions for all products
query_5 = """
SELECT p.name, o.description
FROM Products p
JOIN Opinions o ON p.id = o.product_id;
"""

# 4. Retrieve opinions for a specific product
query_6 = """
SELECT o.description
FROM Opinions o
WHERE o.product_id = 1;
"""