#!/usr/bin/env python3
"""A flask route that uses flask Babel to configure en to fr
"""

from flask import Flask, render_template, request
from flask_babel import Babel
from typing import Union, Dict


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
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@app.before_request
def before_request() -> None:
    """A before request to retrieve users
    """
    user = get_user()
    g.user = user


@babel.localeselector
def get_locale() -> str:
    """Retreives the locale for a web page from request
    """
    if 'locale' in request.args:
        if request.args.get('locale') in app.config['LANGUAGES']:
            return request.args.get('locale')

    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def hello_world() -> str:
    """Implementation of the flask app
    """
    return render_template('5-index.html')


def get_user() -> Union[Dict, None]:
    """@param (u_id): <int>
    Returns a user dictionary else None
    """
    u_id = request.args.get('login_as')
    if u_id:
        return u_id.get(int(u_id))
    return None


if __name__ == '__main__':
    app.run()
