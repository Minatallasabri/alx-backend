#!/usr/bin/env python3
"""_summary_

    Returns:
        _type_: _description_
    """
from flask_babel import Babel
from flask import Flask, render_template, request


class Config:
    """_summary_
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
    """_summary_

    Returns:
        str: _description_
    """
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route('/')
def get_index() -> str:
    """_summary_

    Returns:
        str: _description_
    """
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
