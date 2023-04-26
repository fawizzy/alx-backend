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
