import requests

from bs4 import BeautifulSoup

r = requests.get(input())
soup = BeautifulSoup(r.content, "html.parser")

title = soup.find("h1").text
print(title)
