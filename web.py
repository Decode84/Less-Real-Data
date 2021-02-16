import requests
from requests import get
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

from time import sleep
# from random import randint
from tqdm import tqdm

headers = {"Accept-Language": "en-US,en;q=0.5"}

animes = []
characters = []
quotes = []

pages = np.arange(1, 443, 1)

for page in tqdm(range(443)):

  page = requests.get("https://www.less-real.com/?p=" + str(page), headers=headers)

  soup = BeautifulSoup(page.text, 'html.parser')
  quote_div = soup.find_all('div', class_='quote')

  for items in quote_div:

        # Anime
        anime = items.find(class_="quoteAnime").text
        animes.append(anime)

        # Character
        character = items.a.text
        characters.append(character)

        # Quote
        quote = items.find('span', class_="quoteText").text
        quotes.append(quote)

data = {
	'Anime': animes,
	'Character': characters,
	'Quote': quotes,
}

df = pd.DataFrame(data)

df.to_csv('less-real_data.csv')
