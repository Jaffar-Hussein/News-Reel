from distutils.command import config
from app import app
import urllib3
import json
from .models import articles,news_source

# Imports of article class and news source class
News_Source  = news_source.News_Source
Article = articles.Articles

# Imports of Api Key and base url

api_key = app.config('NEWS_APP_API_KEY')
sources_url = app.config('NEWS_BASE_URL_SOURCES')
categories_url = app.config('NEWS_BASE_URL_CATEGORIES')
articles_url = app.config('NEWS_BASE_URL_ARTICLES')

