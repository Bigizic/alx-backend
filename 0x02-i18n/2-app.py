#!/usr/bin/env python3@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(app.config['LANGUAGES'])@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(app.config['LANGUAGES'])
"""A flask route that uses flask Babel to configure en to fr
"""

from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)
app.url_map.strict_slashes = False


class Config():
    """Implementation of the config class that has a language class
    attribute equal to ["en", "fr"]
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """Retreives the locale for a web page from request
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def hello_world():
    """Implementation of the flask app
    """
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run()
