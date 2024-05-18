#!/usr/bin/python3
""" Flask tutorial module
"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """ Function to display HBNB
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hhbnb():
    """ FUnction to display Hello HBNB
    """
    return "HBNB"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
