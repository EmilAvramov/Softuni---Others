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

-- 7
CREATE VIEW v_employees_hired_after_2000 AS
SELECT first_name, last_name 
FROM employees
WHERE YEAR(hire_date) > 2000;

-- 8
SELECT first_name, last_name
FROM employees
WHERE LENGTH(last_name) = 5;

-- 9
USE geography;

-- 10
SELECT country_name, iso_code
FROM countries
WHERE country_name LIKE "%a%a%a%"
ORDER BY iso_code ASC;

-- 11
SELECT 
peaks.peak_name, 
rivers.river_name,
LOWER(CONCAT(LEFT(peaks.peak_name, LENGTH(peaks.peak_name) - 1), rivers.river_name)) AS mix
FROM peaks JOIN rivers
ON RIGHT(peaks.peak_name, 1) = LEFT(rivers.river_name, 1)
ORDER BY mix;
