from bs4 import BeautifulSoup
import requests
import re

url = "https://news.ycombinator.com/news"
response = requests.get(url)
content = response.text
soup = BeautifulSoup(content, "html.parser")

tables = soup.select("table")

news_table = tables[2]

data_rows = news_table.find_all("tr", class_=lambda x: x != "spacer")

class News:
    def __init__(self, title, url, points):
        self.title = title
        self.url = url
        self.points = points
    
    def __str__(self):
        return f"{self.title} - {self.url} - {self.points} points"
    
    def __repr__(self):
        return f"{self.title} - {self.url} - {self.points} points"

all_news:list[News] = []
for i, tr in enumerate(data_rows[:-1]):
    text_content = tr.getText()
    if i % 2 == 0:
        search_title = re.search(r"\d+\. (.+)( \(.+\))?", text_content)
        if search_title:
            title = search_title.group(1).strip()
        else:
            title = "Not available"
        link_search = re.search(r'"(https://.+?)"', str(data_rows[i]))
        if link_search:
            link = link_search.group(1)
        else:
            link = "Not available"
    else:
        search_points = re.search(r"(\d+) points by", text_content)
        if search_points:
            points = int(search_points.group(1))
        else:
            points_na = "Not available"
        all_news.append(News(title, link, points_na))        
            

def sort_func(news:News):
    if type(news.points) == int:
        return news.points
    else:
        return -1

all_news.sort(key=sort_func, reverse=True)

all_news


