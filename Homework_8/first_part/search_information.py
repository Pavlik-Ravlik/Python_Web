from models import Authors, Quotes
import connect
import time


AUTHORS = Authors.objects()
QUOTES = Quotes.objects()


def find_quotes_name(name: str) -> list:
    return [quotes.quote for quotes in QUOTES if name in quotes.author.fullname]


def find_quotes_tags(tag: str) -> list:
    list_quotes = []
    
    for quotes in QUOTES:
        for tags in quotes.tags:
            
            if tag in tags:
                list_quotes.append(quotes.quote)
    return list_quotes


def find_many_quotes_tags(many_tags: str) -> list:
    many_tags = many_tags.split(',')
    list_quotes = []

    for quote in QUOTES:
        found = False
        
        for tag in quote.tags:
            if tag in many_tags and not found:
                list_quotes.append(quote.quote)
                found = True
    return list_quotes



if __name__ == '__main__':
 
    while True:
        
        time.sleep(1)
        command = input('Пожалуйста введите команду и значение например (name:Albert Einstein)\n >>>>> ')
        
        if command == 'exit':
            print('Good buy')
            break

        key, value = command.split(':')

        if key == 'name':
            result = find_quotes_name(value)
            
            for quote in result:
                print(quote)

        elif key == 'tag':
            result = find_quotes_tags(value)

            for quote in result:
                print(quote)

        elif key == 'tags':
            result = find_many_quotes_tags(value)

            for quote in result:
                print(quote)
        
        else:
            print('This command not in list commands')
