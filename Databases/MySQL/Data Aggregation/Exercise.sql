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

-- 6
SELECT deposit_group, SUM(deposit_amount) AS total_sum
FROM wizzard_deposits
WHERE magic_wand_creator = "Ollivander family"
GROUP BY deposit_group
ORDER BY deposit_group ASC;

-- 7
SELECT deposit_group, SUM(deposit_amount) AS total_sum
FROM wizzard_deposits
WHERE magic_wand_creator = "Ollivander family"
GROUP BY deposit_group
HAVING SUM(deposit_amount) < 150000
ORDER BY total_sum DESC;

-- 8
SELECT 
deposit_group, 
magic_wand_creator, 
MIN(deposit_charge) as min_deposit_charge
FROM wizzard_deposits
GROUP BY deposit_group, magic_wand_creator
ORDER BY magic_wand_creator ASC, deposit_group ASC;

-- 9
SELECT 
IF(age BETWEEN 0 AND 10, "[0-10]",
IF(age BETWEEN 11 and 20, "[11-20]",
IF(age BETWEEN 21 and 30, "[21-30]",
IF(age BETWEEN 31 and 40, "[31-40]",
IF(age BETWEEN 41 and 50, "[41-50]",
IF(age BETWEEN 51 and 60, "[51-60]", "[61+]")))))) AS age_group, 
COUNT(id)
FROM wizzard_deposits
GROUP BY age_group
ORDER BY age_group ASC

-- 10
SELECT DISTINCT(LEFT(first_name, 1)) AS first_letter
FROM wizzard_deposits
WHERE deposit_group = "Troll Chest"
ORDER BY first_letter ASC;

-- 11
SELECT 
deposit_group, 
ROUND(is_deposit_expired, 1),
AVG(deposit_interest)
FROM wizzard_deposits
WHERE deposit_start_date >= '1985/01/01'
GROUP BY deposit_group, is_deposit_expired
ORDER BY deposit_group DESC, is_deposit_expired ASC
