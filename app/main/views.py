from unicodedata import category
from app import app
from flask import render_template
from ..requests import get_top_story, get_articles, get_news_sources,categories

import urllib3
import json
from datetime import datetime

api_key = app.config['NEWS_APP_API_KEY']
sources_url = app.config['NEWS_BASE_URL_SOURCES']
categories_url = app.config['NEWS_BASE_URL_CATEGORIES']
articles_url = app.config['NEWS_BASE_URL_ARTICLES']

@app.route('/')
def index():
    trending_news = get_top_story()
    news_sources = get_news_sources()
    return render_template('home.html', trending_news=trending_news, news_sources=news_sources)


@app.route('/sources/<site>')
def articles(site):
    articles_news = get_articles(site)
    return render_template('articles.html', articles_news=articles_news)

@app.route('/categories/<categorie>')
def cat(categorie):
    url_article = categories_url.format(categorie, api_key)

    http = urllib3.PoolManager()
    r = http.request('GET', url_article)
    response = json.loads(r.data.decode('utf-8'))
    
    articles_news = categories(categorie)
    print(response)
    return render_template('articles.html', articles_news=articles_news)