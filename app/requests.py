from distutils.command import config
from turtle import pu
from app import app
import urllib3
import json
from .models import articles, news_source
from datetime import datetime


# Imports of article class and news source class
News_Source = news_source.News_Source
Article = articles.Articles

# Imports of Api Key and base url

api_key = app.config['NEWS_APP_API_KEY']
sources_url = app.config['NEWS_BASE_URL_SOURCES']
categories_url = app.config['NEWS_BASE_URL_CATEGORIES']
articles_url = app.config['NEWS_BASE_URL_ARTICLES']
top_story_url = app.config['NEWS_BASE_URL_TOP_STORIES']


def process_data(news_source:list):
    """
    Function  that processes the news source result and transform them to a list of Objects


    Args:
        news_source: A list of dictionaries that contain movie details
    Returns :
        source_results: A list of movie objects
    """
    source_results = []
    for source in news_source:
        name = source.get('name')
        url = source.get('url')
        description = source.get('description')
        country = source.get('country')
        category = source.get('category')
        language = source.get('language')
        id = source.get('id')

        source_object = News_Source(
            name, url, description, country, category, language,id)
        source_results.append(source_object)
    return source_results


def get_top_story():
    """
        Function that gets top story response

    """
    top_story = top_story_url.format('us', api_key, 1, 1)
    http = urllib3.PoolManager()
    response = http.request('GET', top_story)
    news_response = json.loads(response.data.decode('utf-8'))
    the_article = news_response['articles']
    news_object = articles_process(the_article)
    return news_object


def get_news_sources():
    """
    function gets news sources as json converts to dict and returns a list

    Returns:
        source: list of news sources
    """
    news_sources_url=sources_url.format(api_key)

    http = urllib3.PoolManager()
    response = http.request('GET',news_sources_url)
    get_news_response = json.loads(response.data.decode('utf-8'))
    source = None

    if get_news_response['sources']:
        source_results_list = get_news_response['sources']
        source = process_data(source_results_list)
    return source


def get_articles(source):
    """
    Takes in a news source and returns all of their articles
    Args:
        source (str): The site of the news that is to be queryed
    """
    url_article = articles_url.format(source, api_key)

    http = urllib3.PoolManager()
    r = http.request('GET', url_article)
    response = json.loads(r.data.decode('utf-8'))

    list_of_articles = []
    if response:
        for i in response["articles"]:
            list_of_articles.append(i)

    article_objects = articles_process(list_of_articles)
    return article_objects

def categories(category):
    """
    Takes in a news category and returns all of their articles
    Args:
        source (str): The category of the news that is to be queryed
    """
    url_article = categories_url.format(category, api_key)

    http = urllib3.PoolManager()
    r = http.request('GET', url_article)
    response = json.loads(r.data.decode('utf-8'))

    list_of_articles = []
    if response:
        for i in response["articles"]:
            list_of_articles.append(i)

    article_objects = articles_process(list_of_articles)
    return article_objects


def articles_process(list_of_articles: list):
    """
    This distills the list of articles to a form of the articles class

    Args:
        list_of_articles (list): The list of articles  to be distilled
    """

    final_articles = []
    for i in list_of_articles:
        author = i.get('author')
        title = i.get('title')
        description = i.get('description')
        url = i.get('url')
        publishedAt = i.get('publishedAt')
        publishedAt = publishedAt[:10]
        publishedAt = datetime.strptime(publishedAt,"%Y-%m-%d")
        # publishedAt=datetime.fromisoformat(publishedAt.replace('Z', '+00:00'))
        publishedAt=datetime.date(publishedAt)
        # publishedAt = publishedAt.strftime('%Y-%m-%d')
        urlToImage = i.get('urlToImage')
        if urlToImage:
            
            final_articles.append(
                Article(author, title, description, urlToImage, url, publishedAt))
    return final_articles
