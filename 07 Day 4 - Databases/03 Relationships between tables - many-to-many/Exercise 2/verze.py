create_screenings_table = """
CREATE TABLE IF NOT EXISTS screening (
        id SERIAL PRIMARY KEY,
        cinema_id INT NOT NULL,
        movie_id INT NOT NULL,
        datetime TIMESTAMP,
    FOREIGN KEY(cinema_id)
    REFERENCES cinemas(id) ON DELETE CASCADE,
    FOREIGN KEY(movie_id)
    REFERENCES movies(id) ON DELETE CASCADE
);
"""

add_cinemas = """
INSERT INTO cinemas (name, address, seats) VALUES
    ('CinemaCity Aupark', 'Aupark, Bratislava', 200),
    ('CinemaCity Eurovea', 'Eurovea, Bratislava', 180),
    ('Multikino Cinemax', 'Optima, Košice', 150),
    ('Palace Cinemas', 'Aupark, Žilina', 120),
    ('Kino Lumiere', 'Nám. SNP, Bratislava', 100);
"""

add_screenings = """
INSERT INTO screening (cinema_id, movie_id, datetime) VALUES
    (1, 22, '2026-06-01 16:00:00'),
    (1, 23, '2026-06-01 18:30:00'),
    (1, 24, '2026-06-01 21:00:00'),
    (2, 25, '2026-06-02 17:00:00'),
    (2, 26, '2026-06-02 19:30:00'),
    (3, 27, '2026-06-03 15:00:00'),
    (3, 28, '2026-06-03 20:00:00'),
    (4, 29, '2026-06-04 18:00:00'),
    (4, 30, '2026-06-04 20:30:00'),
    (5, 22, '2026-06-05 19:00:00');
"""