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

-- 3
CREATE TABLE exams (
    exam_id INT NOT NULL,
    name NVARCHAR(50) NOT NULL,
    CONSTRAINT pk_exams PRIMARY KEY (exam_id)
);

CREATE TABLE students (
    student_id INT AUTO_INCREMENT NOT NULL,
    name NVARCHAR(50) NOT NULL,
    CONSTRAINT pk_students PRIMARY KEY (student_id)
);

CREATE TABLE students_exams (
    student_id INT NOT NULL,
    exam_id INT NOT NULL,
    CONSTRAINT pk_students_exams PRIMARY KEY (student_id, exam_id),
    CONSTRAINT fk_student_id FOREIGN KEY (student_id) REFERENCES students (student_id),
    CONSTRAINT fk_exam_id FOREIGN KEY (exam_id) REFERENCES exams (exam_id)
);

INSERT INTO exams (exam_id, name)
VALUES
(101, "Spring MVC"),
(102, "Neo4j"),
(103, "Oracle 11g");

INSERT INTO students (name)
VALUES ("Mila"), ("Toni"), ("Ron");

INSERT INTO students_exams (student_id, exam_id)
VALUES
(1, 101),
(1, 102),
(2, 101),
(3, 103),
(2, 102),
(2, 103);

-- 4
CREATE TABLE teachers (
    teacher_id INT NOT NULL,
    name NVARCHAR(50),
    manager_id INT,
    CONSTRAINT pk_teachers PRIMARY KEY (teacher_id)
);

INSERT INTO teachers (teacher_id, name, manager_id)
VALUES
(101, "John", NULL),
(102, "Maya", 106),
(103, "Silvia", 106),
(104, "Ted", 105),
(105, "Mark", 101),
(106, "Greta", 101);

ALTER TABLE teachers
ADD CONSTRAINT fk_teachers FOREIGN KEY (manager_id) REFERENCES teachers (teacher_id);


-- 5
CREATE DATABASE online_store;

USE online_store;

CREATE TABLE item_types (
    item_type_id INT(11) NOT NULL,
    name VARCHAR(50) NOT NULL,
    CONSTRAINT pk_types PRIMARY KEY (item_type_id)
);

CREATE TABLE items (
    item_id INT(11) NOT NULL,
    name VARCHAR(50) NOT NULL,
    item_type_id INT(11) NOT NULL,
    CONSTRAINT pk_items PRIMARY KEY (item_id),
    CONSTRAINT fk_types FOREIGN KEY (item_type_id) REFERENCES item_types (item_type_id)
);

CREATE TABLE cities (
    city_id INT(11) NOT NULL,
    name VARCHAR(50) NOT NULL,
    CONSTRAINT pk_cities PRIMARY KEY (city_id)
);

CREATE TABLE customers (
    customer_id INT(11) NOT NULL,
    name VARCHAR(50) NOT NULL,
    birthday DATE NOT NULL,
    city_id INT(11) NOT NULL,
    CONSTRAINT pk_customers PRIMARY KEY (customer_id),
    CONSTRAINT fk_customers FOREIGN KEY (city_id) REFERENCES cities (city_id)
);

CREATE TABLE orders (
    order_id INT(11) NOT NULL,
    customer_id INT(11) NOT NULL,
    CONSTRAINT pk_orders PRIMARY KEY (order_id),
    CONSTRAINT fk_orders FOREIGN KEY (customer_id) REFERENCES customers (customer_id)
);

CREATE TABLE order_items (
    order_id INT(11) NOT NULL,
    item_id INT(11) NOT NULL,
    CONSTRAINT pk_order_items PRIMARY KEY (order_id, item_id),
    CONSTRAINT fk_order_ids FOREIGN KEY (order_id) REFERENCES orders (order_id),
    CONSTRAINT fk_items FOREIGN KEY (item_id) REFERENCES items (item_id)
);

-- 5
CREATE DATABASE university;

USE university;

CREATE TABLE majors (
    major_id INT(11) NOT NULL,
    name VARCHAR(50) NOT NULL,
    CONSTRAINT pk_majors PRIMARY KEY (major_id)
);

CREATE TABLE students (
    student_id INT(11) NOT NULL,
    student_number VARCHAR(12) NOT NULL,
    student_name VARCHAR(50) NOT NULL,
    major_id INT(11) NOT NULL,
    CONSTRAINT fk_students PRIMARY KEY (student_id),
    CONSTRAINT fk_students FOREIGN KEY (major_id) REFERENCES majors (major_id)
);

CREATE TABLE payments (
    payment_id INT(11) NOT NULL,
    payment_date DATE NOT NULL,
    payment_amount DECIMAL(8, 2) NOT NULL,
    student_id INT(11) NOT NULL,
    CONSTRAINT pk_payments PRIMARY KEY (payment_id),
    CONSTRAINT fk_payments FOREIGN KEY (student_id) REFERENCES students(student_id)
);

CREATE TABLE subjects (
    subject_id INT(11) NOT NULL,
    subject_name VARCHAR(50) NOT NULL,
    CONSTRAINT pk_subjects PRIMARY KEY (subject_id)
);

CREATE TABLE agenda (
    student_id INT(11) NOT NULL,
    subject_id INT(11) NOT NULL,
    CONSTRAINT pk_agenda PRIMARY KEY (student_id, subject_id),
    CONSTRAINT fk_agenda_student FOREIGN KEY (student_id) REFERENCES students (student_id),
    CONSTRAINT fk_agenda_subject FOREIGN KEY (subject_id) REFERENCES subjects (subject_id)
);

-- 6
SELECT m.mountain_range, p.peak_name, p.elevation
FROM mountains AS m
JOIN peaks as p
ON m.id = p.mountain_id AND m.mountain_range = "Rila"
ORDER BY p.elevation DESC;