CREATE SCHEMA minions;
GO
USE minions;

-- 1

CREATE TABLE minions (
    id INT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    age INT NOT NULL
);

CREATE TABLE towns (
    town_id INT PRIMARY KEY,
    name VARCHAR(50) NOT NULL
);

-- 2

ALTER TABLE towns
RENAME COLUMN town_id to id;

ALTER TABLE minions
ADD COLUMN town_id INT NOT NULL;

ALTER TABLE minions
ADD FOREIGN KEY (town_id)
REFERENCES towns (id);

-- 3
INSERT INTO towns (id, name)
VALUES (1, "Sofia"), (2, "Plovdiv"), (3, "Varna");

INSERT INTO minions (id, name, age, town_id)
VALUES 
(1, "Kevin", 22, 1), 
(2, "Bob", 15, 3), 
(3, "Steward", NULL, 2);

-- 4
DELETE FROM minions;

-- 5
DROP TABLE minions;
DROP TABLE towns;

-- 6
CREATE TABLE people (
    id INT AUTO_INCREMENT,
    name NVARCHAR(200) NOT NULL,
    picture VARBINARY(2000),
    height REAL(3, 2),
    weight NUMERIC(5, 2),
    gender ENUM('m', 'f') NOT NULL,
    birthdate DATE NOT NULL,
    biography NVARCHAR(8000),
    PRIMARY KEY (id)
);

INSERT INTO people
(name, gender, birthdate)
VALUES
(
       'First Name',
       'M',
       '2000-01-01'
),
(
       'Second Name',
       'F',
       '2001-05-03'
),
(
       'Third Name',
       'F',
       '2005-07-08'
),
(
       'Fourth Name',
       'F',
       '2007-03-05'
),
(
       'Fifth Name',
       'M',
       '2003-08-09'
);

-- 7

CREATE TABLE users (
    id BIGINT AUTO_INCREMENT NOT NULL,
    username VARCHAR(30) NOT NULL UNIQUE,
    password VARCHAR(26) NOT NULL,
    profile_picture VARBINARY(8000),
    last_login_time TIME,
    is_deleted BIT,
    PRIMARY KEY (id)
);


INSERT INTO users 
(username, password) 
VALUES 
("John Doe", "aoe"), 
("Mike Doe", "m_doe"), 
("Jane Doe", "jdoe"),
("Nicky Doe", "ane"), 
("Nana Doe", "n_doe");

-- 8
ALTER TABLE users
DROP PRIMARY KEY,
ADD CONSTRAINT pk_users PRIMARY KEY (id, username);

-- 9
ALTER TABLE users
MODIFY last_login_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP;

-- 10
ALTER TABLE users
DROP PRIMARY KEY,
ADD CONSTRAINT pk_person PRIMARY KEY(id),
ADD CONSTRAINT un_users UNIQUE(username);

-- 11
CREATE SCHEMA movies;
GO;
USE movies;

CREATE TABLE directors (
    id INT AUTO_INCREMENT NOT NULL,
    director_name NVARCHAR(50) NOT NULL,
    notes NVARCHAR(200),
    PRIMARY KEY (id)
);

CREATE TABLE genres (
    id INT AUTO_INCREMENT NOT NULL,
    genre_name NVARCHAR(50) NOT NULL,
    notes NVARCHAR(200),
    PRIMARY KEY (id)
);

CREATE TABLE categories (
    id INT AUTO_INCREMENT NOT NULL,
    category_name NVARCHAR(50) NOT NULL,
    notes NVARCHAR(200),
    PRIMARY KEY (id)
);

CREATE TABLE movies (
    id INT AUTO_INCREMENT NOT NULL,
    title NVARCHAR(50) NOT NULL,
    director_id INT,
    copyright_year DATE,
    length NVARCHAR(20),
    genre_id INT,
    category_id INT,
    rating INT,
    notes NVARCHAR(200),
    PRIMARY KEY (id)
);

INSERT INTO directors (director_name)
VALUES ("Mike"), ("Smith"), ("Robert"), ("Samantha"), ("Angela");

INSERT INTO genres (genre_name)
VALUES ("Drama"), ("Horror"), ("Thriller"), ("Sci-Fi"), ("Action");

