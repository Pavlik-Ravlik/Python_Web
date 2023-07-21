SELECT t.name as teacher_name, AVG(g.grade) as avg_grade
FROM teachers t
JOIN subjects s ON t.teacher_id = s.teacher_id
JOIN grades g ON s.subject_id = g.subject_id
WHERE t.teacher_id = '4'
GROUP BY t.name;
