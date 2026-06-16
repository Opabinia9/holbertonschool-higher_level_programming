-- display the number of times each score appears exluding single ocurences and sorted by highest count
SELECT score, count(name) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
