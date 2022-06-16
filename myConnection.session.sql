CREATE PROCEDURE usp_get_towns_starting_with (string NVARCHAR(100))
BEGIN
    SELECT name FROM towns
    WHERE name LIKE CONCAT(string, "%")
    ORDER BY name;
END;