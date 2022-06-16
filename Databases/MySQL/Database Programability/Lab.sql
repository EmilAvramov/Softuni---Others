-- 1
CREATE FUNCTION ufn_count_employees_by_town(town_name VARCHAR(100))
RETURNS INT
DETERMINISTIC
BEGIN
    RETURN (
    SELECT COUNT(*)
    FROM towns AS t
    JOIN addresses AS a ON t.town_id = a.town_id
    JOIN employees AS e on e.address_id = a.address_id
    WHERE t.name = town_name
    );
END

-- 2
CREATE PROCEDURE usp_raise_salaries(department_name VARCHAR(100))
BEGIN
    UPDATE employees AS e
    JOIN departments AS d 
    ON e.department_id = d.department_id
    SET e.salary = e.salary * 1.05
    WHERE d.name = department_name;
END

-- 3

-- No transaction

-- CREATE PROCEDURE usp_raise_salary_by_id (id INT)
-- BEGIN
--     UPDATE employees AS e
--     SET e.salary = e.salary * 1.05
--     WHERE e.employee_id = id;
-- END

-- With transaction
CREATE PROCEDURE usp_raise_salary_by_id (id INT)
BEGIN
    START TRANSACTION;
    IF ((SELECT COUNT(*) FROM employees WHERE employee_id = id) > 0)
    THEN
        UPDATE employees SET salary = salary * 1.05 WHERE employee_id = id;
        COMMIT;
    ELSE 
        ROLLBACK;
    END IF;
END;

-- 4
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