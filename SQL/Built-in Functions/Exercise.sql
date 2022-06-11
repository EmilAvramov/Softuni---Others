-- 1
USE soft_uni;

SELECT first_name, last_name
FROM employees
WHERE first_name LIKE "Sa%"
ORDER BY employee_id;

-- 2
SELECT first_name, last_name
FROM employees
WHERE last_name LIKE "%ei%"
ORDER BY employee_id;

-- 3
SELECT first_name
FROM employees
WHERE (department_id = 3 OR department_id = 10) AND (hire_date BETWEEN "19950101" AND "20051231")
ORDER BY employee_id;

-- 4
SELECT first_name, last_name
FROM employees
WHERE job_title NOT LIKE "%engineer%"
ORDER BY employee_id;

-- 5
SELECT name
FROM towns
WHERE LENGTH(name) = 5 OR LENGTH(name) = 6
ORDER BY name ASC;

-- 6
SELECT * FROM towns
WHERE 
name LIKE "M%" OR
name LIKE "K%" OR
name LIKE "B%" OR
name LIKE "E%"
ORDER BY name ASC;