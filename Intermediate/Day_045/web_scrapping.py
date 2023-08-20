from bs4 import BeautifulSoup
import requests


site = requests.get("https://news.ycombinator.com/").text
soup = BeautifulSoup(site, "html.parser")
titles = soup.find_all(name="a", class_="titleline",)
    