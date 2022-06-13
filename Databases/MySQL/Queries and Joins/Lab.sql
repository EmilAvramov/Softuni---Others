-- 1
SELECT 
e.employee_id, 
CONCAT(e.first_name, " ", e.last_name) AS full_name, 
d.department_id, 
d.name
FROM employees AS e
JOIN departments AS d
ON e.manager_id = d.manager_id
GROUP BY e.department_id
ORDER BY e.employee_id
LIMIT 5;

-- 2
SELECT t.town_id, t.name, a.address_text
FROM towns AS t
JOIN addresses AS a
ON t.town_id = a.town_id AND t.name IN ("San Francisco", "Sofia", "Carnation")
ORDER BY t.town_id, a.address_id

-- 3
SELECT 
employee_id, 
first_name, 
last_name,
department_id, 
salary
FROM employees
WHERE manager_id IS NULL

-- 4
SELECT COUNT(salary)
FROM employees
WHERE salary > (
    SELECT AVG(salary)
    FROM employees
)