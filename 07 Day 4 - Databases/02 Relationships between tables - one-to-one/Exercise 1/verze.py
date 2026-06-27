create_table_client_address = """
CREATE TABLE IF NOT EXISTS customer_address (
    id SERIAL,
    city VARCHAR(255) NOT NULL,
    street VARCHAR(255) NOT NULL,
    house_number VARCHAR(30) NOT NULL,
    customer_id int NOT NULL UNIQUE,
    PRIMARY KEY(id),
    FOREIGN KEY(customer_id)
    REFERENCES customers(id) ON DELETE CASCADE
);
"""


add_client_address_1 = """
INSERT INTO customer_address(city, street, house_number, customer_id) VALUES
('Brno', 'Česká', '23/12', 1),
('Bratislava', 'Hlavná', '15/3', 2),
('Košice', 'Námestie slobody', '8/1', 3),
('Praha', 'Wenceslasovo námestie', '42/7', 4),
('Žilina', 'Mariánske námestie', '11/5', 5),
('Nitra', 'Štefánikova', '33/9', 6),
('Banská Bystrica', 'Námestie SNP', '6/2', 7),
('Trenčín', 'Mierové námestie', '19/4', 8),
('Trnava', 'Hlavná', '27/6', 9),
('Poprad', 'Námestie sv. Egídia', '5/8', 10);
"""