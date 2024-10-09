import requests
from bs4 import BeautifulSoup

data = input("Enter the date using the following format YYYY-MM-DD: ")

url = f"https://www.billboard.com/charts/hot-100/{data}/"
request = requests.get(url)

content = request.text

soup = BeautifulSoup(content, 'html.parser')

for music in soup.findAll("div", class_="o-chart-results-list-row-container"):
    print(music.find("h3").getText().strip())