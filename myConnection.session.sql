USE minions;

DROP TABLE users;

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