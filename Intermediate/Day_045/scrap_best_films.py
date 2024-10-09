from bs4 import BeautifulSoup
import requests
import re

url = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(url)
content = response.text
soup = BeautifulSoup(content, "html.parser")

class Film:
    def __init__(self, title, rank):
        self.title = title
        self.rank = rank


    def __str__(self):
        return f"{self.rank}. {self.title}"

    
    def __repr__(self):
        return f"{self.rank}. {self.title}"

films_list:list = soup.find_all("section", {"data-slide-pos": lambda x: x is not None})

final_list:list[Film] = []
for i, film in enumerate(films_list):
    if i == 15:
        pass
    match_pos_and_name = re.search(r"(?P<number>\d+)\) (?P<name>[\w ]+)", film.find("h3").text)
    if match_pos_and_name:
        number = match_pos_and_name.group("number")
        name = match_pos_and_name.group("name")
    final_list.append(Film(name, number))

final_list.reverse()

with open("./best_films.txt", "w", encoding="utf-8") as file:
    for i, film in enumerate(final_list, start=1):
        file.write("{}. {}\n".format(i, film.title))
