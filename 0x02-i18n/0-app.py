#!/usr/bin/env python3

from flask import Flask, render_template
'''
flask code to render html file
'''
app = Flask(__name__)


@app.route('/')
def index():
    '''
    Function to render the 0-index html file
    '''
    return render_template("0-index.html")


if __name__ == "__main__":
    app.run(port="5000", host="0.0.0.0", debug=True)
