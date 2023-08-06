import pika
import json
import time

# Функция-заглушка для отправки email (можно заменить на реальную логику отправки email)
def send_email(contact_id):
    print(f"Sending email to contact with ID: {contact_id}")
    time.sleep(2)  # Имитация отправки email

# Подключение к RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='email_queue') # Очередь сообщений

# Обработка сообщений из очереди
def callback(ch, method, properties, body):
    message = json.loads(body)
    contact_id = message['contact_id']
    send_email(contact_id)
    print(f"Email sent for contact with ID: {contact_id}")
    ch.basic_ack(delivery_tag=method.delivery_tag)

channel.basic_consume(queue='email_queue', on_message_callback=callback)

print('Waiting for messages...')
channel.start_consuming() # Обработчик сообщений, отправляет сообщения обратно в функцию callback
