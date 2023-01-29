from bs4 import BeautifulSoup
# import lxml
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")

web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")

titlelines = soup.find_all(name="h3", class_="title")


titles = [movie.getText() for movie in titlelines]
movies = titles[::-1]
# for titleline in titlelines:
#     title = titleline.find('h3')
#     titles.append(title)

with open("movies.txt", mode="w") as file:
    for movie in movies:
        file.write(f'{movie}\n')