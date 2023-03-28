# import requests
# from bs4 import BeautifulSoup
# import random

# def get_bird_words():
#     url = 'https://www.audubon.org/news/the-audubon-dictionary-birders'
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, 'html.parser')
#     print(soup)
#     bird_words = [soup.text for word in soup.select('li strong')]
#     return bird_words

# # def generate_haiku():
# #     bird_words = get_bird_words()
# #     haiku = []
# #     haiku.append(' '.join(random.choices(bird_words, k=5)))
# #     haiku.append(' '.join(random.choices(bird_words, k=7)))
# #     haiku.append(' '.join(random.choices(bird_words, k=5)))
# #     return '\n'.join(haiku)

# # print(generate_haiku())
# get_bird_words()

import requests
from bs4 import BeautifulSoup
import random

def get_bird_words():
    """Scrape Audubon Dictionary for bird names"""
    url = 'https://www.audubon.org/news/the-audubon-dictionary-birders'
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    bird_list = soup.find('div', {'class': 'bird-list'}).find_all('li')
    bird_words = []
    for bird in bird_list:
        bird_name = bird.find('a').text.strip().lower()
        bird_words.extend(bird_name.split())
    return bird_words

def generate_haiku():
    """Generate random haiku using bird words"""
    bird_words = get_bird_words()
    line1 = ' '.join(random.choices(bird_words, k=5))
    line2 = ' '.join(random.choices(bird_words, k=7))
    line3 = ' '.join(random.choices(bird_words, k=5))
    haiku = f"{line1.capitalize()}\n{line2.capitalize()}\n{line3.capitalize()}"
    return haiku

get_bird_words()
generate_haiku()
