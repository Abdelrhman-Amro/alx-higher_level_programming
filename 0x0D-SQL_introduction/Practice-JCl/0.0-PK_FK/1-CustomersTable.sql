-- drop TABLE customers;

-- create customers table
CREATE TABLE if not exists customers (
    c_id INT PRIMARY KEY AUTO_INCREMENT,
    f_name VARCHAR(50),
    l_name VARCHAR(50)
);

-- add some data into customers
insert into customers (f_name, l_name)
VALUES ("Fred", "Fish"),
	   ("Larry", "Lobster"),
	   ("Bubble", "Bass");

-- view table
SELECT * FROM customers;