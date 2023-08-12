import requests 
from bs4 import BeautifulSoup
import json


def find_info_quotes():
    url = 'https://quotes.toscrape.com/'
    list_file_write = []
    
    while True:
        respone = requests.get(url)
        soup = BeautifulSoup(respone.content, features='lxml')
        
        for quote_div in soup.find_all("div", class_="quote"):
            quote = {"tags": [tag.get_text() for tag in quote_div.find_all("a", class_="tag")],
                    "author": quote_div.find("small", class_="author").get_text(), 
                    "quote": quote_div.find('span', class_='text').get_text()
                    }
            list_file_write.append(quote)

        next_page = soup.find("li", class_="next")
            
        if next_page:
            url = url + next_page.find("a")["href"]
            
        else:
            break

    return list_file_write



def find_info_authors():
    base_url_perm = base_url = "http://quotes.toscrape.com"
    authors = []

    while True:
        response = requests.get(base_url)
        soup = BeautifulSoup(response.text, "lxml")

        for author_div in soup.find_all("div", class_="quote"):
            author_info = {
                "fullname": author_div.find("small", class_="author").get_text()}
            author_about = base_url_perm + author_div.find("small", class_="author").find_next("a")["href"]
            
            inner_response = requests.get(author_about)
            inner_soup = BeautifulSoup(inner_response.content, "html.parser")
            
            born_date = inner_soup.select("span.author-born-date")
            born_date_text = ''.join([i.text.strip() for i in born_date])

            born_location = inner_soup.select("span.author-born-location")
            born_location_text = ''.join([i.text.strip() for i in born_location])

            description = inner_soup.select("div.author-description")
            description_text = ''.join([i.text.strip() for i in description])

            author_info.update({
                'born_date': born_date_text,
                'born_location': born_location_text,
                'description': description_text,
            })

            if author_info["fullname"] not in [author["fullname"] for author in authors]:
                authors.append(author_info)

        next_page = soup.find("li", class_="next")
        if next_page:
            base_url = base_url + next_page.find("a")["href"]
        
        else:
            break

    return authors


def save_quotes_to_json(quotes):
    with open('quotes.json', 'w', encoding='utf-8') as file:
        save = json.dump(quotes, file, ensure_ascii=False, indent=4)


def save_authors_to_json(authors):
    with open('authors.json', 'w', encoding='utf-8') as file:
        save = json.dump(authors, file, ensure_ascii=False, indent=4)

quotes = find_info_quotes()
save_quotes = save_quotes_to_json(quotes)

authors = find_info_authors()
save_authors = save_authors_to_json(authors)