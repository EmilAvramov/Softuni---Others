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