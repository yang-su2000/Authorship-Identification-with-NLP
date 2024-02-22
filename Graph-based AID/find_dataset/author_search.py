import requests
from bs4 import BeautifulSoup
import pandas as pd
import time


def find_author_info(author):
    url = 'https://dblp.uni-trier.de/search/author?q='
    append = "+".join(author.split(" "))
    url = url + append
    # print(url)
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    links = soup.find_all("a")
    mydivs = soup.find_all("span", {"class": "homonym-nr"})
    if len(mydivs) == 0: #no match
        return " $PersonNotFound "
    marker = mydivs[0]
    target_web = ""

    for link in links:
        if marker in link:
            target_web = link.get('href')
            break

    print(target_web)
    if target_web is '':
        return " $NoInformation "
    r2 = requests.get(target_web)
    soup = BeautifulSoup(r2.content, 'html.parser')

    mydivs = soup.find_all("li", {"itemprop":"affiliation"})
    temp = mydivs[0]
    affiliation = temp.contents[2].contents[0]


    return(affiliation)

df = pd.read_csv("authors.csv")
authors = df["authors"].values
# print(authors)

author_set = set()
for ls in df['authors'].values:
  authors = ls[1:-1].split(', ')
  author_set.update(authors)
authors = list(author_set)
authors = [a[1:-1] for a in authors]



f = open("author_features.txt", "w+")

for au in authors:
    try:
        result = find_author_info(au)
        f.write(au + " ," + result + "\n")
    except Exception as e:
        print(e)
        pass

