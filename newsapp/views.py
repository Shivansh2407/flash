# API Importing
from django.shortcuts import render
from newsapi import NewsApiClient

import config
def index(request):
    newsapi = NewsApiClient(api_key = config.api_key)
    top = newsapi.get_top_headlines(country='in', category='technology')

    l = top['articles']
    desc = []
    news = []
    img  = []
    url  = []

    for i in range(len(l)):
        f = l[i]
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
        url.append(f['url'])
    mylist = zip(news, desc, img, url)

    return render(request, 'index.html', context ={"mylist":mylist})