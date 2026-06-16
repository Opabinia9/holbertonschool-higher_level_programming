-- show score and name where name is not null and order by score descending
SELECT `score`, `name`
FROM second_table
WHERE `name` IS NOT NULL
ORDER BY `score` DESC
