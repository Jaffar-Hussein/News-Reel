from app import app
from flask import render_template
from ..requests import get_top_story, get_articles, get_news_sources, categories


@app.route('/')
def index():
    trending_news = get_top_story()
    news_sources = get_news_sources()
    title_head = "HOME"
    return render_template('home.html', trending_news=trending_news, news_sources=news_sources,title_head=title_head)


@app.route('/sources/<site>')
def articles(site):
    articles_news = get_articles(site)
    title_head = site.upper() 
    return render_template('articles.html', articles_news=articles_news,title_head=title_head)


@app.route('/categories/<categorie>')
def cat(categorie):
    title_head = categorie.upper() + " NEWS"
    articles_news = categories(categorie)
    return render_template('articles.html', articles_news=articles_news,title_head=title_head)
