from datetime import datetime
import requests
import bs4
import dateparser
from models import *
from pprint import pprint as pp

def get_headline_midi():
    re = requests.get('https://midi-madagasikara.mg/category/a-lire/')
    bs = bs4.BeautifulSoup(re.content, "html.parser")
    rslt = bs.find_all('div', {'class': 'tdb_module_loop'})

    data = []
    for r in rslt:
        d_str = r.find('time')['datetime']
        # d = datetime.strptime(d_str, "%Y-%m-%dT%H:%M:%S%z") 
        d = dateparser.parse(d_str)
        print(d)
        link = r.find('a')['href']
        data.append(Headline("Midi Madagasikara",r.find('h3').get_text(), r.find('span')['data-img-url'], d, link))
    return data

def get_headline_lexpress():
    re = requests.get('https://lexpress.mg/')
    bs = bs4.BeautifulSoup(re.content, "html.parser")

    rslt = bs.find_all('article', {'class': 'herald-lay-f'})

    data = []
    for r in rslt:
        title = r.find('h2').get_text()
        date = r.find('div', {'class': 'herald-date'}).get_text()
        link = r.select('.herald-post-thumbnail a')[0]['href']
        image = r.find('img')['src']
        data.append(Headline("L'expresse de Madagascar",title, image, dateparser.parse(date), link))
    return data
