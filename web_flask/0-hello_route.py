#!/usr/bin/python3
'''
This script is a start file with flask in python
'''
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home():
    '''
    A trial method to start with flask
    '''
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
