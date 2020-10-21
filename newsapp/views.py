# API Importing
from django.shortcuts import render
from newsapi import NewsApiClient

import config

def index(request):
    countryvar = 'IN'
    if request.method == "POST":
        countryvar = request.POST['country']
    newsapi = NewsApiClient(api_key = config.api_key)
    countryvar = countryvar.lower()
    print(countryvar)
    top = newsapi.get_top_headlines(country=countryvar)

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