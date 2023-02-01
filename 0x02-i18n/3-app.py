#!/usr/bin/env python3
"""
3-app.py
parametization of template
"""
from flask import Flask, request, render_template
from flask_babel import Babel, _


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


@babel.localeselector
def get_locale():
    """
    determine best match from supported languages
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == "__main__":
    app.run()
