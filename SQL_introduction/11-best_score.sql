-- show score and name of all entrys in second_table ordered by score, highest to lowest
SELECT `score`, `name`
FROM second_table
WHERE `score` >= 10
ORDER BY `score` DESC;
