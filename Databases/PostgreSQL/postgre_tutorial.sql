-- #1 CREATE DATABASE

CREATE DATABASE pet_hotel;

CREATE TABLE hotel (
    hotel_id serial PRIMARY KEY,
    hotel_name VARCHAR(25) NOT NULL,
    hotel_stars INT NOT NULL,
    CHECK (hotel_stars BETWEEN 1 AND 5)
);

CREATE TABLE pet_owner (
    owner_id serial PRIMARY KEY,
    owner_name VARCHAR(15),
    owner_age INT NOT NULL,
    CHECK (owner_age BETWEEN 1 AND 110)
);

CREATE TABLE dog_room (
    room_id serial PRIMARY KEY,
    dog_id INT NOT NULL UNIQUE,
    hotel_id INT NOT NULL UNIQUE,
    register_date DATE,
    unregister_date DATE,
    FOREIGN KEY (hotel_id) REFERENCES hotel (hotel_id) ON DELETE CASCADE
);

CREATE TABLE cat_room (
    room_id serial PRIMARY KEY,
    cat_id INT NOT NULL UNIQUE,
    hotel_id INT NOT NULL UNIQUE,
    register_date DATE,
    unregister_date DATE,
    FOREIGN KEY (hotel_id) REFERENCES hotel (hotel_id) ON DELETE CASCADE
);

CREATE TABLE dog (
    dog_id serial PRIMARY KEY,
    owner_id INT NOT NULL UNIQUE,
    dog_name VARCHAR(15) NOT NULL,
    dog_age INT NOT NULL,
    FOREIGN KEY (dog_id) REFERENCES dog_room (dog_id) ON DELETE CASCADE,
    CHECK (dog_age BETWEEN 1 and 25)
);

CREATE TABLE cat(
    cat_id serial PRIMARY KEY,
    owner_id INT NOT NULL UNIQUE,
    cat_name VARCHAR(15) NOT NULL,
    cat_age INT NOT NULL,
    FOREIGN KEY (cat_id) REFERENCES cat_room (cat_id) ON DELETE CASCADE,
    CHECK (cat_age BETWEEN 1 AND 25)
);


ALTER TABLE cat 
ADD FOREIGN KEY (owner_id) REFERENCES pet_owner (owner_id) ON DELETE CASCADE;

ALTER TABLE dog 
ADD FOREIGN KEY (owner_id) REFERENCES pet_owner (owner_id) ON DELETE CASCADE;