from __future__ import print_function
from bs4 import BeautifulSoup
import json
import urllib
import requests
import pandas as pd

URL = "https://www.moma.org/collection/works/89286"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
#results = soup.find("div", class_="main-content")
#description = [div.text.strip() for div in soup.find(class_="artbase-summary-1").find_all('div')]
#summary_statement = [div.text.strip() for div in soup.find(class_="artbase-description-1").find_all('div')]
#accordion = [p.text.strip() for p in soup.find(id="AccordionDescriptionBody").find_all('div')]
print(page.status_code)

#moma script

def url_to_text_moma(url):
    page = requests.get(url).text
    soup = BeautifulSoup(page, "lxml")
    text = [p.text for p in soup.find(class_="main-content").find_all('p')]
    print(url)
    return text

#moma urls 

#urls = ['https://www.moma.org/collection/works/10', 'https://www.moma.org/collection/works/11', 'https://www.moma.org/collection/works/12']

#moma_text = [url_to_text_moma(u) for u in urls]

#print(moma_text) 




#rhizome script 

def url_to_text_rhizome(url):
    page = requests.get(url).text
    soup = BeautifulSoup(page, "lxml")
    #text = [p.text for p in soup.find(class_="mw-parser-output").find_all('p')]
    description = [div.text.strip() for div in soup.find(class_="artbase-summary-1").find_all('div')]
    summary_statement = [div.text.strip() for div in soup.find(class_="artbase-description-1").find_all('div')]
    accordion = [p.text.strip() for p in soup.find(id="AccordionDescriptionBody").find_all('div')]
    print(url)
    return accordion

#rhizome urls 

#with open('query.json') as file:
#    rhizome_dump = json.load(file)

#urls_2 = [link['document_url'] for link in rhizome_dump]

#rhizome_text = [url_to_text_rhizome(u) for u in urls_2]

#test = 'https://artbase.rhizome.org/wiki/Q3241'
#list = [item for item in url_to_text_rhizome(test)]

#print(list[0])

#query ttl dump for artwork label, description label, and documentl_url 

#google searches

""" def google_graph_query(search):
    api_key = 'AIzaSyDg0OU1DRA8ApbW0mqwBZ64eAPyaSYQy-I'
    query = search
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
        if ('detailedDescription') in element['result']:
            if query in element['result']['detailedDescription']['articleBody']:
                print(element['result']['detailedDescription'])

google_queries = ['Mark Tribe', 'Owen Mundy']

google_search = [google_graph_query(u) for u in google_queries]

print(google_search) """

#what format do we want the divs into? 