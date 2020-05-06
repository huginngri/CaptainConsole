INSERT INTO manufacturer_manufacturer (name, description, logo) VALUES('Playstation', 'The best console', 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Playstation_logo_colour.svg/1200px-Playstation_logo_colour.svg.png');
INSERT INTO products_productconsole (name) VALUES('Playstation 1');
INSERT INTO products_product (name, description, price, rating, console_type_id, manufacturer_id) VALUES ('MGS1', 'The game mgs', 10.1, 4.5, 1, 1)
INSERT INTO products_productimage (image, product_id) VALUES ('https://romsemulator.net/wp-content/uploads/mnt2/images/2018/07/5139front-61287-2.jpg', 1)
INSERT INTO products_productimage (image, product_id) VALUES ('https://cdn.mos.cms.futurecdn.net/nHysFiFzH3k9jfV6VCcgb.jpg', 1)


INSERT INTO products_productimage (image, product_id) VALUES ('images/captain-console.jpg', 1)

INSERT INTO manufacturers_manufacturer (name, description) VALUES('Playstation9', 'The best console');
