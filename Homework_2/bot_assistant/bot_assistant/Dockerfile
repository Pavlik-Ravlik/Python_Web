# Використовуємо офіційний Python образ з базовою версією
FROM python:3.11

# Встановлюємо залежності pipenv
RUN pip install pipenv

# Створюємо директорію для нашого проекту
WORKDIR /app

# Копіюємо файли проекту до контейнера
COPY . /app

# Встановлюємо залежності за допомогою Pipenv
RUN pipenv install --system --deploy

# Запускаємо "Персональний помічник"
CMD ["pipenv", "run", "python", "homework_2/bot_assistant/bot_assistant/run.py"]