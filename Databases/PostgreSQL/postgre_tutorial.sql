-- #1 CREATE DATABASE

CREATE DATABASE pet_hotel;

CREATE TABLE hotel (
    hotel_id INT PRIMARY KEY NOT NULL,
    hotel_name VARCHAR(25) NOT NULL,
    hotel_stars INT NOT NULL,
    CHECK (hotel_stars BETWEEN 1 AND 5)
);

CREATE TABLE pet_owner (
    owner_id INT PRIMARY KEY NOT NULL,
    owner_name VARCHAR(15),
    owner_age INT NOT NULL,
    CHECK (owner_age BETWEEN 1 AND 110)
);

CREATE TABLE dog_room (
    room_id INT PRIMARY KEY NOT NULL,
    dog_id INT NOT NULL UNIQUE,
    hotel_id INT NOT NULL,
    register_date DATE,
    unregister_date DATE,
    FOREIGN KEY (hotel_id) REFERENCES hotel (hotel_id) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE cat_room (
    room_id INT PRIMARY KEY NOT NULL,
    cat_id INT NOT NULL UNIQUE,
    hotel_id INT NOT NULL,
    register_date DATE,
    unregister_date DATE,
    FOREIGN KEY (hotel_id) REFERENCES hotel (hotel_id) ON DELETE CASCADE ON UPDATE CASCADE
);

CREATE TABLE dog (
    dog_id INT PRIMARY KEY NOT NULL,
    owner_id INT NOT NULL,
    dog_name VARCHAR(15) NOT NULL,
    dog_age INT NOT NULL,
    CHECK (dog_age BETWEEN 1 and 25)
);

CREATE TABLE cat(
    cat_id INT PRIMARY KEY NOT NULL,
    owner_id INT NOT NULL,
    cat_name VARCHAR(15) NOT NULL,
    cat_age INT NOT NULL,
    CHECK (cat_age BETWEEN 1 AND 25)
);

ALTER TABLE cat 
ADD TINYTEXTFOREIGN KEY (cat_id) REFERENCES cat_room (cat_id) ON DELETE CASCADE ON UPDATE CASCADE,
ADD FOREIGN KEY (owner_id) REFERENCES pet_owner (owner_id) ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE dog 
ADD FOREIGN KEY (dog_id) REFERENCES dog_room (dog_id) ON DELETE CASCADE ON UPDATE CASCADE,
ADD FOREIGN KEY (owner_id) REFERENCES pet_owner (owner_id) ON DELETE CASCADE ON UPDATE CASCADE;

-- #2 Insert
INSERT INTO pet_owner
VAlUES 
(1, 'Peter', 26),
(2, 'George', 32),
(3, 'Amy', 67);

INSERT INTO hotels
VALUES
(1, 'Grand Pets Hotel', 5),
(2, 'Pets Heaven', 2);

INSERT INTO dog_room
VALUES
(1, 1, 1, '2020-06-08', '2020-06-10'),
(2, 2, 2, '2020-06-10', '2020-06-15'),
(3, 3, 2, '2020-06-20', '2020-06-23');

INSERT INTO cat_room
VALUES
(1, 1, 1, '2020-06-08', '2020-06-10'),
(2, 2, 2, '2020-06-10', '2020-06-15'),
(3, 3, 2, '2020-06-20', '2020-06-23');

INSERT INTO dog
VALUES
(1, 1, 'Fluffu', 2),
(2, 3, 'Bully', 3),
(3, 1, 'Rousey', 5);

INSERT INTO cat
VALUES
(1, 2, 'Tommy', 1),
(2, 3, 'Jessy', 7),
(3, 2, 'Bubbles', 3);

-- 3 SELECT
SELECT c.cat_name, c.cat_id 
FROM cat AS c
LEFT JOIN cat_room AS cr 
ON cr.cat_id = c.cat_id
WHERE c.cat_id = 2;

-- 4 ORDER BY
SELECT owner_id, owner_name, owner_age
FROM pet_owner
ORDER BY owner_age DESC;

-- 5 COUNT
SELECT COUNT(cat_age)
FROM cat
WHERE cat_age >= 3;

-- 6 DELETE
DELETE FROM cat
WHERE cat_age <= 2;

DELETE FROM dog
WHERE dog_age <= 2;