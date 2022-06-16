-- 1
CREATE PROCEDURE usp_get_employees_salary_above_35000()
BEGIN
    SELECT first_name, last_name
    FROM employees
    WHERE salary > 35000
    ORDER BY first_name, last_name, employee_id;
END

-- 2
CREATE PROCEDURE usp_get_employees_salary_above (num DOUBLE(19, 4))
BEGIN
    SELECT first_name, last_name
    FROM employees
    WHERE salary >= num
    ORDER BY first_name, last_name, employee_id;
END

-- 3
CREATE PROCEDURE usp_get_towns_starting_with (string NVARCHAR(100))
BEGIN
    SELECT name FROM towns
    WHERE name LIKE CONCAT(string, "%")
    ORDER BY name;
END;