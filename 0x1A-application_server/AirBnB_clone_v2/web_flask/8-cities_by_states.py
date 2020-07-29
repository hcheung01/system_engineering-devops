#!/usr/bin/python3
"""web application to generate list of states dynamically"""
from flask import Flask, render_template
from models import storage


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/cities_by_states')
def cities_by_states():
    """list cities per related state"""
    return render_template('8-cities_by_states.html',
                           states=[c for c in storage.all('State').values()])


@app.teardown_appcontext
def teardown_db(exception):
    """Closes the database again at the end of the request."""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
