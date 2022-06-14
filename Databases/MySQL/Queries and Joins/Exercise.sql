-- 1
USE soft_uni;

SELECT e.employee_id, e.job_title, e.address_id, a.address_text
FROM employees AS e
JOIN addresses AS a
ON e.address_id = a.address_id
ORDER BY e.address_id
LIMIT 5;

-- 2
SELECT
e.first_name, 
e.last_name, 
a.name, 
a.address_text
FROM employees AS e
JOIN (
    SELECT a.address_text, a.address_id, t.name
    FROM addresses AS a
    JOIN towns as t
    ON a.town_id = t.town_id
) AS a
ON e.address_id = a.address_id
ORDER BY e.first_name, e.last_name
LIMIT 5;

-- 3
SELECT 
e.employee_id,
e.first_name,
e.last_name,
d.name
FROM employees AS e
JOIN departments AS d
ON e.department_id = d.department_id AND d.name = "Sales"
ORDER BY e.employee_id DESC

-- 4
SELECT
e.employee_id,
e.first_name,
e.salary,
d.name
FROM employees AS e
JOIN departments AS d
ON e.department_id = d.department_id AND e.salary > 15000
ORDER BY e.department_id DESC, e.first_name ASC
LIMIT 5;

-- 5
SELECT e.employee_id, e.first_name
FROM employees AS e
LEFT JOIN employees_projects AS p
ON e.employee_id = p.employee_id
WHERE p.employee_id IS NULL
ORDER BY e.employee_id DESC
LIMIT 3;

-- 6
SELECT
e.first_name,
e.last_name,
CAST(e.hire_date as DATETIME) AS hire_date,
d.name
FROM employees AS e
JOIN departments AS d
ON e.department_id = d.department_id AND e.hire_date > "1999/1/1"
WHERE d.name = "Sales" OR d.name = "Finance"
ORDER BY e.hire_date

-- 7
SELECT e.employee_id, e.first_name, p.name
FROM employees AS e
JOIN employees_projects AS ep ON e.employee_id = ep.employee_id
JOIN projects AS p ON ep.project_id = p.project_id
WHERE p.start_date > "2002/08/13" AND p.end_date IS NULL
ORDER BY e.first_name, p.name
LIMIT 5;

-- 8
SELECT 
e.employee_id, 
e.first_name, 
IF(p.start_date >= "2005/01/01", NULL, p.name) AS project_name
FROM employees AS e
JOIN employees_projects AS ep ON e.employee_id = ep.employee_id
JOIN projects AS p ON ep.project_id = p.project_id
WHERE e.employee_id = 24
ORDER BY project_name
LIMIT 5;

-- 9
SELECT 
e1.employee_id,
e1.first_name,
e1.manager_id,
e2.first_name AS manager_name
FROM employees AS e1
JOIN employees AS e2
ON e1.manager_id = e2.employee_id
WHERE e1.manager_id IN (3, 7)
ORDER BY first_name;

-- 10
SELECT 
e1.employee_id,
CONCAT(e1.first_name, " ", e1.last_name) AS employee_name,
CONCAT(e2.first_name, " ", e2.last_name) AS manager_name,
d.name AS department_name
FROM employees AS e1
JOIN employees AS e2 ON e1.manager_id = e2.employee_id
JOIN departments AS d ON e1.department_id = d.department_id
ORDER BY e1.employee_id
LIMIT 5;

-- 11
SELECT 
ROUND(AVG(salary), 4) AS min_average_salary
FROM employees
GROUP BY department_id
ORDER BY min_average_salary ASC
LIMIT 1;
