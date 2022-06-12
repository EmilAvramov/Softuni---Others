SELECT first_name, last_name, department_id
FROM employees AS orig
WHERE salary > (
    SELECT AVG(salary)
    FROM employees AS copy
    WHERE orig.department_id = copy.department_id
)
ORDER BY department_id, employee_id
LIMIT 10;