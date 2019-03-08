#!/usr/bin/python3
"""
Script to start a web server
"""
from flask import Flask
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello():
    """Output Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """Output HBNB"""
    return 'HBNB'


@app.route('/c/<text>')
def c(text):
    """Output C"""
    return 'C {}'.format(text.replace('_', ' '))

if __name__ == "__main__":
    app.run(host='0.0.0.0')
