SELECT s.user_id,
       CASE 
           WHEN COUNT(c.user_id) = 0 THEN 0.00
           ELSE ROUND(COUNT(CASE WHEN c.action = 'confirmed' THEN 1 END) / COUNT(c.user_id), 2)
       END AS confirmation_rate
  FROM Signups s
       LEFT JOIN Confirmations c
       ON s.user_id = c.user_id
GROUP BY s.user_id;
