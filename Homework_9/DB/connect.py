from mongoengine import connect
import configparser

config = configparser.ConfigParser()

try:
    config.read(r'C:\Users\PC\Documents\GitHub\Python_Web\Homework_8\config.ini')

    mongo_user = config.get('DB', 'user')
    mongodb_pass = config.get('DB', 'password')
    db_name = config.get('DB', 'name')
    domain = config.get('DB', 'domain')

    connect(
        host=f"mongodb+srv://{mongo_user}:{mongodb_pass}@{domain}/{db_name}?retryWrites=true&w=majority",
        ssl=True,
        alias='default' 
    )
    print("Connected to MongoDB Atlas successfully!")
except Exception as e:
    print("Error connecting to MongoDB Atlas:", e)