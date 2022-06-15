SELECT
ranked.country_name,
ranked.elevation,
ranked.length
FROM (
    SELECT
    c.country_name,
    p.elevation,
    r.length,
    DENSE_RANK() OVER (PARTITION BY c.country_name ORDER BY p.elevation DESC) AS peak,
    DENSE_RANK() OVER (PARTITION BY c.country_name ORDER BY r.length DESC) AS river
    FROM countries AS c
    JOIN mountains_countries AS mc ON c.country_code = mc.country_code
    JOIN peaks AS p ON mc.mountain_id = p.mountain_id
    LEFT JOIN countries_rivers AS cr ON c.country_code = cr.country_code
    LEFT JOIN rivers AS r on cr.river_id = r.id
    ORDER BY 
    p.elevation DESC,
    r.length DESC,
    c.country_name ASC
) AS ranked
WHERE ranked.peak = 1 AND ranked.river = 1
LIMIT 5;