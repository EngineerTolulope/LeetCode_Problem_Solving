# Write your MySQL query statement below
SELECT unique_id, name
FROM employees
LEFT JOIN employeeuni
ON employeeuni.id = employees.id
