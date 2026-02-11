-- Query 1: Average marks per department
SELECT department, AVG(marks) AS avg_marks
FROM cleaned
GROUP BY department;

-- Query 2: Data quality audit metrics
SELECT source_file, total_rows, valid_rows, invalid_rows
FROM audit;
