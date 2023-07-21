SELECT s.group_id, AVG(g.grade) as avg_grade
FROM students s
JOIN grades g ON s.student_id = g.student_id
WHERE g.subject_id = '2'
GROUP BY s.group_id;
