CREATE DATABASE products_api;
USE products_api;


CREATE TABLE products(
id INT auto_increment PRIMARY KEY,
name VARCHAR(255) NOT NULL,
description TEXT,
price DECIMAL(10, 2),
quantity INT NOT NULL
);

INSERT INTO products(name, description, price, quantity)
VALUES
('rice', 'aman rice', 3000, 100),
('oil', 'Teer', 1200, 300);

SELECT * FROM products;

SELECT * FROM products WHERE id = 1;

UPDATE products
SET name = 'atap rice',
	description = 'atap aman rice',
    price = 2500,
    quantity = 100
WHERE id = 1;

DELETE FROM products WHERE id = 2;

 
