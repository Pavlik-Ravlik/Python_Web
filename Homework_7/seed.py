from faker import Faker
from models import Group, Student, Teacher, Subject, Grade
from connect_db import session
import random


fake = Faker()

# Создаем группы
groups = ['Group A', 'Group B', 'Group C']
for item_group in groups:
    add_group = Group(name=item_group)
    session.add(add_group)
session.commit()

# Создаем преподавателей
random_teacher = random.randint(3, 6)
teachers = [Teacher(name=fake.name()) for _ in range(random_teacher)]
session.add_all(teachers)
session.commit()


# Создаем предметы с преподавателями
random_subjects = random.randrange(5, 8)
subjects = [Subject(name=fake.word(), teacher_id=fake.random_element(teachers).id) for _ in range(random_subjects)]
session.add_all(subjects)
session.commit()


# Создаем студентов и добавляем оценки
random_students = random.randrange(30, 50)
students = []
for _ in range(random_students):
    name = fake.name()
    group_id = random.choice(session.query(Group).all()).id
    student = Student(name=name, group_id=group_id)
    students.append(student)

session.add_all(students)
session.commit()

for student in students:
    for subject in subjects:
        grade = Grade(value=fake.pyint(min_value=2, max_value=5), subject_id=subject.id, student_id=student.id)
        session.add(grade)

session.commit()

print("Database seeded successfully!")
