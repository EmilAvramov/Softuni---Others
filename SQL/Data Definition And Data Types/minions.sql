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