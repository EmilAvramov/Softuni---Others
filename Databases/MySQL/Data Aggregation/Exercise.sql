-- 1
USE gringotts;

SELECT COUNT(id) AS "count"
FROM wizzard_deposits;

-- 2
SELECT MAX(magic_wand_size) AS "longest_magic_wand"
FROM wizzard_deposits

-- 3
SELECT deposit_group, MAX(magic_wand_size) AS longest_magic_wand
FROM wizzard_deposits
GROUP BY deposit_group
ORDER BY longest_magic_wand ASC, deposit_group ASC;

-- 4
SELECT deposit_group
FROM wizzard_deposits
GROUP BY deposit_group
ORDER BY AVG(magic_wand_size)
LIMIT 1;

-- 5
SELECT deposit_group, SUM(deposit_amount) As total_sum
FROM wizzard_deposits
GROUP BY deposit_group
ORDER BY total_sum ASC;