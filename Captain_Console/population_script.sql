INSERT INTO manufacturer_manufacturer (name, description, logo) VALUES('Playstation', 'The best console', 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Playstation_logo_colour.svg/1200px-Playstation_logo_colour.svg.png');
INSERT INTO products_productconsole (name) VALUES('Playstation 1');
INSERT INTO products_product (name, description, price, rating, console_type_id, manufacturer_id) VALUES ('MGS1', 'The game mgs', 10.1, 4.5, 1, 1)
INSERT INTO products_productimage (image, product_id) VALUES ('https://romsemulator.net/wp-content/uploads/mnt2/images/2018/07/5139front-61287-2.jpg', 1)
INSERT INTO products_productimage (image, product_id) VALUES ('https://cdn.mos.cms.futurecdn.net/nHysFiFzH3k9jfV6VCcgb.jpg', 1)
<<<<<<< HEAD
=======


>>>>>>> 9e5a64e7bd6daa6b2ea207bba0c19795f4db5159
INSERT INTO products_productimage (image, product_id) VALUES ('images/captain-console.jpg', 1)
INSERT INTO manufacturer_manufacturer (name, description, logo) VALUES('Playstation', 'The best console', 'images/captain-console');


INSERT INTO manufacturers_manufacturer(name, description, image) VALUES('Nintendo', 'Epic manufacturer', 'images/captain-console.jpg');
INSERT INTO products_productconsole (name) VALUES('Nintendo NES');
INSERT INTO products_product (name, description, price, rating, console_type_id, manufacturer_id) VALUES ('Teenage mutant ninja turtles', 'A very cool game', 10.1, 4.5, 5, 5);


INSERT INTO products_product (name, description, price, rating, console_type_id, manufacturer_id) VALUES ('Mario bros', 'A classic game', 12, 4, 5, 5);


INSERT INTO products_product (name, description, price, rating, console_type_id, manufacturer_id) VALUES ('Nintendo NES console', 'An average console', 11, 3, 5, 5);


INSERT INTO products_productimage (image, product_id) VALUES ('images/TMNT-nintendo-nes.jpg', 8);
INSERT INTO products_productimage (image, product_id) VALUES ('images/mario-bros-nintendo-nes.jpg', 11);
INSERT INTO products_productimage (image, product_id) VALUES ('images/nintendo-nes.jpg', 10)

DElETE FROM products_product WHERE id=9;

INSERT INTO manufacturers_manufacturer (name, description, image) VALUES('Playstation', 'The best manufacturer', 'images/captain-console.jpg');
INSERT INTO products_productconsole (name) VALUES('Playstation 2');
INSERT INTO products_product (name, description, price, rating, console_type_id, manufacturer_id) VALUES ('Playstation 2 console', 'Legendary console', 40.99, 4.5, 4, 4);
INSERT INTO products_product (name, description, price, rating, console_type_id, manufacturer_id) VALUES ('Spiderman - PS2', 'Legendary game', 3.79, 4.6, 4, 4);
INSERT INTO products_product (name, description, price, rating, console_type_id, manufacturer_id) VALUES ('Madagascar - PS2', 'A lovely game', 8.59, 4.8, 4, 4);
INSERT INTO products_product (name, description, price, rating, console_type_id, manufacturer_id) VALUES ('GTA - San Andreas - PS2', 'A thrilling game', 6.19, 5.0, 4, 4);

INSERT INTO products_productimage (image, product_id) VALUES ('images/ps2.jpg', 4);
INSERT INTO products_productimage (image, product_id) VALUES ('images/spiderman-ps2.jpg', 5);
INSERT INTO products_productimage (image, product_id) VALUES ('images/madagascar-ps2.jpg', 6);
INSERT INTO products_productimage (image, product_id) VALUES ('images/gta-san-andreas-ps2.jpg', 7);

INSERT INTO manufacturers_manufacturer (name, description, image) VALUES('Atari', 'The one and only', 'images/captain-console.jpg');
INSERT INTO products_productconsole (name) VALUES('Atari2600');

INSERT INTO products_product (name, description, price, rating, console_type_id, manufacturer_id) VALUES ('Atari 2600 console', 'A lovely console', 20.99, 4.5, 6, 6);
INSERT INTO products_productimage (image, product_id) VALUES ('images/atari2600.jpg', 12);

