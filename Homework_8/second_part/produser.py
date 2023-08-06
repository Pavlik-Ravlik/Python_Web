import pika
import json
import connect
from models import Contact
from faker import Faker

fake = Faker()

# Генерация фейковых контактов и запись в MongoDB
def generate_fake_contacts(count):
    fake_contacts = []
    for _ in range(count):
        fake_contacts.append(Contact(
            full_name=fake.name(),
            email=fake.ascii_free_email(),
            message_sent=False
        ))

    Contact.objects.insert(fake_contacts)

# Отправка сообщений в RabbitMQ
def send_messages_to_rabbitmq():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    contacts = Contact.objects(message_sent=False)
    for contact in contacts:
        message = {"contact_id": str(contact.id)}
        channel.basic_publish(exchange='', routing_key='email_queue', body=json.dumps(message)) # Отправляем само сообщение routing_key - очередб должна совпадать с именем очереди
        print(f"Sent message for contact: {contact.full_name}")

        contact.message_sent = True
        contact.save()

    connection.close() # Закрываем соеденение

if __name__ == "__main__":
    generate_fake_contacts(10)
    send_messages_to_rabbitmq()
