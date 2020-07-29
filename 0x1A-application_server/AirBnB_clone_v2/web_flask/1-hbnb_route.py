#!/usr/bin/python3
"""
Flask script that starts web application
"""
from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello():
    """Output Hello HBNB"""
    return ('Hello HBNB!')


@app.route('/hbnb')
def hbnb():
    """Output HBNB"""
    return ('HBNB')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
