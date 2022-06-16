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

-- 4
CREATE PROCEDURE usp_get_employees_from_town (t_name NVARCHAR(100))
BEGIN
    SELECT e.first_name, e.last_name FROM employees AS e
    JOIN addresses AS a on e.address_id = a.address_id
    JOIN towns AS t on a.town_id = t.town_id
    WHERE t.name = t_name
    ORDER BY e.first_name, e.last_name;
END

-- 5
CREATE FUNCTION ufn_get_salary_level (salary DOUBLE(19, 2))
RETURNS VARCHAR(20)
DETERMINISTIC
BEGIN
	DECLARE s_level VARCHAR(20);
	IF salary > 50000 THEN SET s_level = "High";
	ELSEIF salary BETWEEN 30000 AND 50000 THEN SET s_level = "Average";
		ELSE SET s_level = "Low";
	END IF;
	RETURN s_level;
END;

-- 6
CREATE PROCEDURE usp_get_employees_by_salary_level (s_level VARCHAR(7))
BEGIN
    SELECT first_name, last_name
    FROM employees
    WHERE ufn_get_salary_level(salary) = s_level
    ORDER BY first_name DESC, last_name DESC;
END;

-- 7
