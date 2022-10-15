from datetime import datetime


class Headline:
    def __init__(self,source, title, image_url, date:datetime, link, ) -> None:
        self.title = title
        self.image_url = image_url
        self.date = date
        self.link = link
        self.source = source
    
    def toJson(self):
        return {
            'title': self.title,
            'image_url': self.image_url,
            'date': self.date.strftime("%d/%m/%Y"),
            'link': self.link
        }
    def __repr__(self) -> str:
        return f"{self.title} - {self.image_url} - {self.date}"
