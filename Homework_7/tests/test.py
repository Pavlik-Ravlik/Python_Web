from faker import Faker
import random

fake = Faker()


random_teachers = random.randrange(3, 6)
teacher = []
for _ in range(random_teachers):
    fake_name_teachers = fake.name()
    teacher.append(fake_name_teachers)
print(teacher)