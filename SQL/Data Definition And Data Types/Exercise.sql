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
