import os
import django
import json

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "quotes.settings")
django.setup()

from quotesapp.models import Quote, Tag, Author

def read_authors(): 
    with open('authors.json', 'r') as file:
        load_data = json.load(file)
    
    return load_data

def read_quotes():
    with open('quotes.json', 'r') as file:
        load_data = json.load(file)
    
    return load_data


authors_data = read_authors()
quotes_data = read_quotes()



for author_data in authors_data:
    Author.objects.get_or_create(
        fullname=author_data["fullname"],
        born_date=author_data["born_date"],
        born_location=author_data["born_location"],
        description=author_data["description"]
    )

for quote_data in quotes_data:
    author = Author.objects.get(fullname=quote_data["author"])
    tags = [Tag.objects.get_or_create(name=tag)[0] for tag in quote_data["tags"]]
    
    Quote.objects.get_or_create(
        quote=quote_data["quote"],
        author=author,
    )

    quote = Quote.objects.get(quote=quote_data["quote"])
    quote.tags.set(tags)






