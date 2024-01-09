#!/usr/bin/env python3
"""A flask route that uses flask Babel to configure en to fr
"""

from flask import Flask, render_template
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

@app.route('/')
def hello_world():
    """Implementation of the flask app
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run()
