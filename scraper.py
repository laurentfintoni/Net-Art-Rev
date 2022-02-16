from __future__ import print_function
from bs4 import BeautifulSoup
import json
import urllib
import requests

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

""" def url_to_text_rhizome(url):
    page = requests.get(url).text
    soup = BeautifulSoup(page, "lxml")
    text = [p.text for p in soup.find(class_="mw-parser-output").find_all('p')]
    print(url)
    return text

#rhizome urls 

with open('query.json') as file:
    rhizome_dump = json.load(file)

urls_2 = [link['document_url'] for link in rhizome_dump]

rhizome_text = [url_to_text_rhizome(u) for u in urls_2]

print(len(rhizome_text)) """

#query ttl dump for artwork label, description label, and documentl_url 

#google searches

"""Example of Python client calling Knowledge Graph Search API."""


api_key = 'AIzaSyDg0OU1DRA8ApbW0mqwBZ64eAPyaSYQy-I'
query = 'Mark Tribe'
service_url = 'https://kgsearch.googleapis.com/v1/entities:search'
params = {
    'query': query,
    'limit': 5,
    'indent': True,
    'key': api_key,
}
url = service_url + '?' + urllib.parse.urlencode(params)
response = json.loads(urllib.request.urlopen(url).read())
for element in response['itemListElement']:
    if 'artist' in element['result']:
        print(element['result'])

#what format do we want the divs into? 