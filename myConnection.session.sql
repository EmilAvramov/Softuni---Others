CREATE TABLE deleted_employees(
    employee_id INT NOT NULL,
    first_name NVARCHAR(50) NOT NULL,
    last_name NVARCHAR(50) NOT NULL,
    job_title NVARCHAR(100) NOT NULL,
    SALARY NUMERIC(8, 2) NOT NULL,
    CONSTRAINT pk_de PRIMARY KEY (employee_id)
);