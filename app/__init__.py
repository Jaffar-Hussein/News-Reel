from flask import Flask
from flask_bootstrap import Bootstrap5
from pip import main

app = Flask(__name__)

bootstrap = Bootstrap5(app)

from  app.main import views