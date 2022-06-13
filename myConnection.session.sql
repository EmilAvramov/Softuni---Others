SELECT m.mountain_range, p.peak_name, p.elevation
FROM mountains AS m
JOIN peaks as p
ON m.id = p.mountain_id AND m.mountain_range = "Rila"
ORDER BY p.elevation DESC;