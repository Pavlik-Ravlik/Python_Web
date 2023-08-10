from models import Authors, Quotes
from read_from_json import read_json_authors, read_json_quotes
import connect


AUTHORS = read_json_authors()
QUOTES = read_json_quotes()
    

for author_data in AUTHORS:
    author = Authors(**author_data)
    author.save()

for quote_data in QUOTES:
    author_name = quote_data.pop('author')
    author = Authors.objects(fullname=author_name).first()
    if author:
        quote_data['author'] = author
        quote = Quotes(**quote_data)
        quote.save()
    