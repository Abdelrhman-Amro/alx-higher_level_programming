-- DROP TABLE transactions;

CREATE TABLE IF NOT EXISTS transactions (
    t_id INT PRIMARY KEY AUTO_INCREMENT,
    amount DECIMAL(5 , 2 ),
    c_id INT,
    FOREIGN KEY (c_id)
        REFERENCES customers (c_id)
);

select * from transactions;