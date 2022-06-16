-- 1
CREATE DATABASE softuni_imdb;
USE softuni_imdb;

CREATE TABLE countries (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(30) NOT NULL UNIQUE,
    continent VARCHAR(30) NOT NULL,
    currency VARCHAR(5) NOT NULL
);

CREATE TABLE genres (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL UNIQUE
);

CREATE TABLE actors (
    id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    birthdate DATE NOT NULL,
    height INT,
    awards INT,
    country_id INT NOT NULL,
    CONSTRAINT fk_actors FOREIGN KEY (country_id) REFERENCES countries (id)
);

CREATE TABLE movies_additional_info (
    id INT PRIMARY KEY AUTO_INCREMENT,
    rating DECIMAL(10, 2) NOT NULL,
    runtime INT NOT NULL,
    picture_url VARCHAR(80) NOT NULL,
    budget DECIMAL(10, 2),
    release_date DATE NOT NULL,
    has_subtitles TINYINT(1),
    description TEXT
);

CREATE TABLE movies (
    id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(70) NOT NULL UNIQUE,
    country_id INT NOT NULL,
    movie_info_id INT NOT NULL UNIQUE,
    CONSTRAINT fk_countries FOREIGN KEY (country_id) REFERENCES countries (id),
    CONSTRAINT fk_movie_info FOREIGN KEY (movie_info_id) REFERENCES movies_additional_info (id)
);

CREATE TABLE movies_actors (
    movie_id INT,
    actor_id INT,
    KEY (movie_id, actor_id),
    CONSTRAINT fk_movies FOREIGN KEY (movie_id) REFERENCES movies (id),
    CONSTRAINT fk_actors_2 FOREIGN KEY (actor_id) REFERENCES actors (id)
);

CREATE TABLE genres_movies (
    genre_id INT,
    movie_id INT,
    KEY (genre_id, movie_id),
    CONSTRAINT fk_genres FOREIGN KEY (genre_id) REFERENCES genres (id),
    CONSTRAINT fk_movies_2 FOREIGN KEY (movie_id) REFERENCES movies (id)
);

-- 2
INSERT INTO actors (
    first_name, 
    last_name, 
    birthdate,
    height,
    awards,
    country_id
    )
SELECT 
    (REVERSE(first_name)),
    (REVERSE(last_name)),
    (DATE(birthdate - 2)),
    (height + 10),
    (country_id),
    (3)
FROM actors
WHERE id <= 10;

-- 3
UPDATE movies_additional_info
SET runtime = runtime - 10
WHERE id BETWEEN 15 AND 25;

-- 4
DELETE c
FROM countries AS c LEFT JOIN movies AS m on c.id = m.country_id
WHERE m.country_id IS NULL;

-- 5
SELECT id, name, continent, currency
FROM countries
ORDER BY currency DESC, id;

-- 6
SELECT m1.id, m2.title, m1.runtime, m1.budget, m1.release_date
FROM movies_additional_info AS m1
JOIN movies AS m2 ON m1.id = m2.movie_info_id
WHERE YEAR(m1.release_date) BETWEEN 1996 AND 1999
ORDER BY m1.runtime, m1.id
LIMIT 20;

-- 7
SELECT 
CONCAT(a.first_name, " ", a.last_name) AS full_name,
CONCAT(REVERSE(a.last_name), LENGTH(a.last_name), "@cast.com") AS email,
(2022 - YEAR(a.birthdate)) AS age,
a.height
FROM actors AS a
LEFT JOIN movies_actors AS m ON a.id = m.actor_id
WHERE m.actor_id IS NULL
ORDER BY a.height;

-- 8
SELECT c.name, COUNT(m.country_id) AS movie_count
FROM countries AS c
JOIN movies AS m ON c.id = m.country_id
GROUP BY c.name
HAVING COUNT(m.country_id) >= 7
ORDER BY c.name DESC;

-- 9
CREATE FUNCTION language_ (field INT)
RETURNS VARCHAR(10)
DETERMINISTIC
BEGIN
    IF field = 1 THEN
        RETURN "english";
    ELSE 
        RETURN "-";
    END IF;
END;

CREATE FUNCTION ratings_ (field DECIMAL(19, 2))
RETURNS VARCHAR(10)
DETERMINISTIC
BEGIN
    IF field <= 4 THEN 
        RETURN "poor";
    ELSEIF field <= 7 THEN
        RETURN "good";
    ELSE
        RETURN "excellent";
	END IF;
END;

SELECT m2.title, ratings_(m1.rating), language_(m1.has_subtitles), m1.budget
FROM movies_additional_info AS m1
JOIN movies AS m2 ON m1.id = m2.movie_info_id
ORDER BY m1.budget DESC;

-- 10
CREATE FUNCTION udf_actor_history_movies_count(full_name VARCHAR(50))
    RETURNS INT
    DETERMINISTIC
BEGIN
    DECLARE movies_count INT;
    SET movies_count := (
        SELECT COUNT(g.name) AS movies
        FROM actors AS a
                 JOIN movies_actors AS ma on a.id = ma.actor_id
                 JOIN genres_movies AS gm on ma.movie_id = gm.movie_id
                 JOIN genres AS g on g.id = gm.genre_id
        WHERE CONCAT(a.first_name, ' ', a.last_name) = full_name AND g.name = 'History'
        GROUP BY g.name);
    RETURN movies_count;
END; 

-- 11
CREATE PROCEDURE udp_award_movie (movie_title VARCHAR(50))
BEGIN
    UPDATE actors AS a
        JOIN movies_actors AS ma on a.id = ma.actor_id
        JOIN movies AS m on m.id = ma.movie_id
    SET a.awards = a.awards + 1
    WHERE m.title = movie_title;
END;