CREATE TABLE customers(
    customer_id BIGINT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    gender VARCHAR(10),
    email VARCHAR(50),
    phone VARCHAR(20),
    address TEXT,
    country VARCHAR(30),
    date_added TIMESTAMP NOT NULL
);



CREATE TABLE products (
    product_id INT PRIMARY KEY,
    brand VARCHAR(30) NOT NULL,
    model VARCHAR(40) NOT NULL,
    color VARCHAR(30) NOT NULL,
    [memory] FLOAT NOT NULL,
    [storage] FLOAT NOT NULL,
    rating FLOAT,
    selling_price FLOAT NOT NULL
);

CREATE TABLE salesperson (
    sales_person_id INT PRIMARY KEY,
    [name] VARCHAR(50) NOT NULL,
    age INT NOT NULL,
    gender VARCHAR(10) NOT NULL,
    position VARCHAR(30) NOT NULL,
    joining_date DATE NOT NULL,
    salary FLOAT NOT NULL
);




CREATE TABLE sales (
    sale_id BIGINT PRIMARY KEY,
    customer_id BIGINT REFERENCES customers(customer_id) ON DELETE CASCADE,
    sales_person_id INT REFERENCES salesperson(sales_person_id) ON DELETE CASCADE,
    product_id INT REFERENCES products(product_id) ON DELETE CASCADE,
    quantity INT NOT NULL,
    sale_date TIMESTAMP NOT NULL
);


DROP TABLE customers;

DROP TABLE products;

DROP TABLE sales;

DROP TABLE salesperson;