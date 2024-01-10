#!/usr/bin/env python3
"""A flask route that uses flask Babel to configure en to fr
"""

from flask import Flask, render_template, request
from flask_babel import Babel


class Config():
    """Implementation of the config class that has a language class
    attribute equal to ["en", "fr"]
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.url_map.strict_slashes = False
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """Retreives the locale for a web page from request
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def hello_world() -> str:
    """Implementation of the flask app
    """
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
