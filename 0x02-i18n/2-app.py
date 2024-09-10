from flask import Flask, render_template, request
from flask_babel import Babel

# Initialize Flask app
app = Flask(__name__)

# Config class with available languages and default settings
class Config:
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

# Apply the configuration to the app
app.config.from_object(Config)

# Instantiate the Babel object
babel = Babel(app)

# Locale selector function
@babel.localeselector
def get_locale():
    # Request the best match from supported languages
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/')
def index():
    return render_template('0-index.html')

if __name__ == '__main__':
    app.run(debug=True)

