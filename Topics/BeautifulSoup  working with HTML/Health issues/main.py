import requests

from bs4 import BeautifulSoup

letter = 'S'
url = input()

r = requests.get(url)
soup = BeautifulSoup(r.content, "html.parser")

topic_titles = soup("a")
letter_topic_titles = list()

for tag in topic_titles:
    if tag.text.startswith(letter) and len(tag.text) > 1:
        if str(tag["href"]).find("topic") != -1 or str(tag["href"]).find("entity") != -1:
            letter_topic_titles.append(tag.text.replace('"', "'"))

print(letter_topic_titles)