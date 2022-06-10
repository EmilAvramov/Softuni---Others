CREATE SCHEMA gamebar;
GO;
USE gamebar;

-- 1

CREATE TABLE employees (
    id INT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL
);

CREATE TABLE categories (
    id INT PRIMARY KEY,
    name VARCHAR(50) NOT NULL
);

CREATE TABLE products (
    id INT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    category_id INT NOT NULL
);

-- 2

INSERT INTO employees (id, first_name, last_name)
VALUES ('1', 'John', 'Doe');

INSERT INTO employees (id, first_name, last_name)
VALUES ('2', 'Merry', 'Doe');

INSERT INTO employees (id, first_name, last_name)
VALUES ('3', 'Mark', 'Doe');

-- 3

ALTER TABLE employees 
ADD COLUMN middle_name VARCHAR(50);

-- 4

ALTER TABLE employees
MODIFY middle_name VARCHAR(100);

-- 5

ALTER TABLE products
ADD FOREIGN KEY (category_id)
REFERENCES categories (id)
