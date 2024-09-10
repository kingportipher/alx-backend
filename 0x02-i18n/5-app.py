from flask import Flask, render_template, request, g
from flask_babel import Babel, _

app = Flask(__name__)

# User database mockup
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

# Config class with available languages and default settings
class Config:
    LANGUAGES = ['en', 'fr']  # Available languages
    BABEL_DEFAULT_LOCALE = 'en'  # Default language
    BABEL_DEFAULT_TIMEZONE = 'UTC'  # Default timezone

app.config.from_object(Config)

# Instantiate the Babel object
babel = Babel(app)

# Locale selector function
@babel.localeselector
def get_locale():
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    if g.user and g.user.get('locale') in app.config['LANGUAGES']:
        return g.user['locale']
    return request.accept_languages.best_match(app.config['LANGUAGES'])

# Function to retrieve user based on login_as parameter
def get_user():
    try:
        user_id = int(request.args.get('login_as'))
        return users.get(user_id)
    except (TypeError, ValueError):
        return None

# before_request function to set user in flask.g
@app.before_request
def before_request():
    g.user = get_user()

@app.route('/')
def index():
    if g.user:
        message = _('logged_in_as', username=g.user['name'])
    else:
        message = _('not_logged_in')
    return render_template('5-index.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)

