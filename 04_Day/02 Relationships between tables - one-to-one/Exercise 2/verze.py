create_table_payments = """

CREATE TABLE IF NOT EXISTS payments (
        id SERIAL PRIMARY KEY,
        type VARCHAR(255),
        date TIMESTAMP,
    ticket_id int NOT NULL UNIQUE,
    FOREIGN KEY(ticket_id)
    REFERENCES tickets(id) ON DELETE CASCADE
);
"""