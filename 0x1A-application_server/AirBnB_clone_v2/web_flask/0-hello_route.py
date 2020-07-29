#!/usr/bin/python3
"""Flask script for to setup web application"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Output string"""
    return ('Hello HBNB!')

if __name__ == "__main__":
    app.run(host='0.0.0.0')
