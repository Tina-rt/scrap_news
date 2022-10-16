from datetime import datetime
import requests
import bs4
import dateparser
from models import *
from pprint import pprint as pp


def get_details_lexpress(url):
    re = requests.get(url)
    bs = bs4.BeautifulSoup(re.content, "html.parser")
    print(bs)
    header_ = bs.find('header', {'class':'entry-header'})
    title = header_.find('h1').get_text()
    
    content = bs.find('div', {'class': 'entry-content'})
    all_p = content.find_all('p')
    paragraph = "\n".join([p.get_text() for p in all_p])
    image_content = bs.find('img')
    # image_url = image_content.find('img')
    
    author = bs.find('span', {'class': 'author'})
    
    # print(title, "\n".join([p.get_text() for p in all_p]))
    print(image_content)

# get_details_lexpress('https://lexpress.mg/15/10/2022/ukraine-madagascar-condamne-la-guerre-mais-reste-neutre/')
get_details_lexpress('https://lexpress.mg/15/10/2022/antananarivo-les-victimes-de-la-pollution-de-lair-envahissent-les-hopitaux/')
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
