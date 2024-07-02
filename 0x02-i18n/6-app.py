#!/usr/bin/env python3
"""
Flask app that renders a template
"""

from typing import Dict, Union
from flask import Flask, render_template, request, g
from flask_babel import Babel


app = Flask(__name__)


class Config:
    """
    Config class for app
    """

    DEBUG = True
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user(user_id):
    """
    Returns a user dictionary or None if it doesn't exist
    """

    login_id = request.args.get('login_as')
    if login_id:
        user_id = int(login_id)
        return users.get(user_id)

    return None


@app.before_request
def before_request() -> None:
    """
    Find a user if any, and set it as a global on `g.user`.
    """

    user = get_user()
    g.user = user


@babel.localeselector
def get_locale() -> str:
    """
    Determine the user's locale
    Returns:
        - best match language code for user.
    """

    # Locale from URL parameters
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale

    # Locale from user settings
    if g.user:
        user_locale = g.user.get('locale')
        if user_locale and user_locale in app.config['LANGUAGES']:
            return user_locale

    # Locale from request header
    header_locale = request.accept_languages.best_match(
        app.config['LANGUAGES']
        )
    if header_locale:
        return header_locale

    # Default locale
    return request.accept_languages.best_match(
        app.config['LANGUAGES']
        )


@app.route('/')
def index() -> str:
    """
    Main route
    Returns:
        - Rendered template
    """

    return render_template('6-index.html')


if __name__ == "__main__":
    app.run()
