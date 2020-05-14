INSERT INTO manufacturer_manufacturer (name, description, logo) VALUES('Playstation', 'The best console', 'https://upload.wikimedia.org/wikipedia/commons/thumb/4/4e/Playstation_logo_colour.svg/1200px-Playstation_logo_colour.svg.png');
INSERT INTO products_productconsole (name) VALUES('Playstation 1');
INSERT INTO products_product (name, description, price, rating, console_type_id, manufacturer_id) VALUES ('MGS1', 'The game mgs', 10.1, 4.5, 1, 1)
INSERT INTO products_productimage (image, product_id) VALUES ('https://romsemulator.net/wp-content/uploads/mnt2/images/2018/07/5139front-61287-2.jpg', 1)
INSERT INTO products_productimage (image, product_id) VALUES ('https://cdn.mos.cms.futurecdn.net/nHysFiFzH3k9jfV6VCcgb.jpg', 1)

INSERT INTO products_productimage (image, product_id) VALUES ('images/captain-console.jpg', 1)

INSERT INTO manufacturer_manufacturer (name, description, logo) VALUES('Playstation', 'The best console', 'images/captain-console');


INSERT INTO manufacturers_manufacturer(name, description, image) VALUES('Nintendo', 'Epic manufacturer', 'images/captain-console.jpg');
INSERT INTO products_productconsole (name) VALUES('Nintendo NES');
INSERT INTO products_product (name, description, price, rating, console_type_id, manufacturer_id) VALUES ('Teenage mutant ninja turtles', 'A very cool game', 10.1, 4.5, 5, 5);


INSERT INTO products_product (name, description, price, rating, console_type_id, manufacturer_id) VALUES ('Mario bros', 'A classic game', 12, 4, 5, 5);

UPDATE products_product SET rating = 5, review_count = 2 WHERE id = 44 ;
INSERT INTO products_product (name, description, price, rating, console_type_id, manufacturer_id) VALUES ('Nintendo NES console', 'An average console', 11, 3, 5, 5);


INSERT INTO products_productimage (image, product_id) VALUES ('images/TMNT-nintendo-nes.jpg', 8);
INSERT INTO products_productimage (image, product_id) VALUES ('images/mario-bros-nintendo-nes.jpg', 11);
INSERT INTO products_productimage (image, product_id) VALUES ('images/nintendo-nes.jpg', 10)

DELETE FROM auth_user WHERE id>0 ;

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
DELETE FROM consoles_console where id =6
DELETE FROM manufacturers_manufacturer where id =4
TRUNCATE Table products_product CASCADE ;
TRUNCATE Table consoles_console CASCADE ;
TRUNCATE Table manufacturers_manufacturer CASCADE ;
TRUNCATE Table django_migrations CASCADE ;


CREATE TABLE products_productconsole (
    PersonID int,
    LastName varchar(255),
    FirstName varchar(255),
    Address varchar(255),
    City varchar(255)
);

INSERT INTO manufacturers_manufacturer (name, description, image) VALUES('Playstation', 'The best manufacturer', 'images/captain-console.jpg');
INSERT INTO consoles_console (name, manufacturer_id) VALUES('Playstation 2', 1);
INSERT INTO products_product (name, description, price, rating, console_type_id, manufacturer_id, type) VALUES ('Playstation 2 console', 'Legendary console', 40.99, 4.5, 1, 1, 'console');
INSERT INTO products_product (name, description, price, rating, console_type_id, manufacturer_id, type) VALUES ('Spiderman - PS2', 'Legendary game', 3.79, 4.6, 1, 1, 'game');
INSERT INTO products_product (name, description, price, rating, console_type_id, manufacturer_id, type) VALUES ('Madagascar - PS2', 'A lovely game', 8.59, 4.8, 1, 1, 'game');
INSERT INTO products_product (name, description, price, rating, console_type_id, manufacturer_id, type) VALUES ('GTA - San Andreas - PS2', 'A thrilling game', 6.19, 5.0, 1, 1, 'game');

