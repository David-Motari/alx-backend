#!/usr/bin/env python3
"""
0-app.py
initialization of basic flask app
"""
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def greetings():
    """
    Initialization of app
    """
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run()
