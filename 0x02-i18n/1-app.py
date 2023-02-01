#!/usr/bin/env python3
"""
1-app.py
initialization of basic flask app with babel
"""
from flask import Flask, request, render_template
from flask_babel import Babel
from os import getenv



class Config(object):
    """
    configuration of available languages in the app
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
babel = Babel(app)
app.config.from_object(Config)


@app.route('/')
def greetings():
    """
    Initialization of app
    """
    return render_template('1-index.html', strict_slashes=False)


if __name__ == "__main__":
    app.run()
