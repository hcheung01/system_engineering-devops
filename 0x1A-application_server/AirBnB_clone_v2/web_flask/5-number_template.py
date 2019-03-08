#!/usr/bin/python3
"""
Start a Flask web application and display...
"""
from flask import Flask, render_template


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello():
    """Output: Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """Output: HBNB"""
    return 'HBNB'


@app.route('/c/<text>')
def c(text):
    """Output: C + text and replace all underscore with white space"""
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python', defaults={'text': 'is cool'})
@app.route('/python/<text>')
def python(text):
    """Output: Python + text variable and replace underscore with space"""
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>')
def number(n):
    """Output: n is a number only if int"""
    return '{:d} is a number'.format(n)


@app.route('/number_template/<int:n>')
def number_template(n):
    """Output: html page only if n is int"""
    return render_template('5-number.html', n=n)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
