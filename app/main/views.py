from app import app
from flask import render_template
from ..requests import get_top_story,get_articles


@app.route('/')
def index():
    trending_news = get_top_story()
    return render_template('home.html', trending_news=trending_news)

@app.route('/articles')
def articles():
    reuteres = get_articles('Reuters')
    return render_template('articles.html',reuteres=reuteres)
    
    