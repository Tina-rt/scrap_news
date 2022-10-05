from datetime import datetime
import requests
import bs4

class Headline:
    def __init__(self, title, image_url, date:datetime) -> None:
        self.title = title
        self.image_url = image_url
        self.date = date
    
    def toJson(self):
        return {
            'title': self.title,
            'image_url': self.image_url,
            'date': self.date.strftime("")
        }
    def __repr__(self) -> str:
        return f"{self.title} - {self.image_url} - {self.date}"


re = requests.get('https://midi-madagasikara.mg/category/a-lire/')
bs = bs4.BeautifulSoup(re.content, "html.parser")
rslt = bs.find_all('div', {'class': 'tdb_module_loop'})

data = []
for r in rslt:
    d_str = r.find('time')['datetime']
    d = datetime.strptime(d_str, "%Y-%m-%dT%H:%M:%S%z") 
    data.append(Headline(r.find('h3').get_text(), r.find('span')['data-img-url'], d))
    # print(r.find('time').get_text())

print(data)