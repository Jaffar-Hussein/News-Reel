from . import main
from flask import render_template

@main.app_errorhandler(404)
def page_not_found(e):
    return render_template('error.html'),404
    