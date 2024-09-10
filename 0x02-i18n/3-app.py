from flask import Flask, render_template, request
from flask_babel import Babel, _

# Initialize Flask app
app = Flask(__name__)

# Config class with available languages and default settings
class Config:
    LANGUAGES = ['en', 'fr']  # Available languages
    BABEL_DEFAULT_LOCALE = 'en'  # Default language
    BABEL_DEFAULT_TIMEZONE = 'UTC'  # Default timezone

# Apply the configuration to the app
app.config.from_object(Config)

# Instantiate the Babel object
babel = Babel(app)

# Locale selector function
@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/')
def index():
    return render_template('0-index.html', home_title=_('home_title'), home_header=_('home_header'))

if __name__ == '__main__':
    app.run(debug=True)
