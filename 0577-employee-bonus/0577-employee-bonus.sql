# Write your MySQL query statement below
SELECT name, bonus 
FROM employee e
LEFT JOIN bonus b ON e.empId = b.empId
HAVING b.bonus < 1000 OR b.bonus IS NULL