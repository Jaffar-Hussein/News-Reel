from app import app
from flask import render_template
from ..requests import get_top_story, get_articles, get_news_sources


@app.route('/')
def index():
    trending_news = get_top_story()
    news_sources = get_news_sources()
    return render_template('home.html', trending_news=trending_news, news_sources=news_sources)


@app.route('/articles')
def articles():
    reuteres = get_articles('Reuters')
    return render_template('articles.html', reuteres=reuteres)
