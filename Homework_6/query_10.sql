SELECT s.name as subject_name
FROM subjects s
JOIN grades g ON s.subject_id = g.subject_id
JOIN teachers t ON s.teacher_id = t.teacher_id
WHERE g.student_id = '25'
AND t.teacher_id = '5';
