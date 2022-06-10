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

ALTER TABLE minions
RENAME COLUMN town_id to id;
