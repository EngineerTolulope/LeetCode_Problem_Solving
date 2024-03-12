# Write your MySQL query statement below
-- SELECT e.name
-- FROM employee e
-- JOIN (SELECT managerId
--         FROM employee
--         GROUP BY managerId
--         HAVING COUNT(managerId) >= 5) m
-- ON e.id = m.managerId

SELECT e.name
FROM Employee e
JOIN (
    SELECT managerId, COUNT(*) AS numReports
    FROM Employee
    GROUP BY managerId
) AS reports ON e.id = reports.managerId
WHERE reports.numReports >= 5;