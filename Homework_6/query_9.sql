SELECT s.name as subject_name
FROM subjects s
JOIN grades g ON s.subject_id = g.subject_id
WHERE g.student_id = '15';
