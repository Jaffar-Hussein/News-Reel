from flask import Flask
from flask_bootstrap import Bootstrap5
from .config import config_options



bootstrap = Bootstrap5()


def create_app(config_name):

    app = Flask(__name__)
    # Initalizing bootstrap
    bootstrap.init_app(app)
    # Initalizing the config file containig the API key

    app.config.from_object(config_options[config_name])
    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    # setting config 
    from .requests import configure_request
    configure_request(app)

    # Adding the views and errors
    return app