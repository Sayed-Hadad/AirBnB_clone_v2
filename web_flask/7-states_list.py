#!/usr/bin/python3
'''
This script is a training on flask in python
'''
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.teardown_appcontext
def close_conn(exc):
    """
    remove the current SQLAlchemy Session
    """
    storage.close()


@app.route("/states_list", strict_slashes=False)
def state_list():
    '''
    display states in html page
    '''
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
