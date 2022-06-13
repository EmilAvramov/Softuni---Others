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