USE movies;

CREATE TABLE movies (
    id INT AUTO_INCREMENT NOT NULL,
    title NVARCHAR(50) NOT NULL,
    director_id INT,
    copyright_year DATE,
    length NVARCHAR(20),
    genre_id INT,
    category_id INT,
    rating INT,
    notes NVARCHAR(200),
    PRIMARY KEY (id)
);

INSERT INTO movies (title)
VALUES ("Big Ben"), ("Suits"), ("Jurassic Park"), ("Andromeda"), ("Happy Hour");