-- Создание таблицы студентов
DROP TABLE IF EXISTS students;
CREATE TABLE students (
    student_id INTEGER PRIMARY KEY,
    name TEXT,
    group_id INTEGER
);

-- Создание таблицы групп
DROP TABLE IF EXISTS groups;
CREATE TABLE groups (
    groups_id INTEGER PRIMARY KEY,
    name TEXT
);

-- Создание таблицы преподавателей
DROP TABLE IF EXISTS teachers;
CREATE TABLE teachers (
    teacher_id INTEGER PRIMARY KEY,
    name TEXT
);

-- Создание таблицы предметов
DROP TABLE IF EXISTS subjects;
CREATE TABLE subjects (
    subject_id INTEGER PRIMARY KEY,
    name TEXT,
    teacher_id INTEGER
);

-- Создание таблицы оценок
DROP TABLE IF EXISTS grades;
CREATE TABLE grades (
    grade_id INTEGER PRIMARY KEY,
    student_id INTEGER,
    subject_id INTEGER,
    grade INTEGER,
    date DATE,
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (subject_id) REFERENCES subjects(subject_id)
);
