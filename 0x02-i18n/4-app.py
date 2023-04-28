#!/usr/bin/env python3
'''
Flask app
'''
from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)


class Config(object):
    '''
    class to config babel
    '''
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
    return render_template("3-index.html")


@babel.localeselector
def get_locale():
    '''
    Select and return best language match based on supported languages
    '''
    locale = request.args.get('locale')
    # check if the locale argument is present
    if locale is not None:
        # check if the argument's value is a supported locale
        if locale in Config.LANGUAGES:
            return locale
    # if no argument is present, or if the argument is not supported, resort to the default behavior
    return request.accept_languages.best_match(app.config["LANGUAGES"])


if __name__ == "__main__":
    app.run(port="5000", host="0.0.0.0", debug=True)
