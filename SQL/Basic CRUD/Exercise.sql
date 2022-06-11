-- 1
SELECT *
FROM departments
ORDER BY department_id;

-- 2
SELECT name FROM departments ORDER BY department_id;

-- 3
SELECT first_name, last_name, salary 
FROM employees 
ORDER BY employee_id;

-- 4
SELECT first_name, middle_name, last_name
FROM employees 
ORDER BY employee_id;

-- 5
SELECT CONCAT(first_name, ".", last_name, "@softuni.bg") AS full_email_address
FROM employees;

-- 6
SELECT DISTINCT(salary) FROM employees;

-- 7
SELECT * FROM employees
WHERE job_title = "Sales Representative";

-- 8
SELECT first_name, last_name, job_title FROM employees
WHERE salary >= 20000 AND salary <= 30000
ORDER BY employee_id;

-- 9
SELECT CONCAT(first_name, " ", middle_name, " ", last_name) AS "Full Name"
FROM employees
WHERE salary = 25000
    OR salary = 14000
    OR salary = 12500
    OR salary = 23600;

-- 10
SELECT first_name, last_name
FROM employees
WHERE manager_id IS NULL;