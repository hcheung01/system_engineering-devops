#!/usr/bin/python3
"""web app"""
from flask import Flask, render_template
from models import storage


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states/<id>')
def state_and_id(id=None):
    """list cities and states"""

    states = [st for st in storage.all('State').values()]
    match_st = None
    if id:
        for st in states:
            if st.id == id:
                match_st = st
    return render_template('9-states.html', state=match_st)


@app.route('/cities_by_states', strict_slashes=False)
def all_states_with_cities_html():
    """ all states and cities"""

    states = [st for st in storage.all('State').values()]
    return(render_template('8-cities_by_states.html', states=states))


@app.route('/states')
def states():
    """access File/DB Storage for all State objects and render to HTML"""
    states = [st for st in storage.all('State').values()]
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """Closes the database again at the end of the request."""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
