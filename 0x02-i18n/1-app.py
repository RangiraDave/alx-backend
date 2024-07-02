#!/usr/bin/env python3
"""
This module contains a Flask application with internationalization support.

It defines a Flask application object and configures it with Flask-Babel
for internationalization.
The application is configured with two languages: English and French.
The default language is set to English and the default timezone is set to UTC.

Usage:
    - Run the application using the Flask development server
    or a production server.
"""

from flask import Flask
from flask_babel import Babel

app = Flask(__name__)


class Config:
    """
    Configuration class for the Flask application.
    """

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)

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

    Returns:
        A string.
    """

    return render_template("1-index.html")
