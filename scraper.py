import requests
import json
from bs4 import BeautifulSoup

""" URL = "https://www.moma.org/collection/works/10"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find("div", class_="main-content")
print(results.text.strip()) """

""" #moma script

def url_to_text_moma(url):
    page = requests.get(url).text
    soup = BeautifulSoup(page, "lxml")
    text = [p.text for p in soup.find(class_="main-content").find_all('p')]
    print(url)
    return text

#moma urls 

urls = ['https://www.moma.org/collection/works/10', 'https://www.moma.org/collection/works/11', 'https://www.moma.org/collection/works/12']

moma_text = [url_to_text_moma(u) for u in urls]

print(moma_text) """


#rhizome script 

def url_to_text_rhizome(url):
    page = requests.get(url).text
    soup = BeautifulSoup(page, "lxml")
    text = [p.text for p in soup.find(class_="mw-parser-output").find_all('p')]
    print(url)
    return text

#rhizome urls 

""" with open('query.json') as file:
    rhizome_dump = json.load(file) """

urls_2 = [link['document_url'] for link in rhizome_dump]

rhizome_text = [url_to_text_rhizome(u) for u in urls_2]

print(len(rhizome_text))

#query ttl dump for artwork label, description label, and documentl_url 


#what format do we want the divs into? 