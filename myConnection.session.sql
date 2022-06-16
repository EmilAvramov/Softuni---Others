CREATE TABLE deleted_employees(
    employee_id INT AUTO_INCREMENT NOT NULL,
    first_name NVARCHAR(50) NOT NULL,
    last_name NVARCHAR(50) NOT NULL,
    middle_name NVARCHAR(50) NOT NULL,
    job_title NVARCHAR(100) NOT NULL,
    department_id INT NOT NULL,
    salary NUMERIC(8, 2) NOT NULL,
    CONSTRAINT pk_de PRIMARY KEY (employee_id)
);

CREATE TRIGGER trigger_employee BEFORE DELETE ON employees
FOR EACH ROW
    INSERT INTO deleted_employees(
        first_name, last_name, middle_name, job_title, department_id, salary
    )
    VALUES
    (
    OLD.first_name, 
    OLD.last_name, 
    OLD.middle_name, 
    OLD.job_title,
    OLD.department_id, 
    OLD.salary);