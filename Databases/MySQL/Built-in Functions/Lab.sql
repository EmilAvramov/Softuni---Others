-- 1
USE book_library;

SELECT title
FROM books
WHERE title LIKE "The%"
ORDER BY id ASC;

-- 2
SELECT REPLACE(title, "The", "***") AS title
FROM books
WHERE title LIKE "The%"
ORDER BY id ASC;

-- 3
SELECT ROUND(SUM(cost), 2)
FROM books;

-- 4
SELECT 
CONCAT(first_name, " ", last_name) AS "Full Name",
DATEDIFF(died, born) AS "Days Lived"
FROM authors;

-- 5
SELECT title
FROM books
WHERE title LIKE "Harry%"
