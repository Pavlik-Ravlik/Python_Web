import json

FILENAME_AUTHORS = 'authors.json'
FILENAME_QUOTES = 'quotes.json'

def read_json_authors():
    with open(FILENAME_AUTHORS, 'r') as file:
        load_json = json.load(file)
        return load_json
    
def read_json_quotes():
    with open(FILENAME_QUOTES, 'r') as file:
        load_json = json.load(file)
        return load_json

