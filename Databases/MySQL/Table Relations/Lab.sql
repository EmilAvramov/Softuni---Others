-- 1
USE camp;

CREATE TABLE mountains (
    id INT NOT NULL,
    name NVARCHAR(50) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE peaks (
    id INT NOT NULL,
    name NVARCHAR(50) NOT NULL,
    mountain_id INT,
    PRIMARY KEY (id)
);

ALTER TABLE peaks
ADD FOREIGN KEY (mountain_id) REFERENCES mountains (id);

-- 2