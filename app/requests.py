from distutils.command import config
from app import app
import urllib3
import json
from .models import articles,news_source

# Imports of article class and news source class
News_Source  = news_source.News_Source
Article = articles.Articles

# Imports of Api Key and base url

api_key = app.config['NEWS_APP_API_KEY']
sources_url = app.config['NEWS_BASE_URL_SOURCES']
categories_url = app.config['NEWS_BASE_URL_CATEGORIES']
articles_url = app.config['NEWS_BASE_URL_ARTICLES']

def process_data(news_source):
    """
    Function  that processes the news source result and transform them to a list of Objects


    Args:
        news_source: A list of dictionaries that contain movie details
    Returns :
        source_results: A list of movie objects
    """
    source_results = []
    for source in news_source:
        name= source.get('name')
        url=source.get('url')
        description= source.get('description')
        country=source.get('country')
        category= source.get('category')
        language= source.get('language')
        
        source_object=News_Source(name,url,description,country,category,language)
        source_results.append(source_object)
    return source_results
def get_top_story():
    """
        Function that gets top story response 
        
    """
    top_story='http://newsapi.org/v2/top-headlines?country{}&apiKey={}&page={}&PageSize={}'.format('us',api_key,1,1)
    http=urllib3.PoolManager()
    response=http.request('GET',top_story)
    news_response = json.loads(response.data.decode('utf-8'))
    news_object = None
    
    if news_response:
        author=news_response.get('author')
        title=news_response.get('title')
        description=news_response.get('description')
        url=news_response.get('url')
        publishedAt=news_response.get('publishedAt')
        urlToImage=news_response.get('urlToImage')
        
    news_object=Article(author,title,description,url,publishedAt,urlToImage)
    
    return news_object


def get_news_sources():
    """
    function gets news sources as json converts to dict and returns a list

    Returns:
        source: list of news sources
    """
    sources_url.format(api_key)
    
    http=urllib3.PoolManager()
    response=http.request('GET',sources_url)
    get_news_response = json.loads(response.data.decode('utf-8'))
    source = {}

    if get_news_response['sources']:
        source_results_list=get_news_response['sources']
        source=process_data(source_results_list)
    return source
    
def get_articles(source):
    pass
        
