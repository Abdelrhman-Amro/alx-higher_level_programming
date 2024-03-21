-- lists the number of records with the same score
SELECT score, count(name) FROM second_table
GROUP BY score
ORDER BY score DESC;
