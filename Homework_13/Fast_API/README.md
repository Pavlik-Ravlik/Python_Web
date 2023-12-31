# Homework_13

У цьому домашньому завданні доопрацьовував застосунок REST API із домашнього завдання 12.

Завдання:

- Реалізував механізм верифікації електронної пошти зареєстрованого користувача;
- Обмежив кількість запитів до своїх маршрутів контактів. Обов’язково обмежив швидкість - створення контактів для користувача;
- Увімкнув CORS для свого REST API;
- Реалізував можливість оновлення аватара користувача. Використував сервіс Cloudinary;

Загальні вимоги:

- Усі змінні середовища зберігаються у файлі .env. Всередині коду немає конфіденційних даних у «чистому» вигляді;
- Для запуску всіх сервісів і баз даних у застосунку використовується Docker Compose;

Додаткове завдання:

- Реалізував механізм кешування за допомогою бази даних Redis. Виконав кешування поточного користувача під час авторизації;
- Реалізував механізм скидання паролю для застосунку REST API;