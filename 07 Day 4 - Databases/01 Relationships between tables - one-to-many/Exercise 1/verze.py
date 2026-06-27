create_opinions_table = """
CREATE TABLE IF NOT EXISTS opinions (
    id SERIAL,
    description TEXT,
    product_id INT NOT NULL,
    PRIMARY KEY(id),
    FOREIGN KEY(product_id)
    REFERENCES products(id)
);
"""


add_opinions = """
INSERT INTO opinions(description, product_id) VALUES
('mlieko bolo velmi kvalitne vidiet ze je z bio chovu', 1),
('chlieb bol cerstvy a chrumkavy presne ako z pekarne', 2),
('maslo ma vybornu chuť a kremovu konzistenciu', 3),
('vajcia boli cerstve zo dna nakupu este teplucke', 4),
('syr eidam mal prijemnu jemnu chuť hodí sa na sendvice', 5),
('jogurt bol hustý a kremovy bez zbytocneho cukru', 6),
('kuracie prsia boli cerstve a lahko sa pripravili', 7),
('ryza sa uvarila rychlo a zrna ostali pekne oddelene', 8),
('cestoviny mali skvelú texturu a dobre drzali omacku', 9),
('paradajky boli zrale a stavnate skvelé do salaту', 10);
"""

select_opinions = """
SELECT products.id, products.name, opinions.description, COUNT(opinions.description)
FROM products 
LEFT JOIN opinions
ON products.id = opinions.product_id
GROUP BY products.id, products.name, opinions.description;
"""