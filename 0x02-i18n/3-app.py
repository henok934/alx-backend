#!/usr/bin/env python3
"""
file 3-app
"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config(object):
    """create config class"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route("/", strict_slashes=False)
def index():
    """displays a basic hello world message"""
    return render_template("3-index.html")


@babel.localeselector
def get_locale():
    """Gets best fmatch locale according to request"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port="5000")
