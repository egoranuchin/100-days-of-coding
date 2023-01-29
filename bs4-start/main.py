from bs4 import BeautifulSoup
# import lxml
import requests

response = requests.get("https://news.ycombinator.com/")

yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
# print(soup.title)

titlelines = soup.find_all(class_="titleline")
article_texts  = []
article_links = []
for titleline in titlelines:
    title_link = (titleline.find('a'))
    text = (title_link.getText())
    article_texts.append(text)
    link = title_link.get('href')
    article_links.append(link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(class_="score")]

largest_number = max(article_upvotes)
largest_index = article_upvotes.index(largest_number)
print(largest_number)
print(largest_index)
print(article_texts[largest_index])
print(article_links[largest_index])

# print(article_texts)
# print(article_links)
# print(article_upvotes)