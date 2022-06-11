CREATE VIEW v_employees_job_titles AS
SELECT IF(middle_name IS NOT NULL, 
CONCAT(first_name, " ", middle_name, " ", last_name),
CONCAT(first_name, " ", last_name)) AS full_name, job_title
FROM employees;