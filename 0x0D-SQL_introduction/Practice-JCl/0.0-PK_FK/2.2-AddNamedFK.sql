ALTER TABLE transactions
ADD CONSTRAINT fk_c_id
FOREIGN KEY(c_id) REFERENCES customers(c_id);