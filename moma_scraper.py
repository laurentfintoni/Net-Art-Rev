import requests
from bs4 import BeautifulSoup

""" URL = "https://www.moma.org/collection/works/10"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find("div", class_="main-content")
print(results.text.strip()) """

def url_to_transcript(url):
    page = requests.get(url).text
    soup = BeautifulSoup(page, "lxml")
    text = [p.text for p in soup.find(class_="main-content").find_all('p')]
    print(url)
    return text

urls = ['https://www.moma.org/collection/works/10', 'https://www.moma.org/collection/works/11', 'https://www.moma.org/collection/works/12']

transcripts = [url_to_transcript(u) for u in urls]

print(transcripts)

#what format do we want the divs into? 