from flask import Flask
from flask_bootstrap import Bootstrap5
from app.config import DevConfig

app = Flask(__name__, instance_relative_config=True)
# Initalizing bootstrap
bootstrap = Bootstrap5(app)
# Initalizing the config file containig the API key
app.config.from_pyfile('config.py')
app.config.from_object(DevConfig)

from app.main import errors
from app.main import views