#!/usr/bin/env python3
"""_summary_
        """

from flask import Flask, render_template
from flask_babel import Babel
from flask import request


class Config:
    """_summary_
        """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.route('/', strict_slashes=False)
def get_index():
    """_summary_

    Returns:
        _type_: _description_
    """
    return render_template('2-index.html')


@babel.localeselector
def get_local():
    """_summary_

    Returns:
        _type_: _description_
    """
    return request.accept_languages.best_match(app.config["LANGUAGES"])


if __name__ == '__main__':
    app.run()
