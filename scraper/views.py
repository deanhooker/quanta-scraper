from django.shortcuts import render

import requests

from bs4 import BeautifulSoup

# Create your views here.
def index(request):
    """The home page for scraper."""
    return render(request, 'scraper/index.html')

def scrape():
    website = 'https://www.quantamagazine.org' # base url used to create links, can't end with '/'
    res = requests.get(website)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('.card')

    articles = []

    for elem in elems:
        titleElem = elem.select('.card__title')
        excerptElem = elem.select('.card__excerpt')
        linkElem = elem.select('.card__content > a')

        articleDict = {
            'title': titleElem[0].getText(),
            'excerpt': excerptElem[0].getText().strip(),
            'link': website + linkElem[0]['href'],
        }
        articles.append(articleDict)

    print(articles)

scrape()