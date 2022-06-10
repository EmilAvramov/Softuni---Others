USE car_rental;

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