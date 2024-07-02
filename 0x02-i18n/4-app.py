#!/usr/bin/env python3
"""
This is a Flask application that demonstrates internationalization
(i18n) using Flask-Babel.

To run the application, execute this script directly.
"""

from flask import Flask, render_template, request
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
app.url_map.strict_slashes = False
babel = Babel(app)


@babel.localeselector
def get_locale():
    """
    Locale selector function that determines the best matching
    language based on the user's preferences.
    """

    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    """
    Route handler for the root URL ("/").
    Renders the "4-index.html" template.
    """

    return render_template("4-index.html")


if __name__ == "__main__":
    app.run()
