import sqlite3
from faker import Faker
import random
import datetime

fake = Faker()

def main():
    # Подключение к базе данных
    with sqlite3.connect('salary.db') as conn:
        cursor = conn.cursor()

        # Заполнение таблицы групп
        groups = ['Group A', 'Group B', 'Group C']
        for group in groups:
            cursor.execute("INSERT INTO groups (name) VALUES (?)", (group,))

        # Заполнение таблицы преподавателей
        for _ in range(5):
            cursor.execute("INSERT INTO teachers (name) VALUES (?)", (fake.name(),))

        # Заполнение таблицы предметов
        subjects = ['Math', 'Physics', 'Chemistry', 'History', 'Literature', 'Biology', 'Computer Science']
        for subject in subjects:
            teacher_id = random.randint(1, 5)  # Выбираем случайного преподавателя
            cursor.execute("INSERT INTO subjects (name, teacher_id) VALUES (?, ?)", (subject, teacher_id))

        # Заполнение таблицы студентов и оценок
        for _ in range(50):
            name = fake.name()
            group_id = random.randint(1, 3)  # Выбираем случайную группу для студента
            cursor.execute("INSERT INTO students (name, group_id) VALUES (?, ?)", (name, group_id))
            student_id = cursor.lastrowid  # Получаем ID последнего добавленного студента

            # Заполнение таблицы оценок
            for subject_id in range(1, len(subjects) + 1):
                grade = random.randint(2, 5)  # Генерируем случайные оценки от 2 до 5
                date = fake.date_between(start_date='-1y', end_date='today')  # Случайная дата за последний год
                cursor.execute("INSERT INTO grades (student_id, subject_id, grade, date) VALUES (?, ?, ?, ?)",
                            (student_id, subject_id, grade, date))

        # Сохранение изменений
        conn.commit()

if __name__ == '__main__':
    main()
