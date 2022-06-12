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

-- 12
USE diablo;

SELECT name, CAST(start AS DATE) AS start
FROM games
WHERE YEAR(start) BETWEEN "2011" AND "2012"
ORDER BY start ASC, name ASC
LIMIT 50;

-- 13
SELECT 
user_name, 
RIGHT(email, LENGTH(email) - LOCATE("@", email)) AS email_provider
FROM users
ORDER BY email_provider ASC, user_name ASC

-- 14
SELECT user_name, ip_address
FROM users
WHERE ip_address LIKE "___.1%.%.___"
ORDER BY user_name ASC;

-- 15
SELECT
name, 
IF(HOUR(start) BETWEEN 0 AND 11, "Morning",
IF(HOUR(start) BETWEEN 12 and 17, "Afternoon", "Evening")) AS "Part of the Day",
IF(duration <= 3, "Extra Short", 
IF(duration > 3 AND duration <= 6, "Short",
IF(duration > 6 AND duration <= 10, "Long", "Extra Long"
))) AS duration
FROM games

-- 16
USE orders;

SELECT 
product_name, 
order_date,
DATE_ADD(order_date, INTERVAL 3 DAY) AS payment_date,
DATE_ADD(order_date, INTERVAL 1 MONTH) AS delivery_date
FROM orders