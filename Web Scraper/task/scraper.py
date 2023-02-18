import requests
from bs4 import BeautifulSoup
import string
import os


def format_article_title(name):
    new_name = str()
    name = name.strip()
    for char in name:
        if char in string.ascii_letters or char in string.digits:
            new_name += char
        elif char == " ":
            new_name += "_"
    return new_name + ".txt"


def get_article_content(relative_url_of_article, name_of_article):
    r_article = requests.get("https://www.nature.com" + relative_url_of_article,
                             headers={"Accepts-Language": "en_US,en;q=0.5"})
    soup_article = BeautifulSoup(r_article.content, "html.parser")
    body_article = soup_article("div", {"class": "c-article-body main-content"})
    with open(format_article_title(name_of_article), "wb") as f:
        for text in body_article:
            f.write(str(text.text).encode())


url = "https://www.nature.com/nature/articles?sort=PubDate&year=2020"
BASE_DIRECTORY = os.getcwd()
number_of_pages = int(input())
article_category = input()
print(os.listdir())
# Delete previous directories
for num_del in range(len(os.listdir(os.getcwd()))):
    if os.access(f"Page_{num_del + 1}", os.F_OK):
        if len(os.listdir(f"Page_{num_del + 1}")) > 0:
            for item in os.listdir(f"Page_{num_del + 1}"):
                os.remove(f"Page_{num_del + 1}/{item}")
        os.rmdir(f"Page_{num_del + 1}")

# Create directories
for num in range(number_of_pages):
    os.mkdir(f"Page_{num + 1}")

for page in range(number_of_pages):
    os.chdir(BASE_DIRECTORY + f"/Page_{page + 1}")
    if page > 0:
        r = requests.get(url + f"&page={page + 1}", headers={"Accepts-Language": "en_US,en;q=0.5"})
    else:
        r = requests.get(url, headers={"Accepts-Language": "en_US,en;q=0.5"})
    soup = BeautifulSoup(r.content, "html.parser")

    link_of_articles = soup("a", {"class": "c-card__link u-link-inherit"})
    type_of_article = soup("span", {"class": "c-meta__type"})
    index_of_right_section = list()
    index_helper = 0
    for section in type_of_article:
        if section.text == article_category:
            index_of_right_section.append(index_helper)
        index_helper += 1
    article_list = list()
    for i in index_of_right_section:
        article_list.append(format_article_title(link_of_articles[i].text))
        get_article_content(link_of_articles[i]["href"], link_of_articles[i].text)


"""url = input("Input the URL:\n")
r = requests.get(url)
status_code = r.status_code
if status_code == 200:
    with open("source.html", "wb") as file:
        r = r.content
        file.write(bytes(r))
        print("Content saved.")
else:
    print(f"The URL returned {status_code}")"""


"""article_dict = dict()

if url.find("nature.com/articles/") != -1:
    r = requests.get(url, headers={"Accepts-Language": "en_US,en;q=0.5"})
    soup = BeautifulSoup(r.content, "html.parser")

    split_tag = str(soup("meta", {"name": "description"})).split('"')

    article_dict["title"] = soup.find("title").text
    article_dict["description"] = split_tag[1]

    print(article_dict)
else:
    print("Invalid page!")"""