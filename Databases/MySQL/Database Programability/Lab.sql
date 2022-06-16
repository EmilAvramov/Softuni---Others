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
CREATE PROCEDURE usp_raise_salary_by_id (id INT)
BEGIN
    UPDATE employees AS e
    SET e.salary = e.salary * 1.05
    WHERE e.employee_id = id;
END