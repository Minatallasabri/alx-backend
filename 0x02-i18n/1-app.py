from flask import Flask, render_template
from flask_babel import Babel, _
import os


class Config:
    """_summary_
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)


@app.route('/')
def index():
    """_summary_

    Returns:
        _type_: _description_
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(debug=True)
