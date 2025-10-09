import requests
from bs4 import BeautifulSoup
import pandas as pd

def collect_theatre_events(price=0):
    data = []
    url = f'https://spb.kinoafisha.info/theater/'
    html_content = requests.get(url).text
    soup = BeautifulSoup(html_content, 'lxml')
    entries = soup.find_all('div', class_='eventCardItem_main')
    for entry in entries:
        div_event = entry.find('div', class_='eventCardItem_info')
        event_name = div_event.find('a', class_='eventCardItem_title').text
        event_genres = ''
        genres_temp = entry.find_all('a', class_='eventCardItem_genresItem')
        for genre in genres_temp:
            if len(event_genres) == 0: 
                event_genres += genre.text
            else: 
                event_genres += (', ' + genre.text)
        event_place = entry.find('a', class_='eventCardItem_detailsItem').text
        event_price = entry.find('a', class_='eventCardItem_price').text
        if event_price.startswith('от '): 
            event_price = event_price[3:]
        if event_price.endswith(' ₽'): 
            event_price = event_price[:-2]
        if not event_price.isdigit(): 
            event_price = float('inf')
        else: 
            event_price = int(event_price)
        data.append({'Event name': event_name, 'Event genres': event_genres, 'Event place': event_place, 'Minimal ticket price': event_price})
    if price != 0:
        data = list(filter(lambda x: x['Minimal ticket price'] <= price, data))
    return data


MAX_PRICE = 2000
theatre_data = collect_theatre_events(MAX_PRICE)
df = pd.DataFrame(theatre_data)

df.to_excel('available events.xlsx')
