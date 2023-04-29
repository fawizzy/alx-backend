#!/urs/bin/env python3
'''
Flask app
'''
from flask import Flask, request, render_template, g
from flask_babel import Babel


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config(object):
    '''
    class to config babel
    '''
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


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

    locale = g.user['locale']
    if locale in Config.LANGUAGES:
        return g.user["locale"]
    locale = request.headers.get('locale', None)
    if locale in Config.LANGUAGES:
        return locale
    return Config.BABEL_DEFAULT_LOCALE


def get_user():
    '''
    Get user from url
    '''
    id = request.args.get('login_as', None)
    if id is not None and int(id) in users.keys():
        return users[int(id)]
    return None


@app.before_request
def before_request():
    '''
    get user from url and set as global user
    '''
    user = get_user()
    g.user = user


@app.route('/')
def index():
    '''
    render template
    '''
    return render_template('6-index.html')


if __name__ == "__main__":
    app.run(port="5000", host="0.0.0.0", debug=True)