INSERT INTO products_productimage (image, product_id) VALUES ('images/ps2.jpg', 1);
INSERT INTO products_productimage (image, product_id) VALUES ('images/spiderman-ps2.jpg', 2);
INSERT INTO products_productimage (image, product_id) VALUES ('images/madagascar-ps2.jpg', 3);
INSERT INTO products_productimage (image, product_id) VALUES ('images/gta-san-andreas-ps2.jpeg', 4);

INSERT INTO products_productimage (image, product_id) VALUES ('images/ps2.jpg', 1);
INSERT INTO products_productimage (image, product_id) VALUES ('images/spiderman-ps2.jpg', 2);
INSERT INTO products_productimage (image, product_id) VALUES ('images/madagascar-ps2.jpg', 3);
INSERT INTO products_productimage (image, product_id) VALUES ('images/gta-san-andreas-ps2.jpeg', 4);

INSERT INTO products_productimage (image, product_id) VALUES ('images/madagascar1.jpeg', 3);
INSERT INTO products_productimage (image, product_id) VALUES ('images/gta1jpeg', 4);
INSERT INTO products_productimage (image, product_id) VALUES ('images/gta2jpeg', 8);
INSERT INTO products_productimage (image, product_id) VALUES ('images/mariobros.jpeg', 7);
INSERT INTO products_productimage (image, product_id) VALUES ('images/mariobros2.jpeg', 8);
INSERT INTO products_productimage (image, product_id) VALUES ('images/nintendo_nes.jpeg', 8);
INSERT INTO products_productimage (image, product_id) VALUES ('images/nintendo_nes.png', 8);

INSERT INTO manufacturers_manufacturer (name, description, image) VALUES('Atari', 'The one and only', 'images/atari-logo.jpg');
INSERT INTO consoles_console (name, manufacturer_id) VALUES('Atari2600', 2);

INSERT INTO products_product (name, description, price, rating, console_type_id, manufacturer_id, type) VALUES ('Atari 2600 console', 'A lovely console', 20.99, 4.5, 2, 2, 'console');
INSERT INTO products_productimage (image, product_id) VALUES ('images/atari2600.jpg', 5);

DELETE FROM products_product WHERE id=26;

INSERT INTO manufacturers_manufacturer(name, description, image) VALUES('Nintendo', 'Epic manufacturer', 'images/nintendo-logo.jpg');
INSERT INTO consoles_console (name, manufacturer_id) VALUES('Nintendo NES', 3);
INSERT INTO products_product (name, description, price, rating, console_type_id, manufacturer_id, type, stock, discount, on_sale,discount_price) VALUES ('Teenage mutant ninja turtles', 'A very cool game', 10.1, 4.5, 10, 10, 'game', 10, 10, True, 10);


INSERT INTO products_product (name, description, price, rating, console_type_id, manufacturer_id, type) VALUES ('Mario bros', 'A classic game', 12, 4, 3, 3, 'game');


INSERT INTO products_product (name, description, price, rating, console_type_id, manufacturer_id, type) VALUES ('Nintendo NES console', 'An average console', 11, 3, 3, 3, 'console');


INSERT INTO products_productimage (image, product_id) VALUES ('images/TMNT-nintendo-nes.jpg', 8);
INSERT INTO products_productimage (image, product_id) VALUES ('images/mario-bros-nintendo-nes.jpg', 8);
INSERT INTO products_productimage (image, product_id) VALUES ('images/nintendo-nes.jpg', 8);

INSERT INTO auth_user (id, password, username, is_superuser, first_name, last_name, email, is_staff, is_active, date_joined) VALUES (10, 'super', 'admin', True, 'super', 'user', 'super@user.com', False, True, '2020-05-12 23:45:51.286803');

TRUNCATE TABLE orders_orderproduct;
TRUNCATE TABLE orders_orderproduct CASCADE ;
TRUNCATE TABLE orders_order CASCADE ;
TRUNCATE TABLE orders_billing CASCADE ;
TRUNCATE TABLE orders_payment CASCADE ;

UPDATE  users_payment SET card_number='1234123443214321' WHERE id<1000;
UPDATE  users_payment SET exp_date='12/24' WHERE id<1000;
UPDATE  users_payment SET cvc='123' WHERE id<1000;

DELETE FROM manufacturers_manufacturer WHERE id=13 or id =14;

