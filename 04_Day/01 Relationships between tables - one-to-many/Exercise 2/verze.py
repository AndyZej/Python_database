create_comments_table = """
CREATE TABLE IF NOT EXISTS comments (
    id SERIAL,
    content TEXT,
    movies_id INT NOT NULL,
    PRIMARY KEY(id),
    FOREIGN KEY(movies_id)
    REFERENCES movies(id) ON DELETE CASCADE
);
"""

add_comments = """
INSERT INTO comments(content, movies_id) VALUES
('bol to super film', 22),
('titanic ma dojal až som plakal skvelý príbeh', 23),
('dark knight je najlepší batman film akí bol nakrútený', 24),
('forrest gump je klasika ktorú treba vidieť každý', 25),
('inception ma totalne zmiatol ale v dobrom zmysle', 26),
('krstný otec je nadčasový film odporúčam každému', 27),
('interstellar ma dostal scény vo vesmíre sú úžasné', 28),
('joker je temný ale phoenix podal fenomenálny výkon', 29),
('endgame bol skvelé vyvrcholenie celého mcu', 30),
('parasite je originálny film s nečakaným koncom', 22);
"""

query = """
SELECT *
FROM movies 
LEFT JOIN comments
ON movies.id = comments.movies_id;
"""