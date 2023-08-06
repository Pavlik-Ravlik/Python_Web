from mongoengine import Document, StringField, BooleanField


# Модель для контактов
class Contact(Document):
    full_name = StringField(required=True)
    email = StringField(required=True)
    message_sent = BooleanField(default=False)