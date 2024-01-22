# Write your MySQL query statement below
# SELECT enui.unique_id, employee.name
# FROM Employees AS employee
# LEFT JOIN EmployeeUNI AS enui ON employee.id = enui.id


SELECT EUNI.unique_id, E.name
FROM Employees E
LEFT JOIN EmployeeUNI EUNI ON E.id = EUNI.id;