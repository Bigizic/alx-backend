#!/usr/bin/env python3
"""A basic flask app with a single route
"""

from flask import Flask, render_template


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_world():
    """A route that simply outputs welcome to Holberton
    """
    return render_template("index.html")


if __name__ == '__main__':
    app.run()
