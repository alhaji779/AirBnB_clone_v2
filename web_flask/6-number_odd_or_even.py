#!/usr/bin/python3
""" Flask tutorial module
"""
from flask import Flask, render_template

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


@app.route('/c/<text>', strict_slashes=False)
def htext(text):
    """ Function that takes text params
    """
    new_text = text.replace('_', ' ')
    return "C {}".format(new_text)


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def hpython(text='is cool'):
    """ Fuction with default params
    """
    new_text = text.replace('_', ' ')
    return "Python {}".format(new_text)


@app.route('/number/<int:n>', strict_slashes=False)
def hnumber(n):
    """ Function that returns a number
    """
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def ntemplate(n):
    """ Function to show number on template
    """
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def hevenodd(n):
    """ Function to render odd/even on html page
    """
    if n%2 == 0:
        e_type = 'even'
    else:
        e_type = 'odd'
    return render_template('6-number_odd_or_even.html', n=n, e_type=e_type)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
