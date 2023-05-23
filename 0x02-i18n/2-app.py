#!/usr/bin/env python3
"""
Get locale from request
"""
from flask import Flask
from flask_babel import Babel


class Config:
    """flask Babel configuration
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
app.url_map.strict_slashes = False
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """Retrieve a locale for a web page
    """
    return request.accept_language.best_match(app.config["LANGUAGE"])


@app.route('/')
def get_index() -> str:
    """home/index page
    """
    return render_template('2-index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
