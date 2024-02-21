-- This added to primary key
ALTER TABLE transactions
AUTO_INCREMENT = 1000;

INSERT INTO transactions (amount, c_id)
VALUES (4.99, 3),
	   (2.89, 2),
       (3.38, 3),
       (4.99, 1);

SELECT * FROM transactions;