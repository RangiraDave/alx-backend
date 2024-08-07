#!/usr/bin/env python3
"""
This module contains a Flask application with internationalization support.
"""

from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)


class Config:
    """
    Configuration class for the Flask application.
    """

    DEBUG = True
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@babel.localeselector
def get_locale():
    """
    Determine the language to use for localization.
    Returns:
        The best language for the user.
    """

    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    """
    Default route of the Flask application.
    Returns a string
    """

    return render_template("2-index.html")


if __name__ == "__main__":
    app.run()
