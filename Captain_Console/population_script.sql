INSERT INTO manufacturer_manufacturer (name, logo, year_of_start) VALUES('Nestle', 'https://ceowatermandate.org/wp-content/uploads/2017/08/nestle-company-vector-logo-400x400.png', '01-01-1866');
INSERT INTO manufacturer_manufacturer (name, logo, year_of_start) VALUES('Haribo', 'http://www.logospng.com/images/182/logo-haribo-182083.png', '12-13-1920');
INSERT INTO manufacturer_manufacturer (name, logo, year_of_start) VALUES('Ferrero SpA', 'https://www.brandtld.news/wp-content/uploads/2016/05/ferrero-logo.png', '01-01-1946');
INSERT INTO manufacturer_manufacturer (name, logo, year_of_start) VALUES('Hershey Co.', 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/81/HersheyCo.svg/1280px-HersheyCo.svg.png', '02-09-1894');
INSERT INTO manufacturer_manufacturer (name, logo, year_of_start) VALUES('Mars Inc', 'https://www.intelemark.com/wp-content/uploads/MARS_incorporated_Logo.svg-640x227.png', '06-23-1911');

INSERT INTO candy_candycategory (name) VALUES('Chocolate');
INSERT INTO candy_candycategory (name) VALUES('Gummy');
INSERT INTO candy_candycategory (name) VALUES('Sour');
INSERT INTO candy_candycategory (name) VALUES('Toffee');

INSERT INTO candy_candy (name, description, price, on_sale, category_id, manufacturer_id) VALUES('KitKat', 'First launched in the UK in 1935 it has become an iconic snack bar ever since. Just unwrap the bar, break off one of the fingers and savour the deliciously smooth milk chocolate.', 4.99, false, 1, 1);
INSERT INTO candy_candy (name, description, price, on_sale, category_id, manufacturer_id) VALUES('Hershey’s Cookies n Chocolate', 'Delicous Hershey’s Milk Chocolate with crunchy little cookie pieces', 1.99, true, 1, 4);
INSERT INTO candy_candy (name, description, price, on_sale, category_id, manufacturer_id) VALUES('Ferrero Rocher', 'At the centre lies a perfectly roasted hazelnut, surrounded by a luscious, smooth filling and a delicate crisp wafer, all enveloped in creamy milk chocolate and finely chopped hazelnuts.', 2.49, false, 1, 3);
INSERT INTO candy_candy (name, description, price, on_sale, category_id, manufacturer_id) VALUES('Happy Cola', 'From America''s #1-selling Gummi Bear, try delicious Happy Cola! These two-toned gummies come in a fun bottle shape and have a delcious cola taste.', 2.99, true, 2, 2);
INSERT INTO candy_candy (name, description, price, on_sale, category_id, manufacturer_id) VALUES('Goldbears', 'HARIBO Goldbears have been the gummi candy gold standard worldwide for over 90 years. Each bag contains five fruity flavors- Lemon, Orange, Pineapple, Raspberry, and Strawberry.', 1.59, false, 2, 2);
INSERT INTO candy_candy (name, description, price, on_sale, category_id, manufacturer_id) VALUES('Fizzy Cola', 'Sour taste combines with a refreshing cola flavor in these delightful little gummies! HARIBO FIZZY COLA takes your favorite cola gummies and adds a tangy sour coating for maximum taste!', 3.49, false, 3, 2);
INSERT INTO candy_candy (name, description, price, on_sale, category_id, manufacturer_id) VALUES('Skittles', 'A variety of bite-sized chewy candies with a colorful candy shell, fans have been enjoying Skittles® candies for decades. Taste The Rainbow®.', 2.55, false, 3, 5);
INSERT INTO candy_candy (name, description, price, on_sale, category_id, manufacturer_id) VALUES('Starburst', 'Starburst candies are packed with a variety of great tasting fruit flavors and a deliciously chewy texture, to be enjoyed anytime and anywhere.', 0.99, true, 4, 5);
INSERT INTO candy_candy (name, description, price, on_sale, category_id, manufacturer_id) VALUES('Tic Tac', 'Tic Tac is a brand of small, hard mints. Refreshment to be shared!', 0.49, false, 4, 3);

INSERT INTO candy_candyimage (image, candy_id) VALUES('http://www.nestle-family.com/uploads/product/615f12a8d73e42f395addd1e68af9bdc.png', 1);
INSERT INTO candy_candyimage (image, candy_id) VALUES('https://www.kitkat.com/images/kitkat-snap.png', 1);
INSERT INTO candy_candyimage (image, candy_id) VALUES('https://theamericancandystore.co.uk/643-thickbox_default/hersheys-cookies-n-chocolate.jpg', 2);
INSERT INTO candy_candyimage (image, candy_id) VALUES('https://9044c4.medialib.edu.glogster.com/5gv8bPybSZp90oKKp5Y0/media/0f/0f96edc829ff81139d0ff34cead1d558f84ecccb/himom.png', 2);
INSERT INTO candy_candyimage (image, candy_id) VALUES('https://www.jeancoutu.com/catalog-images/888729/viewer/0/ferrero-canada-limited-ferrero-rocher-200-g.png', 3);
INSERT INTO candy_candyimage (image, candy_id) VALUES('https://talenthouse-res.cloudinary.com/image/upload/c_limit,h_1280,q_90,w_480/v1/invites/kv4pahmpydnmidlzroaj.png', 3);
INSERT INTO candy_candyimage (image, candy_id) VALUES('https://www.haribo.com/fileadmin/upload/USA/Startpage/products/cola_pack.png', 4);
INSERT INTO candy_candyimage (image, candy_id) VALUES('https://cdn.shopify.com/s/files/1/0972/7116/products/haribo-happy-cola-bulk.png?v=1459346724', 4);
INSERT INTO candy_candyimage (image, candy_id) VALUES('https://www.haribo.com/fileadmin/upload/USA/Startpage/products/gb_pack.png', 5);
INSERT INTO candy_candyimage (image, candy_id) VALUES('https://cdn.shopify.com/s/files/1/0972/7116/products/haribo-original-gold-bear-gummies.png?v=1482867150', 5);
INSERT INTO candy_candyimage (image, candy_id) VALUES('https://www.haribo.com/enUS/world/fileadmin/_processed_/4/6/csm_fizzcola-h_8c4e625740.png', 6);
INSERT INTO candy_candyimage (image, candy_id) VALUES('https://www.haribo.com/enUS/world/fileadmin/user_upload/USA/top_products/fizzy_Cola/fizzycola-pieces.jpg', 6);
INSERT INTO candy_candyimage (image, candy_id) VALUES('http://paradisealacarte.com/wp-content/uploads/2016/10/0030.png', 7);
INSERT INTO candy_candyimage (image, candy_id) VALUES('https://cdn.shopify.com/s/files/1/0743/2055/products/Skittles_medium.png?v=1461295432', 7);
INSERT INTO candy_candyimage (image, candy_id) VALUES('https://cdn.shopify.com/s/files/1/0972/7116/products/starburst-original-bar.png?v=1498406174', 8);
INSERT INTO candy_candyimage (image, candy_id) VALUES('https://cdn.shopify.com/s/files/1/0972/7116/products/starburst-theater-box.png?v=1459345159', 8);
INSERT INTO candy_candyimage (image, candy_id) VALUES('https://www.tictacuk.com/image/journal/article?img_id=22210258&t=1547468914662', 9);
INSERT INTO candy_candyimage (image, candy_id) VALUES('https://www.tictacuk.com/image/journal/article?img_id=18506308&t=1536579236701', 9);