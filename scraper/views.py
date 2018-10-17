from django.shortcuts import render, redirect

import requests

from bs4 import BeautifulSoup
from .models import Article

# Create your views here.
def index(request):
    """The home page for scraper."""
    articles = Article.objects.all()
    context = {
        'article_list': articles,
    }
    return render(request, 'scraper/index.html', context)

def scrape(request):
    website = 'https://www.quantamagazine.org' # base url used to create links, can't end with '/'
    res = requests.get(website)
    res.raise_for_status()

    soup = BeautifulSoup(res.text, 'html.parser')
    elems = soup.select('.card')

    for elem in elems:
        titleElem = elem.select('.card__title')
        excerptElem = elem.select('.card__excerpt')
        linkElem = elem.select('.card__content > a')

        new_article = Article()
        new_article.title = titleElem[0].getText()
        new_article.excerpt = excerptElem[0].getText().strip()
        new_article.link = website + linkElem[0]['href']
        try:
            new_article.save()
        except:
            print('Error: duplicate entry')
            continue

    return redirect('/')

def delete_article(request, article_id):
    """Delete a stored article."""
    article = Article.objects.get(title=article_id)
    article.delete()

    return redirect('/')