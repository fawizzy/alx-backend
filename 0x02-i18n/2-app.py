#!/usr/bin/env python3

from flask import Flask, render_template, request
from flask_babel import Babel

'''
Flask app
'''

app = Flask(__name__)


class Config(object):
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app)


@app.route('/')
def index():
    '''
    Function to render the 0-index html file
    '''
    return render_template("1-index.html")


@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(app.config["LANGUAGES"])


if __name__ == "__main__":
    app.run(port="5000", host="0.0.0.0", debug=True)