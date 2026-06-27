# 1. Add 4 new movies
ADD_MOVIES = """
INSERT INTO movies (name, description, rating) VALUES
('War of Worlds', 'Sci-fi movie about alien invasion', 8),
('Wonder Woman', 'Superhero movie', 7),
('Whiplash', 'Drama about a jazz drummer', 9),
('Wolverine', 'Action superhero movie', 7);
"""

# 2. Add one ticket for each movie
ADD_TICKETS = """
INSERT INTO tickets (quantity, price) VALUES
(2, 12.50),
(4, 18.00),
(1, 20.00),
(5, 10.00);
"""

# 3. Select movies whose names start with letter W
SELECT_MOVIES_W = """
SELECT * FROM movies
WHERE name LIKE 'W%';
"""

# 4. Select tickets with price greater than 15.30
SELECT_TICKETS_PRICE = """
SELECT * FROM tickets
WHERE price > 15.30;
"""

# 5. Select tickets with quantity greater than 3
SELECT_TICKETS_QUANTITY = """
SELECT * FROM tickets
WHERE quantity > 3;
"""