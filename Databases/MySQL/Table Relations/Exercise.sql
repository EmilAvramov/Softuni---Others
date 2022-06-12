-- 1
USE geography;

CREATE TABLE passports (
    passport_id INT NOT NULL,
    passport_number NVARCHAR(20) NOT NULL,
    PRIMARY KEY (passport_id)
);

CREATE TABLE people (
    person_id INT AUTO_INCREMENT NOT NULL,
    first_name NVARCHAR(50) NOT NULL,
    salary NUMERIC(10, 2) NOT NULL,
    passport_id INT UNIQUE,
    PRIMARY KEY (person_id),
    FOREIGN KEY (passport_id) REFERENCES passports (passport_id)
);

INSERT INTO passports (passport_id, passport_number)
VALUES 
(101, "N34FG21B"),
(102, "K65LO4R7"),
(103, "ZE657QP2");

INSERT INTO people (first_name, salary, passport_id)
VALUES 
("Roberto", 43300.00, 102),
("Tom", 56100.00, 103),
("Yana", 60200.00, 101);

-- 2
CREATE TABLE manufacturers (
    manufacturer_id INT AUTO_INCREMENT NOT NULL,
    name NVARCHAR(50) NOT NULL,
    established_on DATE NOT NULL,
    PRIMARY KEY (manufacturer_id)
);

CREATE TABLE models (
    model_id INT NOT NULL,
    name NVARCHAR(50) NOT NULL,
    manufacturer_id INT NOT NULL,
    PRIMARY KEY (model_id),
    FOREIGN KEY (manufacturer_id) REFERENCES manufacturers (manufacturer_id)
);

INSERT INTO manufacturers (name, established_on)
VALUES 
("BMW", "1916/03/01"),
("Tesla", "2003/01/01"),
("Lada", "1966/05/01");

INSERT INTO models (model_id, name, manufacturer_id)
VALUES 
(101, "X1", 1),
(102, "i6", 1),
(103, "Model S", 2),
(104, "Model X", 2),
(105, "Model 3", 2),
(106, "Nova", 3);