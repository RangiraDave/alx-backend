#!/usr/bin/env python3
"""
Script to Create the class App that inherits from Flask
It creates a single / route and return a string
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home() -> str:
    """
    Return a string
    """

    return render_template("0-index.html")


if __name__ == "__main__":
    app.run(debug=True)