INSERT INTO categories (category_name)
VALUES ("For Kids"), ("Over 13"), ("Over 16"), ("Over 18"), ("No Restriction");

INSERT INTO movies (title)
VALUES ("Big Ben"), ("Suits"), ("Jurassic Park"), ("Andromeda"), ("Happy Hour");

-- 12
CREATE SCHEMA car_rental;
GO;
USE car_rental;

CREATE TABLE categories (
    id INT AUTO_INCREMENT NOT NULL,
    category NVARCHAR(50) NOT NULL,
    daily_rate DECIMAL(10, 2),
    weekly_rate DECIMAL(10, 2),
    monthly_rate DECIMAL(10, 2),
    weekend_rate DECIMAL(10, 2),
    PRIMARY KEY (id)
);

ALTER TABLE categories
ADD CONSTRAINT Ck_rate CHECK(
    (daily_rate IS NOT NULL) OR 
    (weekly_rate IS NOT NULL) OR 
    (monthly_rate IS NOT NULL) OR
    (weekend_rate IS NOT NULL));

INSERT INTO categories (category, daily_rate, weekly_rate, monthly_rate, weekend_rate)
VALUES 
("First", 10, 20, 30, 40),
("Second", 100, 200, 300, 400),
("Third", 1000, 2000, 3000, 4000);

CREATE TABLE cars (
    id INT AUTO_INCREMENT NOT NULL,
    plate_number NVARCHAR(50) NOT NULL,
    manufacturer NVARCHAR(50) NOT NULL,
    model NVARCHAR(50) NOT NULL,
    car_year INT,
    category_id INT,
    doors TINYINT,
    picture VARBINARY(2000),
    car_condition NVARCHAR(200),
    available BIT DEFAULT 1,
    PRIMARY KEY (id)
);

ALTER TABLE cars
ADD FOREIGN KEY (category_id) REFERENCES categories (id);

INSERT INTO cars (plate_number, manufacturer, model) 
VALUES 
("CA2341AB", "Toyota", "Supra"),
("CA1234AA", "Skoda", "Octavia"),
("CB9999CB", "Skoda", "Kamiq");

CREATE TABLE employees (
    id INT AUTO_INCREMENT NOT NULL,
    first_name NVARCHAR(50) NOT NULL,
    last_name NVARCHAR(50) NOT NULL,
    title NVARCHAR(20),
    notes NVARCHAR(200),
    PRIMARY KEY (id)
);

INSERT INTO employees (first_name, last_name)
VALUES
("John", "Doe"),
("Max", "Williams"),
("Jessica", "Roberts");

CREATE TABLE customers (
    id INT AUTO_INCREMENT NOT NULL,
    driver_license NVARCHAR(50) NOT NULL,
    full_name NVARCHAR(100) NOT NULL,
    address_ NVARCHAR(250),
    city NVARCHAR(50),
    zip_code NVARCHAR(50),
    notes NVARCHAR(200),
    PRIMARY KEY (id)
);


INSERT INTO customers (driver_license, full_name)
VALUES
("21321312AA", "John Doe"),
("29A2938W99", "Marta Borg"),
("999ASD2222", "Max Smith");

CREATE TABLE rental_orders (
    id INT AUTO_INCREMENT NOT NULL,
    employee_id INT NOT NULL,
    customer_id INT NOT NULL,
    car_id INT NOT NULL,
    car_condition NVARCHAR(200),
    tank_level NUMERIC(5, 2),
    kilometrage_start INT,
    kilometrage_end INT,
    total_kilometrage INT,
    startDate DATE,
    endDate DATE,
    total_days INT,
    rate_applied Numeric(10, 2),
    tax_rate Numeric(10, 2),
    order_status NVARCHAR(50),
    notes NVARCHAR(200),
    PRIMARY KEY (id)
);

ALTER TABLE rental_orders
ADD FOREIGN KEY (employee_id) REFERENCES employees (id),
ADD FOREIGN KEY (customer_id) REFERENCES customers (id),
ADD FOREIGN KEY (car_id) REFERENCES cars (id);

INSERT INTO rental_orders (employee_id, customer_id, car_id)
VALUES
(1, 2, 3),
(3, 2, 1),
(2, 3, 1);